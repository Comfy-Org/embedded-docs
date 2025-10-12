> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageReferenceNode/ja.md)

ByteDance Image Referenceノードは、テキストプロンプトと1～4枚の参照画像を使用して動画を生成します。このノードは画像とプロンプトを外部APIサービスに送信し、参照画像の視覚的なスタイルや内容を取り入れながら、あなたの説明に合った動画を作成します。ノードは、動画の解像度、アスペクト比、長さ、その他の生成パラメータを制御するための様々なオプションを提供します。

## 入力

| パラメータ | データ型 | 入力タイプ | デフォルト | 範囲 | 説明 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seedance_1_lite | seedance_1_lite | モデル名 |
| `prompt` | STRING | STRING | - | - | 動画を生成するために使用するテキストプロンプトです。 |
| `images` | IMAGE | IMAGE | - | - | 1枚から4枚の画像です。 |
| `resolution` | STRING | COMBO | - | 480p, 720p | 出力動画の解像度です。 |
| `aspect_ratio` | STRING | COMBO | - | adaptive, 16:9, 4:3, 1:1, 3:4, 9:16, 21:9 | 出力動画のアスペクト比です。 |
| `duration` | INT | INT | 5 | 3-12 | 出力動画の長さ（秒単位）です。 |
| `seed` | INT | INT | 0 | 0-2147483647 | 生成に使用するシード値です。 |
| `watermark` | BOOLEAN | BOOLEAN | True | - | 動画に「AI生成」の透かしを追加するかどうかです。 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 入力されたプロンプトと参照画像に基づいて生成された動画ファイルです。 |
