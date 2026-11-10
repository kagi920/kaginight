# Adversarial review: docs/reports/90年代スーファミCM実写比率仕様.md (v1.0)

Scope: report checked against verification_of_muse_spec.md ("ledger"), focus_direct_observation.md ("focus note"), measurement/results.md, results.json, pass2_part*.tsv, the two input drafts, and (for snippet labels) the other notes. No web research. Nothing was edited.

What checked out (so it is not re-checked): all 倉恒良彰 quotations in §3.1, §5, §7.4, §7.5 match the ledger character for character (elisions "…" are the ledger's own); JBA wording and "2023年版のみ" caveat; SFC hardware/software shipments; software-sales discrepancy; セレナ; せがた三四郎 20項目; 金巻康朗 = 1990 FE「演出」only; ストII デスバレー/ダウンタウン; all §2 tables against results.md; §2.8 position counts; funnel arithmetic; type counts in §7.1 (85/42/41/24/17/11/1); the three timelines sum to 15.0 s / 30.0 s and 450 / 900 frames.

---

## BLOCKER

**B1. §7.2.2 / §7.2.3 "average" timelines produce 3-point signatures that do not exist in the sample, and do not meet M4 when measured the report's own way.**
- §7.7 item 4 requires L・G・L (30 s) and L・G・A (15 s). results.json: L-G-L = 1 unit of 221 (DQV 15 s; 0 among 30 s units); L-G-A = 0 units. The modal real sequences are L-L-L 40, L-L-E 22, A-A-A 20, A-A-E 18.
- Per-point modes are also missed: 15 s at 25% is A 46% > L 37%; at 75% is E 46% (design: A). 30 s at 75% is E 41% > L 32% (design: L).
- The "配分はM4に合わせた" claim compares seconds with sample-point shares. §1.2 limit 1 itself says 「割合は標本点に占める割合であって秒数の割合ではない」. Coded by the 3-point method, the 30 s design scores 実写系 67 / G 33 / A 0 / E 0 (target 46/11/21/21) and the 15 s design 33/33/33/0 (target 36/11/35/18).
- Fix: state the seconds=share assumption explicitly, give the counts above, and make the primary deliverable a timeline for the modal form (L-L-L / L-L-E); keep the blended form as a labelled secondary option, with the card starting before the 75% point if M2/M4 are to hold under the 3-point test.

**B2. No timeline exists for the most common type.** §7.1 says 「平均的な1本を作るなら型1か型2」 (型1 = 38%), but §7.2 gives no 15 s or 30 s timeline for 型1 (nor 型3–6). §7.2.4 is 15 s only and RPG-specific. An editor asked for a 30 s 全編実写 spot has only a one-line recipe. Fix: add 15 s and 30 s timelines for 型1 (and at least 型3).

**B3. §7.2.4 contradicts the checklist and its own evidence.**
- C3 (game screen 8.5–10.0 s) does not contain the 50% point (7.5 s). With C3 the spot is 型2, so it fails §7.7 item 6 (「ゲーム画面の区間が50%地点を含み」) and M1; item 4 simultaneously demands L・L・L (no game at any point). Items 4 and 6 cannot both pass.
- Order: the only order evidence is FFVI #756 (focus note: 25% 渋谷の引き「#30 約50%と同じ画」, 50% 女性＋タイトル, 75% ゲーム画面), i.e. the game screen comes after the title overlay, near 12 s. A snippet in focus_rpg_cluster.md (line 34) gives the same order (渋谷 → 本編イベントシーン). §7.2.4 puts the game screen before the title. §4.1 dropped the note's 「#30 約50%と同じ画」 remark and summarises CM 1 as ending at the title.
- "【実測】FFVI 15秒…実写系73%と同じ水準" compares 11.0 s of 15 s with a 3-point share; by the 3-point method the design is 100/0/0.
- Fix: either move C3 to span 7.5 s or after C4 (and label which evidence each follows), and rewrite items 4/6 for this type.

**B4. Nothing in §7 supports the intended 9:16 SNS use, and three checklist items forbid it.** Both input drafts flag this (Muse 6: 「15〜30秒の縦動画やSNS動画」; GPT 10.1: 「16:9・9:16へ切り出す場合は別コンポジションを組む」); the report dropped it. Conflicts: item 2 (「4:3。黒帯を後付けしていない」) fails any 4:3 window on a 1080×1920 canvas; §7.3/item 7 require 四辺の黒枠 on the game screen, which contradicts "game screen full-height"; §7.3 specifies 29.97i, which SNS cannot deliver. Missing and needed:
  1. Canvas 1080×1920, window size and y-position (4:3 at full width = 1080×810), and what fills the other ~1110 px.
  2. What "full-height" means: 256×224 scaled to 1920 high is 2194 px (8:7) or 2560 px (4:3) wide, so over half the width is cropped; or full height of the 810 px window (non-integer 3.6× scale). Pixel aspect (8:7 vs 4:3) and integer scaling rule.
  3. Whether the game screen leaves the 4:3 window (then the 3-point code and item 7 need redefinition).
  4. Platform UI safe zones (top/bottom/right rail) and whether telops sit inside the window or in the outer area; 80% title-safe of 1080×810 is 864×648, so "小" text is unreadable on a phone — minimum px heights needed.
  5. Delivery frame rate (30p/60p), progressive, codec; how 450/900 "nominal" frames map.
  6. Audio: loudness target for SNS, muted autoplay (the 「音の柱」 is lost — captions?), and whether the 0.5 s head silence (a broadcast delivery rule, 2023 text) should apply at all.
  7. How the acceptance test (3-point coding, 主成分) is applied to a composite canvas.
  8. Where the "not a period broadcast" disclosure (§7.6) goes; it is not in §7.7.

---

## MAJOR

**M1. §0 BLUF: 「ゲーム画面はどの作品でも1投稿あたり0〜1地点にしか現れない」 is false.** Focus note, テイルズ #41: 50% 「下部に小さなゲーム画面のウィンドウ」 and 75% ゲーム画面 = 2 points in one upload; the report's own §4.6 counts テイルズ 3点 over two uploads. Fix: "0〜2地点".

**M2. §6.1 row 「実写は看板タイトルで主役だった」: 「ゼルダ、MOTHER2、ストIIは3地点とも実写系」 contradicts §5 and results.json.** ゼルダ = E-L-L (25% is an SFC-logo card), MOTHER2 = L-L-E, ストII 15 s = L-L-E. Only ストII 30 s is L-L-L. Fix: "3地点にゲーム画面が無い".

**M3. §2.10 item 2: 「ゲーム画面が2地点以上を占める単位は11（5%）」 is wrong.** results.json: 16 units have G as modal code at ≥2 points (11 in game(+art), 5 in live+game, e.g. 聖剣伝説3 30 s G-L-G); by game_share3 ≥ 2/3 it is 10, > 1/3 it is 13. 11 is only the 型6 count. Fix: 16 (7%), or state the definition.

**M4. 型1 「全編実写型」 / 「実写のみ」 is misnamed, and the BLUF repeats it.** The pattern is flag-based (live flag somewhere, no game flag). Of the 85 units only 37 have 実写系 share > 2/3; 18 have ≤ 1/3; 3 have no live-coded point at all (スーパーファミコン本体 E-A-A, リターン・オブ・双截龍 E-A-E, 風来のシレン 15 s A-A-E). 初代エストポリス — which §4.4 says has 「人物の実写が無い」 — is in this type (pattern live_only, P-E-A, 17%). "全編" also cannot be known from 3 points. Likewise 型2's 「実写を主にして」: mean 実写系 39%, game 25%; テイルズ (33%) is listed as a representative. Fix: rename ("ゲーム画面なし・実写あり型"), give the share distribution, pick representatives with share > 2/3.

**M5. M1 constraint (「使うなら中盤の1か所」) and §0 「共通するのは…」 overstate.** pass2 flags, unit level: of 80 units with a game flag, 40 (50%) have it at 50% only; 28 (35%) at two or more points; 15 (19%) not at 50% at all. Positional shares cannot show "1か所" or length. §7.7 item 6 turns this into a pass/fail rule. Fix: report the distribution and state M1 as "most common", not a rule.

**M6. M2 mixes any telop with title/release notice, and is worded three ways.** Evidence cited is card 46/41% and テロップあり 77/65% (any text, including logos, credits, trademark line). Readable release date at 75% is 62/221, status 26/221 (lower bounds). §0 says 「終盤4分の1までに」, M2 「約75%地点までに」, §7.1 型1 「最後の4分の1で」, item 8 「75%地点のフレームに」 — these are different instructions. Fix: one wording; cite date/status/title counts.

**M7. §1.2 limit 1 and §7.2.1 imply coverage that does not exist.** 「冒頭と末尾の各およそ8分の1は観測しておらず」 and table rows 「冒頭 0〜約1.9秒 未観測」「末尾 約13.1〜15秒 未観測」 read as if 1.9–13.1 s were observed. Only three instants were. The 1/8 figure is an unstated assumption. The designs then assign whole segments (e.g. S1 0–5.5 s) from one instant. Fix: say "3 instants; everything between is unobserved".

**M8. 【直接観察】 claims beyond the focus note.**
- §4.3 / §4.6 / §7.2.4: 「好評発売中」「9,800円（税別）」 are from #52/#57, which the note says were 「縮小シートで確認」 — not 原寸 as §1.1 defines the label. §7.2.4 also cites #48 for the post-release version; the note did not read #48's text (「下に白文字」).
- §4.6, §7.2.4 C1, §7.4, item 13: 「左上に常時（KONAMI）」. The note's table shows KONAMI top-left in only 3 of 12 MADARA2 cells (#48 25%, #54 25%, #46 50%); "常時" cannot come from 3 points. (The note's §5.3 says it too; the table does not support it.)
- §4.6 / §7.2.4 「末尾は社名ロゴのカード」 for FFVI: the SQUARESOFT card is seen only at ~75% (≈22 s) of #20, a 30 s upload the report itself suspects is two 15 s spots; no 15 s FFVI upload shows it, and the tail is unobserved by §1.2.
- §7.2.4 C1 「商標注記（小）」 cites FFVI #30, where the note says only 「小さな白文字」 (unread). §4.6 「クレジット文字：FFVI なし」 should be "none read".
- Fix: downgrade each to "推定" or cite the actual cell.

