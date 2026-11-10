# Adversarial review: 90年代スーファミCM実写比率仕様 (v1.0)

Scope: report `docs/reports/90年代スーファミCM実写比率仕様.md` (line numbers = that file), `measurement/*.tsv`, `results.json`, `tools/sfc_cm_aggregate.py`, `tools/sfc_cm_sampler.py`, `tools/build_cm_spec_html.py` and the built `.html`.
Method: independent re-aggregation from the raw TSVs (own code; only `norm_title` was imported, to reproduce the unit keys). `results.json` agrees with that recomputation everywhere (all / by_length / by_year / by_publisher / by_stratum, kappa, bootstrap CIs, sensitivity). Nothing was edited.

Headline numbers reproduce: 834 → 421 → 369 → 221 units; L+P 40.02 %, G 11.09 %, A 29.40 %, E 18.71 %; kappa 0.8347 over 1,087 frames. The findings below concern derived numbers, labels and interpretation.

## BLOCKER

**B1. "3地点の並び" counts are an artefact of `max()` tie-breaking (aggregate.py L237 and L275; report §2.3 L95-97, §5 L377-396, §7.1 L486-492, BLUF L9).**
`max(share, key=share.get)` returns the first code in `CODES = L,P,G,A,E,X` on a tie. 51 of 221 units (54 % of the 94 multi-upload units) have a tie at one or more positions, so L always beats E/A and G beats A/E.
- Evidence: reversing the tie order gives L-L-L 27 (report: 40), A-A-E 26 (18), L-L-E 24 (22), A-A-A 22 (20), P-P-P 7 (9).
- §2.3 "実写で通す62単位のうち22（35%）" becomes 51 / 24 (47 %); "絵で通す38単位のうち18（47%）" becomes 48 / 26 (54 %). At upload level (no ties possible) it is 45/99 = 45 % and 32/61 = 52 %. The report's 35 % understates how often the 75 % point is a card.
- §7.1 type counts move: type 6 ゲーム画面主体型 11 → 6, type 4 24 → 29, type 5 17 → 15, type 2 42 → 44.
- §5 examples: スーパードンキーコング "G-G-G" is one G-G-G upload plus one A-G-E upload; スーパーメトロイド "L-L-L" is L-L-L plus L-P-E; ドラゴンクエストIII 30秒 "L-L-L" is L-L-E plus L-E-L.
- A unit "sequence" also mixes different edits (マリオペイント "L-G-P" is L-G-P plus G-A-A), so it is not the sequence of any real CM.
- Fix: report sequences at upload level (L-L-L 54, L-L-E 45, A-A-E 32, A-A-A 29, A-G-E 16 of 369), or mark ties explicitly, and derive types from shares rather than tie-broken codes.

**B2. §2.7 describes the two strata the wrong way round, and the "対照層" is contaminated (sampler.py dedup loop; aggregate.py L211; report L150-157).**
`queries.tsv` runs the 71 title queries first, then the 28 generic ones, and the sampler skips any id already in `corpus`. So `stratum=generic` means "found only by a generic query", and `stratum=title` means "found by a title query (may also be findable generically)". The report says the opposite: "年と機種だけの検索で見つかった単位（対照層）と、タイトル指名検索でしか見つからなかった単位（指名層）".
- `stratum_generic = any(...)` then puts 25 named-title units (FFIV, FFVI ×2, MOTHER2, ゼルダ, スターフォックス, マリオRPG …) into the 119-unit "対照層" because a single upload was generic-only.
- Clean split: units whose uploads are all generic-only (94) = live 35.8 %, art 34.7 %, game 10.6 %; units with any title-query upload (127) = live 43.1 %, art 25.5 %, game 11.4 %. The gap is about 7 points live and 9 points art, not the "4ポイント" of L157.
- Fix: rewrite the definition, recompute with the three-way split, and soften "結論を変えない".

## MAJOR

