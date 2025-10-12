> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFlip/ja.md)

ImageFlipノードは、異なる軸に沿って画像を反転させます。x軸に沿って垂直方向、またはy軸に沿って水平方向に画像を反転することができます。このノードは、選択された方法に基づいて反転を行うためにtorch.flip操作を使用します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | はい | - | 反転させる入力画像 |
| `flip_method` | STRING | はい | "x-axis: vertically"<br>"y-axis: horizontally" | 適用する反転方向 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `image` | IMAGE | 反転された出力画像 |