**M9. Who made the 【直接観察】 is not stated.** §1.1: 「主担当の解析者が…目視」; focus note: 「観察者：本セッションの主担当（分類担当とは別）」; §1.2: 「人間の第二分類者は使っていない」. A production reader will assume a human looked. If the observer was the AI session lead, say so; the label currently outranks 【実測】 and 【抜粋】 on that implied basis.

**M10. 【実測】 is used for unvalidated free-text notes, with a wrong source.** §5 (「並びと内容」 column), §7.3 (ゲーム画面の他の置き方 ②〜④, 実写の質感, FFIV) cite 「分類時の備考」 as 【実測】 and attribute it to results.json. results.json units have no notes field (keys: title, length, uploads, nos, year, publisher, stratum_generic, pattern, text, shares, codes); the notes are in pass2_part*.tsv. §1.1 defines 【実測】 as 集計値; κ covers codes only. Fix: separate label ("分類者メモ") and correct the path.

**M11. §7.5 / item 15 「音の柱を画より先に決める」 is taken from Muse 6.1 without attribution.** Muse 6.1: 「音の柱を先に決める…映像より先に「口ずさめる要素」を設計する」. The report presents it as its own 【設計】 from text sources; audio was never observed. Item 15 is also untestable as written: 「S1〜S4を通して途切れずに続く」 conflicts with the 0.5 s head silence inside S1, with S4 「または人物の声」, and §7.2.4 uses C1–C5 with 環境音 first.

