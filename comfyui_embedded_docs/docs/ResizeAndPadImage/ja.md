> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeAndPadImage/ja.md)

ResizeAndPadImageノードは、画像を指定された寸法内に収まるようにリサイズし、元のアスペクト比を維持します。画像をターゲットの幅と高さ内に収まるように比例して縮小し、残りのスペースを埋めるために周囲にパディングを追加します。パディングの色と補間方法をカスタマイズすることで、パディング領域の外観とリサイズの品質を制御できます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | はい | - | リサイズおよびパディングを行う入力画像 |
| `target_width` | INT | はい | 1 ～ MAX_RESOLUTION | 出力画像の希望幅（デフォルト: 512） |
| `target_height` | INT | はい | 1 ～ MAX_RESOLUTION | 出力画像の希望高さ（デフォルト: 512） |
| `padding_color` | COMBO | はい | "white"<br>"black" | リサイズされた画像の周囲のパディング領域に使用する色 |
| `interpolation` | COMBO | はい | "area"<br>"bicubic"<br>"nearest-exact"<br>"bilinear"<br>"lanczos" | 画像のリサイズに使用する補間方法 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `image` | IMAGE | リサイズおよびパディングされた出力画像 |
