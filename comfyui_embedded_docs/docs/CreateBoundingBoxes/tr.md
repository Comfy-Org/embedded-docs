# Sınır Kutuları Oluştur

Bir tuvalde sınır kutuları çiz. Ideogram istem öğeleri, piksel alanında sınır kutuları ve bir önizleme görüntüsü çıktısı verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `arka plan` | Tuvalde ve önizlemede arka plan olarak kullanılan isteğe bağlı görüntü. | IMAGE | No | - |
| `bboxes` | Bounding boxes, elements, or a JSON string to initialize the canvas. A new upstream value initializes the canvas; edits made on the canvas take priority and are kept until the upstream value changes again. | BOUNDING_BOX, ARRAY, STRING | No | - |
| `genişlik` | Tuvalin ve sınır kutuları için piksel ızgarasının genişliği. | INT | Yes | 64 to 16384 (step: 16) |
| `yükseklik` | Tuvalin ve sınır kutuları için piksel ızgarasının yüksekliği. | INT | Yes | 64 to 16384 (step: 16) |
| `düzenleyici durumu` | Sınır kutuları çizin ve her kutunun türünü, metnini, açıklamasını, renk paletini ayarlayın. Önce arka plan öğesiyle başlayın, en son ön planı ekleyin. | BOUNDING_BOXES | Yes | - |
| `last_incoming` | Internal state managed by the canvas: the upstream bboxes value that last initialized it. Leave empty to re-initialize the canvas from the bboxes input on the next run. | BOUNDING_BOXES | No | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `preview` | An RGB image showing the canvas with all bounding boxes rendered, including labels, color palette swatches, and descriptive text. | IMAGE |
| `bboxes` | A list of bounding boxes in pixel coordinates, with each box containing x, y, width, and height values. | BOUNDING_BOX |
| `elements` | A structured array of element objects, each containing type, bounding box coordinates (normalized 0-1000), text (for text type), description, and color palette. | ARRAY |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateBoundingBoxes/tr.md)

---
**Source fingerprint (SHA-256):** `dc5545dffefdccf14f3919ff4d9966dbfd1a497dcd64e1863556d5728659ee94`