**M12. §7.4 【一次】 for 「発売前後で文言だけを替える運用」 overreaches.** Ledger quote: 「発売前のＣＭは「ファミコンウォーズが“出るぞ”」なんですが発売日以降は「…“出たぞ”」になっています。」 — a sung lyric in a 1988 Famicom CM; nothing says the picture was unchanged or that on-screen text was swapped. Item 11 (「画を替えず、文字だけを替えられる」) rests on it. The ledger also marks ゼルダ「出た出た」版 as 未確認.

**M13. §3 argument overreach.**
- §3.1 row 「実写にした理由」 is, in the ledger, the continuation of the ファミコンウォーズ (1988, Famicom) passage (「平面的なキャラがマップ上を動きます」); the table does not say so. Only two of 倉恒's four works are SFC. §0 cites him without the scope limit that §3.1 gives.
- 「画面の解像度の不足でも費用の安さでもなく」 is an argument from silence. The cost quote is about the 1990 FE CM (a faithful world depiction was too costly, so opera — still live action); it says nothing on live action vs game footage.
- §3.2: 「出せなかったのではなく、出さない企画を選んだ、というのが【一次】の示す線」 — playing a pre-release ROM before planning does not show capture was available or schedule-free; 倉恒 does not say this.

**M14. §2.10 reconciliation item 3 overreaches.** 1992 = 24 units, CI [0.097, 0.361], years taken from upload titles only (§1.2 limit 4), survivorship unaddressed; ストII itself is in the 1992 cell. 「整合する」 should be "not contradicted". The closing comparison (snippet-estimated 61.9% / 53.8% vs measured 40%) compares guessed time ratios with point shares; dataset_nintendo_first_party.md line 128 itself warns the figure is 「危険」.

**M15. Game-screen 黒枠 is specified from n=2 with an acknowledged confound and no size.** §7.3 / item 7 rest on FFVI #756 and テイルズ #33. §7.3 row 1 and §1.2 limit 5 say uploads carry black borders; thumbnails add their own. Border width is listed as unmeasured in §8.2 step 4. Fix: mark as 【設計】 with a stated width, or drop the checklist item.

**M16. Telop spec is not executable.** §7.4 / §7.2 give only 「小」「大きな白文字」「右下」: no height (% of frame), margins, weight, edge/shadow, colour, on-screen duration, or timing inside a segment. S5 packs two cards into 6.5 s (30 s) and 2.73 s (15 s) with no split; 15 s S2 is 1.23 s yet carries a credit telop. Shot counts/lengths, transitions and narration (yes/no) are unspecified for §7.2.2–7.2.3.

