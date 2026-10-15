# KAGI NIGHT 基盤づくり — 元アイデア台帳（2026-10-13 時点）

このチャットで出た「元のアイデア」を、決まったこと／保留／やらないこと に分けて記録する。
作業の正本はこの台帳と `.claude/skills/kaginight-foundation/SKILL.md`。

## 1. 核になるアイデア（決定）

| # | アイデア | 状態 |
|---|---|---|
| 1 | ホームページの主役は **WebGL 点群のクラゲ**（holtsetio/aurelia の鐘の収縮・縁のフリル・触手・口腕・光のパルス・コースティクスを raw WebGL1 に移植）。クラゲの群れが上へ泳ぎ、下から戻る | 完成・公開中 |
| 2 | **iPhone と Android でそのまま見られる**こと。依存ライブラリなし、1 ファイル、viewport と safe-area を持つ。Android 向けにシェーダー精度の自動切替と描画失敗時の案内（v11） | 完成 |
| 3 | 開いたときの**組み上がる演出**（intro アセンブリ）、グリッチ行、タップで一打（hit scatter）、右の金の鍵、左のダイヤル「融／分」 | 完成 |
| 4 | **音**は手続き生成ループ（D ドリアンのパッド、鐘の収縮にキック、ティック、ガラスのアルペジオ、タップでスネア）。**SOUND ボタンを押したときだけ**鳴る。iPhone のマナースイッチを回避する無音アンロック入り | 完成（v10） |
| 5 | **二重配置**: (a) BASE ショップのテーマ（HTML編集 App）に差し込む、(b) 独自ホームページ **https://kagi920.github.io/kaginight/**（GitHub Pages、ずっと無料） | 両方稼働 |
| 6 | ページ構成: ヒーロー → BASE 必須ロゴ（金枠）＋HOME/ABOUT/CONTACT → 紹介文 → **5 つの扉**（ONLINE / LIVE / KEY / PROFILE / CONTACT）→ GOODS → フッター | 完成 |
| 7 | **商品は同じページに並べない**。GOODS は商品検索 App の検索ページへ飛ばす。無い場合だけ一覧を表示 | 完成 |
| 8 | 文章は**お客さん向け**。「準備中」「決まってない」「何も売っていない」は書かない。KEY（KAGI ROOM）は COMING SOON として価格を出さない | 完成 |
| 10 | **3D モーション参照の学習を反映（v13）**: 一打で画角が開き距離を補正して主役の大きさを保つレンズ（dolly compensation、減衰ばね）、鐘の残像を視線奥行きに沿って 2〜3 体、ポインタ視差、時定数ベースの平滑化、フレーム時間のヒステリシス付き画質段階。主役の静止時の見た目は不変 | 完成 |
| 11 | **演出モード（スキン）切替**: いつもは元の HP（v21 の見た目）のまま。ライブやイベントが近づいたら、その夜の色に合わせて HP の演出を切り替える（例: サブカル寄りの夜→サブカル 30%／120%、ポップな夜→ポップ）。時間帯で少し変える案も。→ 同日さらに決定: **KAGI スキン＝方向 C を 120%**（赤い糸の網＋糸から吊るしたドアの鍵＋脇役が糸のクラゲ）を、**毎時 10 分間だけ**出す。基本のクラゲ（主役）は絶対に触らない。プレビュー `subcul/`、本番投入は GO 待ち | 決定（2026-10-15） |
| 9 | 稼ぎ方は **note の有料記事**（既存アカウントを使う）と **受注生産・在庫ゼロのグッズ** | 承認済み（「ノートいいよ」「曲もいいよ」） |

## 2. 元ネタ・参照

- 鍵山からの引き継ぎ資料（KAGI XR の A/B 検証・Charakuru・費用・Anatomy 原則）は `docs/kagixr_handoff/`。これはライブ演奏システム（Mac 演奏者画面＋iPhone 参加）の話で、ホームページのクラゲとは別系統。混同しない。

- 参考: https://holtsetio.com/lab/aurelia/ （コード https://github.com/holtsetio/aurelia 、MIT）
- 鍵山の公開リポジトリ: AeroDrumsOSCBridge（MIDI→OSC `/drum/*` 9000）、VisionDrumOSC（UDP 受信、7 アバター）、EtherealJellyfish（2025-07）
- 過去ライブ: KAGI NIGHT 2022 @ Shibuya B.Y.G + Beat Wave、KAGI NIGHT 2026 Vol.1「衝突の夜」@ unravel tokyo（2026-07-17）

## 3. 保留（鍵山の判断待ち）

- （解決）note は https://note.com/kagi03 。KEY シートからリンク済み（v14）
- 「水の夜」T シャツ絵柄（print_jellyfish_A）と販売先（BASE オリジナルプリント App か SUZURI）
- 金の鍵ロゴ 3 案、XR DRUMMER T シャツの版下
- 商品検索 App を入れるか（GOODS を一覧ページにするため）
- ONLINE / LIVE の参加 URL、KAGI ROOM の開く日と中身
- note 第 2・3 回の 20 分インタビュー

## 4. やらないと決めたこと

- 人物（アバター）の点群は 2D でもシーン内でも使わない（「なしだよ」「0 点」）
- 他メンバーの名前・顔・アバター、14 アバター T シャツ絵柄は使わない。鍵山ソロのみ
- 価格の創作（実在は ¥7,170 のみ）、KEY の会員特典や商品の創作
- 職・収入・健康などの私的情報を HP とリポジトリに載せない
- visualgate-livesystem の成果（XR_DRUM、GHOST RACK、Scratch Box）を鍵山の制作物として書かない
- BASE 必須タグの削除、LogoTag の非表示、自動再生の音
- 「128 BPM」表記、本番への「適用」を OK なしで押すこと、PR を作ること

## 5. 作業で学んだこと（次回の近道）

- BASE はプレビューのたびに**全文を貼り直す**。貼り付けページは 1 ボタンコピーにし、見出しに版番号を出す（「治ってない」の原因はキャッシュと古い貼り付け）
- テーマ CSS の `word-break:break-all` が英字ボタンを縦に割る → `white-space:nowrap`。`body.shop a` の色に負けるので `!important`
- BASE テンプレートタグ `{a:b}` と衝突しないよう、CSS は必ずセミコロン終端。ブロックタグの開閉数を毎回数える
- ハッシュアンカーは overflow:hidden のステージをスクロールさせる → JS で開き `scrollTop=0` 固定
- iPhone Safari はマナースイッチで Web Audio が消音される → 無音 `<audio>` をタップ内で再生して再生セッションへ
- GitHub Pages は `main` 直下の `index.html`。Pages API と新規リポジトリ作成はこの環境から不可（鍵山が手動）
- 検証は Playwright（swiftshader）でスクショ＋JS エラー 0＋音の RMS 計測
