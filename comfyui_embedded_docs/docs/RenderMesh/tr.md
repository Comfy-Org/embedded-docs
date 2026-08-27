# RenderMesh

Bu düğüm, tek bir görünümü ray-casting (ışın izleme) yöntemiyle işleyerek 3D bir mesh'i 2D bir görüntüye dönüştürür. Dokulu mesh, köşe renkleri, gölgeli katı bir yüzey, yüzey normalleri veya derinlik çıktısı verebilir. Kamera ve isteğe bağlı model dönüşümü bir Load3D / Preview3D görüntüleyicisinden gelebilir; bir kamera bağlı değilse, varsayılan önden görünüm otomatik olarak çerçevelenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | İşlenecek 3D mesh. | MESH | Evet | — |
| `mode` | Ne işleneceğini belirler. auto: varsa doku, aksi halde vertex colors, aksi halde gölgeli kil. (varsayılan: "auto") | COMBO | Evet | `"auto"`<br>`"texture"`<br>`"vertex colors"`<br>`"solid"`<br>`"normal"`<br>`"depth"` |
| `width` | İşlenen görüntünün piksel cinsinden genişliği. (varsayılan: 1024) | INT | Evet | 64 to 4096 (step 8) |
| `height` | İşlenen görüntünün piksel cinsinden yüksekliği. (varsayılan: 1024) | INT | Evet | 64 to 4096 (step 8) |
| `background` | Mesh'in kaplamadığı pikseller için kullanılan arka plan rengi. (varsayılan: "#000000") | COLOR | Evet | — |
| `model_3d_info` | Aynı Load3D / Preview3D görüntüleyicisinden alınan model dönüşümü. Görüntüleyici çerçevesiyle eşleşmesi için camera_info ile birlikte bağlayın. | LOAD3D_MODEL_INFO | Hayır | — |
| `camera_info` | Bir Load3D / Preview3D görüntüleyicisinden veya Create Camera Info düğümünden alınan kamera. Hiçbiri bağlı değilse, varsayılan önden görünüm otomatik olarak çerçevelenir. | LOAD3D_CAMERA | Hayır | — |

Not: Batch (toplu) mesh'in yalnızca ilk öğesi işlenir — mesh batch'i birden fazla öğe içeriyorsa düğüm bir uyarı kaydeder ve ilkini kullanır. `texture` modu, mesh'in hem dokuya hem de UV'lere sahip olmasını gerektirir; `vertex colors` modu ise köşe renklerine sahip olmasını gerektirir. Seçilen mod için veri mevcut değilse, düğüm gölgeli katı (solid) görünüme geri döner. `model_3d_info` ve `camera_info`'nun, işlenen görüntünün görüntüleyici çerçevesiyle eşleşmesi için aynı Load3D / Preview3D görüntüleyicisinden birlikte bağlanması amaçlanmıştır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Mesh'in işlenmiş görüntüsü. | IMAGE |
| `mask` | Mesh'in işlendiği yerlerde 1.0, diğer yerlerde 0.0 olan bir maske. | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderMesh/tr.md)

---
**Source fingerprint (SHA-256):** `d23e85a904520eb2dfed899eb3e6a9cf45c980df00c034503687ac4eccc66ac4`
