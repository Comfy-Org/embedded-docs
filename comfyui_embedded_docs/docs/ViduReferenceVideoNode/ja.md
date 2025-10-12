> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduReferenceVideoNode/ja.md)

Vidu Reference Videoノードは、複数の参照画像とテキストプロンプトから動画を生成します。AIモデルを使用して、提供された画像と説明に基づいて一貫性のある動画コンテンツを作成します。このノードは、動画の長さ、アスペクト比、解像度、動きの制御など、さまざまな動画設定をサポートしています。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | はい | `"vidu_q1"`<br>`"vidu_q2"`<br>`"vidu_q3"`<br>`"vidu_q4"`<br>`"vidu_q5"`<br>`"vidu_q6"`<br>`"vidu_q7"`<br>`"vidu_q8"`<br>`"vidu_q9"`<br>`"vidu_q10"`<br>`"vidu_q11"`<br>`"vidu_q12"`<br>`"vidu_q13"`<br>`"vidu_q14"`<br>`"vidu_q15"`<br>`"vidu_q16"`<br>`"vidu_q17"`<br>`"vidu_q18"`<br>`"vidu_q19"`<br>`"vidu_q20"`<br>`"vidu_q21"`<br>`"vidu_q22"`<br>`"vidu_q23"`<br>`"vidu_q24"`<br>`"vidu_q25"`<br>`"vidu_q26"`<br>`"vidu_q27"`<br>`"vidu_q28"`<br>`"vidu_q29"`<br>`"vidu_q30"`<br>`"vidu_q31"`<br>`"vidu_q32"`<br>`"vidu_q33"`<br>`"vidu_q34"`<br>`"vidu_q35"`<br>`"vidu_q36"`<br>`"vidu_q37"`<br>`"vidu_q38"`<br>`"vidu_q39"`<br>`"vidu_q40"`<br>`"vidu_q41"`<br>`"vidu_q42"`<br>`"vidu_q43"`<br>`"vidu_q44"`<br>`"vidu_q45"`<br>`"vidu_q46"`<br>`"vidu_q47"`<br>`"vidu_q48"`<br>`"vidu_q49"`<br>`"vidu_q50"`<br>`"vidu_q51"`<br>`"vidu_q52"`<br>`"vidu_q53"`<br>`"vidu_q54"`<br>`"vidu_q55"`<br>`"vidu_q56"`<br>`"vidu_q57"`<br>`"vidu_q58"`<br>`"vidu_q59"`<br>`"vidu_q60"`<br>`"vidu_q61"`<br>`"vidu_q62"`<br>`"vidu_q63"`<br>`"vidu_q64"`<br>`"vidu_q65"`<br>`"vidu_q66"`<br>`"vidu_q67"`<br>`"vidu_q68"`<br>`"vidu_q69"`<br>`"vidu_q70"`<br>`"vidu_q71"`<br>`"vidu_q72"`<br>`"vidu_q73"`<br>`"vidu_q74"`<br>`"vidu_q75"`<br>`"vidu_q76"`<br>`"vidu_q77"`<br>`"vidu_q78"`<br>`"vidu_q79"`<br>`"vidu_q80"`<br>`"vidu_q81"`<br>`"vidu_q82"`<br>`"vidu_q83"`<br>`"vidu_q84"`<br>`"vidu_q85"`<br>`"vidu_q86"`<br>`"vidu_q87"`<br>`"vidu_q88"`<br>`"vidu_q89"`<br>`"vidu_q90"`<br>`"vidu_q91"`<br>`"vidu_q92"`<br>`"vidu_q93"`<br>`"vidu_q94"`<br>`"vidu_q95"`<br>`"vidu_q96"`<br>`"vidu_q97"`<br>`"vidu_q98"`<br>`"vidu_q99"`<br>`"vidu_q100"` | 動画生成に使用するモデル名（デフォルト: "vidu_q1"） |
| `images` | IMAGE | はい | - | 一貫性のある被写体で動画を生成するための参照画像（最大7枚） |
| `prompt` | STRING | はい | - | 動画生成のためのテキストによる説明 |
| `duration` | INT | いいえ | 5-5 | 出力動画の長さ（秒単位）（デフォルト: 5） |
| `seed` | INT | いいえ | 0-2147483647 | 動画生成のためのシード値（0でランダム）（デフォルト: 0） |
| `aspect_ratio` | COMBO | いいえ | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` | 出力動画のアスペクト比（デフォルト: "16:9"） |
| `resolution` | COMBO | いいえ | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"1440p"`<br>`"2160p"` | サポートされる値はモデルと動画の長さによって異なる場合があります（デフォルト: "1080p"） |
| `movement_amplitude` | COMBO | いいえ | `"auto"`<br>`"low"`<br>`"medium"`<br>`"high"` | フレーム内のオブジェクトの動きの振幅（デフォルト: "auto"） |

**制約と制限事項:**

- `prompt`フィールドは必須であり、空にすることはできません
- 参照画像は最大7枚まで使用可能です
- 各画像のアスペクト比は1:4から4:1の間である必要があります
- 各画像の最小寸法は128x128ピクセルである必要があります
- 動画の長さは5秒に固定されています

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 参照画像とプロンプトに基づいて生成された動画 |
