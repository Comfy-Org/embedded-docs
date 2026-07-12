# バウンディングボックスを作成

キャンバス上にバウンディングボックスを描画します。Ideogramプロンプト要素、ピクセル空間のバウンディングボックス、プレビュー画像を出力します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `背景画像` | キャンバスやプレビューで背景として使用する画像（任意）。 | IMAGE | No | - |
| `bboxes` | Bounding boxes, elements, or a JSON string to initialize the canvas. A new upstream value initializes the canvas; edits made on the canvas take priority and are kept until the upstream value changes again. | BOUNDING_BOX, ARRAY, STRING | No | - |
| `幅` | キャンバスおよびバウンディングボックス用ピクセルグリッドの幅。 | INT | Yes | 64 to 16384 (step: 16) |
| `高さ` | キャンバスおよびバウンディングボックス用ピクセルグリッドの高さ。 | INT | Yes | 64 to 16384 (step: 16) |
| `エディタ状態` | バウンディングボックスを描画し、各ボックスのタイプ、テキスト、説明、カラーパレットを設定します。背景要素から始め、前景を最後に設定してください。 | BOUNDING_BOXES | Yes | - |
| `last_incoming` | Internal state managed by the canvas: the upstream bboxes value that last initialized it. Leave empty to re-initialize the canvas from the bboxes input on the next run. | BOUNDING_BOXES | No | - |

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `preview` | An RGB image showing the canvas with all bounding boxes rendered, including labels, color palette swatches, and descriptive text. | IMAGE |
| `bboxes` | A list of bounding boxes in pixel coordinates, with each box containing x, y, width, and height values. | BOUNDING_BOX |
| `elements` | A structured array of element objects, each containing type, bounding box coordinates (normalized 0-1000), text (for text type), description, and color palette. | ARRAY |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateBoundingBoxes/ja.md)

---
**Source fingerprint (SHA-256):** `dc5545dffefdccf14f3919ff4d9966dbfd1a497dcd64e1863556d5728659ee94`
