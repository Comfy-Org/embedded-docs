> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/ja.md)

ByteDance Image Editノードを使用すると、APIを通じてByteDanceのAIモデルを使って画像を編集できます。入力画像と希望の変更内容を説明するテキストプロンプトを提供すると、ノードが指示に従って画像を処理します。ノードはAPI通信を自動的に処理し、編集された画像を返します。

## 入力

| パラメータ | データ型 | 入力タイプ | デフォルト | 範囲 | 説明 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seededit_3 | Image2ImageModelNameオプション | モデル名 |
| `image` | IMAGE | IMAGE | - | - | 編集するベース画像 |
| `prompt` | STRING | STRING | "" | - | 画像編集の指示 |
| `seed` | INT | INT | 0 | 0-2147483647 | 生成に使用するシード値 |
| `guidance_scale` | FLOAT | FLOAT | 5.5 | 1.0-10.0 | 値が高いほどプロンプトに忠実な画像になります |
| `watermark` | BOOLEAN | BOOLEAN | True | - | 画像に「AI生成」の透かしを追加するかどうか |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | ByteDance APIから返された編集済み画像 |
