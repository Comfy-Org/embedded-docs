> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetFromFolderNode/ja.md)

LoadImageSetFromFolderNodeは、トレーニング目的で指定されたフォルダから複数の画像を読み込みます。一般的な画像形式を自動的に検出し、オプションでさまざまな方法を使用して画像をリサイズしてから、バッチとして返します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `folder` | STRING | はい | 複数のオプション利用可能 | 画像を読み込む元のフォルダです。 |
| `resize_method` | STRING | いいえ | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | 画像のリサイズに使用する方法です（デフォルト: "None"）。 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 読み込まれた画像のバッチを単一のテンソルとして出力します。 |