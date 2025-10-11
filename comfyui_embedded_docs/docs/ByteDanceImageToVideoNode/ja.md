> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/ja.md)

ByteDance Image to Videoノードは、入力画像とテキストプロンプトに基づいて、APIを通じてByteDanceモデルを使用して動画を生成します。開始画像フレームを受け取り、提供された説明に沿った動画シーケンスを作成します。このノードは、動画の解像度、アスペクト比、長さ、その他の生成パラメータに関する様々なカスタマイズオプションを提供します。

## 入力

| パラメータ | データ型 | 入力タイプ | デフォルト | 範囲 | 説明 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | STRING | COMBO | seedance_1_pro | Image2VideoModelName オプション | モデル名 |
| `prompt` | STRING | STRING | - | - | 動画生成に使用するテキストプロンプト。 |
| `image` | IMAGE | IMAGE | - | - | 動画の最初のフレームとして使用される画像。 |
| `resolution` | STRING | COMBO | - | ["480p", "720p", "1080p"] | 出力動画の解像度。 |
| `aspect_ratio` | STRING | COMBO | - | ["adaptive", "16:9", "4:3", "1:1", "3:4", "9:16", "21:9"] | 出力動画のアスペクト比。 |
| `duration` | INT | INT | 5 | 3-12 | 出力動画の長さ（秒単位）。 |
| `seed` | INT | INT | 0 | 0-2147483647 | 生成に使用するシード値。 |
| `camera_fixed` | BOOLEAN | BOOLEAN | False | - | カメラを固定するかどうかを指定します。プラットフォームはプロンプトにカメラを固定する指示を追加しますが、実際の効果を保証するものではありません。 |
| `watermark` | BOOLEAN | BOOLEAN | True | - | 動画に「AI生成」の透かしを追加するかどうか。 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 入力画像とプロンプトパラメータに基づいて生成された動画ファイル。 |