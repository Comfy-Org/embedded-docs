# EmptyChromaRadianceLatentImage

以下に、英語ドキュメントの日本語翻訳を示します。

---

The EmptyChromaRadianceLatentImage node creates a blank latent image with specified dimensions for use in chroma radiance workflows. It generates a tensor filled with zeros (containing 3 color channels) that serves as a starting point for latent space operations. The node allows you to define the width, height, and batch size of the empty latent image.

EmptyChromaRadianceLatentImage ノードは、クロマラディアンスワークフローで使用するために、指定された寸法の空白の潜在イメージを生成します。ゼロで満たされたテンソル（3つのカラーチャンネルを含む）を生成し、潜在空間操作の開始点として機能します。このノードでは、空の潜在イメージの幅、高さ、バッチサイズを定義できます。

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `width` | 潜在イメージの幅（ピクセル単位）（デフォルト: 1024、16で割り切れる必要があります） | INT | はい | 16 to MAX_RESOLUTION |
| `height` | 潜在イメージの高さ（ピクセル単位）（デフォルト: 1024、16で割り切れる必要があります） | INT | はい | 16 to MAX_RESOLUTION |
| `batch_size` | バッチで生成する潜在イメージの数（デフォルト: 1） | INT | いいえ | 1 to 4096 |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `samples` | 指定された寸法でゼロで満たされた、生成された空の潜在イメージテンソル | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/ja.md)

---
**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`
