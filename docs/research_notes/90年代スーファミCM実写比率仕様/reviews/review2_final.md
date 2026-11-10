# Round-2 adversarial re-review (2026-11-10)

Scope: (1) spec v1.1 `docs/reports/90年代スーファミCM実写比率仕様.md` + `.html`, `tools/sfc_cm_aggregate.py`, measurement data; (2) `ストロベリーパンケーキCM設計書_v2.md`. Nothing was edited. "L" = line number in the spec .md; "D" = line number in the design doc.
Method: independent recomputation from the raw TSVs (own code; only `norm_title` imported), scripted row check of the design tables against the cut list, ffmpeg runs on lavfi sources, Playwright run on the HTML. Scripts are in `/tmp/claude-0/-workspace-kaginight/8671131d-d68d-5324-a094-d5642c3e14f4/scratchpad/r2/`. No `__pycache__` was left under `/workspace/kaginight/tools`.

## BLOCKER

None. `results.json` reproduces from the raw TSVs, all spec timelines sum and hit their stated 3-point signatures, and all 42 design rows pass against the cut list.

## MAJOR

1. **Spec: title-card minimum duration contradicts three timelines and checklist item 8.**
   - Where: §7.4.2 L844 ("題名（カード）… 最短2.0秒") vs design B row B3 L641 (12.0–13.5 s = 1.5 s), the A-A-A variant of E L685, the L-G-L variant of F L699 (cards 12.0–13.5 s), and item 8 L894 ("題名と告知のカードが1.5秒以上").
   - Evidence: item 9 L895 requires the §7.4.2 minimum, so design B as written fails item 9 while passing item 8.
   - Correction: set the title-card minimum to 1.5 s in L844, or lengthen B3 and the two variants to 2.0 s (logo card 13.5→14.0 leaves 1.0 s, so changing L844 is the simpler fix).

2. **Spec: design D row D4 cannot be executed with the §7.4.2 telop table (4:3 and 9:16).**
   - Where: L665 (D4 shows 題名＋コピー, then adds 発売告知＋価格) vs L845, L852.
   - Evidence, 4:3: コピー occupies y=0.735H–0.80H (bottom 0.80H, height 0.065H, centred); 発売告知 occupies 0.70H–0.76H (centred). They overlap by 0.025H once the notice is "added". 9:16: コピー is at y=1200–1264 and "題名と同時には出さない", but the title card puts the title text in the same band at y=1200–1296 for the whole card.
   - Correction: in D4 remove the copy when the notice appears and give the copy its own position on a title card (e.g. 4:3 bottom at 0.66H; 9:16 y=1320–1384 before the notice), or drop "コピー" from D4.

3. **Design v2 fails five items of the spec v1.1 acceptance test it cites as its basis (spec §7.7/§7.8 vs design §1.2–1.3, §4).** Each is a difference to resolve one way or the other:
   - Item 4 (boundary ≥15 frames from a check frame): 15A card starts at frame 330, check frame 337 → 7 frames (D135). 30A/30B/15B are 15/15/18.
   - Item 13 and §7.8 L955/L957 (pixel art = integer nearest-neighbour then area average): design default is direct 1.385× nearest-neighbour (D43); the spec-conformant method is only the "代案" (D44). Measured: default gives column widths alternating 1 px and 2 px; alternative gives 44% pure pixels on a 1 px stripe test.
   - Item 25 (注記 at y=250–320; title/notice/price in the band y=1180–1480): design puts the 注記 at y=1400–1460 and only on game segments (D55); on the title cards the notice is at y=1010 / y=980, inside the window area, not in the band (D60, D62).
   - Items 16/31 (disclosure "new homage, not a period broadcast"): absent from the design and from its checklist (D188–203).
   - Item 11 (fictional platform logo + trademark-equivalent line): absent from the design.
   - Correction: either add a sentence to the design stating which spec items it deliberately departs from and why, or bring the five points into line (start the 15A card at frame 322 or earlier; swap default and alternative scaling or amend the spec; add a disclosure line).

