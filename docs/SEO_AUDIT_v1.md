# 発見性（検索・SNS の推薦）監査と改善 v1 — 2026-10-15

依頼: 「アルゴリズムを使ってホームページの価値を上げてほしい。専門家の作法で」。
解釈: 検索エンジンと SNS の推薦（ランキング）に、HP がどう扱われるかを上げる。
作法（SEO／発見性の技術者の手順）: ① 計測して現状を数字で出す → ② 検索意図と競合を調べる → ③ 効果×確度×手間で優先順位 → ④ 実装 → ⑤ 計測の仕組みを入れ、4 週ごとに見る。推測で直さない。

## 1. 計測（2026-10-15、ローカル配信＋ヘッドレス Chromium、iPhone 相当の UA。実機・実回線ではない「ラボ値」）
| 項目 | v26（前） | v27（後） | 判定の根拠 |
|---|---|---|---|
| Google Fonts の CSS | 61,679 B、描画を止める 445 ms | 1,057 B ＋ 2,576 B | CSS が 100 以上の unicode-range に分割されていた |
| フォントのファイル数 | 35 | 3 | Noto Serif JP を**使っている字だけ**（421 字形）に絞った |
| load | 2,717 ms | 1,806 ms | |
| LCP（最大コンテンツ描画） | 2,156 ms | 1,228 ms | Core Web Vitals の良好は 2.5 s 以下（75 パーセンタイル、実機データ） |
| CLS（レイアウトのずれ） | 0 | 0 | 良好は 0.1 以下 |
| OG 画像 | og.png 832 KB | og.jpg 87 KB | SNS のカード生成が速くなる |
| HTML | 64.8 KB、1 ファイル、外部 JS なし | 同じ | |
| 本文テキスト | 約 1,500 字 | 同じ | **薄い**（§4 の最優先） |
| 構造化データ | Person のみ | WebSite ＋ Person（画像つき）＋ MusicEvent（2026-07-17 unravel tokyo） | Google の Event 構造化データの必須項目（name, startDate, location）を満たす |
| 見出し | h1 1、h2 5、img 0 | 同じ | |
| robots / sitemap / canonical / OG / Twitter card | あり | lastmod 更新 | |

注: ヘッドレスはソフトウェア描画なので long task の値は実機を代表しない。INP は実機でしか測れない。

## 2. 検索の現状（2026-10-15、米国経由の検索結果の抜粋。日本の結果は鍵山が確認）
- 「XRドラマー」: 競合する結果が無い。**この語は HP が独占できる**（title・h1・description に既にある）。
- 「KAGI NIGHT」: Metropolis Japan のイベントページ（2026 Vol.1 “Night of Collision”）と MoguraVR の記事（2022、Beat Wave）が出る。どちらも HP への**被リンク候補**。Metropolis の表記が「鍵山共一」になっている可能性があり、表記ゆれは人物認識を弱める（鍵山が確認して修正依頼）。
- 「鍵山喬一」: Wikipedia の記事がある（構造化データの sameAs に登録済み）。

## 3. 根拠（公式・一次に近いもの）
- JavaScript の描画と索引: Google は「クロール → レンダリング → インデックス」の 3 段階。HTML に最初から入っている文章は確実（[Google Search Central: JavaScript SEO の基本](https://developers.google.com/search/docs/ajax-crawling)）。この HP の 5 つの扉の文章は HTML に最初から入っている。
- 折りたたみ・タブの中の文章: モバイルファーストでは HTML にあるものは全部索引に入り、重みも下げない（John Mueller 2020、Gary Illyes 2016。[Search Engine Journal](https://www.searchenginejournal.com/googles-mueller-on-myth-of-hidden-tab-content/358724/)）。
- Event 構造化データ: name・startDate・location が必要、eventStatus は推奨（[Google: Event 構造化データ](https://developers.google.com/search/docs/appearance/structured-data/event)）。
- Core Web Vitals: LCP 2.5 s、INP 200 ms、CLS 0.1 が「良好」。2021 年からページ体験の順位信号（[まとめ](https://www.mintlify.com/addyosmani/web-quality-skills/concepts/thresholds)、原典は web.dev）。

## 4. 残りの優先順位（効果 × 確度 × 手間）
| 順 | 施策 | 効果 | 確度 | 手間 | 誰が |
|---|---|---|---|---|---|
| 1 | **本文を増やす**: 「KAGI NIGHT とは何か」「どう参加するか」「鍵山は何者か」を HP 内の文章として 600〜1,000 字置く（扉の中でよい）。検索は文章で意味を取る | 大 | 高 | 中（鍵山の承認が要る） | 制作担当が §5 の草案 → 鍵山が直す |
| 2 | **Google Search Console** に登録（所有権確認はメタタグか HTML ファイル。制作担当が置ける） | 大（計測の土台） | 高 | 小 | 鍵山がアカウント、制作担当が設置 |
| 3 | **被リンク**: Metropolis のイベントページと MoguraVR 記事に HP の URL を載せてもらう依頼。note・X・Instagram のプロフィールのリンクを HP に統一（済みの部分あり） | 大 | 中 | 小 | 鍵山 |
| 4 | Wikipedia の記事の外部リンクに公式サイトを置く。本人による編集は利益相反として嫌われるので、ノートページで依頼する形が作法 | 中 | 中 | 小 | 鍵山 |
| 5 | 次の KAGI NIGHT の日時が決まったら MusicEvent を「今後の公演」として更新（リッチリザルトの対象は今後の公演） | 中 | 高 | 小 | 制作担当 |
| 6 | 訪問計測（Cloudflare Web Analytics か GoatCounter） | 中 | 高 | 小 | 鍵山がアカウント |
| 7 | 画像: 鍵山本人の写真を 1 枚（Person.image と OG に使える。顔が出る写真は本人の判断） | 中 | 中 | 小 | 鍵山 |

やらないこと: meta keywords の調整（Google は無視）、キーワードの詰め込み、隠しテキスト、被リンクの購入。

## 5. 本文の草案（§4-1。鍵山の承認後に入れる。**まだ HP には入れていない**）
扉「LIVE」または「PROFILE」の末尾に置く想定。既存の文を骨にして、検索で聞かれる 3 つの問いに答える形。
```
KAGI NIGHT は、XR ドラマー 鍵山喬一が企画する夜。鍵山が実際に叩いた一打が、そのまま光と空間と人の動きになる。
配信からは、スマホか PC のブラウザで参加する。現地では、会場で QR を読んで参加する。どちらも、見るだけでなく、叩く人として参加できる。
これまでに、KAGI NIGHT 2022（渋谷 B.Y.G）、KAGI NIGHT 2026 Vol.1「衝突の夜」（六本木 unravel tokyo）を開催。
鍵山喬一は埼玉県出身。1998 年ごろから都内のライブハウスで叩きはじめ、cocobat、JUDGEMENT、アーバンギャルドを経て、多くのアーティストのサポートドラマーとして活動している。
```

## 6. 計測の仕組み（入れたら 4 週ごとに見る）
- Search Console: 表示回数・クリック・掲載順位を「XRドラマー」「KAGI NIGHT」「鍵山喬一」で追う。
- Core Web Vitals は Search Console の「ウェブに関する主な指標」で実機データが見える。
- X のリンククリック数（`docs/X_VERIFICATION_AND_UPDATE_SPEC_v1.md` §B-4）。