**M17. Frame/time base is ambiguous.** §7.3 sets 29.97 fps; item 1 demands 「15.00秒（公称450フレーム）」「30.00秒（公称900フレーム）」. At 29.97, 450 frames = 15.015 s and 900 = 30.03 s. Drop-frame or 30.00 timebase is not stated.

**M18. §7.2.2 S2 breaks its own budget.** S2 allows 「実写に造形物・絵を合成した画」; §8.1 codes composites as L. Choosing it gives 実写系 66.7%, 絵 0%, failing item 14 (35–55%). S2's 由来 says 「絵20%＝M4」; M4 says 21%.

---

## MINOR

1. §6.1 餓狼伝説スペシャル: 「SFCのCMではない」 and, in the same cell, 「SFC版（タカラ、15秒、2投稿）」. Ledger: the title is NEOGEO/arcade, an SFC port exists, and no document records its CM. Say "Muse describes the NEOGEO CM (out of scope)".
2. §6.1 uses 「確認」 for rows backed only by 【抜粋】 or by absence (row 1 秒数配分の資料, last row 立命館), against its own definition (開いたページ・実測・直接観察). Also non-defined verdicts: 「不一致（解消）」「Muse版が確認」「不一致（二次との差）」.
3. §6.1 「1990〜91年の主流はゲーム画面中心」→ 不一致 on n=4 and n=16 units; §2.5 body says only 「この標本では支持されない」. Use the weaker verdict.
4. §6.1 GPT 「MADARA2：紙媒体・イラスト移植型」→ 不一致. Ledger notes GPT framed this as a design type and wrote 「史実としてのカット割りは要原版確認」. Verdict should say so.
5. §6.1 / §4.3 MADARA2 曲名: ledger verdict is 一部確認 (three spellings in the article; "CMソング" is snippet-only; the article lists it as a live song). Report says 「Muse版が確認」 and gives one spelling.
6. §6.1 テイルズ 「実写の要素は確認できない」→ 不一致; focus note says 「一部不一致」.
7. §2.11 / §6.1 広告費: ledger says limit to 「1990年代の中での頂点」; report writes 「1990年代前半」. Neither note has 1992–98 totals; both limits are unverified.
8. §7.4 「好評発売中（25）」: results.json gives 21 units (22 with a partial read) out of 28 status units; 25 does not fit 28 minus the other six.
9. §4.1 / §4.6 FFVI 15 s 「73／20／0／0%」 sums to 93%; the missing 7% is X (#29 25% 黒). The unit also bundles two different CMs (CM 1, CM 2) and includes #769, not in the focus note.
10. §4.1: #20 / #766 are suspected concatenations but stay in the 30 s statistics (concatenations are an exclusion criterion in §1.2).
11. §4.3 / §4.6 「27秒版」: 27 s is an upload length, possibly a truncated 30 s; not shown to be a version.
12. §4.3: 「一次の出典も示されていない」 about a page that was not opened.
13. §3.2 知恵袋: 「グラフィックが稚拙だから」 is in quotation marks; community_analysis.md line 20 says 「原文の文言は未確認」. academic_literature.md line 61 rates this answer 「根拠資料として使えない」; not carried over.
14. §5 スーパードンキーコング: absence of a CM mention in Wikipedia is called 「食い違う」 with a snippet; it is not a contradiction, and the measured G-G-G fits the snippet.
15. §7.3 縦横比・フレームレート rows are factual claims labelled 【設計】, taken from GPT 211–214 (only the 1440×1080 row credits GPT). The label set has no "unverified general knowledge" class.
16. §7.3 点滅: date 1998-04-08 is from tcv21 / saiki.tv skill.pdf in the note; the report links gideline.pdf and calls it 「本文PDF」 under 【抜粋】.
17. §7.2.2 S1 由来 「約25%地点が実写＝M4」: M4 is the average allocation, not a positional constraint. §7.2.3 has no composition summary line.
18. §7.7: item 3 (no silence threshold), item 16 (no luminance/area definition), items 12–13 (「小さな」 unsized) cannot be tested; item 6 refers to 型2・型4 but no timeline is labelled with its type; §7.6 「当時の放送物であるかのように見せて公開しない」 has no checklist item.
19. §2.2 「いずれかの地点に実写がある」 includes 人形・模型 (P); say 実写系.
20. §2.11 「訂正は三つ」: the third is not a correction.
21. §6.3 「独立した2回の分類」: pass 2 saw only uploads pass 1 admitted; κ measures self-consistency, not validity.
22. Ledger items judged for Muse but absent from §6.1: 「出た出た」版, ガノンのパペット, 天野喜孝デザイン, ゼルダ116万本, 湯川専務8本, サテラビュー30秒・宇宙服マリオ, DQ 6分類.
