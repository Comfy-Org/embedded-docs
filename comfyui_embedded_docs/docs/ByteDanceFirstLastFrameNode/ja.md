> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/ja.md)

このノードは、テキストプロンプトと最初と最後のフレーム画像を使用して動画を生成します。あなたの説明と2つのキーフレームを受け取り、それらの間を遷移する完全な動画シーケンスを作成します。このノードは、動画の解像度、アスペクト比、長さ、およびその他の生成パラメータを制御するためのさまざまなオプションを提供します。

## 入力

| パラメータ | データ型 | 入力タイプ | デフォルト | 範囲 | 説明 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | COMBO | combo | seedance_1_lite | seedance_1_lite | モデル名 |
| `prompt` | STRING | string | - | - | 動画の生成に使用されるテキストプロンプトです。 |
| `first_frame` | IMAGE | image | - | - | 動画で使用する最初のフレームです。 |
| `last_frame` | IMAGE | image | - | - | 動画で使用する最後のフレームです。 |
| `resolution` | COMBO | combo | - | 480p, 720p, 1080p | 出力動画の解像度です。 |
| `aspect_ratio` | COMBO | combo | - | adaptive, 16:9, 4:3, 1:1, 3:4, 9:16, 21:9 | 出力動画のアスペクト比です。 |
| `duration` | INT | slider | 5 | 3-12 | 出力動画の長さ（秒単位）です。 |
| `seed` | INT | number | 0 | 0-2147483647 | 生成に使用するシード値です。（オプション） |
| `camera_fixed` | BOOLEAN | boolean | False | - | カメラを固定するかどうかを指定します。プラットフォームはプロンプトにカメラを固定する指示を追加しますが、実際の効果を保証するものではありません。（オプション） |
| `watermark` | BOOLEAN | boolean | True | - | 動画に「AI生成」の透かしを追加するかどうかです。（オプション） |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成された動画ファイル |