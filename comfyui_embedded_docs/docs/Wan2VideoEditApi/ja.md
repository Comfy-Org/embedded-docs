> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/ja.md)

このドキュメントはAI生成です。誤りや改善のご提案がございましたら、ぜひご協力ください。[GitHubで編集する](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/en.md)

Wan2VideoEditApiノードは、Wan 2.7モデルを使用して、テキスト指示、参照画像、またはスタイル変換に基づいて動画を編集します。入力動画を処理し、解像度、長さ、アスペクト比などの指定されたパラメータに従って新しい動画を生成します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | はい | `"wan2.7-videoedit"` | 動画編集に使用するモデルです。 |
| `model.prompt` | STRING | はい | - | 編集指示またはスタイル変換の要件です。（デフォルト：空文字列） |
| `model.resolution` | COMBO | はい | `"720P"`<br>`"1080P"` | 出力動画の解像度です。 |
| `model.ratio` | COMBO | はい | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | 出力動画のアスペクト比です。変更しない場合、入力動画の比率に近似します。 |
| `model.duration` | COMBO | はい | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` | 出力の長さ（秒）です。"auto"は入力動画の長さに一致します。特定の値を指定すると、動画の先頭から切り取られます。（デフォルト："auto"） |
| `model.reference_images` | IMAGE | いいえ | - | 編集をガイドするための最大4枚の参照画像のリストです。 |
| `video` | VIDEO | はい | - | 編集する動画です。 |
| `seed` | INT | いいえ | 0 ～ 2147483647 | 生成に使用するシード値です。（デフォルト：0） |
| `audio_setting` | COMBO | いいえ | `"auto"`<br>`"origin"` | 'auto'：モデルがプロンプトに基づいてオーディオを再生成するかどうかを決定します。'origin'：入力動画の元のオーディオを保持します。（デフォルト："auto"） |
| `watermark` | BOOLEAN | いいえ | - | 結果にAI生成の透かしを追加するかどうかです。（デフォルト：False） |

**制約事項：**
*   `model.prompt`は1文字以上である必要があります。
*   入力`video`の長さは2秒以上10秒以下である必要があります。
*   `model.reference_images`入力は最大4枚の画像まで受け入れ可能です。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output` | VIDEO | モデルによって生成された編集済み動画です。 |