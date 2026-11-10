#!/usr/bin/env python3
# Claude Code のフックから呼ばれる番人。配線は .claude/settings.json。
#   session-start : 失敗台帳の直近を文脈に入れる（絶対指示の台帳は CLAUDE.md が取り込む）。開始時点の状態を記録。
#   prompt        : 毎回の依頼に短い型を添える（訂正かどうかの判断は言葉の一致でなく読む側に任せる）。
#   pre-tool      : 触ってはいけない対象の名前を含む操作を止める（うっかりを止める関所。意図的な回避までは防げない）。
#   stop          : 回帰検査が落ちていたら終了させない（同じ落ち方につき 3 回まで）。
#                   変更があれば、その変更状態につき一度だけ終了前の自己監査を求める。
# 番人自身の故障でセッションを塞がない: 想定外の例外は終了コード 1（止めない）で抜ける。
import sys, json, os, re, subprocess, hashlib, pathlib, tempfile

ROOT = pathlib.Path(os.environ.get('CLAUDE_PROJECT_DIR') or pathlib.Path(__file__).resolve().parent.parent)
FAILS = ROOT / '.claude' / 'FAILURE_LOG.md'
# 基盤スキルの禁則。名前の一部で、大文字小文字を区別せずに見る。
FORBIDDEN = re.compile('visualgate', re.I)
# 本文に禁則の名前を含みうる編集系の道具は、パスだけを見る（スキルや台帳の編集を止めないため）。
PATH_ONLY_TOOLS = {'Edit', 'Write', 'MultiEdit', 'NotebookEdit'}
PATH_KEYS = ('file_path', 'path', 'notebook_path')
INV_BLOCK_CAP = 3


def git(*args):
    try:
        r = subprocess.run(['git', '-C', str(ROOT), '-c', 'core.quotepath=off', *args], capture_output=True)
    except OSError:
        return ''
    return r.stdout.decode('utf-8', 'replace').strip('\n') if r.returncode == 0 else ''


def state_dir():
    gd = git('rev-parse', '--absolute-git-dir')
    if gd:
        d = pathlib.Path(gd) / 'claude-guard'
    else:  # git が使えないときはリポジトリの外に置く（差し戻しの回数だけは数えられるように）
        d = pathlib.Path(tempfile.gettempdir()) / ('claude-guard-' + hashlib.sha256(str(ROOT).encode()).hexdigest()[:16])
    d.mkdir(parents=True, exist_ok=True)
    return d


def state_path(session):
    return state_dir() / ((re.sub(r'[^A-Za-z0-9_-]', '', str(session or '')) or 'nosession')[:80] + '.json')


def load_state(session):
    p = state_path(session)
    try:
        st = json.loads(p.read_text()) if p.exists() else {}
        return st if isinstance(st, dict) else {}
    except ValueError:
        return {}


def save_state(session, st):
    state_path(session).write_text(json.dumps(st))


def tail_entries(path, n):
    if not path.exists():
        return ''
    parts = re.split(r'(?m)^(?=## )', path.read_text(encoding='utf-8', errors='replace'))
    return parts[0] + ''.join(parts[1:][-n:])


def changed(base):
    """基準から変わっているファイルと、その中身の指紋。commit しても中身が同じなら指紋は変わらない。"""
    names = set(filter(None, git('diff', '--name-only', '-z', base or 'HEAD').split('\0')))
    names |= set(filter(None, git('ls-files', '--others', '--exclude-standard', '-z').split('\0')))
    h = hashlib.sha256()
    for f in sorted(names):
        h.update(f.encode('utf-8', 'replace') + b'\0')
        p = ROOT / f
        if p.is_file():
            with p.open('rb') as fh:
                for chunk in iter(lambda: fh.read(1 << 20), b''):
                    h.update(chunk)
        else:
            h.update(b'<deleted>')
        h.update(b'\0')
    return sorted(names), h.hexdigest()


def session_start(inp):
    print('【失敗台帳（直近 8 件）— 同じ失敗を繰り返さない。絶対指示の台帳は CLAUDE.md から読み込み済み】\n' + tail_entries(FAILS, 8))
    sid = inp.get('session_id')
    st = load_state(sid)
    if 'base' not in st:
        st['base'] = git('rev-parse', 'HEAD')
        files, fp = changed(st['base'])
        st['audited'] = fp        # 開始前からあった変更は、このセッションの監査対象にしない
        st['preexisting'] = files
        save_state(sid, st)


def prompt(inp):
    lines = ['[鍵山ガード] ①依頼を番号つきの要件に分ける ②触るのは要件に必要な箇所だけ（ついでの改善をしない）'
             ' ③終わる前に要件ごとに「済／未」と証拠を報告 ④外に出る操作は明示の一言まで実行しない'
             ' ⑤実装→実装者デバッグ→他者コードレビュー→本番反映 を飛ばさない']
    lines.append('[鍵山ガード] ⑥この依頼が鍵山からの訂正・再指摘（直っていない、壊れた、頼んでいない所が変わった、前にも言った など）'
                 'なら、直す前に前回なにを外したかを特定し、同じターンで .claude/FAILURE_LOG.md に 1 件追記する。'
                 '「今後ずっと」の指示なら .claude/STANDING_ORDERS.md にも足す。訂正でなければ何も書かない。')
    print('\n'.join(lines))


