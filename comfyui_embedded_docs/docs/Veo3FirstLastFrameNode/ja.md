> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/ja.md)

Veo3FirstLastFrameNodeは、GoogleのVeo 3モデルを使用して動画を生成します。テキストプロンプトに基づいて動画を作成し、提供された最初と最後のフレームを使用してシーケンスの開始と終了をガイドします。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | はい | N/A | 動画のテキストによる説明（デフォルト：空文字列）。 |
| `negative_prompt` | STRING | いいえ | N/A | 動画内で避けるべき内容をガイドするネガティブなテキストプロンプト（デフォルト：空文字列）。 |
| `resolution` | COMBO | はい | `"720p"`<br>`"1080p"` | 出力動画の解像度。 |
| `aspect_ratio` | COMBO | いいえ | `"16:9"`<br>`"9:16"` | 出力動画のアスペクト比（デフォルト："16:9"）。 |
| `duration` | INT | いいえ | 4 から 8 | 出力動画の長さ（秒単位）（デフォルト：8）。 |
| `seed` | INT | いいえ | 0 から 4294967295 | 動画生成のためのシード値（デフォルト：0）。 |
| `first_frame` | IMAGE | はい | N/A | 動画の開始フレーム。 |
| `last_frame` | IMAGE | はい | N/A | 動画の終了フレーム。 |
| `model` | COMBO | いいえ | `"veo-3.1-generate"`<br>`"veo-3.1-fast-generate"` | 生成に使用する特定のVeo 3モデル（デフォルト："veo-3.1-fast-generate"）。 |
| `generate_audio` | BOOLEAN | いいえ | N/A | 動画の音声を生成するかどうか（デフォルト：True）。 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成された動画ファイル。 |
