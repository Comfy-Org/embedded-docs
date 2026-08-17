# ByteDance Seedream 5.0 Pro レイヤー分離

ByteDance Seedream 5.0 Pro Layer Separation は、画像を背景プレートと最大16枚の透明レイヤー（それぞれに独自の重なり順、バウンディングボックス、名前、説明が付属）に分解します。背景、レイヤーごとのマスク付き画像、配置ボックス、すぐに編集できるレイヤースタックを返します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `image` | 分離する画像。画像は正確に1枚で、512x512ピクセル以上、アスペクト比は1:16から16:1の間である必要があります。約4MPより大きい入力はアップロード前に縮小されます。 | IMAGE | はい | 単一画像 |
| `prompt` | 画像の分離方法。空のままにすると、主要な要素を自動検出してすべて分離します。要素を自然言語で記述して分離を制御したり、`<bbox>left top right bottom</bbox>` タグ（0〜1000のパーミル座標）で正確な領域を指定したりできます。デフォルト: 空文字列。 | STRING | はい | 複数行テキスト |
| `size` | 出力解像度レベル。"auto"は入力画像サイズに従います（1K〜2Kの範囲に制限されます）。デフォルト: "auto"。 | COMBO | はい | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | 生成に使用するシード。デフォルト: 0。 | INT | はい | 0 to 2147483647 |
| `prompt_optimization` | プロンプト最適化モード。"standard"は高品質、"fast"は生成時間が短くなります。デフォルト: "standard"。 | COMBO | いいえ | "standard"<br>"fast" |
| `watermark` | 画像に「AI生成」ウォーターマークを追加するかどうか。デフォルト: false。 | BOOLEAN | いいえ | false<br>true |
| `crop_layers` | レイヤー/マスクのバッチ出力の形状（layer_stackは影響を受けず、常にタイトな状態）。フルキャンバス: 各レイヤーをベースサイズのキャンバス上のバウンディングボックス位置に配置 - ImageCompositeMaskedで直接再合成できます。最小サイズ: 各レイヤーをバウンディングボックスにクロップ（バッチ用に最大レイヤーにパディング）- テンソルがはるかに小さくなります。bboxes出力を使用してLayers From Bounding Boxesで配置を再構築します。デフォルト: false（フルキャンバス）。 | BOOLEAN | いいえ | false（フルキャンバス）<br>true（最小サイズ） |

注: 入力画像は単一画像である必要があります。バッチには対応していません。画像は512x512ピクセル以上で、アスペクト比が1:16から16:1の間である必要があります。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `base_image` | レイヤーが重ねられるベース画像（背景プレート）。 | IMAGE |
| `base_mask` | ベース画像の透明度（1 = 透明、LoadImageの規約）。現在は常に完全に不透明です。 | MASK |
| `layers` | 下から上に並べられた透明レイヤー。フルキャンバスモード: バウンディングボックスの位置にベースサイズの黒いキャンバス上に配置。最小サイズモード: バウンディングボックスにクロップされ、左上を基準に最大レイヤーにパディングされます。 | IMAGE |
| `masks` | レイヤーごとの透明度。layersバッチとインデックスが一致します（1 = 透明、LoadImageの規約）。ImageCompositeMaskedスタイルの合成では、最初にInvertMaskを追加してください。 | MASK |
| `bboxes` | レイヤーごとに1つの配置ボックス。layersバッチとインデックスが一致します（layersバッチとbboxesの両方を、マスクと一緒にLayers From Bounding Boxesに渡すと、レイヤーごとの配置を再構築できます）。`{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`。`content_rect = [left, top, width, height]` はレイヤー自身のフレーム内でのコンテンツ領域です。この領域は、ボックス位置にそのオフセットを加えた位置でキャンバス上に配置されます。 | BOUNDING_BOX |
| `layer_stack` | Create Layered Image用のすぐに編集できるレイヤードキュメント。ベースプレートに加え、各要素が独自の名前付きタイトクロップレイヤーとして、実際の位置と重なり順で含まれます。直接接続するか、Add Layerで拡張できます。 | LAYERS |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/ja.md)

---
**Source fingerprint (SHA-256):** `5062760f2930333f8ed7d8b09dff2492c23fdf906ef71b111348687bef572821`
