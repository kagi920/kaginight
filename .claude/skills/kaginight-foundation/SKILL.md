---
name: kaginight-foundation
description: KAGI NIGHT（XR Drummer 鍵山喬一）のホームページ・BASE ショップ・GitHub Pages・note・グッズという「基盤」を設計・更新するときの手順と禁則。ホームページ、クラゲ、BASE、テーマ、貼り付け、GitHub Pages、kaginight、SOUND、note、グッズ、KEY、KAGI ROOM、ONLINE、LIVE のどれかが話題に出たら、頼まれていなくても必ずこのスキルを読んでから作業する。鍵山の価値を上げる方向にだけ動き、禁則に触れる提案はしない。
---

# KAGI NIGHT 基盤設計スキル

鍵山喬一（kagi920 / @KAGI920）の「基盤」は 4 つの面でできている。どれを触るときも、他の 3 面との整合を先に確認する。

| 面 | 場所 | 役割 |
|---|---|---|
| 独自 HP | https://kagi920.github.io/kaginight/ （repo kagi920/kaginight、`index.html` 1 枚） | 名刺。クラゲ＋音＋5 つの扉 |
| BASE | https://kaginight.base.shop/ （HTML編集 App のテーマに差し込み） | 物販。同じクラゲを `kn-` 接頭辞で埋め込む |
| note | 既存アカウント（表示名 鍵山喬一、登録 kagiyama1707@gmail.com） | 有料記事で稼ぐ。URL は本人から受け取る |
| グッズ | 受注生産・在庫ゼロ（BASE の印刷 App か SUZURI） | 作る前に必ず鍵山に絵柄と販売先を確認 |

元アイデアの台帳は `docs/IDEA_LEDGER.md`。決定・保留・やらないこと が分かれているので、提案の前に必ず読む。

## 先に守る禁則（鍵山の明言）

これらは好みではなく指示なので、代替案を出さずに従う。
- 鍵山ソロのみ。他メンバーの名前・顔・アバターは出さない。人物の点群は使わない。
- 価格を作らない（実在は ¥7,170 のみ）。KEY の特典や商品を創作しない。
- 職・収入・健康などの私的情報を HP とリポジトリに書かない。
- visualgate-livesystem の成果を鍵山の制作物として書かない。
- クラゲのヒーローは変えない（「クラゲのところはいいんだよ」）。追加はクラゲに合わせる。
- 音は SOUND ボタンからだけ。自動再生しない。
- BASE 必須タグ（`{LogoTag}` など）を消さない・隠さない。本番への「適用」は鍵山の OK 後。
- 文章はお客さん向け。「準備中」「決まってない」「何も売っていない」を書かない。
- PR は作らない。`main` に直接 push する（鍵山の指示）。

## 共有エンジンの構造

`index.html` の `<script>` は 3 つの塊でできている。順番と境界を崩さない。
1. `LINKS` — URL 差し替え表。空文字なら導線は「ここで公開」の文言のまま。
2. `window.KN_AUDIO` — 手続き音（`/* KAGI NIGHT sound:` で始まり `})();` で終わる IIFE）。`start/stop/toggle/kick/hit/isOn/state`。
3. `window.KN` — WebGL 点群エンジン。`KN({pre:'',stage:null,canvas:'gl'})` が独自 HP、`KN({pre:'kn-',stage:'kn-stage',canvas:'kn-gl'})` が BASE。

音と絵の同期点は 2 か所だけ: ヒーローの鐘が収縮する周期で `KN_AUDIO.kick()`、タップで `KN_AUDIO.hit()`。ここを壊すと「曲がクラゲに合わない」に戻る。

## 更新の手順（毎回この順）

1. **台帳を読む** → 変更が「決定」と矛盾しないか、「やらない」に触れないか確認。
2. **1 か所だけ直す**。エンジンや音は `kn_engine.js` / `kn_audio.js` を直し、正規表現で両 HTML に差し込む（手で 2 回書かない）。
3. **BASE 一式を再生成**: 元テーマ（鍵山が貼ったもの、無改変）＋ `<body … class="shop template">` 直後に挿入ブロック＋最初の `</header>` 直後に紹介文と扉。
4. **検査**: ブロックタグ `{block:X}` と `{/block:X}` の数が一致、必須タグあり、CSS は全部セミコロン終端、JS エラー 0。
5. **実機想定の検証**: Playwright（`--use-gl=swiftshader`）で 390×844 のスクショ、iPhone UA で SOUND をタップして `state==='running'`、出力 RMS が 0 より大きいこと。
6. **公開**: `index.html` を repo に commit → `git push -u origin main`。貼り付けページ（1 ボタンコピー）は見出しの版番号を上げてから再公開。鍵山には「⌘R で開き直す」と「BASE は全文を貼り直す」を毎回伝える。
7. **報告**: 何が変わったか 3 行、鍵山がやる操作 1〜3 手、保留の判断事項。

## 落とし穴（実際に踏んだもの）

- BASE テーマの `word-break:break-all` は英字ボタンを縦に割る → ステージ内は `word-break:normal` と `white-space:nowrap`。
- `body.shop a` が文字色を上書きする → ステージ内のリンク色は `!important`。
- `{a:b}` 形はテンプレートタグに見える → CSS 宣言は必ず `;` で終える。`@media` も中身を `;` 終端に。
- Chrome の `backdrop-filter` が BASE 内で四角い残像を作る → ステージ内では使わない。
- ハッシュアンカーは `overflow:hidden` のステージをスクロールさせる → `[data-kn-open]` クリックで JS が開き、`stage.scrollTop=0` を固定。
- iPhone Safari はマナースイッチで Web Audio が消音 → SOUND と同じタップで無音 `<audio>` を loop 再生。中断後は `touchend` で `ctx.resume()`。
- 貼り付けページのコピー処理が assert で止まると古い版が残る → 版番号を見出しに出し、`html.unescape` で往復一致を検証。
- ヘッドレスで暗いのは正常。明るさはスクショで判断せず、実機の報告を優先。
- この環境から note.com・x.com・Wayback・Pages API は届かない。URL は鍵山に聞く。

## 提案のしかた

- 提案は「鍵山の値段を上げるか」「作業が 10 秒で済むか」で選ぶ。長い選択肢の列挙より、推し 1 つと理由 2 行。
- 調査結果の数字は実測だけ書く。推定は「だいたい」と明記。
- 新しいグッズ・記事・会員特典は、絵柄・文面・価格を**作る前に**鍵山に見せる。
- 成果物は必ず URL（GitHub Pages、貼り付けページ）で渡す。ファイルパスだけで終わらない。

## 参照

- `references/structure.md` — ページ構成と各扉の文面、LINKS のキー一覧、BASE 挿入点
- `docs/IDEA_LEDGER.md` — 元アイデアの台帳（決定／保留／やらない）
