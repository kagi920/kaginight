# Charakuru / Tripo の費用・要件確認
確認日：2026-10-14 UTC。公開一次資料のみ。ログイン、購入、画像アップロード、インストール、実機テストは行っていない。

## 結論
B（Charakuru → Tripo → Blender → VRM）を「無料」と案内するのは不正確。キットの無償利用条件と、画像生成・エージェント・Tripoの料金は別。Charakuruは現在Tripo StudioのSmart Meshを利用する構成で、ローカルTripoSRに置換できるという公式説明は確認できない。

## 1. Charakuruの確認済み要件
公式READMEの1.0.4案内：Node.js 22以上、デスクトップChromiumブラウザ、画像生成とブラウザ操作ができるCodex、ブラウザにログインしたTripoアカウント、Blender 5.2、VRM Add-on for Blender、Blender MCP、利用権のある全身イラスト。外部サービスは利用者自身のアカウント・規約・料金で使用。実体は専用Release ZIPで、GitHub自動生成のSource code ZIPには入っていない。
新規キャラクターの表情・視線移動は現状含まれない。完成VRMはそのまま表情付きVTuber完成品とは限らない。
出典：[README](https://github.com/nanocle/Charakuru)

キット自体：純粋な個人利用、または事業全体の年商と累積調達額がそれぞれ1億円未満なら条件付き無償。どちらか以上の業務利用は事前の別途書面契約が必要。キットの再配布、同梱アセットの単独再配布には制限がある。正当に作成した成果物にキット側のロイヤルティやクレジット義務は課さないが、元絵・外部AI・第三者素材の権利までは保証しない。
出典：[正式LICENSE §2–3,6,8](https://raw.githubusercontent.com/nanocle/Charakuru/main/LICENSE)

## 2. Tripo Studio：現在の料金表で確認した内容
- Free：$0、月200 credits、公開モデル・非商用。保存と書き出しに制限。比較表に「15（H2.5 only）」とあり、P2の無料書き出しまで保証する数字ではない。
- Pro：月3,000 credits。ページには$20/月、年払い$240/年、比較表にはMonthly $20と表示。月払い選択と最終請求額は購入画面で再確認が必要。非公開モデル・商用利用・Smart Mesh・複数視点生成・無制限書き出しを案内。
- 追加credits表示：$10で1,000。ただし購入資格・税・プラン機能解放は未確認。追加creditsだけでPro機能を解放できるとは判断しない。
- 料金表の「約200 models」等は、Charakuruの完成VRM数ではない。
出典：[Studio料金表](https://www.tripo3d.ai/pricing)

Studioの月次creditsは翌月へ繰り越さない。APIは別購入・別残高で、Studio契約に含まれない。
出典：[公式Help](https://www.tripo3d.ai/help/api-plugins/tripo-studiotripo-api)

## 3. 工程別creditsと試作枠
Tripo公式の新パイプライン記事（ドイツ語公開版）では、P2 Official生成100、Mesh Edit 50/編集、Smart UV 20、UV再実行10、Texture 20、Rigging 20、Text to Motion 20 credits。1体を一括生成する例は180 creditsと説明。最大4つのポリゴン数違いを同額で生成できる旨もある。FreeでP2/UVの試用を案内するが、無料回数・出力権限は明示されていない。
出典：[公式Studioパイプライン](https://www.tripo3d.ai/de/blog/3d-game-pipeline)

**限定試作案（提案であり購入・完成保証ではない）**
1. まず支出$0で、利用アカウントのP2試用、Multi-view、書き出し可否とボタン上のcreditsを確認。無料でB全工程を完走できるとは約束しない。
2. Bの本試作をする場合、Proの「月払い1期間」の条件を確認し、表示価格$20＋実際の税等を承認してから開始。年契約$240を1か月の試用と取り違えない。エージェント／画像生成費は別途。
3. 最初は1キャラクター、頭・体の候補各1バッチ。頭・体を別々に生成すると仮定した参考計算は、100×2＋UV20×2＋Texture20×2＋Rig20＝300 credits。これは公開単価を足した仮計算で、Charakuruの実消費量の実測値ではない。
4. Tripo部分は最大600 creditsを暫定停止ラインにし、各実行前の表示額を記録。600到達・見積外操作・追加購入の時点で止めて見直す。再生成、修正、追加テクスチャ、候補の扱いで増える。追加購入や年間契約は自動で行わない。
5. 試作判定は顔の正面・側面、髪と服の貫通、肩肘膝、髪揺れ、VRM再読み込み。合格しなければ反復予算を増やす前にAとの用途適合を再評価。

上記300/600 creditsは円やドルの完成品価格ではない。Studioプラン・API・追加creditsの換算を混ぜない。公式記事の「180 credits / $1.8」も、サブスクリプション込みの実際の支払総額と同義ではない。

## 4. APIは別ルート
現行開発者料金表は1 credit＝US$0.01、$1から追加可能。Auto Rig 25、基本形式変換5、Smart UV20 credits。Studio記事のRig20とは異なる。APIをCharakuruの必要契約と誤案内しない。
出典：[現行API料金](https://developers.tripo3d.ai/en/pricing)
旧OpenAPIドキュメントは2週間で300無料creditsの開始案内があるが、現行アカウントでの付与条件・残高は未確認。Studioの月200とは別。P2価格の現在のタブ内容は今回テキスト取得で確認できず、旧P1/H系の価格をP2に流用しない。
出典：[旧OpenAPI料金](https://docs.tripo3d.ai/get-started/pricing.html)

## 5. 出力ライセンスの注意
現行料金表はFree非商用、Pro以上商用と明記。一方、公式の画像→3D紹介ページにはFree＝CC BY 4.0という記載が残り、公式資料間に矛盾がある。無料モデルを商用可と断言しない。無料生成後のアップグレードで過去出力へ商用権が遡及するかも未確認。
正式規約§5.2は無料ユーザー入出力にTripoの広い権利、有料ユーザーには条件付きの利用・配布等の権利を規定。元画像の権利、用途制限も別途適用。商用制作は生成時のプランと規約を記録し、Free出力の扱いが必要ならTripoに明確化してもらう。
出典：[料金表](https://www.tripo3d.ai/pricing)、[規約](https://www.tripo3d.ai/terms)、[矛盾する機能紹介](https://www.tripo3d.ai/features/image-to-3d-model)

規約は自動更新・税別・原則返金不可を規定。購入するなら最終画面の請求周期、税、解約条件を確認する。
出典：[規約§6](https://www.tripo3d.ai/terms)

## 6. M1 Mac / GTX 1660 SUPERの実現性
**Charakuru + Studio**：生成は外部サービスで、ローカルはレビューアプリとBlender工程。公開READMEにキット全体の最低RAM・VRAM、M1/1660 SUPERのベンチマークは見つからない。従って「M1なら確実」「1660なら何分」とは言えない。OS、RAM、空き容量、Blender5.2とアドオンの互換性を実機で確認する必要がある。
Blender5系はApple siliconをサポートするが、これだけでキット全工程の動作保証にはならない。
出典：[Blender公式5.2マニュアル](https://docs.blender.org/manual/es/latest/getting_started/installing/macos.html)

**ローカルTripoSR**：別の公開モデル。公式はPython3.8以上、環境に合うPyTorch/CUDA等、標準の単一画像処理で約6GB VRAMと案内。コード・重みはMIT。CharakuruのP2 Smart Mesh／リグ／VRM生成一式ではない。
出典：[TripoSR公式](https://github.com/VAST-AI-Research/TripoSR)
GTX1660 SUPERの標準VRAMは6GB。TripoSRの目安と同容量なので余裕がある構成とは言えず、起動や速度を保証しない。M1の統合メモリとNVIDIA VRAMの数字を同一視しない。今回確認したREADMEはM1/MPS動作を保証していない。
出典：[NVIDIA公式比較表](https://www.nvidia.com/en-us/geforce/graphics-cards/compare/)

## 未確認として残す事項
- 実アカウントでのP2無料試用回数・出力可否、Pro月払いの最終税額
- Charakuru1体当たりの実測credits、エージェント・画像生成の追加費用
- 使用機のRAM/OS/ドライバ、アドオン互換性、所要時間
- Free生成モデルへの後日アップグレードの権利遡及
- ユーザーの利用目的に対する商用条件の個別適合
