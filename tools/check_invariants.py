#!/usr/bin/env python3
# 回帰検査: 「ここを直したら別のところが壊れた」を機械で止める。
# 壊れてはいけない事実を 1 行ずつ足していく。鍵山が「これは絶対」と言ったものは、文章だけでなくここにも入れる。
# 使い方: python3 tools/check_invariants.py   （失敗があれば終了コード 1）
import json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
fails = []


cache = {}


def read(rel):
    if rel not in cache:
        p = ROOT / rel
        if p.is_file():
            cache[rel] = p.read_text(encoding='utf-8', errors='replace')
        else:
            fails.append('%s: ファイルがない' % rel)
            cache[rel] = None
    return cache[rel]


def has(rel):
    return read(rel) is not None


def must(rel, needle, why):
    if has(rel) and needle not in read(rel):
        fails.append('%s: %s（必要な文字列: %s）' % (rel, why, needle[:60]))


def must_not(rel, pattern, why):
    m = has(rel) and re.search(pattern, read(rel))
    if m:
        fails.append('%s: %s（見つかった: %s）' % (rel, why, m.group(0)[:60]))


# --- 公開面: index.html は kaginight.pages.dev への転送（2026-10-17 の決定） ---
must('index.html', "location.replace('https://kaginight.pages.dev/'+location.search+location.hash)", '転送がクエリとハッシュを保つこと')
must('index.html', '<meta http-equiv="refresh" content="0; url=https://kaginight.pages.dev/">', 'JS なしでも転送されること')
must('index.html', '<link rel="canonical" href="https://kaginight.pages.dev/">', 'canonical が新 URL を指すこと')
must('index.html', '<meta name="robots" content="noindex">', '旧 URL を検索に載せないこと')
must('robots.txt', 'Sitemap: https://kaginight.pages.dev/sitemap.xml', 'robots が新 URL の sitemap を指すこと')
if has('VERSION') and not re.fullmatch(r'\d+\n?', read('VERSION')):
    fails.append('VERSION: 整数の版番号だけであること')
if not (ROOT / '.nojekyll').exists():
    fails.append('.nojekyll: ファイルがない')

# --- 基盤スキルの禁則が消されていないこと ---
SKILL = '.claude/skills/kaginight-foundation/SKILL.md'
for needle, why in [
    ('外に出る操作（メール送信・投稿・push・公開・申請）は、その操作ごとに鍵山の明示の一言', '外向き操作の禁則'),
    ('は超禁止。push だけでなく、読む・開く・cd する・API で照会する・言及することも含めて一切触らない', '触れてはいけないリポジトリの禁則'),
    ('職・収入・健康などの私的情報を HP とリポジトリに書かない', '私的情報を書かない禁則'),
    ('他人のリポジトリには一切 push しない', '他人のリポジトリへの push 禁止'),
    ('鍵山ソロのみ', 'ソロのみの禁則'),
    ('価格を作らない', '価格を創作しない禁則'),
    ('クラゲのヒーローは変えない', 'クラゲ不変の禁則'),
    ('音は SOUND ボタンからだけ', '自動再生しない禁則'),
    ('モチーフを画面に貼ること', '貼り付け演出の禁止'),
]:
    must(SKILL, needle, '%s が残っていること' % why)

# --- 作業の型と台帳が消されていないこと（台帳は追記だけ。項目が減ったら落ちる） ---
must('CLAUDE.md', '実装 → 実装者デバッグ → 他者コードレビュー → 本番反映', '4 段の作業の型')
if has('CLAUDE.md'):
    if not re.search(r'(?m)^@\.claude/STANDING_ORDERS\.md\s*$', read('CLAUDE.md')):
        fails.append('CLAUDE.md: 絶対指示の台帳を取り込む行（@.claude/STANDING_ORDERS.md だけの行）があること')
    if '```' in read('CLAUDE.md'):
        fails.append('CLAUDE.md: コードの囲み（```）を使わないこと（囲みの中の取り込み行は読み込まれない）')
for i in range(1, 9):
    must('.claude/STANDING_ORDERS.md', '\n## O-%02d ' % i, '絶対指示 O-%02d が残っていること' % i)
for i in range(1, 4):
    must('.claude/FAILURE_LOG.md', '\n## F-%02d ' % i, '失敗 F-%02d の記録が残っていること' % i)
for needle in ('実装者ではない', 'この状況で／こうすると／こうなるからダメ', '判定: `OK` か `NG`', 'tools: Read, Grep, Glob, Bash'):
    must('.claude/agents/critical-reviewer.md', needle, 'レビュー担当の定義が残っていること')