**M1. The CI of the population mean is used as a pass/fail tolerance for a single CM, and point shares are used as seconds (§7.7 #14 L650, #5 L641; M4 L529; §7.2.2 L533-543; §7.2.3).**
"実写系が主成分である時間が、15秒で30〜45%、30秒で35〜55%" comes from the bootstrap CI of the mean across units. The per-unit distribution is bimodal (`live_share3_distribution`: 0 → 86, ≤1/3 → 36, ≤2/3 → 51, >2/3 → 48), so a CM with 30–45 % live action is an uncommon case, not the typical one. The same lines convert "share of three sampled instants" into "時間" and seconds (14.0 s / 46.7 % etc.), although L50 says the shares are not time shares.
- Fix: label #5 and #14 as 【設計】 only, drop the CI as their source, and state that the 3-point share is not a duration.

**M2. The "live" flag is Y for every P frame, so "実写" claims include puppets, models and possible CG (report L42, L79, L87, type 1 L486, BLUF L9).**
All 86 P/P? frames in pass 2 have live=Y. "いずれかの地点に実写がある 144/221 (65%)" is therefore "live action or model". Units with any L-coded frame: 113 (51 %). 17 of the 144 get the flag only from P/P? frames, and 24 have no firm L or P frame at all (only `?`-marked or A/E/G-coded frames with the flag).
- 49 of the 86 P frames are `P?`, where the coder notes say "could be CG". Headline L+P 40.0 % becomes 35.6 % if `P?` is not counted and 32.1 % for L alone. That is a larger swing than the pass-1/pass-2 sensitivity the report publishes (36 % vs 40 %), and it is not disclosed.
- "全編実写型（85単位）" is a misnomer: 18 of the 85 have live share ≤ 1/3 and 3 have 0 (スーパーファミコン本体 E-A-A, 風来のシレン 15秒 A-A-E, リターン・オブ・双截龍 E-A-E). It includes エストポリス伝記 (P-E-A), which §4.4 says has no live action. Only 64 have live share ≥ 2/3.
- "実写＋ゲーム画面型（42）…実写を主にして": 25 of the 42 have live share ≤ 1/3 (mean 39 %), and only 14 have G as the main code at the 50 % point alone.
- Fix: rename the flag column "実写または造形物", rename types 1 and 2 by rule ("ゲーム画面なし・実写/造形物あり"), and add the L-only and `P?`-excluded sensitivities.

**M3. "ゲーム画面は中盤の1地点に集中" and constraint M1 are stronger than the data (BLUF L9, L526, check #6 L642).**
Of the 83 units with a game flag, 41 (49 %) have it only at the 50 % point; 42 have it at 25 % or 75 % or at several points. At upload level, 61 of 114 (54 %) are mid-only, 31 have two or more points and 22 are first-only or last-only. "1か所" cannot be inferred from three instants anyway.
- BLUF "ゲーム画面はどの作品でも1投稿あたり0〜1地点にしか現れない" is contradicted by the report's own §4.2 table: テイルズ #41 has a game window at 50 % and a full game screen at 75 % (pass-2 flags N,Y,Y).
- Fix: "ゲーム画面がある単位の約半数は50%地点のみ"; delete "0〜1地点".

**M4. "ゲーム画面が2地点以上を占める単位は11（5%）" (L190) is not reproducible as worded.**
By the report's own sequence definition, 16 units (7 %) have G at two or more positions. 11 is only type 6, which excludes 聖剣伝説3 30秒 (G-L-G), 超魔界村 15秒 (L-G-G), 桃太郎電鉄HAPPY 30秒 (G-G-G), スーパードンキーコング3 (G-G-E) and 摩訶摩訶 (A-G-G), because they carry a live flag. By share (game ≥ 2/3) it is 10; with the opposite tie-break it is 10.
- Fix: state the definition, or use 16 / 221.

**M5. "共通するのは…終盤4分の1までにタイトルと発売告知を出す" and constraint M2 rest on the any-text flag (BLUF L9, L527, check #8 L644).**
"テロップあり 72 %" at the 75 % point counts any text (credits, copy, logos, disclaimers). Units with a date/status/price tag at the 75 % point: 88/221 (40 %); with title added: 115 (52 %); upload level 117/369 and 151/369. These are lower bounds, and pass2_part3 tagged `title:` only 9 times against about 50 in the other parts, and `credit:` never.
- Fix: say "約75%地点で何らかの文字が72%、発売告知が読めたのは40%（下限）"; drop "共通する".

**M6. The unit-level "どの地点にもゲーム画面が無い 62 %" depends on how many uploads a unit has (§2.2 L83-91, BLUF).**
The pattern is "any upload, any point". No-game share is 71 % for the 127 single-upload units and 51 % for the 94 multi-upload units; at upload level it is 255/369 = 69 %. Famous titles have more uploads and hence more sampled instants, so the unit figure mixes prevalence with sampling intensity. The same applies to the §7.1 type counts.
- Fix: give the upload-level 69 % alongside, and note the dependence.

**M7. The second pass is narrower than "独立に2回" implies (L42-46, §6.3 L466).**
- Pass 2 coded only the 369 rows pass 1 had already included. Inclusion (421/834), platform, title, publisher and year, which define the units and all breakdowns, were coded once by one machine pass. Kappa covers frame codes only.
- Agreement is concentrated in easy frames: for frames pass 1 marked `?` (163), agreement is 56 % and kappa 0.42; for firm frames (924) it is 93 % / 0.91. Only 62.5 % of pass-2 P frames were P in pass 1.
- 54 eligible rows are `dup_of` copies of the same video, which inflates agreement; kappa is not unit-weighted.
- L46 "動くのは実写系とカードの境目" does not match the disagreement table: the largest flows are E→A 32 and A→P/L 37 (plus P→A 14); E→L is 13. The unstable boundaries are card/art and art/live-or-model.
- Both passes are machine codings with no human ground truth, and `override_rows` is 0. The report says so, but still calls the agreement a check on validity (L711 is the honest version).
- Fix: add the inclusion caveat, the `?`-stratified kappa, and correct the boundary sentence.

**M8. Uploads that pass 1 itself flagged as joins with non-SFC CMs are counted as 30-second SFC CMs (aggregate.py L124 checks only the literal strings `multi_spot` / `crt_reshoot`).**
- #242 and #250 "超魔界村 (+ロックマン4)": notes say f1-f2 belong to the FC ロックマン4 half. `norm_title` strips the parenthesis, so they form the unit "超魔界村 30秒" (A-L-E, live_only, year 1991) and are listed under type 1.
- #288 "スーパーワギャンランド (+ファミスタ'94)": "no frame clearly shows SFC content"; counted as a 30-second live_only unit.
- #438 サムライスピリッツ/餓狼伝説スペシャル: "upload contains two CMs", the 50 % frame is a GAME BOY end card.
- #141 アクトレイザー 33 s "probably two spots joined"; #69 ロマサガ3 "title says two 15s versions"; #640 and #679 are re-recordings of a screen with player UI (pass-2 notes) but lack the keyword. #711 is excluded only because its note contains "crt_reshoot look".
- No "PS half" join was found among eligible rows; PS rows are excluded as other_platform.
- Effect of excluding #242, #250, #288, #438: 218 units, live 39.88 %, game 11.25 %, art 29.57 %, card 18.50 %, no-game 135/218 = 61.9 %. Also excluding #141, #69, #640, #679: 215 units, live 39.68 %, game 11.40 %, no-game 61.4 %, 30-second live 45.98 % (was 46.44 %). Headline moves < 1 point; the 1991 row (16 units) and the type-1 list do change.
- Fix: exclude by a structured column rather than a notes substring, and rerun.

**M9. The 6.1 verdict "1990〜91年の主流はゲーム画面中心 → 不一致" rests on two titles for 1990 (L116, L124, L412).**
The four 1990 units are アクトレイザー 15秒/30秒 and グラディウスIII 15秒/30秒. The 1991 row has 16 units (15 titles), one of them the 超魔界村+ロックマン4 join. Year is the uploader's title claim (6 of 234 year rows do not have the year literally in the upload title; 7 units have conflicting years resolved by mode / first seen, aggregate.py L199-209). Three sampled instants cannot establish what was "主流".
- Fix: downgrade to "未確認（標本が小さい）".

## MINOR

**m1. Title and both-length counts (L40, BLUF, L209).** "192タイトル" and "両方ある題名は29" count raw `title` strings, including the blank title of #714 and "超魔界村 (+ロックマン4)" as separate from 超魔界村. By the aggregation's own normalised key there are 191 titles (190 named + 1 untitled) and 30 with both lengths. Three units are hardware (SFC本体, サテラビュー, スーパーゲームボーイ), so "192タイトルは発売タイトルの約14%" is slightly high.

**m2. Title normalisation (aggregate.py L61-72).** Actual effects in this data:
- Splits: スーパードンキーコング2 / スーパードンキーコング2 ディクシー&ディディー (2 units, 3 uploads, same game); スーパーファミコン本体 / 本体/スーパーマリオワールド / スーパーマリオワールド / スーパーマリオワールド / 本体 (4 units, 5 uploads, same launch campaign per the notes). Merging them: 217 units, live 39.79 %, game 11.14 %. With M8 exclusions as well: 211 units, live 39.43 %, game 11.46 %, no-game 61.1 %. All < 1 point.
- FFIV: all 7 fifteen-second uploads are in one unit; no split.
- §5 L387 says "スーパーマリオワールド／SFC本体（30秒、3単位計4投稿）"; the data has 4 units and 5 uploads (#661 E-A-A omitted).
- Latent bugs, not triggered here: `ドラゴンクエストI・II` normalises to `ドラゴンクエスト3` (the "・" is removed, then `iii$` → 3). Roman numerals are converted only at end of string, so "ドラゴンクエストV" → `…5` but "ドラゴンクエストV 天空の花嫁" → `…v天空の花嫁`, and "ストリートファイターIIターボ" ≠ "ストリートファイター2ターボ". `\(.*?\)` removal merges any parenthetical variant.

**m3. Double rounding in results.md (aggregate.py L292 formats values already rounded to 4 places).** §2.1 L69 "約25% ゲーム画面 G 6%": exact value is 6.5008 %, so 7 %. L75 "前後では6〜7%" should be 7 %. タイトー 絵 "62%" is exactly 62.5 % (half-even).

**m4. §7.4 L596 「好評発売中」（25）** is an upload count in a column headed as units; units = 21 (22 with the partly read "(好)評発売中").

**m5. False precision about what was observed (L50, L507-519, L695).** "冒頭と末尾の各およそ8分の1は観測しておらず" implies the middle three quarters were observed; only three instants were. "3.75秒（112フレーム付近）" gives frame numbers for a thumbnail position the report itself calls undocumented.

**m6. Bootstrap CIs (aggregate.py L97-102)** are computed correctly (percentile, 2,000 reps, seed 1; reproduced exactly) but treat units as independent although 30 titles contribute both a 15s and a 30s unit, and they exclude classification uncertainty (pass 1 vs pass 2 differ by 4 points, about one CI half-width).

**m7. Flag parsing (aggregate.py L139).** `Y?` counts as Y and `N?` as N (14 and 13 flags; 5 `Y?` on game). Treating `Y?` as N moves no-game from 138 to 141. Negligible, undocumented.

**m8. Pass-1 code C.** 20 eligible frames; dropped from kappa and mapped to L only in the sensitivity run. Pass 2 coded them L 9, P/P? 6, G 4, A? 1, so the mapping is tolerable and does not affect adopted values (all 369 use pass 2).

**m9. §7.2.4 vs check #6.** The FFVI-style design puts the game screen at 8.5–10.0 s (57–67 %), which does not contain the 50 % point that M1 and check #6 require for type 2; check #4 expects L-L-L for it. State that check #6 does not apply to 7.2.4.

**m10. "発売元の差は年や尺の差より大きい" (L146).** Year means range 22–66 % (22–49 % without 1990), publishers 17–62 %; with 6–26 units per cell this ranking is not supported.

**m11. HTML search script (build_cm_spec_html.py JS).**
- Section matching uses `section.textContent`, highlighting works per text node. A term that spans an inline boundary shows the section with no highlight: query "平均で実写系" (crosses `<strong>` in the BLUF) returns "1 節 / 0 件".
- While a filter is active, TOC links to hidden sections do nothing (query "渋谷": 31 of 51 TOC targets are inside `section.hide`).
- No width normalisation: "ＦＦ" finds nothing, "FF" does.
- Otherwise clean: 36 markdown tables = 36 `<table>`, 322 rows = 322 `<tr>`, 56 headings, 151 external links, 61 code spans, 29 bold spans all rendered; no raw `**`, `|---`, backticks or `](` in visible text; 51 TOC anchors all resolve, no duplicate ids; the shipped .html is byte-identical to a fresh rebuild; no horizontal overflow at 390 px; no console errors; regex metacharacters, empty and full-width-space queries and Escape behave correctly.

## Task 1 tally

About 560 【実測】/再集計 values were compared against the independent recomputation (funnel and exclusion breakdown, durations, kappa and disagreement counts, sensitivity, all cells of the §2.1, §2.4, §2.5, §2.6, §2.7, §2.8, §7.1, §7.2.1 tables, CIs, pattern counts, sequence counts, type catalogue, telop counts by position, §4 and §5 unit figures, §7.4 and §7.7 references). The count is approximate (tables compared cell by cell, not machine-enumerated).

- Mismatches: 7.
  1. Titles 192 → 191 (m1).
  2. Both lengths 29 → 30 (m1).
  3. §2.1 25 % point G 6 % → 7 % (m3).
  4. "2地点以上がゲーム画面 11（5%）" → 16 (7 %) (M4).
  5. 「好評発売中」25 is uploads; 21 units (m4).
  6. §5 "3単位計4投稿" → 4 units, 5 uploads (m2).
  7. BLUF "1投稿あたり0〜1地点" contradicted by #41 (M3).
- Reproduce but are artefacts of the tie-break: every "並び" figure in §2.3, §2.4, §5 and §7.1, and the type-4/5/6 counts (about 70 values, B1).
- Wrong definition rather than wrong number: the §2.7 stratum labels (B2).
- Not reproducible from the measurement files at all: none.
- Not checked: the 【抜粋】 averages 61.9 % / 53.8 % were only confirmed to appear in the dataset notes; 【直接観察】 descriptions were not re-observed (no images viewed).