4. **Design: card layouts can overlap or overflow under their own sizing rule.**
   - Where: D60, D62.
   - Evidence: S5a logo centre y=780 with "高さ 400 以下" reaches y=980; the notice (centre 1010, height 68) starts at y=976 → 4 px overlap. 15 s card C4: logo centre 760, same rule → bottom 960; notice (centre 980) starts at 946 → 14 px overlap. Five icons with gaps of half a width take 7× the icon width; at the permitted 160 px (square icons) that is 1120 px > 1080.
   - Correction: cap the logo height at 370 on both cards (or move the notice to centre y=1040 / 1010) and add "icon row width ≤ 960 (icon width ≤ 137)".

## MINOR

5. Spec L558: "単位の重み143.79" is a sum of rounded values; exact value is 143.78 (= 0.678223 × 212). Correction: 143.78.
6. Spec L42, L242: the 185 titles include one upload with no identified title (#714, key `untitled_714`), so "185 − 3 hardware = 182" game titles is 181 identified titles (13.1%, still "約13%"). Correction: say "うち1つは題名不明の投稿".
7. Code, `upload_type` (aggregate.py L132–149): the rule uses the game *flag* but the live *primary code*. Effects in the data: 11 of 54 "実写系＋ゲーム画面" uploads have no G primary code (e.g. 聖剣伝説2 P-P-E, #628 A-A-P); 6 of 41 "絵・カード＋ゲーム画面" and 3 of 76 "絵・カードのみ" uploads carry a live flag (#356, #783); 1 "ゲーム画面主体" upload is L-G-G. Counts reproduce; the asymmetry is not stated in §7.1. Correction: add one sentence to L536–544.
8. Code, exclusion by substring (aggregate.py L172): #711 ヨッシーのクッキー is still excluded only because its note contains "crt_reshoot look". 8 uploads are excluded this way and 10 by `exclusions.tsv`. Correction: move the 8 into `exclusions.tsv` and drop the substring test.
9. Code, year by mode with first-seen tie-break (aggregate.py L272): 7 units have conflicting years, 5 of them tied (クロノ・トリガー 30秒, ゴエモン2 15秒, ヨッシーのクッキー, す〜ぱ〜ぷよぷよ, 高橋名人の大冒険島II). The §2.5 table depends on file order for these; not disclosed. Correction: note it in L57 or leave tied units without a year.
10. Title normalisation: no distinct titles are merged in the 185 keys (only 3 keys have more than one raw spelling, all legitimate). Probable remaining split: スーパーフォーメーションサッカー'94 (#758) and 同 ワールドカップエディション (#748) are separate units. The スーパーマリオワールド (#664, same microphone figure) / 本体 (#661) / 合同 (3 uploads) trio stays split into 3 units; L427 discloses it. Latent only: a title with and without subtitle would split (ドラゴンクエストV vs ドラゴンクエストV 天空の花嫁 → `…5` vs `…5天空の花嫁`); only one spelling occurs in the data. ドラゴンクエストI・II → `…12` (round-1 bug fixed), ロックマンX/X2 distinct, all FFIV spellings (IV, Ⅳ, 4) merge.
11. Spec §7.4.2, 9:16 column: 機種ロゴ (L847) and 社名ロゴ（隅） (L850) have the same coordinates (x=108, y=411, width 150), and A1 L628 allows both at once. Correction: put the platform logo at the window's lower right (x=822, y≈1010) in 9:16.
12. Spec §7.4.2, 4:3: 機種ロゴ at the lower-right corner (L847, used in R1 L740) collides with a right-aligned 注記 (bottom 0.90H, L848). Correction: "注記 is centred when the platform logo is lower right".
13. Spec L847 gives only "左上" for 9:16 while R1 L740 specifies "右下"; item 27 L923 says "整数倍" for 896×672, which is 3.5× horizontally (L954 has it right). Correction: align the wording.
14. Spec 9:16 band: no width limit or shrink rule for the 96 px title text (11 full-width characters fill 1080 px); no y-position for the disclosure line or the 標語 (L849, L967). Correction: add "width ≤ 972, two lines allowed at y=1200–1296+" and a y-range for both.
15. Spec item 8 L894 vs 副案30秒 L777: the last "区間" S5 is a combined section with two cards, so "最後の区間が社名ロゴのカード" does not literally hold; D4's "前半／後半" has no split time. Correction: split S5 into two rows; give D4 a time (e.g. 24.5 s).
16. Spec L458: verdict "確認" for "ストII：全編が実写" while the same cell says "「全編」かどうかは分からない". Correction: 一部確認.
17. Spec L399: 【直接観察】 "衣装の女性" for FFVI; the focus note says only "女性" (the costume/Tina identification is from the 【二次】 note). Correction: "女性".
18. Spec L9: the BLUF uses 【実測】【直接観察】【一次】【設計】 before §1.1 defines them. Correction: add "(ラベルの定義は1.1)".
19. Spec L843: "検査フレームで読ませる場合は、その0.75秒以上前に出し終える" reads as "finish showing". Correction: "出し始める".
20. HTML: highlighting skips text whose raw form differs from its NFKC form. Queries "CM"/"ＣＭ" mark 132 places but none of the 12 full-width "ＣＭ" in the 倉恒 quotations; "(a)" matches 1 section with 0 marks (document has "（a）" 9 times). Section filtering itself is correct. Correction: build the mark regex per text node on the normalised string, or note it in the placeholder.
21. Design D181 (15B): the MV starts at frame 243 = source 56.650 s, exactly the C027→CH1-1-WIDE boundary of a cut list with 0.01 s precision (56.65 is on no 24/30 fps frame grid). This is the same one-wrong-frame risk as round-1 finding 3, which 30B fixed by using 56.667. Same zero margin at 15A frame 243 (213.700, E2→E3). Correction: start both MV rows at frame 244.
22. Design D75: "0.4秒より短い MV のカット（C124 の 0.33秒、C025 の 0.43〜0.47秒）" — C025 is not shorter than 0.4 s. Correction: "0.5秒より短い".
23. Design D141: "ゲーム画面は 1.7秒… 当時のCMでゲーム画面が占める割合（3つの瞬間の平均で 11.4%）に合わせた" uses a sampling-point share as a duration target, against D83. Correction: "設計値。11.4% とは物差しが違う".
24. Design D90 vs spec L689/L703: the design counts "実写とゲーム画面の両方がある投稿" by primary codes (15 s: 26, 30 s: 18); the spec's type counts are 32 and 22. Both recompute correctly under their own definition (7 of 26; max 3 of 18). Correction: state the definition in D90.
25. Design D15: "当時は末尾に社名ロゴのカードを置く作品があった" — the spec observed logo cards only at the ~75% point (MADARA2 #49/#54, エストポリスII #58) and states the tail is unobserved (L670, L746). Correction: "約75%地点に社名ロゴのカードがある投稿があった".
26. Design D56: the minimum title height (90 px in v1 and in spec item 26) was dropped; only maxima remain. Correction: add "高さ 90 以上".
27. Design: nothing addresses game UI below y=1500 in full-canvas segments (spec L955 asks for it), and no silence threshold is given for check 10 (spec uses −60 dBFS). Correction: one line each.
28. Design D145: "ゲーム画面の区間は…56.65秒の手前まで" but the row ends at 56.667 s (frame 500). Correction: "56.67秒まで".

## A. Code — results of the independent recomputation

- Eligible 359 (15 s 227 / 30 s 132), units 212 (139/73), titles 185, both lengths 27, single-upload units 120: all match.
- 3-point means all/15 s/30 s/two strata/13 publishers (L+P, L, P, G, A, E), every per-position code share, live/game/any-text flags, notice and notice-or-title shares, card-with-live share, no-game shares (unit-weighted and units), distribution of unit live shares, units with any L / any flag: 0 mismatches with `results.json`.
- Kappa: 0.8329 / 87.32% over 1,057 frames; firm 897 → 0.9062; unsure 160 → 0.4135; L+P merged 0.8355; 20 C-frames skipped. By length (not in the report): 15 s 0.819 (671 frames), 30 s 0.853 (386).
- Type counts (unit-weighted and upload-level), top-14 sequences, game-position distribution, pass-1 sensitivity, text-tag unit counts, bootstrap CIs (25 intervals reproduced exactly): 0 mismatches.
- `tags_at`: 1,163 tagged items in `readable_text`, 1,163 matched by the regex. The only other shape is 24 bare `illegible_small_text` items (no position, no notice content). No spaced or prefix-less date/status/price tags exist; undercount from parsing = 0. Remaining undercount is the coders' own (part 3 has 0 `title` tags in 92 rows, as L62 says).
- Exclusions: 10 applied; aliases: 2 applied.

## B. Spec number audit

About 900 measured values in §0, §1.2, §2, §4, §5, §7.1, §7.2, §7.4.1, §7.7 compared cell by cell with the recomputation (count approximate; tables were compared by script output, not machine-enumerated). Mismatches: 1 (finding 5). Definitional: 1 (finding 6). Stale v1.0 numbers outside the change log (221, 369, 192, 40.0%, 0.8347, 1,087, old type names, "0〜1地点", "常時", "対照層"): none found. Internal inconsistencies of the same quantity: none found.

## C. Spec fix verification

Round-1 `review1_numbers_and_code.md`

| Finding | Status | Evidence |
|---|---|---|
| B1 tie-break sequences | FIXED | aggregate.py L254–255 (per upload, weighted); L108 |
| B2 strata reversed | FIXED | aggregate.py L274 `all(...)`; L180–187; 94/118 units |
| M1 CI as tolerance, shares as seconds | FIXED | L60, L532, L607, L767, L881 |
| M2 live flag includes P | FIXED | column renamed (L74); L46, L50; types renamed (L538–544) |
| M3 "1地点に集中", "0〜1地点" | FIXED | L9 "0〜2地点"; M1 at L604 |
| M4 "11単位" | FIXED | L221: 19 uploads, weight 12.33, 16 units (recomputed) |
| M5 any-text flag | FIXED | notice columns; L605 |
| M6 unit-level no-game | FIXED | L61, L90–92 |
| M7 second pass narrower | FIXED | L46, L48, L514 |
| M8 joins counted | PARTLY | `exclusions.tsv` applied; substring test kept (finding 8) |
| M9 1990–91 verdict | FIXED | L452 未確認 |

Round-1 `review1_evidence_and_spec.md`

| Finding | Status | Evidence |
|---|---|---|
| B1 timelines not in sample | FIXED | designs A–H follow sampled sequences; blended form is 副案 with counts (L767) |
| B2 no timeline for commonest type | FIXED | designs A–D (L624–668), E (L674) |
| B3 §7.2.4 vs checklist | FIXED | (a) L-L-G, game after title (L734–746); items 5–7 exceptions |
| B4 9:16 | FIXED, with new defects | §7.8 and items 23–31; see findings 2, 11, 13, 14 |
| M1 BLUF 0〜1 | FIXED | L9 |
| M2 §6.1 "3地点とも実写系" | FIXED | L451 |
| M3 "11（5%）" | FIXED | L221 |
| M4 type names | FIXED | L538–558 |
| M5 M1 overstated | FIXED | L604 |
| M6 M2 worded three ways | FIXED | L605, L615, L892 use one wording |
| M7 implied coverage | FIXED | L54, L532, L564 |
| M8 direct-observation overreach | FIXED | L350, L352, L401–403, L746, L763 (one residue: finding 17) |
| M9 observer not stated | FIXED | L23, L296 |
| M10 【実測】 for notes | FIXED | 【分類メモ】 L22, L413, L803–805 |
| M11 音の柱 attribution | FIXED | L871; item 14 L900 |
| M12 文言だけ替える | FIXED | L833, L854 |
| M13 §3 overreach | FIXED | L257, L266–273, L286 |
| M14 §2.10 item 3 | FIXED | L222, L225 |
| M15 黒枠 from n=2 | FIXED | L802 (【設計】 with sizes) |
| M16 telop not executable | PARTLY | §7.4.2 added; findings 1, 2, 11, 12, 14, 15 remain |
| M17 timebase | FIXED | L611, L797, item 1 |
| M18 S2 budget | FIXED | L774, L779 |

Regression checks with no finding: all 12 timelines (A–H, (a), (b), 副案 ×2) and their stated variants are contiguous and sum to 450/900 frames; every stated 3-point signature is produced at frames 112/225/337 or 225/450/675; every boundary is ≥15 frames from a check frame (副案30秒 S1 is exactly 15); overlay start times precede their check frames by ≥0.75 s; items 5, 6, 7 hold for every design. All 倉恒良彰 quotations in §3.1, §5, §7.4.1, §7.5 are character-identical to `verification_of_muse_spec.md` (every quoted string of 12+ characters on those lines, script-checked). §4 tables match `focus_direct_observation.md` cell for cell. §7.8 arithmetic checks: bands sum to 1920; 768×672 and 896×672 margins (156/69, 92/69); 0.75× scaling; logo sizes 162/756/378/150; y=411; 4:3 frame 1194×896 (123/92) and 1024×896 (208/92); safe area 1152×864.

## D. HTML

- Shipped .html is byte-identical to a fresh rebuild.
- Tables 53 = 53, rows 449 = 449, headings 60 = 60, external links 155 = 155, bold 64 = 64, code spans 91 = 91. No raw `**`, `|---`, backticks, `](` or `#` headings in visible text.
- 52 TOC anchors, all resolve, no duplicate ids. No horizontal overflow at 390 px. No console errors.
- Full-width queries work: "ＦＦ" = "FF" (5 sections, 31 marks); "ＦＦＶＩ", half-width katakana, "１０８０×１９２０", full-width space as AND separator all match.
- TOC click during an active filter: filter is cleared and the target is scrolled to (51 of 52 land at the top; the 52nd is the last heading, which cannot scroll further). Enter key on a TOC link also works.
- Remaining: finding 20; a term spanning an inline boundary still shows the section with 0 marks ("平均で実写系"), which the tool's docstring now states.

## E. Design v2

(i) Row check: 42 rows (30A 13, 15A 9, 30B 13, 15B 7). Contiguity 0–900 / 0–450, CM seconds, lengths, source seconds = frame/30 + offset, MV rows inside the named cut (first frame ≥ start, last frame < end), cut id / who / size / place, composition lines, 3-point kinds, audio in/out and frame numbers: 0 mismatches. Zero-margin boundaries: finding 21.

(ii) Game segments vs ledger:

| Plan | Source seconds | Ledger | Label in doc | Verdict |
|---|---|---|---|---|
| 30A | 212.007–215.307 | OK 211–218 | OK | correct |
| 15A | 212.000–213.700 | OK 211–218 | OK | correct |
| 30B | 53.000–56.667 | unconfirmed 52–57 | 確認前 | correct |
| 15B | 54.050–56.650 | unconfirmed 52–57 | 確認前 | correct |
| 30A optional card background | 219.74–224.24 | OK 218.5–234 | OK | correct |
| 15A optional extension | 212.000–215.300 | OK 211–218 | OK | correct |

No segment touches an on-hold item (9–18 s, 22–24 s, 38 s).

(iii) The 29 findings of `review_design.md`

| # | Status | Note |
|---|---|---|
| 1 | FIXED | D55; game rows carry the line, MV rows do not |
| 2 | FIXED | D24–33 |
| 3 | FIXED | D157–158 (frame 500); same pattern left in 15B, finding 21 |
| 4 | FIXED | D45; N=180 gives 248 canvas px (measured) |
| 5 | FIXED | D90; 7 of 26 and max 3 of 18 recomputed |
| 6 | FIXED | D91 |
| 7 | FIXED | 75% frame is now the card in all four plans |
| 8 | FIXED | Q6 (D19) |
| 9 | PARTLY | sizing rule and "record the multiplier" added; asset size still unread; minimum height dropped (finding 26) |
| 10 | FIXED | D61–62; new overlap, finding 4 |
| 11 | FIXED | D102, D149; 15 s "30秒版だけ" |
| 12 | FIXED | D116, D139, D165, D186 |
| 13 | FIXED | 30A opens on the head of C120; 15A on 1.30 s of C122 |
| 14 | FIXED | D75 (wording slip, finding 22) |
| 15 | PARTLY | D83, D88 fixed; D141 repeats it (finding 23) |
| 16 | FIXED | D87 |
| 17 | FIXED | D14 |
| 18 | FIXED | D88 (n=13, n=12; preference claim removed) |
| 19 | FIXED | D207–208 |
| 20 | FIXED | D74 |
| 21 | FIXED | D37 |
| 22 | FIXED | note only; game now starts at 212.007 |
| 23 | FIXED | D43–44, check 6; conflicts with the spec, finding 3 |
| 24 | FIXED | D68 |
| 25 | FIXED | checks 4 and 10 |
| 26 | FIXED | D10, check 12 |
| 27 | FIXED | D118–119, D168 |
| 28 | FIXED | D51 |
| 29 | FIXED | D60–62 |

(iv) Layout, filters, figures
- Window-mode bands: window 330–1140, credit 1160–1200, title logo ≤ 1185–1355, copy 1272–1328, notice 1386–1454, 注記 1400–1460. Spatial overlaps (credit/logo, copy/logo, 注記/notice) never coincide in time. Card overlaps: finding 4.
- ffmpeg, all run on lavfi sources: three MV strings (1920×1080 at 24, 23.976 and 60 fps), game default, game alternative, drawbox + default, pad variant (780×1388), logo card string → every output 1080×1920, 30/1 fps, 30 frames per second. Window lands at y=330–1140; logo card at y=656–1264; intermediate game height 1922, 2 px cropped as stated.
- Measurement figures in §0, §2, §8 (22 values: 39.4/31.7/7.7/29.9/18.5/11.4, 57.8/5.4/23.1 n=13, 55.6 n=12, 51%, 26/7, 18/3, 42/73/44%, "約3割/約4割", 359/212/185, κ 0.83, 160 frames 0.41): 0 mismatches.

(v) Design vs spec §7.8

| Item | Spec v1.1 | Design v2 |
|---|---|---|
| Canvas, fps, window | 1080×1920, 30.00p, window y=330–1140 | same |
| Live-action scaling | 4:3 master ×0.75 | 16:9 cropped to 1440×1080, then ×0.75 (equivalent) |
| Vertical game | whole canvas allowed; integer NN then area | whole canvas; direct NN default, integer+area as alternative |
| Title text | band y=1200–1296, height 96 (≥90) | logo centre 1270, height ≤170, no minimum |
| Notice | y=1320–1392, height 72 | centre 1420 (1386–1454), height 68 |
| Credit | y=1440–1472, height 32 | y=1160–1200, height 30 (partly in the spec's black gap) |
| Copy | y=1200–1264, height 64 | centre 1300, height 56 |
| 注記 | y=250–320, ≥28 px, with platform logo | y=1400–1460, 30 px, game segments only; no platform logo |
| Title card | logo in window, title and notice in band | logo 780, notice 1010 (window area), icons 1230 |
| Logo card | window centre, width 378 | 1080×608 at y=656–1264 (extends below the window) |
| Combined 15 s card | only for 副案15秒 | used in 15A/15B |
| Boundary margin | ≥15 frames | 15A: 7 frames |
| Silence | not required for SNS; clean head 0.2–0.5 s recommended; tail optional | 0.5 s head and tail by default, head may shrink to 0.2 s |
| Disclosure | caption or tail-card band | absent |
| Timelines | F (15 s), G (30 s) section times ±3 frames | own timings (game 6.40–8.10 / 14.27–17.57 etc.) |

## Tallies

- Code vs `results.json`: about 700 values machine-compared (18 groups × 35 values, plus kappa, types, sequences, positions, tags, sensitivity, 25 CIs), 0 mismatches.
- Spec report numbers: about 900 checked, 1 mismatch (143.79 → 143.78), 1 definitional (185 titles includes one untitled upload).
- 倉恒 quotations: all checked by script (about 17 strings), 0 differences.
- Round-1 spec findings (BLOCKER + MAJOR): 33 — 31 FIXED, 2 PARTLY, 0 NOT FIXED.
- HTML: 7 parity counts, 52 anchors, 13 queries, 52 TOC clicks — 0 failures, 1 highlight limitation.
- Design rows: 42 checked, 0 mismatches. Game segments: 6 checked, 0 wrong labels. Design figures: 22 checked, 0 mismatches. ffmpeg strings: 8 run, 0 failures.
- Design round-1 findings: 29 — 27 FIXED, 2 PARTLY, 0 NOT FIXED.
- New findings this round: 0 BLOCKER, 4 MAJOR, 24 MINOR.