def strings(v):
    if isinstance(v, str):
        yield v
    elif isinstance(v, dict):
        for x in v.values():
            yield from strings(x)
    elif isinstance(v, list):
        for x in v:
            yield from strings(x)


def pre_tool(inp):
    ti = inp.get('tool_input')
    if not isinstance(ti, dict):
        return
    if inp.get('tool_name') in PATH_ONLY_TOOLS:
        targets = [ti.get(k) for k in PATH_KEYS if isinstance(ti.get(k), str)]
    else:
        targets = list(strings(ti))
    if any(FORBIDDEN.search(t) for t in targets):
        sys.stderr.write('鍵山ガード: 基盤スキルの禁則の対象の名前を含む操作なので取りやめる'
                         '（読む・開く・cd・照会・push・検索・言及すべて禁止。コミット文や検索語に名前を入れるのも不可）。\n')
        sys.exit(2)


def stop(inp):
    sid = inp.get('session_id')
    st = load_state(sid)
    # 回帰検査は、ほかのフックに差し戻された直後でも必ず走らせる。
    try:
        chk = subprocess.run([sys.executable, str(ROOT / 'tools' / 'check_invariants.py')], capture_output=True)
        failed, log = chk.returncode != 0, (chk.stdout + chk.stderr).decode('utf-8', 'replace')
    except OSError as e:
        failed, log = True, str(e)
    if failed:
        sig = hashlib.sha256(log.encode()).hexdigest()
        n = st.get('inv_blocks', 0) if st.get('inv_sig') == sig else 0  # 落ち方が変わったら数え直す
        if n < INV_BLOCK_CAP:
            st['inv_sig'], st['inv_blocks'] = sig, n + 1
            save_state(sid, st)
            print(json.dumps({'decision': 'block', 'reason':
                  '回帰検査 tools/check_invariants.py が落ちている（%d/%d 回目の差し戻し）。壊した箇所を直す。'
                  '鍵山の指示による意図した変更なら、検査側を同じ変更で更新し、その旨を報告する。'
                  '直せないなら、落ちている検査をそのまま鍵山に報告する。\n' % (n + 1, INV_BLOCK_CAP) + log[-3000:]},
                  ensure_ascii=False))
            return
        # 同じ落ち方で 3 回差し戻したあとは、検査では差し戻さない。次に監査が出るとき、落ちている旨を項目に足す
    elif st.get('inv_blocks'):
        st['inv_blocks'], st['inv_sig'] = 0, ''
        save_state(sid, st)
    if inp.get('stop_hook_active'):
        return  # 監査の差し戻しは 1 回の終了につき 1 度だけ（ループ防止）
    if 'base' not in st:  # 開始の記録がないセッション: ここを基準にする（これより前の commit は監査できない）
        st['base'] = git('rev-parse', 'HEAD')
        save_state(sid, st)
    files, fp = changed(st.get('base'))
    if files and st.get('audited') != fp:
        st['audited'] = fp
        save_state(sid, st)
        pre = set(st.get('preexisting') or [])
        shown = '\n'.join('  - ' + f + ('（開始前から変更あり）' if f in pre else '') for f in files[:60])
        if len(files) > 60:
            shown += '\n  …ほか %d 件' % (len(files) - 60)
        print(json.dumps({'decision': 'block', 'reason':
              '終了前の自己監査（この変更状態につき一度だけ）。セッション開始時の commit から変わっているファイル'
              '（自分の変更でないものが混じることがある。その場合は自分の分だけ確かめる）:\n' + shown + '\n'
              '1) git diff を実際に読み、自分の変更行がすべて依頼の要件に対応するか確認する。対応しない変更は元に戻す。\n'
              '2) 依頼の要件を番号で列挙し、それぞれ「済（証拠: 実行した検査と結果）／未（理由）」を鍵山への報告に書く。'
              '言われたのに直していない項目を残さない。\n'
              '3) 直した箇所の周辺で、もともと動いていたものが今も動くことを確かめたか。確かめていないものは「未確認」と書く。\n'
              '4) コードや設定を変えたなら、他者コードレビュー（critical-reviewer エージェント）の OK を得たか。'
              'NG なら直して再レビュー。\n'
              + ('5) 回帰検査が落ちたまま。落ちている項目をそのまま鍵山への報告に書く。\n' if failed else '') +
              '済んでいれば、その結果を報告に含めて終了してよい。'}, ensure_ascii=False))


MODES = {'session-start': session_start, 'prompt': prompt, 'pre-tool': pre_tool, 'stop': stop}

if __name__ == '__main__':
    try:
        for s in (sys.stdout, sys.stderr):
            s.reconfigure(encoding='utf-8', errors='replace')
        fn = MODES.get(sys.argv[1] if len(sys.argv) > 1 else '')
        if fn is None:
            sys.exit(0)
        try:
            data = json.loads(sys.stdin.buffer.read().decode('utf-8', 'replace') or '{}')
        except ValueError:
            data = {}
        fn(data if isinstance(data, dict) else {})
    except SystemExit:
        raise
    except Exception as e:  # 番人の故障で作業を塞がない
        sys.stderr.write('claude_guard: 内部エラーのため今回は素通し: %r\n' % (e,))
        sys.exit(1)
