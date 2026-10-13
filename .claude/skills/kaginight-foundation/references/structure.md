# 構成リファレンス

## 独自 HP（index.html）の UI
- 左上 `.mark`: KAGI NIGHT / XR DRUMMER 鍵山喬一
- `#snd`: SOUND · OFF ↔ SOUND · ON（iPhone では ON 時に 7 秒ヒント）
- 右上 `.hint`: DRAG · ROTATE / PINCH · ZOOM / TAP · HIT（640px 以下は非表示）
- 左下 `#split`: 縦スライダー 融（100）↔ 分（0）
- 右下 `#hit`: 金の円、一打
- 下 `.dock`: ONLINE / LIVE / GOODS（BASE へ外部リンク）/ KEY
- シート `#online` `#live` `#support`（KEY）: `.meta` に NEXT / PLACE（PLACE は「スマホ・PC どちらでも」）、`.bar` が導線、`.steps` が 4 手順

## LINKS のキー
`online` 配信参加 URL / `live` 現地 QR の URL / `room` KAGI ROOM / `ks` `km` `kl` KEY S/M/L / `tee` `shop` BASE。空なら導線文言は変えない。

## BASE 挿入点
- 挿入ブロック: `{block:IndexPage}{block:NoIndexPageSearch} … {/block:NoIndexPageSearch}{/block:IndexPage}` ＋ スキン `<style>`。`<body … class="shop template">` の直後。
- 紹介文と 5 つの扉（`.kn-door`、`data-kn-open` でシートを開く）: 最初の `</header>` の直後。
- GOODS: `<a id="kn-goods" href="{block:AppsSearch}{SearchPageURL}{/block:AppsSearch}">`。検索 App が無いときだけ JS が `kn-showitems` を付けて一覧を表示。
- PROFILE → `{AboutPageURL}`、CONTACT → `{ContactPageURL}`。
- 商品一覧の既定は非表示: `body#shopTopPage:not(.kn-showitems) #mainContent.itemList{display:none;}`

## 紹介文（決定版）
「XR DRUMMER 鍵山喬一の夜。配信からも、現地からも、叩く人として参加できる。」
GOODS 見出し: GOODS / 叩いた人の服

## 音の設計
D ドリアン: Dm9 → Fmaj7(9) → Gm7(11) → Am7(9)、1 コード 5 秒（クラゲの 1 泳ぎ）。サブは各コードのルート。ティック 1.25 秒、ガラス 0.625 秒＋ディレイ 0.375 秒、コンボルバー 3.2 秒。マスター 0.62、立ち上がり 0.35 秒。
