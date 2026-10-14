# XR Drummer 鍵山喬一を研究で裏づける論文仕様書

**結論（BLUF）。** 6本の調査ノート（身体性・トラッキング／XRライブ観客研究／AI共創と経済／日本の発表先・助成／Webグラフィックス・音響／クリエイターエコノミー）を統合した結果、鍵山喬一（XR Drummer）がまず集めるべき文献・報告・一次資料は368件（ID付与分）に整理でき、それらが支える新規性は明確である。すなわち、**人間のXRドラマーがライブコンサートでリアルタイム映像・AIを駆動する査読研究は存在せず、Apple Vision Pro のハンドトラッキング精度・遅延の査読ベンチマークも存在せず、Beat Wave／KAGI NIGHT を扱った学術研究も存在しない**（[embodied_drumming_tracking KQ3/KQ6](https://roadtovr.com/apple-vision-pro-meta-quest-3-hand-tracking-latency-comparison/)、[xr_live_music_audience KQ4](https://www.moguravr.com/?p=187320)、[ai_cocreativity KQ1/KQ5](https://nime.org/proc/nime2025_54/)）。技術選択を正当化する実測値も揃っている。打楽器DMIでは**安定10 msは0 msと区別されず、20 msは劣化、10±3 msのジッタは20 ms相当**（[Jack et al. 2018](https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/44614/Jack%20Action-sound%20Latency%202018%20Accepted.pdf?sequence=1)）、一方で Quest 2 のハンドトラッキング遅延は**約45 ms**（[Abdlkarim et al. 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10830632/)）、Vision Pro は非査読推定で**約127.7 ms**（[Road to VR 2024](https://roadtovr.com/apple-vision-pro-meta-quest-3-hand-tracking-latency-comparison/)）であり、「発音はスティック側の高速経路、ヘッドセットは映像・位置用」という鍵山の設計は文献上必然である。観客側では VR 視聴が YouTube より物理的プレゼンスとアーティストとのつながりを高め（[Onderdijk et al. 2021](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.647929/full)）、完全仮想VRコンサートの支払意思額は**€35–39.99 帯**に集中する（[Bär et al. 2025](https://www.elsevier.es/en-revista-journal-innovation-knowledge-376-articulo-on-edge-digital-event-era-S2444569X25001210)）。実行面では、サイトに15件のRESEARCHセクションを追加し、2026-12-07締切の **IEEE VR 2027 Research Demos**（[公式CfP](https://ieeevr.org/2027/contribute/demos/)）を最初の査読付き発表先とし、次回 KAGI NIGHT で遅延・ジッタ・プレゼンス・支払意思額を計測して引用可能なデータを自ら作ることを本仕様書は指定する。検証フラグは原ノートの表記をそのまま転記し、DOI は原ノートに記載のあるもののみ掲載した。

---

## 1. 凡例 — 検証フラグは原ノートの表記をそのまま転記する

本仕様書の各文献には、調査ノートが付した検証フラグを改変せずに転記した。調査環境では doi.org・ACM DL・多くの出版社サイトがプロキシで遮断されていたため、DOI の多くは一次確認できていない。**「verified / ✔ / yes」以外のフラグが付いた DOI は引用前に必ず確認すること。** フラグの語彙はノートごとに異なるため、以下に対応表を示す。

| 原ノート | フラグ語彙 | 意味 |
|---|---|---|
| ① 身体性・エアドラム・トラッキング | `[snippet-verified]` / `[unverified]` / 併記（例: `[snippet-verified; co-authors unverified]`） | 検索スニペットで書誌を確認／本セッションで未確認 |
| ② XRライブ・観客研究 | `✔` / `(DOI unverified)` / `UNVERIFIED` | 出版社・リポジトリ頁で存在確認／DOI文字列のみ未確認／存在自体未確認 |
| ③ AI共創・経済 | `[verified]` / `[unverified]` / 併記 | DOI を検索結果で確認／記憶由来 |
| ④ 発表先・助成（日本語） | 【受付中】【締切済】【次回未公表】 | 2026-10-14時点の締切状態。文献はURL確認のみでフラグなし |
| ⑤ Web技術 | `yes` / `DOI unverified` / `secondary` / `partial` | 統合書誌表の Verified 列 |
| ⑥ クリエイターエコノミー | `[unverified]` / `[partly verified: …]` | 数値が二次要約由来の場合は partly verified |

フラグのない文献は「（フラグなし・URLあり）」と表記した。OA は原ノートの open-access 判定を転記した。

---

## 2. 文献が示す新規性 — 人間XRドラマーのライブ研究は存在しない

6ノートの「Gaps」を重ねると、鍵山が主張できる新規性は五つの不在として具体化する。第一に、ドラム×XR の先行研究は演奏支援・教育が中心であり、**ライブコンサート文脈の XR ドラム論文は検索で見つからなかった**（[japan_venues_funding KQ5](https://nime.org/proc/nime2026_136/)）。NIME は 2005・2014・2020・2022・2026 年と継続的にジェスチャ打楽器論文を掲載しているが、「XRドラム＋観客側AR同期（iPhone Spectator）＋TouchDesigner連携」の構成は先行例に見当たらない。第二に、ドラマー固有のAI先行研究はすべて**ロボットドラマー**（Haile、Shimon、Georgia Tech の第三の腕、McCormack らのAIドラマー）か**オフラインのパターン生成**（GrooVAE、Jordà 2016）であり、人間のドラマーの打撃が LLM・映像エージェントを駆動する構図は文献上逆転しており未踏である（[ai_cocreativity KQ5 Inferences](https://link.springer.com/10.1007/978-3-030-38930-7)）。さらに、音楽LMではなくテキストLLMエージェントがライブのバンドメンバーとして振る舞う査読論文は 2026年10月時点で見つかっていない（[同 KQ1 Gaps](https://arxiv.org/pdf/2502.21267)）。

第三に、ハンドトラッキングのベンチマークは Quest 2（マーカー基準、[Abdlkarim et al. 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10830632/)）、Leap Motion、Azure Kinect、MediaPipe については査読論文があるが、**Apple Vision Pro についてはマーカー基準の精度・遅延ベンチマークが一件も見つからず**、唯一の遅延値はフレームカウントによる非査読推定（[Road to VR 2024](https://roadtovr.com/apple-vision-pro-meta-quest-3-hand-tracking-latency-comparison/)）と、アプリ応用論文の「60 FPS で安定動作」という記述（[Sensors 2025, PMC12390506](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12390506/)）だけである。高速なスティック動作に対してトラッカーを評価した研究もない。第四に、**Beat Wave と KAGI NIGHT は業界紙（MoguraVR）にしか現れず**、査読文献には存在しない（[MoguraVR](https://www.moguravr.com/?p=187320)）。ボリュメトリック演者の観客研究も V-SENSE（2022–23）と慶應KMD（2023）に限られ薄いため、ボリュメトリック・ハイブリッド公演を既に運営している鍵山は「公開研究より先を行っている」と言える（[xr_live_music_audience KQ1 Inferences](https://v-sense.scss.tcd.ie/wp-content/uploads/2022/03/IEEE_VR_2022_VR_Music_Video_V2.pdf)）。第五に、生成AIが個人の創造性を高める実験経済学（Noy & Zhang、Doshi & Hauser、Zhou & Lee、Brynjolfsson ら）と、AI作品が割り引かれる心理学（Horton ら、Shank ら）は充実しているが、**身体化されたAI拡張ライブの経済的インパクトを測った研究はゼロ**であり、XRコンサートの再来場・継続率の査読データも存在しない（[ai_cocreativity KQ4 Gaps](https://pmc.ncbi.nlm.nih.gov/articles/PMC10914360)、[xr_live KQ2 Gaps](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.647929/full)）。

したがって鍵山が助成・論文で掲げるべき一文は次の通りである。「**人間のXRドラマーが、ヘッドセットのハンドトラッキングとスティック側の高速オンセット検出を分離した構成でリアルタイム映像とAIを駆動し、現地観客と仮想観客の双方を対象にプレゼンス・同期・支払意思額を測定した研究は存在しない。KAGI NIGHT はその最初のフィールドである。**」この主張の根拠は Yakura & Goto 2020、Guang 2025、Young 2022 が提起したまま未解決の問い（疎な仮想観客のプレゼンス、ボリュメトリック演者の体験）に KAGI NIGHT が直接答えられる点にある（[xr_live KQ4 Inferences](https://staff.aist.go.jp/m.goto/PAPER/ISMAR2020yakura.pdf)）。

---

## 3. 技術選択を正当化する実測値 — 10 ms の閾値と 128 ms の隔たり

鍵山の構成（スティック動作→OSC→TouchDesigner、Vision Pro は映像・キャリブレーション用）は、以下の数値を並べるだけで設計理由が説明できる。Wessel & Wright は楽器制御に **<10 ms の遅延と <1 ms のジッタ**を求め、OSC を導入した（[NIME 2001 archive](https://nime.org/proc/nime2001_wessel/)）。Jack らは打楽器DMIで専門打楽器奏者と素人の双方が **0 ms を 10±3 ms および 20 ms より好み、安定10 msは0 msと有意差なし**、真の閾値は10–20 msの間にあると述べた（[Jack et al. 2018](https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/44614/Jack%20Action-sound%20Latency%202018%20Accepted.pdf?sequence=1)）。Dahl & Bresin はドラマーが遅延聴覚フィードバック下で打撃を早め、**約55 ms** に破綻点があることを示した（[DAFx-01](https://dafx.de/paper-archive/details/LKHefqWVPCGLn8Sy0EG00A)）。これに対しヘッドセット側は、Quest 2 で**指先誤差約1.1 cm・関節角誤差約9.6°・遅延約45.0 ms**（[Abdlkarim et al. 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10830632/)）、Vision Pro で**約127.7 ms**（30 FPS 取り込み3.5フレーム + パススルー約11 ms、Quest 3 は約70 ms、非査読）である（[Road to VR](https://roadtovr.com/apple-vision-pro-meta-quest-3-hand-tracking-latency-comparison/)）。つまりヘッドセット単独の遅延は打楽器閾値の **2–4倍以上**であり、発音トリガをIMU／カメラ付きスティックや予測的オンセット検出（[Tavares & Bertoloto 2023](https://ieeexplore.ieee.org/document/10285920)）に委ねる判断は文献的に必然である。Banquiero らは慣性スティック（PocketDrum）と Quest 3 ハンドトラッキングの融合で**慣性単独のドラム割当誤りの19.1%を補正**しており、ヘッドセットを「補正・映像」に使う鍵山の役割分担と一致する（[Sensors 2025](https://www.mdpi.com/1424-8220/25/22/6836)）。

観客側の数値は公演設計の根拠になる。ライブ演奏では録音再生より頭部運動が速く、ファンはより強くリズムに同調した（[Swarbrick et al. 2019](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6336707/)）。132名の観客で心拍・皮膚電気・呼吸率の同期が有意に生じ、感動・没入時に高まった（[Tschacher et al. 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10556000/)）。83件の回答で VR ヘッドセット視聴者は YouTube より物理的プレゼンスとアーティストとのつながりが高く、曲の投票は主体感を増やさなかった（[Onderdijk et al. 2021](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.647929/full)）。仮想観客アバターのうちユーザー操作の割合を 0/50/100% と変えると IPQ プレゼンスが上昇した（n=7 パイロット、[Guang et al. 2025](https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2025.1655545/abstract)）。経済面では、完全仮想VRコンサートの支払意思額は**€35–39.99 帯**が最頻で、支払態度・知覚有用性・月収に規定される（[Bär et al. 2025](https://www.elsevier.es/en-revista-journal-innovation-knowledge-376-articulo-on-edge-digital-event-era-S2444569X25001210)）。AI 関与の開示は作品評価を下げるが、人間の創造性の知覚は側面比較で高まる（6実験、N=2,965、[Horton et al. 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10624838/)）。これは「舞台上の身体＝価値の所在」という鍵山の仮説の直接の根拠である。

### 3.1 実測値一覧（出典と検証フラグ付き）

| 量 | 値 | 出典 | フラグ（原ノート表記） |
|---|---|---|---|
| 楽器制御の設計目標 | <10 ms 遅延、<1 ms ジッタ | [Wessel & Wright 2002](https://nime.org/proc/nime2001_wessel/) | [snippet-verified; CMJ volume/pages unverified] |
| 打楽器DMIの許容遅延 | 安定10 ms≈0 ms、20 ms劣化、10±3 ms≈20 ms | [Jack et al. 2018](https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/44614/Jack%20Action-sound%20Latency%202018%20Accepted.pdf?sequence=1) | [journal volume/DOI unverified in this session] |
| ドラマーのDAF破綻点 | 約55 ms | [Dahl & Bresin 2001](https://dafx.de/paper-archive/details/LKHefqWVPCGLn8Sy0EG00A) | [snippet-verified] |
| 連続ジェスチャ楽器の遅延JND | 約20–30 ms | [Mäki-Patola & Hämäläinen 2004](https://users.aalto.fi/~hamalap5/publications/icmcarticlefinal10.pdf) | [snippet-verified] |
| ライブモニタ許容遅延 | 約1.4–42 ms（楽器・モニタ依存） | [Lester & Boley 2007](https://aes2.org/publications/elibrary-page/?id=14256) | [snippet-verified] |
| ネットワーク合奏のテンポ | <11.5 ms で微加速、遅延増でテンポ低下 | [Stanford MediaX (Chafe)](https://mediax.stanford.edu/research-projects/lat-chafe) | プロジェクト頁（Chafe 2010 論文は UNVERIFIED） |
| Quest 2 ハンドトラッキング | 指先誤差≈1.1 cm、関節≈9.6°、遅延≈45.0 ms | [Abdlkarim et al. 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10830632/) | [snippet-verified; full author list from prior knowledge] |
| Vision Pro ハンドトラッキング遅延 | ≈127.7 ms（Quest 3 ≈70 ms） | [Road to VR 2024](https://roadtovr.com/apple-vision-pro-meta-quest-3-hand-tracking-latency-comparison/) | 非査読 |
| Vision Pro アプリ動作 | 60 FPS、ジェスチャ認識96.3%、技術判定88.5%（n=12） | [Sensors 2025 PMC12390506](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12390506/) | [snippet-verified; authors unverified] |
| visionOS 2 ハンドトラッキング更新 | 30 Hz→表示フレームレート（通常90 Hz） | [MIXED](https://mixed-news.com/en/vision-pro-visionos-2-hand-tracking/) | 報道（一次資料未確認） |
| Leap Motion v1 | 静的<0.2 mm、動的≈1.2 mm | [Weichert et al. 2013](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3690061/) | [snippet-verified] |
| LMC1 vs LMC2 掌位置誤差 | 7.9–9.8 mm vs 5.2–5.3 mm | [Weichert group 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12737223/) | [snippet-verified; authors unverified] |
| LMC2 vs MediaPipe 関節角RMSE | 14.8° vs 22.5°（9月論文）／14.7° vs 10.9°（2月論文、矛盾） | [PMC12473350](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12473350/)、[PMC11858933](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11858933/) | [snippet-verified; authors unverified] |
| Azure Kinect 深度 | SD≤17 mm、誤差<11 mm（3.5 mまで）、暖機40–50分 | [Tölgyessy et al. 2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7827245/) | [snippet-verified] |
| Azure Kinect 骨格 vs mocap | RMSE 20–89 mm；上肢MAE≈5–15° | [PMC9879399](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9879399/)、[PMC9860777](https://pmc.ncbi.nlm.nih.gov/articles/PMC9860777) | [authors unverified] |
| IMU+Quest 3 ドラム融合 | 慣性単独の割当誤りの19.1%を補正 | [Banquiero et al. 2025](https://www.mdpi.com/1424-8220/25/22/6836) | [snippet-verified] |
| 打楽器学習の触覚ガイド | 速度誤差−17%、早期タイミング誤差−18% | [Grindlay 2007](https://opera.media.mit.edu/articles/Grindlay_MSthesis_final.pdf) | [snippet-verified; thesis title unverified] |
| ライブ vs 録音の身体反応 | ライブで頭部運動が高速、ファンは同調大 | [Swarbrick et al. 2019](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6336707/) | ✔ |
| 観客の生理同期 | n=132、心拍・皮膚電気・呼吸率で有意同期 | [Tschacher et al. 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10556000/) | ✔ |
| 配信コンサートのプレゼンス | n=83、VR>YouTube（物理的プレゼンス・アーティスト接続） | [Onderdijk et al. 2021](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.647929/full) | ✔ |
| VRコンサート評価 | n=74、没入感が評価と将来利用意図を規定 | [Onderdijk et al. 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10239717/) | ✔ (DOI unverified) |
| 仮想観客アバター | ユーザー操作率0/50/100%でIPQ上昇（n=7） | [Guang et al. 2025](https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2025.1655545/abstract) | ✔ |
| チャット駆動群衆反応 | n=48、没入・共在感が従来法より強い | [arXiv 2503.13121](https://arxiv.org/abs/2503.13121) | ✔ |
| 空間音響のAV同期許容 | ≈461 ms（空間）vs ≈224 ms（ステレオ）、n=18 | [Lund MSc 2026](https://lup.lub.lu.se/student-papers/record/9233095/file/9233107.pdf) | 学生論文 |
| VRコンサート支払意思額 | €35–39.99 帯が最頻 | [Bär et al. 2025](https://www.elsevier.es/en-revista-journal-innovation-knowledge-376-articulo-on-edge-digital-event-era-S2444569X25001210) | ✔ |
| 配信は有料であるべき | ファン72%・音楽家74%（約1,500名） | [KCL 2021](https://www.kcl.ac.uk/news/report-finds-live-streamed-concerts-are-here-to-stay) | 業界調査 |
| 配信の妥当価格 | 29%が支払意向、£18.09 | [PUSH LIVE 2021](https://www.advanced-television.com/2021/06/09/survey-160m-uk-music-live-streaming-opportunity/) | 業界調査 |
| 現地同額拒否 | 92.1%（n=140） | [AMT Lab 2021/22](https://amt-lab.org/blog/2022/1/expanding-our-live-streaming-future-refining-and-developing-new-arts-amp-entertainment-experiences) | 業界調査 |
| AI作品バイアス | 6実験 N=2,965、AI表示で評価低下、側面比較で人間創造性↑ | [Horton et al. 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10624838/) | [verified] |
| AI作曲バイアス | クラシックで好意低下、電子音楽では効果なし | [Shank et al. 2023](https://scholarsmine.mst.edu/psysci_facwork/254) | [verified] |
| 生成AIと創作市場 | 生産性≈+25%、お気に入り/閲覧≈+50%（>400万作品） | [Zhou & Lee 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC10914360) | [verified] |
| 生成AIと生産性 | +15%（5,172名） | [Brynjolfsson et al. 2025](https://arxiv.org/abs/2304.11771) | [verified] |
| 生成AIと文章 | 時間−40%、品質+18%（453名） | [Noy & Zhang 2023](https://marginalrevolution.com/marginalrevolution/2023/07/shakked-noy-and-whitney-zhang-on-the-productivity-effects-of-llms.html) | [unverified — from recall] |
| StreamDiffusion | 最大91.07 fps img2img（RTX 4090）、≈59倍スループット | [arXiv 2312.12491](https://arxiv.org/html/2312.12491v2) | 著者ベンチマーク |
| Android ブルーム | mipmap 10.29 ms、Kawase+HDR 11.49 ms、Gaussian 14.12 ms | [ETASR 2025](https://etasr.com/index.php/ETASR/article/download/19101/6940) | yes |
| 点群描画 | 7.96億点を62–64 fps（RTX 3090） | [Schütz et al. 2021](https://diglib.eg.org/handle/10.1111/cgf14345) | yes |
| Web第一印象 | 50 ms で視覚的魅力が後の判断に波及 | [Lindgaard et al. 2006](https://www.nature.com/news/2006/060109/full/news060109-13.html) | （フラグなし・URLあり） |
| 視覚嗜好の国際差 | 約240万評価・約4万人 | [Reinecke & Gajos 2014](https://iis.seas.harvard.edu/papers/reinecke14visual.pdf) | （フラグなし・URLあり） |
| ゲーミフィケーション | 15研究中12で有意正効果（10,499名） | [Looyestyn et al. 2017](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5376078/) | （フラグなし・URLあり） |
| サブスク転換 | 試用→有料 6.9倍（準実験、n≈4,100） | [Israfilzade & Pathania 2026](https://reference-global.com/article/10.2478/mosr-2026-0005) | （フラグなし・URLあり） |

---

## 4. 目的別文献リスト — 7表・368件

各表の「意味」列は鍵山にとっての一行の用途、「フラグ」列は原ノートの検証表記である。同一文献は一か所にのみ掲載し、他群からは ID で参照する。

### 4.1 自己紹介・ポートフォリオでの引用（A群）

「エアドラムは身体化音楽認知で研究された現象であり、XRドラムはNIMEの20年の系譜に連なる」と語るための文献。

| ID | 文献 | DOI / URL | OA | 意味 | フラグ |
|---|---|---|---|---|---|
| A-01 | Godøy, Haga & Jensenius (2006). "Playing 'Air Instruments': Mimicry of Sound-Producing Gestures by Novices and Experts." Gesture Workshop 2005, LNCS 3881, 256–267 | DOI 10.1007/11678816_29；[DUO](https://duo.uio.no/handle/10852/26898?show=full) | OA (UiO DUO) | 「エアドラム」自体が研究対象であることを示す最良の一本 | [snippet-verified] |
| A-02 | Godøy & Leman (Eds.) (2010). *Musical Gestures: Sound, Movement, and Meaning*. Routledge | ISBN 9780415998871；[Routledge](https://www.routledge.com/Musical-Gestures-Sound-Movement-and-Meaning/Godoy-Leman/p/book/9780415998871) | 非OA | 音を生むジェスチャの分類（Jensenius ら第2章） | [snippet-verified] |
| A-03 | Godøy (2003). "Motor-mimetic Music Cognition." Leonardo 36(4), 317–319 | [UiO copy](https://uio.no/studier/emner/hf/imv/MUS2006/v15/litteratur/rig.pdf) | 非OA（UiO閲覧用） | 聴き手は発音動作を心的に模倣する——観客が「叩く」身体を見る意味 | [snippet-verified] |
| A-04 | Jensenius (2007). *Action–Sound*. PhD thesis, Univ. of Oslo | [IDMIL PDF](https://www-archive.idmil.org/_media/publications/2007/jensenius_2007_phdthesis.pdf) | OA | エア楽器演奏の観察研究を含む行為–音結合の方法論 | [snippet-verified] |
| A-05 | Repp & Su (2013). "Sensorimotor synchronization: A review of recent research (2006–2012)." Psychon. Bull. Rev. 20, 403–452 | DOI 10.3758/s13423-012-0371-2 | 非OA | 同期指標（非同期・分散）の語彙 | [snippet-verified] |
| A-06 | Repp (2006). "Rate limits of sensorimotor synchronization." Adv. Cogn. Psychol. 2(2–3), 163–181 | [DOAJ](https://doaj.org/article/dc3f29b3977e4adf8dfe9aa998eb40de) | OA | テンポ上限・下限の根拠 | [snippet-verified] |
| A-07 | Dahl (2004). "Playing the Accent." Acta Acustica united with Acustica 90(4), 762–776 | [KTH](https://www.speech.kth.se/~sofiad/thesis.html) | 非OA | ドラマーの準備高さ・打速のモーションキャプチャ | [snippet-verified; pages from prior knowledge] |
| A-08 | Dahl & Friberg (2007). "Visual Perception of Expressiveness in Musicians' Body Movements." Music Perception 24(5), 433–454 | DOI 10.1525/mp.2007.24.5.433；[Sonic Field](https://sonicfield.org/library/visual-perception-of-expressiveness-in-musicians-body-movements) | 非OA | 動きだけで感情が伝わる——映像演出の根拠 | [snippet-verified; DOI from prior knowledge] |
| A-09 | Dahl & Altenmüller (2008). ASA press summary "Movements and grip influence the contact force and sound in drumming" | [ASA](https://acoustics.org/pressroom/httpdocs/155th/dahl.htm) | OA | プロは聴覚フィードバック依存、個人差大 | [snippet-verified] |
| A-10 | Tomás, Gorbach, Tellioğlu & Kaltenbrunner (Eds.) (2022). *Embodied Gestures*. TU Wien Academic Press | [OAPEN](https://library.oapen.org/bitstream/id/94d5de21-3f50-496f-a9d5-6f08c8a56ec1/Embodied_Gestures_E-Book.pdf) | OA | Godøy の音–動作オブジェクト時間尺度章 | [snippet-verified] |
| A-11 | Jensenius, Godøy & Wanderley. Musical Gestures Toolbox (Max/Jitter) | [IDMIL](https://www.idmil.org/?p=3582) | — | 「エアピアノ」模倣の事例 | [snippet-verified] |
| A-12 | Havel & Desainte-Catherine (2004). "Modeling an Air Percussion for Composition and Performance." NIME 2004 | [NIME](https://nime.org/proc/nime2004_havel/) | OA | 磁気トラッカ式エアパーカッションの起点 | [snippet-verified] |
| A-13 | Mäki-Patola (2005). "User Interface Comparison for Virtual Drums." NIME 2005, 144–147 | DOI 10.5281/zenodo.1176784；[NIME](https://nime.org/proc/makipatola2005b) | OA | 物理スティックが仮想スティックより正確——スティック採用の根拠 | [snippet-verified] |
| A-14 | Mäki-Patola, Laitinen, Kanerva & Takala (2005). "Experiments with Virtual Reality Instruments." NIME 2005 | [NIME](https://nime.org/proc/nime2005_makipatola/) | OA | VR楽器プロトタイプの併載論文 | [snippet-verified; co-author list unverified] |
| A-15 | Collicutt, Casciato & Wanderley (2009). "From Real to Virtual: A Comparison of Input Devices for Percussion Tasks." NIME 2009 | [NIME](https://nime.org/proc/nime2009_collicutt/) | OA | 不慣れなジェスチャ制御器でタイミング分散が増大 | [snippet-verified; co-authors unverified] |
| A-16 | Tindale, Kapur, Tzanetakis, Driessen & Schloss (2005). "A Comparison of Sensor Strategies for Capturing Percussive Gestures." NIME 2005, 200–203 | DOI 10.5281/zenodo.1176828；[NIME](https://nime.org/proc/tindale2005) | OA | 応答速度と表現データのトレードオフ空間 | [snippet-verified] |
| A-17 | Tindale et al. (2007). "A Hybrid Method for Extended Percussive Gesture." NIME 2007 | [NIME](https://nime.org/proc/nime2007_tindale/) | OA | 音色からの間接的ジェスチャ取得 | [snippet-verified] |
| A-18 | Martin & Lai (2011). "Strike on Stage: a percussion and media performance." NIME 2011 | [NIME](https://nime.org/proc/nime2011_martin/)；[arXiv 2012.00250](https://arxiv.org/pdf/2012.00250) | OA | 視覚トラッキング打楽器→投影の初期例 | [snippet-verified] |
| A-19 | Alexander & Miller (2016). "Composition #1 for PIGS." NIME 2016 (performance) | [Vimeo](https://vimeo.com/176701173) | — | MIDIドラムで流体映像を「スクラッチ」 | [snippet-verified; NIME proceedings entry unverified] |
| A-20 | Trolland, Ilsar & McCormack (2025). "Visually-Led Design for Gestural Audiovisual Instruments." NIME 2025, paper 45 | [NIME](https://nime.org/proc/nime2025_45/) | OA | 映像を先に設計する——最新の査読先例 | [snippet-verified] |
| A-21 | Ilsar, Havryliv & Johnston (2014). "Evaluating the Performance of a New Gestural Instrument Within an Ensemble." NIME 2014 | [NIME](https://nime.org/proc/nime2014_ailsar/) | OA | AirSticks 第一論文 | （フラグなし・URLあり） |
| A-22 | Ilsar, Hughes & Johnston (2020). "NIME or Mime: A Sound-First Approach to Developing an Audio-Visual Gestural Instrument." NIME 2020, 315–320 | DOI 10.5281/zenodo.4813383；[NIME](https://nime.org/proc/nime2020_60/) | OA | AirSticks の音先行設計；SIGGRAPH Asia 2019 Real-Time Live 受賞 | （フラグなし・URLあり） |
| A-23 | Trolland, Ilsar, Frame, McCormack & Wilson (2022). "AirSticks 2.0." NIME 2022 | DOI 10.21428/92fbeb44.c400bdc2；[NIME](https://nime.org/proc/nime2022_51/) | OA | IMUセンサフュージョン+BLE——最も近い先行例 | （フラグなし・URLあり） |
| A-24 | Zellerbach & Roberts (2022). "A Framework for the Design and Analysis of Mixed Reality Musical Instruments." NIME 2022 | [NIME](https://nime.org/proc/nime2022_29/) | OA | MRMI の定義——GHOST RACK を分類する語彙 | （フラグなし・URLあり） |
| A-25 | "AR Drum Circle: Real-Time Collaborative Drumming in AR." Frontiers in Virtual Reality (2022) | [Frontiers](https://frontiersin.org/articles/10.3389/frvir.2022.847284/full) | OA | HMD AR での遠隔協調ドラム | （フラグなし・URLあり） |
| A-26 | Heyen & Sedlmair. AR visualization for drum kit learning. ISMAR 2022 adjunct；Stuttgart thesis 2021 | [arXiv 2308.01889](https://arxiv.org/abs/2308.01889?context=cs)；[thesis](https://elib.uni-stuttgart.de/items/cd820208-d9f3-4a1c-9df9-5f4b393872b9) | OA | プロジェクタARドラム可視化 | （フラグなし・URLあり） |
| A-27 | Pinkl, Villegas & Cohen (2024). MR drumming education tool. Multimodal Technologies and Interaction | [DOAJ](https://doaj.org/article/bcfb0a2b2b3645afa397f291321a0570) | OA | 20名実験のMRドラム教育 | （フラグなし・URLあり） |
| A-28 | iXeRemin (2026). Apple Vision Pro 向け多声MR楽器. NIME 2026 | [NIME](https://nime.org/proc/nime2026_136/) | OA | Vision Pro+ハンドトラッキング+OSC が NIME に採択された証拠 | （フラグなし・URLあり） |
| A-29 | Rochais (2022). "A7" — TouchDesigner による実時間視覚伴奏. Generative Art Conference 2022 | [GA2022 PDF](https://generativeart.com/papersGA2022/2022/Guillaume%20Rochais%20ebook2022-49.pdf) | OA | TouchDesigner の査読先例 | （フラグなし・URLあり） |
| A-30 | Ferguson & Carroll (2024). "Modular Audiovisual Performance Systems (MAPS)." figshare / NYCEMF 2024 | [figshare](https://figshare.com/articles/media/Modular_Audiovisual_Performance_Systems_MAPS_/27644709) | OA | TouchDesigner 生成映像公演の記録（非査読） | （フラグなし・URLあり） |
| A-31 | Aerodrums（商用、査読なし） | [New Atlas](https://newatlas.com/music/aerodrums-2-system/?amp=true) | — | 高速カメラ+再帰反射マーカー方式の前例 | 非査読 |
| A-32 | Naidu & Fernandez (2012). MIT 6.111 student project | [MIT](https://fpga.mit.edu/videos/2012/team08/report.pdf) | OA | Webカメラ式エアドラムの先行技術 | 非査読 |
| A-33 | Dahl 2014 エアドラム研究（CCRMA 頁での言及のみ） | [CCRMA](https://ccrma.stanford.edu/~lja/vr/StrangeInstruments) | — | 正式出典未特定 | 出典未確認 |

### 4.2 助成・研究提案での引用（B群）

#### B-1 遅延・知覚閾値（設計根拠）

| ID | 文献 | DOI / URL | OA | 意味 | フラグ |
|---|---|---|---|---|---|
| B-01 | Wessel & Wright (2002). "Problems and Prospects for Intimate Musical Control of Computers." CMJ 26(3), 11–22（NIME 2001） | [NIME](https://nime.org/proc/nime2001_wessel/)；[arXiv](https://arxiv.org/pdf/2010.01570) | OA | <10 ms/<1 ms 目標と OSC の原典 | [snippet-verified; CMJ volume/pages unverified] |
| B-02 | Jack, Mehrabi, Stockman & McPherson (2018). "Action-sound Latency and the Perceived Quality of Digital Musical Instruments." Music Perception 36(1), 109–128 | DOI 10.1525/mp.2018.36.1.109；[QMRO PDF](https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/44614/Jack%20Action-sound%20Latency%202018%20Accepted.pdf?sequence=1) | Green OA | 打楽器の10/20 ms閾値とジッタ | [journal volume/DOI unverified in this session] |
| B-03 | Jack, Stockman & McPherson (2016). "Effect of latency on performer interaction…" Audio Mostly 2016, 116–123 | DOI 10.1145/2986416.2986428；[PDF](https://instrumentslab.org/data/andrew/jack_am2016.pdf) | OA | 0/10/20/10±3 ms 条件の演奏者行動 | [snippet-verified] |
| B-04 | McPherson, Jack & Moro (2016). "Action-Sound Latency: Are Our Tools Fast Enough?" NIME 2016 | [NIME](https://nime.org/proc/nime2016_mcpherson/) | OA | 自分のOSC/MIDI鎖の往復遅延を測る方法 | [snippet-verified; content from prior knowledge] |
| B-05 | Dahl & Bresin (2001). "Is the Player More Influenced by the Auditory Than the Tactile Feedback…?" DAFx-01 | [DAFx](https://dafx.de/paper-archive/details/LKHefqWVPCGLn8Sy0EG00A) | OA | 約55 ms 破綻点 | [snippet-verified] |
| B-06 | Mäki-Patola & Hämäläinen (2004). "Latency Tolerance for Gesture Controlled Continuous Sound Instrument without Tactile Feedback." ICMC 2004 | [Aalto PDF](https://users.aalto.fi/~hamalap5/publications/icmcarticlefinal10.pdf) | OA | 触覚なし連続制御の JND 20–30 ms | [snippet-verified] |
| B-07 | Lester & Boley (2007). "The Effects of Latency on Live Sound Monitoring." AES 123, paper 7198 | [AES](https://aes2.org/publications/elibrary-page/?id=14256) | 非OA | モニタ遅延の許容範囲 | [snippet-verified] |
| B-08 | Larsen & Knoche (2017). 遅延聴覚フィードバックとストラミング. NIME 2017 | [PDF](https://vbn.aau.dk/ws/files/295153538/nime2017_paper0086.pdf) | OA | 熟練度がDAF効果を調整 | [snippet-verified; title unverified] |
| B-09 | Audio-latency JND（Regensburg, 2024, ACM） | DOI 10.1145/3678299.3678331；[ePub](https://epub.uni-regensburg.de/59003/3/3678299.3678331.pdf) | OA | 近年のJND研究（内容未取得） | [unverified content] |
| B-10 | Rottondi, Chafe, Allocchio & Sarti (2016). "An Overview on Networked Music Performance Technologies." IEEE Access 4, 8823–8843 | DOI 10.1109/ACCESS.2016.2628440；[DOAJ](https://doaj.org/article/b6289c0973fd4f6d9543aaef43acdb70) | OA | 遠隔合奏の遅延許容の標準レビュー（Mac↔Win OSC配線の根拠） | ✔ |
| B-11 | Chafe (Stanford CCRMA) 遅延–テンポ研究 | [MediaX](https://mediax.stanford.edu/research-projects/lat-chafe) | — | <11.5 ms 微加速、遅延増でテンポ低下 | プロジェクト頁；Chafe, Cáceres & Gurevich 2010 Perception は UNVERIFIED |
| B-12 | 経験則閾値（8–25 ms 自然、25–60 ms 困難） | [baltimorerecorders.org](https://baltimorerecorders.org/html/general/networked_musical_performance.html) | — | 例示のみ、一次は B-10 | 非査読 |
| B-13 | Turchet & Tomasetti (2023). 没入型ネットワーク演奏（空間音響が遅延に加算） | [Trento](https://iris.unitn.it/handle/11572/399757) | — | 空間音響の遅延コスト | ✔ |

#### B-2 ハンドトラッキング・ドラム検出の実測（技術根拠）

| ID | 文献 | DOI / URL | OA | 意味 | フラグ |
|---|---|---|---|---|---|
| B-14 | Abdlkarim, Di Luca, Aves, Maeda, Yeo, Miall, Wing & Galea (2023/24). "A methodological framework to assess the accuracy of VR hand-tracking systems: Meta Quest 2." Behav. Res. Methods 56(2), 1052–1063 | DOI 10.3758/s13428-022-02051-8；[PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10830632/) | OA | 1.1 cm/9.6°/45 ms——Vision Pro 評価の方法論テンプレート | [snippet-verified; full author list from prior knowledge] |
| B-15 | Weichert, Bachmann, Rudak & Fisseler (2013). "Analysis of the Accuracy and Robustness of the Leap Motion Controller." Sensors 13(5), 6380–6393 | DOI 10.3390/s130506380；[PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3690061/) | OA | 産業ロボット基準の精度評価法 | [snippet-verified] |
| B-16 | Guna, Jakus, Pogačnik, Tomažič & Sodnik (2014). Leap Motion の精度と信頼性. Sensors 14(2), 3702–3720 | DOI 10.3390/s140203702；[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3958287) | OA | 動的追跡・距離>250 mm で信頼性低下 | [snippet-verified; DOI/pages from prior knowledge] |
| B-17 | Weichert group (2025). "Comparative Analysis of the Accuracy and Robustness of the Leap Motion Controller 2." Sensors | [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12737223/) | OA | LMC1→LMC2 の改善値 | [snippet-verified; authors unverified] |
| B-18 | "Evaluation of Commercial Camera-Based Solutions for Tracking Hand Kinematics." Sensors (Sept 2025) | [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12473350/) | OA | LMC2 14.8° vs MediaPipe 22.5° | [snippet-verified; authors unverified] |
| B-19 | "Optimisation and Comparison of Markerless and Marker-Based Motion Capture Methods for Hand and Finger Movement Analysis." Sensors 25(4), 1079 (2025) | [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11858933/) | OA | MediaPipe 10.9° vs LMC 14.7°（B-18 と逆順） | [snippet-verified; authors unverified] |
| B-20 | Zhang, Bazarevsky, Vakunov, Tkachenka, Sung, Chang & Grundmann (2020). "MediaPipe Hands." CVPR 2020 Workshop | [arXiv 2006.10214](https://arxiv.org/abs/2006.10214v1) | OA | 単眼RGB 21点ハンドトラッキングの原典 | [snippet-verified] |
| B-21 | Tölgyessy, Dekan, Chovanec & Hubinský (2021). "Evaluation of the Azure Kinect…" Sensors 21(2), 413 | DOI 10.3390/s21020413；[PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7827245/) | OA | TD の Kinect 入力の限界値 | [snippet-verified] |
| B-22 | Tölgyessy et al. (2021). "Skeleton Tracking Accuracy and Precision Evaluation of Kinect V1, V2, Azure Kinect." Appl. Sci. 11(12), 5756 | [MDPI](https://www.mdpi.com/2076-3417/11/12/5756) | OA | Azure Kinect が前世代を上回る | [snippet-verified] |
| B-23 | Azure Kinect 臨床検証 vs Qualisys（30名） | [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9879399/) | OA | RMSE 20–89 mm | [authors unverified] |
| B-24 | Azure Kinect vs Vicon（26名、側方リーチ） | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9860777) | OA | 上肢角度MAE≈5–15° | [authors unverified] |
| B-25 | "Real-Time Hand Tracking and Collision Detection for Immersive MR Boxing Training on Apple Vision Pro." Sensors 2025 | [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12390506/) | OA | Vision Pro 応用論文（関節誤差なし） | [snippet-verified; authors unverified] |
| B-26 | Road to VR (2024). Vision Pro vs Quest 3 ハンドトラッキング遅延 | [Road to VR](https://roadtovr.com/apple-vision-pro-meta-quest-3-hand-tracking-latency-comparison/)；[visionOS 2](https://roadtovr.com/?p=172257) | — | 127.7 ms／70 ms；visionOS 2 の予測は体感のみ改善 | 非査読 |
| B-27 | Apple Developer Forums スレッド（UITextView 時の5–10 s 遅延） | [Forums](https://developer.apple.com/forums/thread/800604) | — | 単一事例 | 単一事例 |
| B-28 | visionOS 2 ハンドトラッキング更新率（MIXED 報道） | [MIXED](https://mixed-news.com/en/vision-pro-visionos-2-hand-tracking/) | — | 30 Hz→90 Hz | 報道 |
| B-29 | Banquiero, Valdeolivas & Juan (2025). "Enhancing Musical Learning Through Mixed Reality: PocketDrum and Meta Quest 3." Sensors 25(22), 6836 | DOI 10.3390/s25226836；[MDPI](https://www.mdpi.com/1424-8220/25/22/6836) | OA | IMU+HMD融合、遅延・ジッタ報告の論文様式 | [snippet-verified] |
| B-30 | Tavares & Bertoloto (2023). "Air Drums, and Bass: Anticipating Musical Gestures in Accelerometer Signals with a Lightweight CNN." IEEE MLSP 2023 | DOI 10.1109/MLSP55844.2023.10285920；[IEEE](https://ieeexplore.ieee.org/document/10285920)；[Insper](https://repositorio.insper.edu.br/handle/11224/6703) | 非OA（著者版あり） | 予備動作から打撃を予測して遅延を打ち消す | [snippet-verified] |
| B-31 | "A2D: Anywhere Anytime Drumming" (2023) | [arXiv 2304.03289](https://arxiv.org/abs/2304.03289) | OA | YOLOv5 によるマーカーレススティック検出 | [snippet-verified; authors unverified] |
| B-32 | Boem & Turchet (2024). "Selection as Tapping." IJHCS 185, 103231 | [Trento](https://iris.unitn.it/handle/11572/429251)；[PDF](https://iris.unitn.it/retrieve/49dcd12c-b95d-4954-9f43-0207e8b37aa3/1-s2.0-S1071581924000156-main.pdf) | Green OA | VR タイミング課題で「追跡安定性が決定的」 | [snippet-verified] |

#### B-3 触覚・リバウンド不在（設計上の補償根拠）

| ID | 文献 | DOI / URL | OA | 意味 | フラグ |
|---|---|---|---|---|---|
| B-33 | Cao et al. (2016). "The dominance of haptics over audition in controlling wrist velocity during striking movements." Exp. Brain Res. | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4785215) | OA | 打速制御は触覚優位——リバウンド代替の必要性 | [snippet-verified; full author list unverified] |
| B-34 | Grindlay (2007). *Haptic Guidance Benefits Musical Motor Learning*. MIT M.S. thesis | [MIT PDF](https://opera.media.mit.edu/articles/Grindlay_MSthesis_final.pdf) | OA | 触覚ガイドで誤差−17%/−18% | [snippet-verified; thesis title unverified] |
| B-35 | Holland, Bouwer, Dalgleish & Hurtig (2010). "Feeling the beat where it counts: the haptic drum kit." TEI 2010 | [ORO](https://oro.open.ac.uk/18900) | OA | 振動触覚による多肢リズム学習 | [snippet-verified] |
| B-36 | Bouwer, Holland et al. Haptic iPod (2011)／Haptic Bracelets (2013) | [ORO](https://oro.open.ac.uk/35072) | OA | 受動的リズム学習 | [snippet-verified] |
| B-37 | Marshall & Wanderley (2006). "Vibrotactile Feedback in Digital Musical Instruments." NIME 2006 | [NIME](https://nime.org/proc/nime2006_marshall/) | OA | スティックへ触覚を足す設計参照 | [snippet-verified] |
| B-38 | Bouënard, Wanderley & Gibet (2010). "Gesture Control of Sound Synthesis: Analysis and Classification of Percussion Gestures." Acta Acustica 96(4), 668–677 | DOI 10.3813/AAA.918321；[HAL](https://hal.archives-ouvertes.fr/hal-00763258) | HAL preprint | 打楽器ジェスチャ分類と物理モデル | [snippet-verified] |
| B-39 | Bouënard, Wanderley & Gibet (2008). "Enhancing the Visualization of Percussion Gestures by Virtual Character Animation." NIME 2008 | [NIME](https://nime.org/proc/nime2008_bouenard/) | OA | 打楽器ジェスチャの可視化 | [snippet-verified] |
| B-40 | Meta Reality Labs. "Perceptual Limits of Visual-Haptic Simultaneity in VR Interactions" | [Meta](https://research.fb.com/publications/perceptual-limits-of-visual-haptic-simultaneity-in-virtual-reality-interactions/) | — | 視覚–触覚同時性 | [unverified content] |
| B-41 | Stanford ME327 "Haptic Drum-Hero" (2023) | [Stanford](https://charm.stanford.edu/ME327/2023-Group2) | — | 授業プロジェクト（先行技術のみ） | 非査読 |

#### B-4 マッピング理論・DMI 設計枠組み

| ID | 文献 | DOI / URL | OA | 意味 | フラグ |
|---|---|---|---|---|---|
| B-42 | Hunt & Wanderley (2002). "Mapping performer parameters to synthesis engines." Organised Sound 7(2), 97–108 | DOI 10.1017/S1355771802002030；[Cambridge](https://www.cambridge.org/core/journals/organised-sound/article/mapping-performer-parameters-to-synthesis-engines/BD8AAF4BC582D3DCACB5AEC5BF49F8FE) | 非OA | スティック→OSC→TD の層状マッピングの理論 | [snippet-verified] |
| B-43 | Wanderley & Depalle (2004). "Gestural control of sound synthesis." Proc. IEEE 92(4), 632–644 | [Sonic Field](https://labs.sonicfield.org/library/mapping-performer-parameters-to-synthesis-engines) | 非OA | ジェスチャ取得→マッピング→合成のレビュー | [snippet-verified existence; DOI unverified] |
| B-44 | Verfaille, Wanderley & Depalle (2006). "Mapping strategies for sound synthesis, digital audio effects, and sonification…" | [Sonic Field](https://labs.sonicfield.org/library/mapping-strategies-for-sound-synthesis-digital-audio-effects-and-sonification-of) | — | エフェクト・ソニフィケーションへの拡張 | [snippet-verified; venue unverified] |
| B-45 | Malloch, Birnbaum, Sinyor & Wanderley (2006). "A New Conceptual Framework for Digital Musical Instruments." DAFx-06, 49–52 | [DAFx](https://www.dafx.de/paper-archive/details/3j-1bIzZgUCXzUo_UFCEeg) | OA | DMI の分類・分析図 | [snippet-verified] |
| B-46 | Malloch & Wanderley (2007). "The T-Stick: From Musical Interface to Musical Instrument." NIME 2007 | [NIME](https://nime.org/proc/nime2007_malloch/) | OA | スティック型DMIが楽器に成熟する事例 | [snippet-verified] |

#### B-5 人間–AI共創・ライブAI（研究提案の系譜）

| ID | 文献 | DOI / URL | OA | 意味 | フラグ |
|---|---|---|---|---|---|
| B-47 | Deterding et al. (2017). "Mixed-Initiative Creative Interfaces." CHI EA '17, 628–635 | DOI 10.1145/3027063.3027072；[White Rose](https://eprints.whiterose.ac.uk/112515) | OA（著者版） | 「MICI」という傘語 | [verified via White Rose + CPS-VO]（著者一覧は ACM DL で要確認） |
| B-48 | Hadjeres, Pachet & Nielsen (2017). "DeepBach." ICML 2017, PMLR 70:1362–1371 | [PMLR](https://proceedings.mlr.press/v70/hadjeres17a.html)；[arXiv 1612.01010](https://arxiv.org/abs/1612.01010) | OA | 操舵可能な生成モデルの起点 | （Sony CSL 所属は未確認） |
| B-49 | Gillick, Roberts, Engel, Eck & Bamman (2019). "Learning to Groove with Inverse Sequence Transformations." ICML 2019, PMLR 97:2269–2279 | [PMLR](https://proceedings.mlr.press/v97/gillick19a.html)；[Groove dataset](https://magenta.tensorflow.org/datasets/groove) | OA | 13.6 時間の電子ドラム演奏データ——XRドラム打撃列と直接比較可能 | （フラグなし・URLあり） |
| B-50 | Mann, Gillick, Dinculescu, Radebaugh & Hawthorne (2019). "Magenta Studio." MUME 2019 | [Google Research](https://research.google/pubs/pub48280) | OA | DAW内AIドラムツール（Drumify 等） | （MUME であり NIME ではない点に注意） |
| B-51 | Louie, Coenen, Huang, Terry & Cai (2020). "Novice-AI Music Co-Creation via AI-Steering Tools." CHI 2020 | DOI 10.1145/3313831.3376739；[Magenta](https://magenta.tensorflow.org/people-first-hci-ml-collaborations) | — | 「操舵性」の標準CHI引用 | [verified] |
| B-52 | Huang, Koops, Newton-Rex, Dinculescu & Cai (2020). "AI Song Contest: Human-AI Co-Creation in Songwriting." ISMIR 2020 | [arXiv 2010.05388](https://arxiv.org/pdf/2010.05388) | OA | 実践者のAI利用実態（13チーム・61名） | （著者一覧は ISMIR 版で要確認） |
| B-53 | Sturm et al. (2019). "Machine Learning Research that Matters for Music Creation: A Case Study." JNMR 48(1), 36–55 | DOI 10.1080/09298215.2018.1515233；[Kingston](https://eprints.kingston.ac.uk/id/eprint/41834) | OA（著者版） | 「公開コンサートは研究成果である」という枠組み | [verified] |
| B-54 | Deruty, Grachten, Lattner, Nistal & Aouameur (2022). "On the Development and Practice of AI Technology for Contemporary Popular Music Production." TISMIR 5(1), 35 | DOI 10.5334/tismir.100；[TISMIR](https://transactions.ismir.net/articles/10.5334/tismir.100) | OA | Sony CSL（東京拠点あり）との接点 | [verified URL]（抄録内容未取得） |
| B-55 | Blanchard, Naseck, Brade, Lecamwasam, Rudess, Huang & Paradiso (2025). "The jam_bot." ISMIR 2025, 755–762 | DOI 10.5281/zenodo.17811478；[MIT Media Lab](https://www.media.mit.edu/publications/the-jam_bot-a-real-time-system-for-collaborative-free-improvisation-with-music-language-models/) | OA | 名のある奏者+AIバンドメンバーの最近接先例 | [verified via MIT Media Lab listing] |
| B-56 | Roberts & Krueger (forthcoming). "Musical agency and collaboration in the digital age." In *Collaborative Embodied Performance* | [Exeter ORE](https://ore.exeter.ac.uk/repository/handle/10871/127636?show=full) | OA preprint | Herndon/Spawn の学術的扱い | forthcoming/unverified publication details |
| B-57 | Herndon on Spawn（SPIN 2019／MusicTech） | [SPIN](https://www.spin.com/2019/06/ai-music-artificial-intelligence-feature-holly-herndon-yacht/) | — | 「アンサンブルの一員としてのAI」 | 報道 |
| B-58 | Caramiaux & Fdili Alaoui (2022). "'Explorers of Unknown Planets'." PACM HCI 6(CSCW2), 477 | DOI 10.1145/3555578；[HAL](https://hal-lara.archives-ouvertes.fr/HCI-SORBONNE/hal-03762351v1) | OA | 「AIを素材として扱う独立研究者としてのアーティスト」 | [verified] |
| B-59 | Azimi & Zareei (2025). "Live Improvisation with Fine-Tuned Generative AI." NIME 2025 | [NIME](https://nime.org/proc/nime2025_54/) | OA | プロンプト駆動ライブAI即興が NIME に採択 | （フラグなし・URLあり） |
| B-60 | ReaLJam (2025). "Real-Time Human-AI Music Jamming with RL-Tuned Transformers" | [arXiv 2502.21267](https://arxiv.org/pdf/2502.21267) | OA | 6名の熟練者によるライブ評価 | 会議名 unverified |

#### B-6 音楽駆動生成映像・VJ 研究

| ID | 文献 | DOI / URL | OA | 意味 | フラグ |
|---|---|---|---|---|---|
| B-61 | Kraasch & Pasquier (2022). "Autolume-Live: Turning GANs into a Live VJing tool." xCoAx 2022 | [PDF](https://2022.xcoax.org/pdf/xcoax2022-kraasch.pdf) | OA | 深層学習ライブ映像の先行研究不在を明言 | （フラグなし・URLあり） |
| B-62 | Kraasch & Pasquier (2022). "Autolume: Automating Live Music Visualization." ISEA2022 artist talk | [ISEA](https://isea-archives.siggraph.org/?p=71647) | — | ISEA がAI-VJをアーティストトークとして採択した前例 | （フラグなし・URLあり） |
| B-63 | Kraasch (2023). M.Sc. thesis, SFU | [SFU](https://summit.sfu.ca/_flysystem/fedora/2023-07/etd22382.pdf) | OA | NIME 2023 Autolume 論文の帰属は unverified/likely wrong | 注意 |
| B-64 | Kodaira, Xu et al. (2023). "StreamDiffusion." | [arXiv 2312.12491](https://arxiv.org/html/2312.12491v2)；[TD fork](https://github.com/dotsimulate/StreamDiffusion) | OA | 鍵山の TD パイプラインのエンジンそのもの | 著者ベンチマーク |
| B-65 | Jeong, Doh & Kwon (2021). "TräumerAI." NeurIPS 2020 Workshop | [arXiv 2102.04680](https://arxiv.org/abs/2102.04680v1) | OA | ムードレベルの音→映像マッピング | （フラグなし・URLあり） |
| B-66 | Erdem, Wallace & Jensenius (2022). "CAVI: A Coadaptive Audiovisual Instrument–Composition." NIME 2022 | [NIME](https://nime.org/proc/nime2022_25/) | OA | ドラマーを含む公演でのEMG/動作駆動AV | （フラグなし・URLあり） |
| B-67 | Beane (Texas A&M). 実時間オーディオ反応映像と交響楽 | [TDL](https://tdl-ir.tdl.org/items/911c91ce-d68e-4780-97d3-9b1760d99a69) | OA | 2006年の先行事例 | 学位論文 |
| B-68 | Comillas 卒業研究：CNN/GRU 音楽イベント検出→TouchDesigner | [repo](https://repositorio.comillas.edu/jspui/handle/11531/95114) | — | 学生研究 | 非査読 |

#### B-7 評価方法論（査読者が期待するプロトコル）

| ID | 文献 | DOI / URL | OA | 意味 | フラグ |
|---|---|---|---|---|---|
| B-69 | Erdem, Wallace, Glette & Jensenius (2022). "Tool or Actor? Expert Improvisers' Evaluation of a Musical AI 'Toddler'." CMJ 46(4), 26–42 | DOI 10.1162/comj_a_00657；[DUO](https://www.duo.uio.no/handle/10852/110981) | OA | 公演2回＋奏者インタビュー＋観客質問紙の評価テンプレート | [verified via OpenAlex] |
| B-70 | Hsu & Sosnick (2009). "Evaluating Interactive Music Systems: An HCI Approach." NIME 2009 | [NIME](https://nime.org/proc/nime2009_hsu/) | OA | リハーサル・本番双方の評価設計 | （フラグなし・URLあり） |
| B-71 | McCormack et al. (2019). "In a Silent Way: Communication Between AI and Improvising Musicians Beyond Sound." CHI 2019 | DOI 10.1145/3290605.3300268；[arXiv 1902.06442](https://arxiv.org/abs/1902.06442v1) | OA | AI が「ドラマー」で、視覚的信号が研究対象 | [unverified — from recall]（DOI） |
| B-72 | Jordanous (2012). "A Standardised Procedure for Evaluating Creative Systems (SPECS)." Cogn. Comput. 4(3), 246–279 | DOI 10.1007/s12559-012-9156-1；[Kent](https://kar.kent.ac.uk/42379/) | — | 助成に書ける評価枠組み名 | [verified via Kent KAR] |
| B-73 | Karimi, Grace, Maher & Davis (2018). "Evaluating Creativity in Computational Co-Creative Systems." ICCC 2018 | [arXiv 1807.09886](https://arxiv.org/pdf/1807.09886) | OA | 共創システム評価のサーベイ | （フラグなし・URLあり） |
| B-74 | Burland & McLean (2016). ライブコーディング観客研究. IJPADM | DOI 10.1080/14794713.2016.1227596；[White Rose](https://eprints.whiterose.ac.uk/id/eprint/109223/) | — | 「機械の過程を見せる」観客調査の雛形 | [verified via White Rose metadata]（authors unverified） |
| B-75 | Diapoulis (2023). "Musical live coding in relation to interactivity variations." Organised Sound | DOI 10.1017/S1355771823000444；[Cambridge PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E0134B8B71E925C7014F59EA411E2406/S1355771823000444a.pdf/musical-live-coding-in-relation-to-interactivity-variations.pdf) | OA | 11 システムの観察研究 | [verified]（author unverified） |
| B-76 | Diapoulis & Dahlstedt (2021). "The creative act of live coding practice in music performance." Chalmers | [Chalmers](https://research.chalmers.se/en/publication/526821) | OA | 概念枠組み | （フラグなし・URLあり） |
| B-77 | "Rehearsal-as-research" 方法論（UiO） | [DUO](https://duo.uio.no/handle/10852/68795) | OA | 即興訓練に沿った評価セッション | （フラグなし・URLあり） |
| B-78 | Hopkins et al. (2025). "BrAIn Jam." Frontiers in Computer Science | DOI 10.3389/fcomp.2025.1570249；[Frontiers](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1570249/abstract) | OA | fNIRS でドラマーの脳状態にAIが適応 | [from search; verify] |
| B-79 | Lederman, Holland & Mulholland (2020/2021). PPIG DC "shedding" | [PPIG 2020](https://ppig.org/papers/2020-ppig-31st-dc-lederman/)；[PPIG 2021](https://ppig.org/papers/2021-ppig-32nd-lederman/) | OA | ドラマー+会話エージェントの混合主導 | （フラグなし・URLあり） |
| B-80 | Jordà, Gómez-Marín, Faraldo & Herrera (2016). "Drumming with style." NIME 2016 | [NIME](https://nime.org/proc/nime2016_jordnicode225/) | OA | オフラインのドラムパターン生成 | （フラグなし・URLあり） |

#### B-8 ロボット・AIドラマーの系譜（対比先例）

| ID | 文献 | DOI / URL | OA | 意味 | フラグ |
|---|---|---|---|---|---|
| B-81 | Weinberg, Bretan, Hoffman & Driscoll (2020). *Robotic Musicianship: Embodied Artificial Creativity and Mechatronic Musical Expression*. Springer | DOI 10.1007/978-3-030-38930-7；[Springer](https://link.springer.com/10.1007/978-3-030-38930-7) | 非OA | 「Embodied Artificial Creativity」の概念的出自 | [verified] |
| B-82 | Weinberg & Driscoll (2006). "Toward Robotic Musicianship." CMJ 30(4), 28–45 | [MUSE](https://muse.jhu.edu/article/206781/pdf) | — | Haile の原典 | DOI unverified; likely 10.1162/comj.2006.30.4.28 |
| B-83 | Weinberg & Driscoll (2005). "Haile — an Interactive Robotic Percussionist." ICMC 2005 | [App State](https://appstate.elsevierpure.com/en/publications/haile-an-interactive-robotic-percussionist/) | — | ロボット打楽器奏者 | no DOI found |
| B-84 | Weinberg. "Jam'aa for Haile." SIGGRAPH art/performance | [SIGGRAPH History](https://history.siggraph.org/?p=167510) | — | SIGGRAPH がロボット打楽器公演を採択した証拠 | （フラグなし・URLあり） |
| B-85 | Weinberg & Driscoll (2007). "The Design of a Robotic Marimba Player." NIME 2007 | DOI 10.5281/zenodo.1179477；[NIME](https://nime.org/proc/weinberg2007) | OA | Shimon 前史 | [from search] |
| B-86 | Weinberg, Blosser, Mallikarjuna & Raman (2009). "The Creation of a Multi-Human, Multi-Robot Interactive Jam Session." NIME 2009 | DOI 10.5281/zenodo.1177705；[NIME](https://nime.org/proc/nime2009_weinberg_b/) | OA | 人–ロボット合同ジャム | [likely; verify on nime.org] |
| B-87 | Hoffman & Weinberg (2010). "Shimon: an interactive improvisational robotic marimba player." CHI EA 2010 | [Academia](https://idc-ac.academia.edu/GuyHoffman) | — | Shimon | DOI unverified; likely 10.1145/1753846.1754021 |
| B-88 | Hoffman & Weinberg (2011). "Interactive Improvisation with a Robotic Marimba Player." Springer | [Springer Professional](https://www.springerprofessional.de/en/interactive-improvisation-with-a-robotic-marimba-player/3685538)；[Robohub](https://robohub.org/robotic-musicianship) | — | 予測的動作で同期 | DOI not shown |
| B-89 | Weinberg (2011). "Gesture-based human-robot Jazz improvisation." ICML 2011 | [ICML PDF](https://icml.cc/imls/conferences/2011/papers/X4_crossconference.pdf) | OA | 聴きながら即興と振付を適応 | （フラグなし・URLあり） |
| B-90 | Georgia Tech 装着型「第三の腕」ドラム肢（2016、Bretan & Weinberg） | [TechCrunch](https://techcrunch.com/2016/02/22/robotic-parasite-helps-drummers-keep-the-beat) | — | 唯一の「拡張ドラマー」先例 | paper/DOI NOT found — only press |
| B-91 | Savery, Zahray & Weinberg (2020). "Shimon the Rapper." ICCC 2020, 212–219 | [Macquarie](https://researchers.mq.edu.au/en/publications/shimon-the-rapper-a-real-time-system-for-human-robot-interactive-/) | — | 実時間音声入出力 | （フラグなし・URLあり） |
| B-92 | MEARL "AI Drummer – Jam buddy"（Memorial University） | [Project](https://www.andrewstaniland.com/ai-drummer) | — | 論文未特定 | unverified |

#### B-9 創造性とAIの経済学（インパクト測定の雛形）

| ID | 文献 | DOI / URL | OA | 意味 | フラグ |
|---|---|---|---|---|---|
| B-93 | Noy & Zhang (2023). "Experimental Evidence on the Productivity Effects of Generative AI." Science 381(6654) | DOI 10.1126/science.adh2586；[MR summary](https://marginalrevolution.com/marginalrevolution/2023/07/shakked-noy-and-whitney-zhang-on-the-productivity-effects-of-llms.html) | — | 生産性効果の標準引用 | [unverified — from recall] |
| B-94 | Doshi & Hauser (2024). "Generative AI enhances individual creativity but reduces the collective diversity of novel content." Sci. Adv. 10(28) | DOI 10.1126/sciadv.adn5290；[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532) | OA | 個人利得 vs 集団均質化——身体的個性が多様性を守る論拠 | [verified] |
| B-95 | Zhou & Lee (2024). "Generative AI, human creativity, and art." PNAS Nexus 3(3) | DOI 10.1093/pnasnexus/pgae052；[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10914360) | OA | 市場価値の大規模測定（value per view） | [verified] |
| B-96 | Brynjolfsson, Li & Raymond (2025). "Generative AI at Work." QJE 140(2), 889–942 | DOI 10.1093/qje/qjae044；[arXiv 2304.11771](https://arxiv.org/abs/2304.11771) | OA（arXiv） | トップ誌の「AIは実践者を拡張する」根拠 | [verified] |
| B-97 | Horton, White & Iyengar (2023). "Bias against AI art can enhance perceptions of human creativity." Sci. Rep. 13 | DOI 10.1038/s41598-023-45202-3；[PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10624838/) | OA | 「舞台上の身体に価値が宿る」仮説 | [verified] |
| B-98 | Shank, Stefanik, Stuhlsatz, Kacirek & Belfi (2023). "AI Composer Bias." JEP: Applied 29(3) | DOI 10.1037/xap0000447；[Scholars' Mine](https://scholarsmine.mst.edu/psysci_facwork/254) | — | 音楽固有の帰属バイアス | [verified] |
| B-99 | 2025 arXiv レビュー（AI作曲バイアスは混在；Millet et al. 2023 を引用） | [arXiv 2512.02785](https://arxiv.org/pdf/2512.02785) | OA | 反証の存在を示す | Millet 完全引用 unverified |
| B-100 | "Valuing AI Art: An Experimental Study." AEA RCT Registry | DOI 10.1257/rct.14469-1.0；[AEA](https://www.socialscienceregistry.org/trials/14469) | — | WTP オークション設計の標準 | 登録のみ（未報告） |
| B-101 | "Humans versus AI: whether and why we prefer human-created…" Cogn. Res. Princ. Implic. (c. 2023) | [Cambridge repo](https://www.repository.cam.ac.uk/handle/1810/354873) | — | 物語性・努力の知覚が差を生む | full citation/DOI unverified |
| B-102 | Montoro-Pons & Cuadrado-García (2011). JCE 35(1), 19–48 | [Live Music Exchange](https://livemusicexchange.org/resources/live-and-prerecorded-popular-music-consumption) | — | ライブ+録音の共同需要モデル | DOI unverified |
| B-103 | "Prices for superstars can flatten out" (2014). JCE 38(4), 369–384 | DOI 10.1007/s10824-014-9219-0；[RePEc](https://ideas.repec.org/a/kap/jculte/v38y2014i4p369-384.html) | — | 文化経済学の掲載先 | [verified; authors unverified] |
| B-104 | Lo & Lai (2023). Sci. Rep. — HMD+能動ナビがプレゼンス→フロー→来場意図 | DOI 10.1038/s41598-023-35369-0；[PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10211280/) | OA | 「来場意図」が XR→売上の中間変数 | [all from search; verify] |
| B-105 | Dire Straits VR コンサート感情分析. Virtual Reality 27(2) | DOI 10.1007/s10055-022-00685-9；[PubMed](https://pubmed.ncbi.nlm.nih.gov/36034584/) | — | VRコンサートの感情反応 | [all from search; verify] |
| B-106 | PwC 2020 ライブ音楽収入 −64%（IQ Magazine）；Australian Live Music Office ≥3:1 便益 | [IQ](https://www.iqmagazine.com/?p=113543)；[APRA AMCOS](https://www.apraamcos.com.au/about/supporting-the-industry/research-papers/live-music-research) | — | 業界ベースライン | 非学術 |

#### B-10 日本の共同研究候補（研究室）

| ID | 機関 | URL | 意味 | フラグ |
|---|---|---|---|---|
| B-107 | 慶應義塾大学 KMD Embodied Media Project（XR CREATIVE AWARD 2023 ファイナリスト、SIGGRAPH Asia 2023 受賞、シドニー–東京ボリュメトリックライブ、Brain Body Jockey） | [KMD news](https://kmd.keio.ac.jp/category/news/page/5)；[Keio 2020-12-04](https://www.keio.ac.jp/en/press-release/20201204-2/) | ライブ音楽×ボリュメトリック×XR の最近接 | 代表教員名は未ソース |
| B-108 | 東京藝術大学 芸術情報センター（松浦知也 特任助教、アートDX） | [garden.matsuuratomoya.com](https://garden.matsuuratomoya.com/ACC申請書2025) | 電子楽器演奏者が窓口 | （フラグなし・URLあり） |
| B-109 | 東京大学 稲見昌彦研究室 | [山形県 PDF](https://www100.pref.yamagata.jp/documents/43878/1216chirashi.pdf) | 音楽XRの具体プロジェクトは未確認 | 未確認 |
| B-110 | 筑波大学 Research Unit for Art and Technology | [vrlab](https://www.vrlab.esys.tsukuba.ac.jp/archives/research-unit-for-art-and-technology) | VR×アート | （フラグなし・URLあり） |
| B-111 | 九州大学 芸術工学研究院 音響設計部門 | [公募PDF](https://kobo.jimu.kyushu-u.ac.jp/pdf/2024091993143.pdf) | 音楽創作実践 | （フラグなし・URLあり） |
| B-112 | 洗足学園音楽大学 先端音楽表現研究所（2025年度設置、XR対象） | [LAMP](https://www.senzoku.ac.jp/music/laboratory/lamp/?p=11) | XR×音楽を明示する国内研究所 | （フラグなし・URLあり） |
| B-113 | 信州大学 宮尾秀俊研究室（MR 演奏支援） | [信州大 PDF](https://www.shinshu-u.ac.jp/faculty/engineering/teachers/2025/12/10/7cfc89413e2a92e0cda663f7a759200f.pdf) | 透過型HMD演奏支援 | （フラグなし・URLあり） |
| B-114 | 広島市立大学 2026 研究発表（音楽系） | [HCU](https://www.hiroshima-cu.ac.jp/research-presentation/files2026/poster/pdf/013.pdf) | 詳細未確認 | 未確認 |

### 4.3 note 記事・トークでの引用（C群）

観客体験・ライブ性・仮想観客・ボリュメトリック演者を語るための、一般読者にも伝わる文献。

| ID | 文献 | DOI / URL | OA | 意味 | フラグ |
|---|---|---|---|---|---|
| C-01 | Onderdijk, Swarbrick, Van Kerrebroeck, Mantei, Vuoskoski, Maes & Leman (2021). "Livestream Experiments." Front. Psychol. 12:647929 | DOI 10.3389/fpsyg.2021.647929；[Frontiers](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.647929/full) | OA | 物理的プレゼンス／社会的プレゼンスの二分——会場+メタバースの設計根拠 | ✔ |
| C-02 | Swarbrick, Seibt, Grinspun & Vuoskoski (2021). "Corona Concerts." Front. Psychol. 12:648448 | DOI 10.3389/fpsyg.2021.648448；[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8260031) | OA | 307名・13か国の仮想コンサート調査 | ✔ (DOI unverified) |
| C-03 | Swarbrick, Bosnyak, Livingstone, Bansal, Marsh-Rollo, Woolhouse & Trainor (2019). "How Live Music Moves Us." Front. Psychol. 9:2682 | DOI 10.3389/fpsyg.2018.02682；[PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6336707/) | OA | ライブは身体を動かす | ✔ |
| C-04 | Charron (2017). "Music Audiences 3.0." Front. Psychol. 8:800 | DOI 10.3389/fpsyg.2017.00800；[Frontiers](https://www.frontiersin.org/articles/10.3389/fpsyg.2017.00800/full) | OA | VRコンサート機会の初期声明 | ✔（ノート⑥では unverified） |
| C-05 | Onderdijk, Bouckaert, Van Dyck & Maes (2023). "Concert experiences in virtual reality environments." Virtual Reality | DOI 10.1007/s10055-023-00814-y；[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10239717/) | OA | 没入感が評価を規定 | ✔ (DOI unverified) |
| C-06 | Tschacher et al. (2023). "Audience synchronies in live concerts…" Sci. Rep. | [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10556000/) | OA | 観客の生理同期 | ✔ |
| C-07 | Leeds 関連 within-subjects 研究：360° VR クラシック vs デスクトップ | [White Rose 172355](https://eprints.whiterose.ac.uk/id/eprint/172355/) | — | VR で快・プレゼンス上昇 | authors/venue need checking |
| C-08 | Project MultiLive (Southampton). "Empirical Insights into Concert Streaming" | [project](https://screeningliveperformance.soton.ac.uk/?p=437) | — | ライブ性＝感覚＋省察 | project page; locate article |
| C-09 | Frontiers in Psychology 2024, 1214930（配信の孤独低減） | [Frontiers](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1214930/epub) | OA | 共有主体感・プレゼンスが孤独を減らす | （フラグなし・URLあり） |
| C-10 | Vandenberg, Berghman & Schaap (2021). "The 'lonely raver'." European Societies 23(S1) | DOI 10.1080/14616696.2020.1818271；[EUR](https://pure.eur.nl/en/publications/the-lonely-raver-music-livestreams-during-covid-19-as-a-hotline-t/) | — | 1,501 コメント分析；物理群衆の不在 | （フラグなし・URLあり） |
| C-11 | Rendell (2021). "Staying In, Rocking Out." Convergence 27(4) | DOI 10.1177/1354856520976451；[USW](https://pure.southwales.ac.uk/en/publications/staying-in-rocking-out-online-live-music-portal-shows-during-the-/) | — | 「ポータルショー」概念 | [DOI from prior knowledge, unverified] |
| C-12 | Weitzner, Freeman, Garrett & Chen (2012). "massMobile." NIME 2012 | [NIME](https://nime.org/proc/nime2012_weitzner/) | OA | スマホ大規模参加の枠組み | ✔ |
| C-13 | Lee & Freeman (2013). "echobo." NIME 2013 | [NIME](https://nime.org/proc/nime2013_lee_a/) | OA | 和声制約付き観客楽器 | ✔ |
| C-14 | Hindle (2013). "SWARMED." NIME 2013 | [NIME](https://nime.org/proc/nime2013_hindle/) | OA | インストール不要参加 | ✔ |
| C-15 | Zhang, Wu & Barthet (2016). "Open Symphony." NIME 2016 | [NIME](https://nime.org/proc/nime2016_zhang/) | OA | 投票参加——制御感と遅延の懸念 | ✔ |
| C-16 | Wu, Zhang, Bryan-Kinns & Barthet (2017). "Open Symphony." IEEE MultiMedia 24(1), 48–62 | DOI 10.1109/MMUL.2017.19；[QMUL](https://qmro.qmul.ac.uk/xmlui/handle/123456789/22542?show=full) | 非OA | ジャーナル版 | ✔ (DOI unverified) |
| C-17 | Hödl, Fitzpatrick, Kayali & Holland (2017). "Design Implications for Technology-Mediated Audience Participation in Live Music." SMC 2017 | [ORO](https://oro.open.ac.uk/52731) | OA | >200名調査；表現性・コミュニケーション・適切性 | ✔ |
| C-18 | Hödl (2016). PhD, TU Wien | [TU Wien](https://repositum.tuwien.at/handle/20.500.12708/6615) | OA | TMAP 設計空間 | ✔ |
| C-19 | Hödl et al. (2019). "TMAP Design Cards." Springer | [PDF](https://eprints.cs.univie.ac.at/6284/1/Pages%20from%202019_Book_NewDirectionsInMusicAndHuman-C.pdf) | — | 設計カード | ✔ |
| C-20 | Kayali, Hödl et al. (2017). CHI PLAY '17 poster | [PDF](https://eprints.cs.univie.ac.at/5453/1/FINAL_p437-kayali.pdf) | OA | ライブ観客インタラクション | ✔ |
| C-21 | Egozy & Lee (2018). "*12*: Mobile Phone-Based Audience Participation in a Chamber Music Performance." NIME 2018 | [NIME](https://nime.org/proc/nime2018_egozy/) | OA | 観客スマホを作曲楽器に | ✔ |
| C-22 | "Pharosphones." NIME 2024 | [NIME](https://nime.org/proc/nime2024_70/) | OA | スマホを光源に、CVで動きを音へ | ✔ |
| C-23 | Yakura & Goto (2020). "Enhancing Participation Experience in VR Live Concerts by Improving Motions of Virtual Audience Avatars." ISMAR 2020, 555–565 | DOI 10.1109/ISMAR50242.2020.00083；[AIST PDF](https://staff.aist.go.jp/m.goto/PAPER/ISMAR2020yakura.pdf) | OA（著者版） | 日本発の VR ライブ観客研究 | ✔（DOI は二次参照のみ） |
| C-24 | Guang, Sakurai, Matsumura & Okafuji (2025). "The impact of audience avatar movements on presence in virtual live events." Front. Virtual Reality | DOI 10.3389/frvir.2025.1655545；[Frontiers](https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2025.1655545/abstract) | OA | 日本（UEC/立命館）の最新研究 | ✔ |
| C-25 | "Concert Interaction Translation." CHI EA 2025 | [arXiv 2503.13121](https://arxiv.org/abs/2503.13121) | OA | チャット感情→群衆反応 | ✔ |
| C-26 | Lin et al. (NTU, CHI EA 2025 LBW). 現地/オンライン観客の接続 | [PDF](https://graphics.cmlab.csie.ntu.edu.tw/~robin/docs/lbw25.pdf) | OA | HMD 視聴者の孤立感の知見 | ✔ |
| C-27 | Ppali et al. (2025). "The Virtual Concert-goer." PACM HCI (CSCW) | DOI 10.1145/3757431（unverified）；[Southampton](https://eprints.soton.ac.uk/509258) | OA（リポジトリ） | 遠隔観客のプラットフォーム別ニーズ | ✔ |
| C-28 | Ppali et al. (2024). "Remote Rhythms." DIS 2024 | [Southampton](https://eprints.soton.ac.uk/508479) | — | 104名の観客側設計 | ✔ |
| C-29 | Ppali, Boem, Covaci, Constantinides, Liarokapis & Turchet (2026). "Looking inside the VR Music Scene." CHI 2026 | DOI 10.1145/3772318.3791497；[Trento PDF](https://iris.unitn.it/retrieve/191a8c8c-e138-4d65-b07c-c87f73bd6e8a/3772318.3791497.pdf) | OA | 無料期待 vs 運営労働の緊張 | ✔ |
| C-30 | Lu, Shen, Li, Shen & Wigdor (2021). "More Kawaii than a Real-Person Live Streamer." CHI 2021 | DOI 10.1145/3411764.3445660；[PDF](https://www.cs.utoronto.ca/~luzhc/assets/pdf/CHI2021Vtuber.pdf) | OA（著者版） | VTuber 受容 | ✔ (DOI unverified) |
| C-31 | "Construction of a VR music live performance system to support improved sense of presence." AHFE | [record](https://openaccess.cms-conferences.org/publications/book/978-1-964867-40-3/article/978-1-964867-40-3_13) | OA | VR ライブシステム構築 | ✔ (authors not captured) |
| C-32 | Young, O'Dwyer, Moynihan & Smolic (2022). "Audience Experiences of a Volumetric VR Music Video." IEEE VR 2022, 775–781 | DOI 10.1109/VR51125.2022.00099；[V-SENSE PDF](https://v-sense.scss.tcd.ie/wp-content/uploads/2022/03/IEEE_VR_2022_VR_Music_Video_V2.pdf) | OA（著者版） | ボリュメトリック演者体験は「ほぼ未開拓」 | ✔（DOI は二次参照のみ） |
| C-33 | Young, O'Dwyer et al. (2023). "Feel the Music!" Arts 12(4):156 | DOI 10.3390/arts12040156；[MDPI](https://www.mdpi.com/2076-0752/12/4/156/htm) | OA | 触覚付きボリュメトリックMV | ✔ |
| C-34 | O'Dwyer, Young, Smolic et al. (2022). ACM MMSys 2022 demo | [PDF](https://v-sense.scss.tcd.ie/wp-content/uploads/2022/06/mmsys2022demo-final50.pdf) | OA | ボリュメトリック制作ワークフロー | ✔ |
| C-35 | 慶應 KMD (2023–24). "Interactive Volumetric Live Performance Between Sydney and Tokyo." SIGGRAPH Asia 2023 | [KMD news](https://www.kmd.keio.ac.jp/news/whats-new/2024/01/3533) | — | 日本のテレマティック・ボリュメトリック先例 | news page; locate record |
| C-36 | Kärki (2021). "Vocaloid Liveness?" In *Researching Live Music*, Routledge, 127–140 | [Turku](https://research.utu.fi/converis/portal/detail/Publication/68848166?lang=en_US) | 非OA | 初音ミク公演のライブ性論 | ✔ |
| C-37 | Royal Holloway / StoryFutures (2023). "Experiments in real-time hybrid performance" | [RHUL](https://pure.royalholloway.ac.uk/en/publications/experiments-in-real-time-hybrid-performance-innovating-in-the-cap) | — | 現地と遠隔は同じ体験を望まない | （フラグなし・URLあり） |
| C-38 | Geelhoed et al. (2016). "Co-present and remote audience experiences: intensity and cohesion." MTAP | [CWI PDF](https://ir.cwi.nl/pub/25045/mta2468.pdf) | OA | 強度・凝集の指標 | ✔ (DOI unverified) |
| C-39 | Andersen & Serafin (2024). Ambisonic concert for hearing-impaired audiences. SMC 2024 | [PDF](https://smcnetwork.org/smc2024/papers/SMC2024_paper_id75.pdf) | OA | 空間音響と没入 | ✔ |
| C-40 | Lund MSc (2026). 仮想オペラハウス、Quest Pro、n=18 | [LUP](https://lup.lub.lu.se/student-papers/record/9233095/file/9233107.pdf) | OA | 空間音響のAV同期許容 | 学生論文 |
| C-41 | Vinkel (2017). Aalborg MSc（一次アンビソニックスとプレゼンス） | [AAU](https://projekter.aau.dk/projekter/files/259989312/Master_Thesis__Simone_Vinkel_.pdf) | OA | 学生論文 | 学生論文 |
| C-42 | Turchet (2023). "Musical Metaverse: vision, opportunities, and challenges." Pers. Ubiquit. Comput. | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9837761) | OA | 議題設定論文 | ✔ |
| C-43 | Boem, Tomasetti & Turchet (2024). "Harmonizing the Musical Metaverse." NIME 2024 | [NIME](https://nime.org/proc/nime2024_33/) | OA | 標準スタック不在——自前インフラの正当化 | ✔ |
| C-44 | Turchet et al. (2025). "From the Internet of Musical Things to the Musical Metaverse" | [PoliTo](https://iris.polito.it/handle/11583/3006481) | — | 5G/B5G 議題 | ✔ |
| C-45 | Fadda et al. (2025). XR コンサートの空間化マルチトラック配信（提案） | [UniCA](https://iris.unica.it/handle/11584/464970) | — | システム提案 | ✔ |
| C-46 | "No More Handshaking" (arXiv 2101.07999) | [arXiv](https://arxiv.org/pdf/2101.07999) | OA | COVID 下の日本アイドル文化 | （フラグなし・URLあり） |
| C-47 | Anderson (Edinburgh 学生誌). 仮想アイドルと音楽体験 | [journal](https://journals.ed.ac.uk/music-ology-eca/article/download/6478/8788/21003) | OA | 学生誌 | 学生誌 |
| C-48 | Gen Z の VTuber 視聴（De Gruyter 2023） | [De Gruyter](https://www.degruyterbrill.com/document/doi/10.1515/omgc-2023-0030/pdf) | — | 若年層の視聴行動 | （フラグなし・URLあり） |
| C-49 | MoguraVR. Beat Wave（ボリュメトリック配信アプリ）と KAGI NIGHT 2022 | [MoguraVR](https://www.moguravr.com/?p=187320) | — | KAGI NIGHT が公的記録に残る唯一の一次資料 | 業界紙（年は推定） |

### 4.4 サイト技術の説明での引用（D群）

kaginight サイト（WebGL1 点群クラゲ、Web Audio 手続き音、SOUND ボタンのみ、`GL_FRAGMENT_PRECISION_HIGH` フォールバック）の技術説明に用いる。

| ID | 文献 | DOI / URL | OA | 意味 | フラグ |
|---|---|---|---|---|---|
| D-01 | Rudolf & Mould (2009). "Interactive Jellyfish Animation Using Simulation." GRAPP/VISIGRAPP 2009 | [Carleton PDF](https://gigl.scs.carleton.ca/papers/jelly.pdf)；[SciTePress](https://www.scitepress.org/Papers/2009/17924) | OA | クラゲ描画の標準モデル | DOI not retrieved |
| D-02 | Rudolf (2007). MSc thesis, Univ. of Saskatchewan | [HARVEST](https://harvest.usask.ca/items/ffd0cee1-8aea-46c2-b785-454298be2fb7/full) | OA | 同手法の学位論文版 | （フラグなし・URLあり） |
| D-03 | Rodic (2011). "Chrysaora: WebGL Jellyfish Simulation." SIGGRAPH 2011 Real-Time Live! | [SIGGRAPH](https://history.siggraph.org/?p=73397)；[Chrome Experiments](https://experiments.withgoogle.com/chrysaora) | OA（デモ） | Web クラゲ美学の直接の祖先 | yes |
| D-04 | holtsetio/aurelia (2025). three.js WebGPU 手続きクラゲ | [gittrend](https://gittrend.io/repo/holtsetio/aurelia) | OA | kaginight の移植元 | スター数は stale の可能性 |
| D-05 | rand-monster/jellyfish | [GitHub](https://github.com/rand-monster/jellyfish) | OA | Rudolf & Mould の WebGPU 版 | （フラグなし・URLあり） |
| D-06 | Dabiri, Colin, Costello & Gharib (2005). J. Exp. Biol. 208, 1257–1269 | DOI 10.1242/jeb.01519；[RWU](https://docs.rwu.edu/fcas_fp/110) | partial | クラゲ推進の渦構造 | DOI unverified |
| D-07 | Dabiri, Colin, Katija & Costello (2010). J. Exp. Biol. 213, 1217–1225 | [WHOI PDF](https://www.whoi.edu/science/AOPE/people/kyoung/Dabiri_etal_JExpBiol_2010.pdf) | OA | 7種の遊泳性能 | yes |
| D-08 | Gemmell et al. (2013). "Passive energy recapture in jellyfish…" PNAS 110(44), 17904–17909 | DOI 10.1073/pnas.1306983110；[Caltech](https://resolver.caltech.edu/CaltechAUTHORS:20190422-155747277) | OA | 収縮/弛緩サイクルが視覚パルスを駆動する生物学的根拠 | yes |
| D-09 | Gemmell, Costello & Colin (2014). Commun. Integr. Biol. 7(4) | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4203578) | OA | 停止渦の寄与 | yes |
| D-10 | Rasmussen et al. (2009). arXiv:0910.3242 | [ar5iv](https://ar5iv.labs.arxiv.org/html/0910.3242) | OA | 渦動力学シミュレーション | （フラグなし・URLあり） |
| D-11 | Crumley et al. (2012). UCT | [UCT PDF](https://people.cs.uct.ac.za/~Jgain/wp-content/papercite-data/pdf/crumley2012.pdf) | OA | 後続クラゲアニメーション | details not verified |
| D-12 | Reeves (1983). "Particle Systems." ACM TOG 2(2), 91–108 | DOI 10.1145/357318.357320；[Princeton PDF](https://www.cs.princeton.edu/courses/archive/spr15/cos426/papers/Reeves83.pdf) | OA（ミラー） | 粒子描画の原典 | DOI via Wikipedia/Synapse |
| D-13 | Zwicker, Pfister, van Baar & Gross (2001). "Surface Splatting." SIGGRAPH 2001, 371–378 | [Harvard VCG](https://vcg.seas.harvard.edu/publications/20010101-surface-splatting) | OA | 点群スプラッティングの原典 | DOI unverified |
| D-14 | Kipfer, Segal & Westermann (2004). "UberFlow." Graphics Hardware 2004, 115–122 | DOI 10.2312/EGGH/EGGH04/115-122；[TUM PDF](https://www.cs.cit.tum.de/fileadmin/w00cfj/cg/Research/Publications/2004/GPU_Particle_Engine/eghw04.pdf) | OA | GPU 粒子エンジン | yes |
| D-15 | Schütz & Wimmer (2019). "Rendering Point Clouds with Compute Shaders." SIGGRAPH Asia 2019 Posters | [arXiv 1908.02681](https://arxiv.org/pdf/1908.02681) | OA | `GL_POINTS` 基準線との対比 | yes |
| D-16 | Schütz, Kerbl & Wimmer (2021). CGF 40(4) | DOI 10.1111/cgf.14345；[EG DL](https://diglib.eg.org/handle/10.1111/cgf14345) | OA | 高スループット点群描画の現行参照 | yes |
| D-17 | Khronos. OpenGL ES Shading Language 1.00 §4.5 | [spec PDF](https://docs.nvidia.com/drive/active/5.0.10.3L/nvvib_docs/NVIDIA%20DRIVE%20Linux%20SDK%20Development%20Guide/baggage/GLSL_ES_Specification_1.0.17.pdf) | OA | `GL_FRAGMENT_PRECISION_HIGH` フォールバックの規範的根拠 | via quoting sources |
| D-18 | Imagination Technologies. `GL_OES_fragment_precision_high` | [docs.imgtec](https://docs.imgtec.com/reference-manuals/open-gl-es-extensions/html/topics/GL_OES/fragment-precision-high.html) | OA | ベンダー側記述 | （フラグなし・URLあり） |
| D-19 | Toasa et al. (2019). "Performance Evaluation of WebGL and WebVR Apps in VR Environments." ISVC 2019 | [UPS](https://pure.ups.edu.ec/en/publications/performance-evaluation-of-webgl-and-webvr-apps-in-vr-environments/) | abstract | 端末横断の WebGL 負荷試験 | yes |
| D-20 | Florez et al. (2021). "Performance of WebGL standard for displaying 3D applications on mobile devices." CISTI 2021 | [UNIR](https://reunir.unir.net/items/245800a5-2e76-4a16-a87f-06219647fa7f/full) | abstract | モバイル WebGL 性能 | yes |
| D-21 | Goukouni et al. (KFUPM). WebGL 最適化手法 | [KFUPM](https://pure.kfupm.edu.sa/en/publications/methods-tested-to-optimize-the-performance-of-webgl-applications/) | — | GPU メモリ・初期化 | （フラグなし・URLあり） |
| D-22 | Basemark Web 3.0 / Browsermark 2.0 | [Khronos](https://www.khronos.org/news/permalink/rightware-introduces-browsermark-2.0-with-tests-for-webgl-css3-html5-and-mo) | — | 業界ベンチマーク | 非学術 |
| D-23 | Kawase (2003). "Frame Buffer Postprocessing Effects in DOUBLE-S.T.E.A.L." GDC 2003 | [Intel](https://www.intel.com/content/www/us/en/developer/videos/improving-real-time-gpu-based-image-blur-algorithms-kawase-blur-and-moving-box-averages.html) | — | 安価な多段ブラー | secondary |
| D-24 | Bjørge (2015). "Bandwidth-Efficient Rendering." SIGGRAPH 2015 course | [SIGGRAPH](https://history.siggraph.org/?p=59817) | PDF not opened | デュアルフィルタ | partial |
| D-25 | Arm Mobile Graphics blog. モバイル後処理 | [Arm](https://developer.arm.com/community/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/post-processing-effects-on-mobile-optimization-and-alternatives) | OA | ブルームの帯域コスト | （フラグなし・URLあり） |
| D-26 | Jimenez (2014). "Next Generation Post Processing in Call of Duty: Advanced Warfare." SIGGRAPH 2014 | [iryoku](https://www.iryoku.com/next-generation-post-processing-in-call-of-duty-advanced-warfare/) | OA | ピラミッド型ブルーム | yes |
| D-27 | Hable (2010). "Uncharted 2: HDR Lighting." GDC 2010 | [SlideShare](https://www.slideshare.net/naughty_dog/lighting-shading-by-john-hable) | OA | フィルミックトーンカーブ | yes |
| D-28 | Hable. "Filmic Tonemapping with Piecewise Power Curves" | [tizian/tonemapper](https://github.com/tizian/tonemapper) | OA | 後継定式 | secondary |
| D-29 | Narkowicz (2016). "ACES Filmic Tone Mapping Curve" | [tonemapper 掲載](https://github.com/tizian/tonemapper) | OA | WebGL 定番の ACES 近似 | secondary |
| D-30 | Reinhard, Stark, Shirley & Ferwerda (2002). "Photographic Tone Reproduction for Digital Images." ACM TOG 21(3) | DOI 10.1145/566654.566575 | — | 写真的トーン再現 | DOI unverified |
| D-31 | ACES Central. トーンマッピング技術詳細 | [docs.acescentral](https://docs.acescentral.com/system-components/output-transforms/technical-details/tone-mapping/) | OA | RRT/ODT の一次資料 | （フラグなし・URLあり） |
| D-32 | ETASR (2025). Android ブルームベンチマーク | [ETASR](https://etasr.com/index.php/ETASR/article/download/19101/6940) | OA | mipmap/Kawase が最安 | yes |
| D-33 | "Neural Bloom" (arXiv 2509.05963, 2025) | [arXiv](https://arxiv.org/html/2509.05963v1) | OA | 文脈引用 | （フラグなし・URLあり） |
| D-34 | W3C (2021-06-17). Web Audio API, W3C Recommendation | [W3C REC](https://www.w3.org/TR/2021/REC-webaudio-20210617/) | OA | 規格の一次資料 | yes |
| D-35 | W3C Audio WG charter (2022) | [charter](https://w3c.github.io/charter-drafts/2022/audio-2022.html) | OA | 保守体制 | （フラグなし・URLあり） |
| D-36 | Wilson (2013). "A Tale of Two Clocks." HTML5Rocks/web.dev | [web.dev](https://web.dev/articles/audio-scheduling) | OA | 先読みスケジューリング——「同期」の説明責任 | yes |
| D-37 | WAAClock (sebpiq) | [GitHub](https://github.com/sebpiq/WAAClock) | OA | 同パターンの実装 | （フラグなし・URLあり） |
| D-38 | Chrome. "Autoplay policy in Chrome" (2018) | [developer.chrome.com](https://developer.chrome.com/blog/autoplay) | OA | SOUND ボタン設計の根拠 | yes |
| D-39 | Chrome. "Web Audio, Autoplay Policy and Games" | [developer.chrome.com](https://developer.chrome.com/blog/web-audio-autoplay) | OA | Chrome 71 で Web Audio 施行 | yes |
| D-40 | WebKit (2017). "Auto-Play Policy Changes for macOS" | [webkit.org](https://webkit.org/?p=7734) | OA | Safari 11 の自動再生制限 | yes |
| D-41 | WebKit Bugzilla 182506（AudioWorklet） | [bugs.webkit](https://bugs.webkit.org/show_bug.cgi?id=182506) | OA | AudioWorklet 経緯 | （フラグなし・URLあり） |
| D-42 | Choi. "Audio Worklet" / design pattern | [developer.chrome.com](https://developer.chrome.com/blog/audio-worklet?hl=ru) | OA | 描画スレッドモデル | （フラグなし・URLあり） |
| D-43 | Gil Panal, Richard & David (2025). MLS 往復遅延推定. WAC 2025 (Best Poster) | [HAL hal-05154354](https://hal.univ-lyon2.fr/S2A/hal-05154354v2) | OA | 唯一の査読付きブラウザ遅延研究 | yes |
| D-44 | Superpowered. 遅延テストアプリ／ブラウザ遅延テスト | [superpowered](https://superpowered.com/latency) | — | ≤10 ms＝プロ品質 | 非査読 |
| D-45 | Kaufman (2021). "Browser Audio Latency" | [jefftk](https://jefftk.com/p/browser-audio-latency) | OA | デスクトップ ~55–67 ms | ブログ |
| D-46 | W3C public-audio スレッド（2012–2014） | [2014](https://lists.w3.org/Archives/Public/public-audio/2014JulSep/0180.html) | OA | 仕様は I/O 遅延を扱わない | （フラグなし・URLあり） |
| D-47 | Generative.fm (Bainter) | [GitHub mirror](https://github.com/libreblog/generative.fm) | OA | ブラウザ生成音楽の同ジャンル | 非論文 |
| D-48 | Research Catalogue：SuperCollider サーバのブラウザ移植 | [RC](https://www.researchcatalogue.net/view/711664/1111185) | OA | Web Audio+Wasm の実現性 | （フラグなし・URLあり） |
| D-49 | W3C WAI. Understanding SC 2.2.2 Pause, Stop, Hide | [WCAG 2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide) | OA | 常時動くクラゲへの停止手段 | yes |
| D-50 | WCAG SC 1.4.2 Audio Control | [Yale](https://usability.yale.edu/digital-accessibility/accessibility-resources/accessibility-articles/animated-content-and-timing) | OA | 自動再生なしで自明に適合 | 二次要約（W3C 頁未取得） |
| D-51 | WCAG SC 2.3.3 Animation from Interactions | [Deque](https://dequeuniversity.com/resources/wcag2.1/2.3.3-animations-from-interactions) | OA | タップ反応の無効化手段 | 二次要約 |
| D-52 | W3C WAI Technique C39 (`prefers-reduced-motion`) | [W3C C39](https://www.w3.org/WAI/WCAG22/Techniques/css/C39.html) | OA | 実装技法 | yes |
| D-53 | WebKit (2017). "Responsive Design for Motion" | [webkit.org](https://webkit.org/blog/7551/responsive-design-for-motion/) | OA | Safari 10.1 で出荷 | yes |
| D-54 | CSSWG 2017/2020 アーカイブ（Media Queries Level 5） | [2017](https://lists.w3.org/Archives/Public/public-css-archive/2017Apr/0498.html) | OA | 仕様経緯 | （フラグなし・URLあり） |
| D-55 | The A11y Project. "Don't auto-play video, music and more" | [a11yproject](https://www.a11yproject.com/posts/never-use-auto-play/) | OA | スクリーンリーダー利用者 | （フラグなし・URLあり） |
| D-56 | 香港 OGCIO Web Accessibility Handbook §6.5 | [OGCIO](https://www.ogcio.gov.hk/en/community/web_mobileapp_accessibility/promulgating_resources/handbook/top_ten_concerns/6_5_difficulties_in_browsing.htm) | OA | 背景音はユーザー起動で | （フラグなし・URLあり） |
| D-57 | axe rule `no-autoplay-audio` | [mirror](https://rocketvalidator.com/accessibility-validation/axe/4.7/no-autoplay-audio.md) | OA | 自動検査規則 | （フラグなし・URLあり） |
| D-58 | Lee & Ahn (2012). "Attention to Banner Ads and Their Effectiveness: An Eye-Tracking Approach." IJEC 17(1) | [KAIST](https://dspace.kaist.ac.kr/handle/10203/101840) | partial | 動くバナーは注意を減らす | yes |
| D-59 | Hong, Cheung & Thong (2021). JAIS 22(1) | [AISeL](https://aisel.aisnet.org/jais/vol22/iss1/2) | partial | 閲覧時は動きが注意を捕捉、検索時は無効果 | yes |
| D-60 | Simola et al. 実ページ眼球運動 | [Turku](https://research.utu.fi/converis/portal/detail/Publication/3550924?lang=en_GB) | — | 動きへの視覚感度 | （フラグなし・URLあり） |
| D-61 | ToCHI 2004 アニメバナー論文 | [PDF](https://thoughtcrumbs.com/publications/ToCHI04.pdf) | OA | 課題妨害、記憶は増えず | author attribution not verified |
| D-62 | Frontiers in Psychology (2017) 8:881 | [Frontiers](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.00881/full) | OA | アニメーションは注意を捕捉 | （フラグなし・URLあり） |
| D-63 | PMC5454066 (2017) | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5454066) | OA | 関連眼球運動研究 | details not extracted |
| D-64 | IZEA／reelflow（NN/g 二次言及） | [IZEA](https://izea.com/resources/4-website-features-that-drive-customers-nuts/) | — | 実務者の意見 | unverified |
| D-65 | Collet et al. (2015). "High-quality streamable free-viewpoint video." ACM TOG 34(4) | DOI 10.1145/2766945；[hhoppe](https://hhoppe.com/proj/fvv/) | OA | 初の端から端までの FVV | yes |
| D-66 | Orts-Escolano et al. (2016). "Holoportation." UIST 2016, 741–754 | DOI 10.1145/2984511.2984517；[MSR](https://www.microsoft.com/en-us/research/?p=509519) | partial | 実時間3Dテレポーテーション | yes |
| D-67 | Schreer, Feldmann, Renault, Zepp, Eisert & Kauff (2019). "Capture and 3D Video Processing of Volumetric Video." IEEE ICIP 2019 | [Fraunhofer](https://publica.fraunhofer.de/handle/publica/410505) | OA | 16ステレオ対→単一点群 | yes |
| D-68 | Schreer et al. "Advanced Volumetric Capture and Processing." SMPTE MIJ 128(5) | [SMPTE](https://journal.smpte.org/periodicals/SMPTE%20Motion%20Imaging%20Journal/128/5/13/) | — | ジャーナル版 | （フラグなし・URLあり） |
| D-69 | Schreer (2023). CWI Spring School keynote | [CWI PDF](https://www.dis.cwi.nl/files/spring-school/Oliver_Schreer_2023_03_KeynoteSpringSchoolCWI_VolumetricVideo_public.pdf) | OA | 概観スライド | （フラグなし・URLあり） |
| D-70 | "FVV Live" (arXiv 2007.00558, 2020) | [arXiv](https://arxiv.org/pdf/2007.00558) | OA | 民生機材での FVV | （フラグなし・URLあり） |
| D-71 | Intel True View（Yale CCAM 言及・特許のみ） | [Yale CCAM](https://ccam.yale.edu/news/exploring-volumetric-video-capture-early-steps) | — | 技術論文なし | gap |

### 4.5 発表先と締切（E群）

2026-10-14 時点のステータスを原ノートの【】表記で示す。

| ID | ベニュー／助成 | 次回締切・状態 | 提出物・条件 | URL |
|---|---|---|---|---|
| E-01 | **IEEE VR 2027 Research Demos**（Melbourne, 2027-02-27〜03-03） | **2026-12-07 AoE【受付中】**、通知 2027-01-07、CR 2027-01-12 | 2頁抄録+レイアウト図+1〜2分動画、PCS、現地実演必須 | [CfP](https://ieeevr.org/2027/contribute/demos/) |
| E-02 | IMWUT（UbiComp/ISWC フルペーパー経路） | 毎年 2/1・5/1・11/1；次回 2026-11-01（第三者情報、要公式確認） | ジャーナル投稿 | [Author Guide](https://ubicomp.org/ubicomp-iswc-2026/iswc_author_guide/)；[PaperPilot](https://www.getpaperpilot.com/deadlines/ubicomp-iswc-2026.html) |
| E-03 | NIME 2027 | 【次回未公表】；NIME 2026 は抄録 2026-02-05／本文 02-12【締切済】。2027 は 5〜7月開催想定 | long/medium/short、alt.nime、Music トラックで同作品を二重提出可。採択率参考 NIME 2022 論文 38% | [NIME 2026 CfP](https://nime.org/web_archive/2026/call/papers/index.html)；[hosting call](https://forum.nime.org/t/call-for-hosting-nime-2026-and-2027/594)；[採択率](https://forum.nime.org/t/nime-2022-acceptance-rates/386) |
| E-04 | CHI 2027 論文／alt.chi | CHI 2027 論文 2026-09-10【締切済】；alt.chi 2027 分【次回未公表】（前回 9月） | — | [CHI 2027](https://chi2027.acm.org/?p=2598)；[alt.chi](https://chi2026.acm.org/tag/alt-chi-2/) |
| E-05 | SIGGRAPH Asia 2026 Art Papers／SIGGRAPH 2027 | SA2026 2026-06-08【締切済】；2027【次回未公表】（SA Art Papers は例年6月） | 匿名化必須（2022） | [SA2026](https://asia.siggraph.org/2026/submissions/)；[PaperPilot](https://www.getpaperpilot.com/deadlines/siggraph-2027.html) |
| E-06 | ISEA2026 Dubai／ISEA2027 | 2026 公募 2025-12-15/20【締切済】；2027 ホスト【次回未公表】。開催時期に情報の食い違い（4月 vs 11月） | 英語必須；パフォーマンス提案・論文・デモ可 | [EasyChair](https://easychair.org/cfp/ISEA2026-Dubai)；[WAM](https://www.wam.ae/en/article/c2nmy3i-isea2026-dubai-connects-global-dialogue-with) |
| E-07 | Prix Ars Electronica 2027 | 2026 締切 2026-03-04【締切済】；2027【次回未公表】（例年3月） | 無料・オンライン、S+T+ARTS Prize 併願可、Golden Nica 最大 €10,000 | [Open Call](https://www.cityofmediaarts.at/?p=3055)；[JA](https://ars.electronica.art/prix/ja/opencall) |
| E-08 | NICOGRAPH International 2027 | 2026 抄録 2026-01-28／論文 02-04【締切済】；2027【次回未公表】 | 採録論文は IEEE Xplore 収録 | [EasyChair](https://www.easychair.org/cfp/NICOInt2026) |
| E-09 | 情報処理学会 SIGMUS | 年5回；第146回以降の締切【未確認】 | 国内研究室との接点づくりに最短 | [DAL](https://av.watch.impress.co.jp/docs/series/dal/1638224.html) |
| E-10 | 情報処理学会 EC2026 | 日程・締切【未確認】 | 研究報告シリーズ継続 | [IPSJ EC](https://ipsj.ixsq.nii.ac.jp/records/217523) |
| E-11 | IEEE ISMAR 2026（Bari） | 論文・ポスター・WS・Pitch Your Lab すべて【締切済】；Demos CfP【未確認】 | — | [CfP](https://web3d.org/pipermail/x3d-public_web3d.org/2026-January/022250.html) |
| E-12 | UbiComp/ISWC 2026 Posters & Demos／Design Exhibition | 2026-06-06／06-08【締切済】 | 著者1名の登録・現地発表必須 | [Posters & Demos](https://www.ubicomp.org/ubicomp-iswc-2026/posters-demos-2026/) |
| E-13 | Web Audio Conference | WAC 2025 締切 2025-06-13；次回 2027 ブラジル（2026 開催未確認） | サイト音響の発表先 | [WAC 2025](https://wac-2025.ircam.fr/) |
| E-14 | ICLC 2027（Antwerp, 2027-03-09〜13） | CfP 流通中 | ライブコーディング隣接 | [CfP](https://groups.google.com/g/nime-community/c/422DJiFP5lM) |
| E-15 | EAI ArtsIT 2026 特別トラック／ACM ICMI 2026 LBR | — | 周辺受け口 | [ArtsIT](https://groups.google.com/g/nime-community/c/to116VASFeg)；[ICMI](https://groups.google.com/g/nime-community/c/rqCCvydrGFo) |
| E-16 | CEDEC 2026 講演公募 | 2026-02-09【締切済】 | 講演（論文ではない） | [GameBusiness](https://www.gamebusiness.jp/article/2026/01/06/25914.html) |
| E-17 | **アーツカウンシル東京「東京芸術文化創造発信助成」** | 2026年度第2期 2026-06-30 公募開始（締切日未確認）；第1期は 2026-02-03〜03-03【締切済】→2027年度第1期 ≒ 2027年2月 | 東京拠点、カテゴリーⅠ 個人上限50万円・補助率1/2、事業期間 2027-01-01〜12-31 | [リリース](https://www.artscouncil-tokyo.jp/uploads/2026/06/2026-2_grant_creation_social_release-260630.pdf)；[ガイドライン](https://www.artscouncil-tokyo.jp/sys/wp-content/uploads/2026/06/2026_2_c1_grant-creation_guideline.pdf) |
| E-18 | 芸術文化振興基金 令和9年度 | 【次回未公表】；令和8年度は 2025-10-31〜11-13【締切済】（例年秋） | 個人応募可否は要項未取得 | [群馬県 PDF](https://www.pref.gunma.jp/uploaded/attachment/658912.pdf) |
| E-19 | 文化庁 クリエイター支援基金 | 個人向け直接公募は確認できず（団体向け中心） | 採択団体の育成枠を探す | [文化庁](https://www.bunka.go.jp/shinsei_boshu/kobo/94310801.html) |
| E-20 | 経産省 IP360 補助金（VIPO 事務局） | 第2回公募 2026-06-30 開始；事業者向け | 事業者経由 | [GameBusiness](https://www.gamebusiness.jp/article/2026/06/24/27310.html) |
| E-21 | Epic MegaGrants | 2026 Cycle 2 審査中（通知 2026-12-07〜11）；Cycle 1 2027 ≒ 2027年1月中旬（推定） | — | [MegaGrants](https://www.unrealengine.com/en-US/megagrants) |
| E-22 | Unity for Humanity 2027 | 2026 締切 2026-02-20【締切済】；2027 ≒ 2027年2月（推定、SDG 文脈必要） | — | [Unity blog](https://unity.com/ja/blog/unity-for-humanity-2026-grant-now-open) |
| E-23 | LACMA Art + Technology Lab 2026（Snap・Anthropic 支援） | 2026 サイクルは2年コホート制（締切日はノート未記載） | 最大 $50,000、個人・世界可 | [Submittable](https://lacma.submittable.com/submit/348727/2026-art-technology-lab-grants) |
| E-24 | STYLY NEWVIEW AWARDS | 2025/2026 回【次回未公表】（2024 は Vision Pro 部門新設） | STYLY 制作作品 | [CGWORLD](https://cgworld.jp/flashnews/2408-news-newviewawards24.html) |
| E-25 | 文化庁メディア芸術祭／後継 | 終了・後継の公式発表は裏付け取れず | — | [About](https://www.bunka.go.jp/j-mediaarts/about/index.html) |
| E-26 | 栃木県メディア芸術クリエイター支援（自治体例） | 2026-06-15【締切済】 | 県ゆかりの個人 | [栃木県](https://www.pref.tochigi.lg.jp/c10/education/bunka/geijyutsu/media-josei2026.html) |
| E-27 | 出展・出演枠：VketReal 2026 Summer（HIKKY）、cluster 新施策、ReVers3:x（Sony Music）、PANDORA×ソニー製作委員会、1st Stage（常設XRライブハウス）、Mixalive TOKYO、CinemaLeap Immersive Journey、拡張音楽堂 | 公募時期は各社告知に依存 | 技術仕様書+実演映像を持ち込む | [VketReal](https://koubo.jp/press-release/prtimes/c34617_r487)；[cluster](https://www.moguravr.com/?p=304457)；[ReVers3:x](https://www.gizmodo.jp/article/revers3x/)；[PANDORA×Sony](https://www.moguravr.com/?p=363283)；[1st Stage](https://www.moguravr.com/?p=316791)；[CinemaLeap](https://ascii.jp/elem/000/004/400/4400961/)；[拡張音楽堂](https://kigyolog.com/interview.php?id=295) |

### 4.6 集客・収益化の根拠（F群）

| ID | 文献 | DOI / URL | OA | 意味 | フラグ |
|---|---|---|---|---|---|
| F-01 | Bär, Boyacıoğlu & Kurscheidt (2025). "On the edge of a digital event era: Which innovative factors influence the willingness to pay for virtual concerts?" J. Innovation & Knowledge 10(5), 100776 | DOI 10.1016/j.jik.2025.100776；[Elsevier](https://www.elsevier.es/en-revista-journal-innovation-knowledge-376-articulo-on-edge-digital-event-era-S2444569X25001210) | OA | VRコンサート WTP €35–39.99 帯 | ✔（ノート⑥では [unverified]） |
| F-02 | Regner (2021). "Crowdfunding a monthly income: Patreon." J. Cultural Economics 45(1) | DOI 10.1007/s10824-020-09381-5；[RePEc](https://ideas.repec.Org/a/kap/jculte/v45y2021i1d10.1007_s10824-020-09381-5.html) | — | 上位1%≥$2,500/月、大半はゼロ——収入計画の現実的下限 | [partly verified: numbers from secondary summary] |
| F-03 | Strauss, Yang & Mazzucato (2025). "'Rich-Get-Richer'? Platform Attention and Earnings Inequality using Patreon." arXiv:2509.26523／ICC | [arXiv](https://arxiv.org/abs/2509.26523v2) | OA | パレート指数≈2 | （フラグなし・URLあり） |
| F-04 | Strauss et al. (2022). Patreon 分析. ICWSM 2022 | [AAAI PDF](https://ojs.aaai.org/index.php/ICWSM/article/download/19338/19110/23351) | OA | 狭く支援するパトロンは忠実 | [partly verified: could not open PDF; exact title/authors unverified] |
| F-05 | Bonifacio, Hair & Wohn (2023). "Beyond fans: The relational labor… of creators on Patreon." New Media & Society 25(10), 2684–2703 | DOI 10.1177/14614448211027961；[NJIT](https://digitalcommons.njit.edu/fac_pubs/1391) | — | 少数パトロンへの依存リスク | （フラグなし・URLあり） |
| F-06 | Bonifacio et al. (2022). "Multi-platform practices among digital patronage creators." Convergence | [NJIT](https://digitalcommons.njit.edu/fac_pubs/2609) | — | マルチプラットフォーム運用 | （フラグなし・URLあり） |
| F-07 | Bärtl (2018). "YouTube channels, uploads and views." Convergence 24(1), 16–32 | DOI 10.1177/1354856517736979；[Offenburg](https://opus.hs-offenburg.de/frontdoor/index/index/year/2018/docId/2616) | — | 3%のチャンネルに85%の視聴 | DOI [unverified] |
| F-08 | Pew Research Center (2019). "A Week in the Life of Popular YouTube Channels" | [Pew](https://www.pewresearch.org/internet/2019/07/25/a-week-in-the-life-of-popular-youtube-channels/) | OA | 上位10%が70%の動画 | （フラグなし・URLあり） |
| F-09 | Twitch 支払データ流出（2021）分析 | [Gigazine](https://gigazine.net/gsc_news/en/20211012-many-twitch-streamer-dont-minimum-wage/)；[Sherwood](https://sherwood.news/tech/twitch-streamers-chasing-viewers) | — | 上位1%が50%超、75%は≤$120 | 二次報道 |
| F-10 | Substack 有料購読 500万（2025-03）；転換率の実務者推定 1–10% | [preIPO](https://preipomedia.substack.com/p/the-numbers-dont-show-a-substack)；[bestwriting](https://bestwriting.com/substack-statistics) | — | 無料→有料の目安 | 非査読 |
| F-11 | Statista (2022). Patreon 収入比率 | [Statista](https://statista.com/statistics/1308585/income-share-patreon-creators-by-source) | — | >40% が Patreon 由来 | 標本不明 |
| F-12 | note株式会社 IR（FY2024 GMV 170.64億円 +24.4%、有料比率24.8%、FY2025 Q3 GMV +27.4%、会員1,000万） | [FY2024](https://www2.jpx.co.jp/disc/52430/140120250114550537.pdf)；[Q3 FY2025](https://www2.jpx.co.jp/disc/52430/140120251007569452.pdf) | OA | note が主戦場である根拠 | [partly verified: figures from search snippets of the PDFs] |
| F-13 | note クリエイター収益（上位1,000人平均 667万円 2021；メンバーシップ +81.3% YoY 2025-11） | [logmi](https://finance.logmi.jp/377715)；[appbank](https://www.appbank.net/2026/01/08/iphone-news/2902024.php) | — | 月額メンバーシップが最成長 | 1,160万円（2024）は [unverified] |
| F-14 | finboard note 集計 | [finboard](https://finboard.jp/companies/JP:5243) | — | 年間GMV 213億円 | [unverified aggregator] |
| F-15 | BASE株式会社 IR（FY2025 Q2 GMV +11.5%、FY2026 Q1 売上 +18.7%） | [Q2 FY2025](https://www2.jpx.co.jp/disc/44770/140120250805530448.pdf)；[Q1 FY2026](https://www2.jpx.co.jp/disc/44770/140120260512525540.pdf) | OA | グッズ基盤の成長 | （フラグなし・URLあり） |
| F-16 | Kelly (2008). "1,000 True Fans" | [kk.org](https://kk.org/thetechnium/1000-true-fans/) | OA | 実務者の古典 | [URL from memory, unverified this session] |
| F-17 | Baym (2018). *Playing to the Crowd*. NYU Press | [OAPEN](https://library.oapen.org/handle/20.500.12657/89477) | OA | 「関係労働」の概念 | （フラグなし・URLあり） |
| F-18 | Ma et al. (2022). K-pop ライブ配信. Front. Psychol. 13:865698 | DOI 10.3389/fpsyg.2022.865698；[Frontiers PDF](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.865698/pdf) | OA | パラソーシャル→愛着→購買意図（N=288） | [partly verified: author list not confirmed] |
| F-19 | Krause, North & Heritage (2018). "Musician interaction via social networking sites." Music & Science 1 | [JCU](https://researchonline.jcu.edu.au/62740/) | OA | N=464、愛着スタイルが SNS 交流を予測 | （フラグなし・URLあり） |
| F-20 | Kulczynski (2014). PhD, Univ. of Newcastle | [NOVA](https://nova.newcastle.edu.au/vital/access/ /manager/Repository/uon:14999) | OA | コンサート来場の9動機 | 学位論文 |
| F-21 | 香港城市大 音声知識課金研究（2021） | [CityU](https://scholars.cityu.edu.hk/en/publications/%E4%B8%BA-%E9%99%AA%E4%BC%B4-%E4%B9%B0%E5%8D%95%E5%87%86%E7%A4%BE%E4%BC%9A%E5%85%B3%E7%B3%BB%E8%A7%86%E8%A7%92%E4%B8%8B%E9%9F%B3%E9%A2%91%E7%9F%A5%E8%AF%86%E4%BB%98%E8%B4%B9%E5%86%B3%E7%AD%96%E7%A0%94%E7%A9%B6/) | — | パラソーシャル→WTP | （フラグなし・URLあり） |
| F-22 | Erasmus MA (2025)／Tonneau (2025, N=235, 負の直接効果)／Indonesian thesis (2023) | [EUR](https://thesis.eur.nl/pub/76683/)；[Pace](https://digitalcommons.pace.edu/honorscollege_theses/322)；[UIN](https://digilib.uin-suka.ac.id/cgi/export/eprint/60940/EndNote/digilib-eprint-60940.enw) | — | 親密さ・互恵性・真正性が鍵；過剰は逆効果 | 学生研究 |
| F-23 | "Sharing Music: Social and Communal Aspects of Concert-Going." Networking Knowledge | [MeCCSA](https://www.ojs.meccsa.org.uk/index.php/netknow/article/view/428) | OA | 共同性 | （フラグなし・URLあり） |
| F-24 | Luminate（2023/2024）スーパーファン：人口の≈15%、ライブに $113/月、物販購入 73% vs 26% | [MBW](https://www.musicbusinessworldwide.com/15-of-the-general-population-of-the-us-are-superfans-heres-what-that-means-for-the-music-business)；[Hypebot](https://www.hypebot.com/forget-taylor-swift-these-stats-will-shape-2024-for-99-of-musicians/) | — | ライブ+物販が収益の中心 | 業界報告 |
| F-25 | Spotify「super listeners」2%／18%+ | [MBW](https://musicbusinessworldwide.com/superfans-make-up-2-of-artists-monthly-listeners-on-spotify-but-account-for-over-18-of-monthly-streams) | — | 少数が消費を支える | 業界報告 |
| F-26 | MIDiA (Q3 2024). "The superfans of music superstars: Identity and cut-through"（2,009名） | [MIDiA](https://midiaresearch.com/reports/the-superfans-of-music-superstars-identity-and-cut-through) | — | 「アイデンティティ共鳴」ファンは物販≈50% vs ≈33% | 業界報告 |
| F-27 | MIDiA (Q1 2025). "Defining entertainment superfans"（10か国・日本含む） | [MIDiA](https://www.midiaresearch.com/reports/defining-entertainment-superfans-characteristics-categories-and-commercial-impact) | 有料 | 日本を含む類型 | paywalled |
| F-28 | Soundcharts（MIDiA/SoundCloud 引用：1.9% のリスナーが 42% の収益） | [Soundcharts](https://soundcharts.com/blog/what-are-superfans-in-music) | — | 二次 | [unverified secondary] |
| F-29 | Lindgaard, Fernandes, Dudek & Brown (2006). "Attention web designers: You have 50 milliseconds…" BIT 25(2), 115–126 | DOI 10.1080/01449290500330448；[Nature news](https://www.nature.com/news/2006/060109/full/news060109-13.html) | — | 第一印象の halo | （フラグなし・URLあり） |
| F-30 | Reinecke et al. (2013). CHI 2013 | [PDF](https://wildlab.cs.washington.edu/Publications_files/Reinecke_CHI2013.pdf) | OA | 色彩度+複雑さで魅力の半分を説明 | （フラグなし・URLあり） |
| F-31 | Reinecke & Gajos (2014). "Quantifying Visual Preferences Around the World." CHI 2014, 11–20 | [PDF](https://iis.seas.harvard.edu/papers/reinecke14visual.pdf) | OA | 国・属性別の嗜好 | （フラグなし・URLあり） |
| F-32 | Akrimi (2016). IJEMR 7(3), 204–228 | [RePEc](https://ideas.repec.org/a/ids/ijemre/v7y2016i3p204-228.html) | — | インタラクティビティ→遊び心→eWOM | （フラグなし・URLあり） |
| F-33 | Suh, Ahn & Pedersen (2014). J. Applied Sport Management | [JASM](https://utk.exodar.janeway.systems/jasm/article/id/1008/) | — | 双方向性→再訪意図（N=235） | （フラグなし・URLあり） |
| F-34 | Hsu, Chang & Chen (2012). ISeB | [NYCU](https://ir.lib.nycu.edu.tw/handle/11536/20722?locale=en) | — | 遊び心・フロー→購買意図 | （フラグなし・URLあり） |
| F-35 | NTU 実験研究（N=292） | [NTU](https://scholars.lib.ntu.edu.tw/handle/123456789/455972) | — | 制御・方向・同期性→満足・推奨 | （フラグなし・URLあり） |
| F-36 | Chung & Tan (2004). "Antecedents of perceived playfulness." I&M | [AUT](https://openrepository.aut.ac.nz/items/6e858644-e636-4a79-a402-5084fd1e7b6b/full) | OA | 基礎 | （フラグなし・URLあり） |
| F-37 | Looyestyn et al. (2017). "Does gamification increase engagement with online programs?" PLOS ONE 12(3) | [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5376078/) | OA | 12/15 研究で正効果 | （フラグなし・URLあり） |
| F-38 | Israfilzade & Pathania (2026). ゲーミフィケーションとサブスク転換 | DOI 10.2478/mosr-2026-0005；[Sciendo](https://reference-global.com/article/10.2478/mosr-2026-0005) | — | 6.9倍（準実験、アプリ） | （フラグなし・URLあり） |
| F-39 | Sketchfab／Binkies 3D／Emersya／Muz.li／Cappasity（3D 埋め込みの滞在 5–10倍、+129% 転換など） | [Sketchfab](https://sketchfab.com/blogs/enterprise/?p=6824)；[Entel](https://binkies3d.com/case-studies/entel-cl) | — | ベンダー事例のみ | [unverified marketing claims] |
| F-40 | Behance 採用ガイド | [Behance](https://behance.net/blog/freelance-work-guide) | — | 発注者は完了実績・レビューを見る | 記述的 |
| F-41 | ぴあ総研（2024 市場 7,605億円・音楽 5,299億円；2025 市場 8,564億円・動員 9,223万人） | [KAI-YOU 2025](https://kai-you.net/article/92753)；[KAI-YOU 2026](https://kai-you.net/article/95702) | — | 日本ライブ市場の成長と大型IP集中 | 二次報道 |
| F-42 | ACPC 2023 基礎調査（動員 56,326,160、売上 5,140億円） | [ACPC PDF](https://www.acpc.or.jp/pdf/marketing/2023_yearround.pdf) | OA | 一次統計 | （フラグなし・URLあり） |
| F-43 | 矢野経済「オタク市場」（FY2024 ≈1兆99億円）／財務省『ファイナンス』2025-11 | [MOF](https://www.mof.go.jp/public_relations/finance/2025011/202511f.html) | OA | 推し活規模 | [partly verified: 矢野 press release itself not opened] |
| F-44 | NRI（2025-08-29）推し活 ≈3.8兆円 | [NRI](https://www.nri.com/jp/media/column/mcs_blog/20250829.html) | OA | 広義推計 | （フラグなし・URLあり） |
| F-45 | afb 調査（2025-06, n=500）月額推し活 ≤5,000円 51.6%、<1万円 ≈70% | [GameBusiness](https://www.gamebusiness.jp/article/2025/12/12/25732.html) | — | 個人の財布規模 | （フラグなし・URLあり） |
| F-46 | マイナビ（2025-10）平均 13,305円／Oshimoa（2023）女性≤34歳 16,091円 | [zaikei](https://www.zaikei.co.jp/releases/2376595/)；[Fashionsnap](https://www.fashionsnap.com/article/2023-08-06/oshikatsu-joshi/) | — | 価格設定の目安 | [partly verified: snippet only] |
| F-47 | 博報堂×SIGNING「オシノミクスレポート」 | [CEIS PDF](https://ceis.jp/wp-content/uploads/2024/11/I2_2024.pdf) | — | ファン心理6類型 | 数値未取得 |
| F-48 | ファンクラブ価格事例（入会金≈1,000円+年会費≈5,000–9,000円；hololive 6,600円） | [JBC](https://www.jbc-ltd.com/column/?p=6916)；[Game Watch](https://game.watch.impress.co.jp/docs/news/2049404.html) | — | 会費アンカー | 事例 |
| F-49 | ライブハウス経済（チケットノルマ／チャージバック） | [ticket.co.jp](https://www.ticket.co.jp/entx/?p=942)；[日大 PDF](https://www.cst.nihon-u.ac.jp/research/gakujutu/65/pdf/J-17.pdf)；[宮入『ライブハウス文化論』](https://www.kinokuniya.co.jp/f/dsg-08-9983303132) | — | 小会場依存の限界 | 統計なし |
| F-50 | Middlesex/KCL (2021). 配信有料化調査（約1,500名） | [KCL](https://www.kcl.ac.uk/news/report-finds-live-streamed-concerts-are-here-to-stay) | — | 72%/74% | 業界調査 |
| F-51 | PUSH LIVE UK (2021). 29%・£18.09 | [Advanced Television](https://www.advanced-television.com/2021/06/09/survey-160m-uk-music-live-streaming-opportunity/) | — | 配信価格アンカー | 業界調査 |
| F-52 | AMT Lab (2021/22, n=140). 92.1% が現地同額を拒否 | [AMT Lab](https://amt-lab.org/blog/2022/1/expanding-our-live-streaming-future-refining-and-developing-new-arts-amp-entertainment-experiences) | — | 配信は現地より安く | 業界調査 |
| F-53 | mySCENA Quebec (2021, 533名) | [mySCENA](https://myscena.org/?p=972019) | — | 同上 | 業界調査 |
| F-54 | Hofwegen (2021). Erasmus MA, n=189 | [EUR](https://thesis.eur.nl/pub/61306/) | OA | 動機とファン度が WTP を予測 | 学生論文 |
| F-55 | Nova SBE MSc (2021)：仮想観客は満足度高いが支払額は低い | [NOVA](https://run.unl.pt/handle/10362/123402?locale=en) | — | 学生論文 | 学生論文 |
| F-56 | US 仮想コンサート 2020 ≈$610M（Denver Channel）／NIVA 独立会場の約2/3が赤字（2024） | [Denver Channel](https://www.thedenverchannel.com/future-of-live-music-is-still-very-digital)；[Hypebot](https://www.hypebot.com/?p=82183) | — | 業界文脈 | [unverified secondary] |

### 4.7 未検証・URLなし——引用前に必ず書誌確認する文献

以下は原ノートで「本セッションで未確認・記憶由来」と明示された基礎文献である。数値・主張は転記しない。

| ID | 文献 | フラグ（原ノート表記） |
|---|---|---|
| U-01 | Leman (2008). *Embodied Music Cognition and Mediation Technology*. MIT Press | [unverified in this session; prior knowledge] |
| U-02 | Repp (2005). "Sensorimotor synchronization: A review of the tapping literature." Psychon. Bull. Rev. 12(6), 969–992. DOI 10.3758/BF03206433 | [DOI from prior knowledge, unverified] |
| U-03 | Maes, Leman, Palmer & Wanderley (2014). "Action-based effects on music perception." Front. Psychol. 4:1008. DOI 10.3389/fpsyg.2013.01008 | [unverified in this session; prior knowledge] |
| U-04 | Hunt, Wanderley & Paradis (2003). "The importance of parameter mapping in electronic instrument design." JNMR 32(4), 429–440 | [unverified in this session; prior knowledge] |
| U-05 | Wanderley & Orio (2002). "Evaluation of Input Devices for Musical Expression." CMJ 26(3), 62–76 | [unverified in this session; prior knowledge] |
| U-06 | Jordà (2004). "Digital Instruments and Players: Part I." NIME 2004 | [unverified in this session; prior knowledge] |
| U-07 | Morreale & McPherson (2017). "Design for Longevity." NIME 2017 | [unverified in this session; prior knowledge] |
| U-08 | Reeves, Benford, O'Malley & Fraser (2005). "Designing the spectator experience." CHI 2005 | UNVERIFIED this session |
| U-09 | Benford & Giannachi (2011). *Performing Mixed Reality*. MIT Press | UNVERIFIED this session |
| U-10 | Auslander (2008/2023). *Liveness: Performance in a Mediatized Culture*. Routledge | UNVERIFIED this session |
| U-11 | Chafe, Cáceres & Gurevich (2010). "Effect of temporal separation on synchronization in rhythmic performance." Perception 39(7) | UNVERIFIED this session |
| U-12 | Tuch, Presslaber, Stöcklin, Opwis & Bargas-Avila (2012). IJHCS 70(11), 794–811. DOI 10.1016/j.ijhcs.2012.06.003 | [unverified this session; from prior knowledge] |
| U-13 | Tractinsky, Katz & Ikar (2000). "What is beautiful is usable." Interacting with Computers 12(2), 127–145 | [unverified this session] |
| U-14 | Pallais (2014). "Inefficient Hiring in Entry-Level Labor Markets." AER 104(11), 3565–99 | [unverified this session; from prior knowledge] |
| U-15 | Gandini (2016). *The Reputation Economy*. Palgrave | [unverified this session] |
| U-16 | Dell'Acqua et al. (2023) "jagged frontier"；Krueger *Rockonomics* (2019)；Connolly & Krueger (2006) | treat as unverified recall |
| U-17 | Flow Machines / "Daddy's Car"（Pachet, Sony CSL 2016）；Pachet, Roy & Carré (2020) 回顧 | unverified |
| U-18 | Georgia Tech 第三の腕の学術論文（Bretan & Weinberg c. 2016） | could not be located |

---

## 5. 実行仕様 — サイト・発表先・計測・読書の順で動く

### 5.1 サイトに追加する RESEARCH セクション（15件）

kaginight サイトに「RESEARCH」節を設け、以下15件を「鍵山の実践がどの研究の問いに答えるか」の一行とともに掲載する。選定基準は (a) OA で読者が辿れる、(b) 検証フラグが ✔／verified／snippet-verified 以上、(c) 自己紹介・技術・観客・経済の4軸を網羅、の三点である。表示順は読者の関心（なぜエアドラムか→なぜこの遅延設計か→観客に何が起きるか→なぜ価値があるか→サイトのクラゲは何か）に沿う。

| 順 | ID | 掲載文献 | サイトでの一行 |
|---|---|---|---|
| 1 | A-01 | Godøy, Haga & Jensenius 2006 | エアドラムは「音を生む動作の模倣」として研究された現象である |
| 2 | A-13 | Mäki-Patola 2005 | 物理スティックは仮想スティックより正確——だからスティックを持つ |
| 3 | B-01 | Wessel & Wright 2002 | 楽器制御は <10 ms・<1 ms ジッタ、OSC で送る |
| 4 | B-02 | Jack et al. 2018 | 打楽器奏者は 10 ms と 20 ms を聞き分ける |
| 5 | B-14 | Abdlkarim et al. 2023 | ヘッドセットのハンドトラッキングは約45 ms——発音には使わない |
| 6 | B-29 | Banquiero et al. 2025 | IMU スティック+HMD の融合が最新の研究構成 |
| 7 | A-23 | Trolland et al. 2022 (AirSticks 2.0) | 最も近い先行楽器 |
| 8 | A-20 | Trolland, Ilsar & McCormack 2025 | 映像を先に設計する打楽器 |
| 9 | B-64 | StreamDiffusion 2023 | リアルタイム拡散映像のエンジン |
| 10 | C-03 | Swarbrick et al. 2019 | ライブは身体を動かす |
| 11 | C-06 | Tschacher et al. 2023 | 観客は生理的に同期する |
| 12 | C-01 | Onderdijk et al. 2021 | VR 視聴はアーティストとのつながりを高める |
| 13 | C-23 | Yakura & Goto 2020 | 日本発の VR ライブ観客研究——KAGI NIGHT が答える問い |
| 14 | F-01 | Bär et al. 2025 | 仮想コンサートの支払意思額は €35–39.99 帯 |
| 15 | D-01 + D-08 | Rudolf & Mould 2009／Gemmell et al. 2013 | サイトのクラゲは手続き的な収縮/弛緩で脈打つ |

実装上の注意は三つある。第一に、D 群の推論に従い、クラゲは「流体シミュレーション」ではなく「位相駆動の変形」であると正確に記述し、ブルームも実装がある場合に限り Kawase／Bjørge を引く（[web_graphics_audio KQ1/KQ3 Inferences](https://gigl.scs.carleton.ca/papers/jelly.pdf)）。第二に、Web の第一印象は 50 ms で決まり（[Lindgaard et al. 2006](https://www.nature.com/news/2006/060109/full/news060109-13.html)）、遊び心は再訪・口コミを予測しても問い合わせを直接生まない（[creator_economy KQ3 Inferences](https://ideas.repec.org/a/ids/ijemre/v7y2016i3p204-228.html)）ため、RESEARCH 節と同時に「出演・制作・共同研究・助成の問い合わせ」導線と実績（クレジット・協業先）を名前・役割・連絡先の上に置く。第三に、常時動くクラゲには WCAG 2.2.2 の停止手段または `prefers-reduced-motion`（Technique C39）を実装する（[W3C C39](https://www.w3.org/WAI/WCAG22/Techniques/css/C39.html)）。

### 5.2 狙うベニュー・助成と 2026–2027 の締切

| 優先 | 目標 | 締切（状態） | 提出形態 | 根拠 |
|---|---|---|---|---|
| 1 | IEEE VR 2027 Research Demos | **2026-12-07 AoE【受付中】** | 2頁抄録+図+1〜2分動画、現地実演 | 唯一の確認済み受付中締切、ライブ実演型と相性良（E-01） |
| 2 | アーツカウンシル東京 2026年度第2期／2027年度第1期 | 第2期は公募開始 2026-06-30（締切日未確認）；第1期 ≒ 2027年2月 | 東京拠点、個人上限50万円 | 無所属個人に最も門戸が広い（E-17） |
| 3 | NIME 2027（論文+Music トラック二重提出） | ≒ 2027年2月【次回未公表】 | long/medium/short + 演奏 | XRドラムを最も継続的に掲載（E-03） |
| 4 | Prix Ars Electronica 2027（S+T+ARTS 併願） | ≒ 2027年3月【次回未公表】 | 無料・オンライン | 資金ではなく「信頼の肩書」（E-07） |
| 5 | SIGMUS 研究発表会（第146回以降） | 年5回、締切【未確認】 | 研究報告 | KMD・藝大 AMC 等との接点（E-09, B-107〜108） |
| 6 | NICOGRAPH International 2027 | ≒ 2027年2月【次回未公表】 | EasyChair、IEEE Xplore 収録 | 国内発・国際索引（E-08） |
| 7 | SIGGRAPH Asia 2027 Art Papers | ≒ 2027年6月【次回未公表】 | 匿名化 | ロボット打楽器公演の採択前例（B-84） |
| 8 | IMWUT | 2026-11-01（第三者情報、要公式確認）／2027-02-01／05-01 | ジャーナル | ウェアラブル・センサ系の受け口（E-02） |
| 9 | LACMA Art + Technology Lab | 2026 サイクルは2年コホート（締切要確認） | 最大 $50,000 | 個人・世界可（E-23） |
| 10 | Epic MegaGrants Cycle 1 2027／Unity for Humanity 2027 | ≒ 2027年1月／2月（推定） | — | 推定日程、要確認（E-21, E-22） |
| 11 | 芸術文化振興基金 令和9年度 | 【次回未公表】（例年秋） | 個人応募可否未確認 | E-18 |
| 12 | VketReal・cluster・1st Stage・ReVers3:x・PANDORA×ソニー | 各社告知依存 | 技術仕様書+実演映像 | 「委嘱」より「出展・出演枠への応募」が実態（E-27） |

前年パターンから逆算すると、**2026年12月〜2027年2月に執筆を集中**させる必要がある（[japan_venues_funding KQ1 Inferences](https://nime.org/web_archive/2026/call/papers/index.html)）。信頼性は (a) 査読付き発表、(b) 顕彰、(c) 公開リポジトリ+定量ログ、(d) 東京拠点の継続ライブ実績の四点で構成され、AirSticks が「論文+アワード+演奏」の三点で実績を積んだ事例がモデルになる（[NIME 2020 Music](https://nime.org/proc_music/nime2020_music_ilsar/)）。確認した要項に無所属を妨げる規定は見当たらず、ORCID と GitHub が著者情報として必要十分である（[同 KQ6 Inferences](https://ieeevr.org/2027/contribute/demos/)）。

### 5.3 次回 KAGI NIGHT で計測する項目（引用可能なデータの自作）

査読者が期待する標準プロトコルは、**公演2回以上、半構造化の奏者インタビュー、観客質問紙（プレゼンス・主体感・知覚された創造性）、システムログ**であり、これにチケット・物販・配信収益を従属変数として加えれば新規となる（[ai_cocreativity KQ3 Inferences](https://www.duo.uio.no/handle/10852/110981)）。以下を仕様として固定する。

| 区分 | 計測項目 | 方法・指標 | 参照する基準 |
|---|---|---|---|
| システム | スティック→音の端対端遅延と**ジッタ**（平均・SD・分布） | McPherson et al. 2016 の往復計測法；10 ms／±3 ms を合否線に | B-01, B-02, B-04 |
| システム | スティック→映像（TD／StreamDiffusion）の遅延 | フレームカウント法（Road to VR と同手法）で photon-to-visual を記録 | B-26, B-64 |
| システム | Vision Pro ハンドトラッキング vs IMU スティックのオンセット時刻差 | 同一打撃を両経路で記録し差分分布を出す——**Vision Pro の査読ベンチマーク不在を埋める最初のデータ** | B-14（方法論）, B-29 |
| システム | OSC 30 Hz の欠落率・Mac↔Win 経路遅延、iPhone Spectator の同期誤差 | ログ集計 | B-10, C-43 |
| 観客 | 物理的プレゼンス／社会的プレゼンス／アーティスト・観客へのつながり | Onderdijk 2021 と同一尺度；会場・メタバース（仮想観客）で層別 | C-01 |
| 観客 | IPQ プレゼンス（仮想観客側） | Guang 2025 と同一尺度で比較可能に | C-24 |
| 観客 | 身体同調 | スマホ加速度または頭部運動で Swarbrick 2019 に倣う；可能なら心拍同期（Tschacher 2023） | C-03, C-06 |
| 観客 | 見た機械の過程への反応 | Burland & McLean 2016 型の質問 | B-74 |
| 経済 | 支払意思額（会場・配信・仮想） | Bär 2025 の帯（€35–39.99）と PUSH LIVE の £18.09 をアンカーに価格帯選択式で質問 | F-01, F-51 |
| 経済 | AI 関与の開示をランダム化した評価・WTP | Horton 2023／Shank 2023 の設計を公演に移植——**ライブ音楽では初** | B-97, B-98 |
| 経済 | 動員、チケット・物販・配信・メンバーシップ収益、再来場意向 | 再来場・継続率の査読データは存在しないため、自前で時系列化 | F-12, F-24 |
| 奏者 | 「道具か行為者か」の知覚、主体感 | Erdem 2022 の半構造化インタビュー | B-69 |

結果は匿名化した上で GitHub リポジトリに CSV で公開し、IEEE VR Demo 抄録と NIME 論文の両方に同じデータセットを引用する。

### 5.4 優先読書リスト（最初に読む20本）

| 順 | ID | 文献 | 読む理由 |
|---|---|---|---|
| 1 | B-02 | Jack et al. 2018 | 設計のすべての数値的根拠 |
| 2 | B-01 | Wessel & Wright 2002 | OSC と 10 ms 目標の原典 |
| 3 | B-14 | Abdlkarim et al. 2023 | Vision Pro を測るための方法論 |
| 4 | B-29 | Banquiero et al. 2025 | 同構成の最新論文、論文様式の手本 |
| 5 | A-01 | Godøy, Haga & Jensenius 2006 | エアドラムの学術的位置 |
| 6 | A-13 | Mäki-Patola 2005 | スティック採用の根拠 |
| 7 | A-22 | Ilsar et al. 2020 | AirSticks の設計哲学 |
| 8 | A-23 | Trolland et al. 2022 | AirSticks 2.0 の実装 |
| 9 | A-20 | Trolland et al. 2025 | 映像先行設計の最新例 |
| 10 | B-69 | Erdem et al. 2022 | 評価プロトコルの雛形 |
| 11 | B-53 | Sturm et al. 2019 | 「公演は研究成果」の枠組み |
| 12 | C-01 | Onderdijk et al. 2021 | 二種のプレゼンスと会場+メタバース設計 |
| 13 | C-03 | Swarbrick et al. 2019 | ライブ性の身体的証拠 |
| 14 | C-06 | Tschacher et al. 2023 | 生理同期の測り方 |
| 15 | C-23 | Yakura & Goto 2020 | 日本の VR ライブ研究の起点 |
| 16 | F-01 | Bär et al. 2025 | WTP の基準値 |
| 17 | B-97 | Horton et al. 2023 | 身体化が価値を生む仮説 |
| 18 | B-95 | Zhou & Lee 2024 | 「閲覧あたり価値」の測定法 |
| 19 | B-55 | Blanchard et al. 2025 | 奏者+AI バンドメンバーの最近接先例 |
| 20 | B-64 | StreamDiffusion 2023 | 自分のエンジンを正確に引く |

次の10本は B-42（Hunt & Wanderley 2002）、B-10（Rottondi 2016）、B-81（Weinberg 2020）、F-17（Baym 2018）、B-94（Doshi & Hauser 2024）、C-43（Boem 2024）、C-32（Young 2022）、A-24（Zellerbach & Roberts 2022）、A-28（iXeRemin 2026）、D-36（Wilson 2013）とする。

---

## 結論

本調査が明らかにしたのは、鍵山喬一の実践が文献の「空白」に正確に位置するということである。遅延知覚（10–20 ms）、ヘッドセット追跡（45–128 ms）、観客プレゼンス、支払意思額の各領域には査読済みの数値が揃っているのに、それらを一人の人間ドラマーのライブで同時に測った研究はなく、Vision Pro の精度ベンチマークも、Beat Wave／KAGI NIGHT の学術記録も存在しない。したがって鍵山にとって文献収集の目的は「権威を借りる」ことではなく、**自分の公演を既存研究の問いに対する実験場として定義し、欠けている数値を自分で供給する**ことにある。5.3 の計測仕様に従えば、次回 KAGI NIGHT は IEEE VR Demo（2026-12-07）と NIME 2027 の両方に投稿可能なデータセットを一度に生む。

同時に、注意すべき含意が二つある。第一に、本仕様書の DOI の相当数は調査環境の制約で未検証であり、verified／✔ 以外のフラグが付いた文献はサイト掲載前に一次確認を要する。第二に、クリエイターエコノミーの文献はパレート分布を一貫して示しており、サイトの遊び心やRESEARCH節だけでは問い合わせは生まれない。研究的信頼（査読・顕彰・公開ログ）と、アイデンティティ共鳴型の少数ファン基盤（メンバーシップ+物販+ライブ）を同じサイト上で並走させることが、「仕事が来る」ための文献上の最小構成である。