# --- push の宛先: origin があるなら、その push 用 URL がすべて鍵山のリポジトリであること（台帳 O-08） ---
# 見るのはこの clone の origin だけ。ほかの remote、git 以外の道具による push、ホスト名までは見ない。
try:
    r = subprocess.run(['git', '-C', str(ROOT), 'remote', 'get-url', '--push', '--all', 'origin'], capture_output=True, timeout=30)
    urls = r.stdout.decode('utf-8', 'replace').split() if r.returncode == 0 else []
except (OSError, subprocess.TimeoutExpired):
    urls = []
for url in urls:
    if not re.search(r'[:/]kagi920/kaginight(\.git)?/?$', url):
        fails.append('git remote origin: push の宛先が kagi920/kaginight ではない（%s）。push・マージをしないこと' % url[:80])

# --- 設定: フックが番人に正しく配線され、切られていないこと ---
GUARD = 'tools/claude_guard.py'
try:
    cfg = json.loads(read('.claude/settings.json') or '{}')
    if not isinstance(cfg, dict) or not isinstance(cfg.get('hooks'), dict):
        fails.append('.claude/settings.json: hooks が設定されていること')
    else:
        for ev, mode in (('SessionStart', 'session-start'), ('UserPromptSubmit', 'prompt'), ('PreToolUse', 'pre-tool'), ('Stop', 'stop')):
            want = 'f="$CLAUDE_PROJECT_DIR/%s"; [ -f "$f" ] || exit 0; python3 -B "$f" %s' % (GUARD, mode)
            groups = cfg['hooks'].get(ev)
            cmds = [h.get('command') for g in groups if isinstance(g, dict) and not g.get('matcher')
                    for h in (g.get('hooks') or []) if isinstance(h, dict)] if isinstance(groups, list) else []
            if want not in cmds:
                fails.append('.claude/settings.json: %s に番人の命令が絞り込みなしで配線されていること（%s）' % (ev, want))
        if cfg.get('disableAllHooks'):
            fails.append('.claude/settings.json: disableAllHooks でフックを切らないこと')
        if cfg.get('effortLevel') not in ('high', 'xhigh'):
            fails.append('.claude/settings.json: effortLevel が high か xhigh であること')
        if cfg.get('switchModelsOnFlag') is not False:
            fails.append('.claude/settings.json: switchModelsOnFlag が false であること')
except ValueError as e:
    fails.append('.claude/settings.json: JSON として読めない（%s）' % e)

# --- 番人が実際に働くこと（禁則の名前を含む操作を止め、普通の操作は通す） ---
if has(GUARD):
    def guard(mode, payload):
        try:
            return subprocess.run([sys.executable, '-B', str(ROOT / GUARD), mode], input=json.dumps(payload).encode(),
                                  capture_output=True, timeout=30)
        except (OSError, subprocess.TimeoutExpired):
            return None
    name = 'Visual' + 'Gate-LiveSystem'
    for tool, ti, want in (('Bash', {'command': 'ls ../' + name}, 2), ('Glob', {'pattern': name.lower() + '/**'}, 2),
                           ('Read', {'file_path': '/x/' + name + '/a'}, 2), ('Bash', {'command': 'ls'}, 0),
                           ('Edit', {'file_path': str(ROOT / 'CLAUDE.md'), 'old_string': name}, 0)):
        r = guard('pre-tool', {'tool_name': tool, 'tool_input': ti})
        if r is None or r.returncode != want:
            fails.append('%s: pre-tool の自己試験（%s）が終了コード %d を返すこと' % (GUARD, tool, want))
    r = guard('prompt', {'prompt': 'x'})
    if r is None or r.returncode != 0 or 'FAILURE_LOG.md' not in r.stdout.decode('utf-8', 'replace'):
        fails.append('%s: prompt が型と訂正時の追記の決まりを出すこと' % GUARD)
    for needle in ("'decision': 'block'", 'check_invariants.py'):
        must(GUARD, needle, '終了前の検査と監査が残っていること')

# --- 私的情報・秘密をリポジトリに入れない ---
for rel in ('CLAUDE.md', '.claude/STANDING_ORDERS.md', '.claude/FAILURE_LOG.md', '.claude/agents/critical-reviewer.md', '.claude/settings.json',
            'tools/claude_guard.py', 'tools/check_invariants.py', 'docs/CLAUDE_QUALITY_SPEC_v1.html', 'index.html', 'README.md'):
    must_not(rel, r'[A-Za-z0-9._%+-]+@(gmail|yahoo|icloud|outlook)\.[a-z.]+', 'メールアドレスを書かないこと')
    must_not(rel, r'(sk-ant-|ghp_|github_pat_)[A-Za-z0-9_-]{10,}', '鍵・トークンを書かないこと')

if fails:
    print('回帰検査 NG（%d 件）' % len(fails))
    for f in fails:
        print(' - ' + f)
    sys.exit(1)
print('回帰検査 OK')
