# RenderMesh

Bu düğüm, tek bir görünümü ışın izleme yöntemiyle işleyerek bir 3D mesh'i 2D görüntüye dönüştürür. Dokulu mesh, köşe renkleri, düz gölgeli bir yüzey, yüzey normalleri veya derinlik çıktısı verebilir. Kamera ve isteğe bağlı model dönüşümü bir Load3D / Preview3D görüntüleyiciden gelebilir; hiçbir kamera bağlı değilse, varsayılan önden görünüm otomatik olarak çerçevelenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ağ` | İşlenecek 3D mesh. | MESH | Evet | — |
| `mod` | Ne işleneceği. auto: mevcutsa texture, aksi takdirde vertex colors, aksi takdirde shaded clay. (varsayılan: "auto") | COMBO | Evet | `"auto"`<br>`"texture"`<br>`"vertex colors"`<br>`"solid"`<br>`"normal"`<br>`"depth"` |
| `genişlik` | İşlenen görüntünün piksel cinsinden genişliği. (varsayılan: 1024) | INT | Evet | 64 ila 4096 (adım 8) |
| `yükseklik` | İşlenen görüntünün piksel cinsinden yüksekliği. (varsayılan: 1024) | INT | Evet | 64 ila 4096 (adım 8) |
| `arka plan` | Meshin kapsamadığı pikseller için kullanılan arka plan rengi. (varsayılan: "#000000") | COLOR | Evet | — |
| `model_3d_info` | Aynı Load3D / Preview3D görüntüleyiciden model dönüşümü. Görüntüleyici çerçevesiyle eşleşmesi için camera_info ile birlikte bağlayın. | LOAD3D_MODEL_INFO | Hayır | — |
| `camera_info` | Bir Load3D / Preview3D görüntüleyiciden veya bir Create Camera Info düğümünden kamera. Hiçbiri bağlı değilse, varsayılan önden görünüm otomatik olarak çerçevelenir. | LOAD3D_CAMERA | Hayır | — |

Not: Toplu bir meshin yalnızca ilk öğesi işlenir — mesh grubu birden fazla öğe içeriyorsa, düğüm bir uyarı kaydeder ve ilk öğeyi kullanır. `texture` modu, meshin hem bir dokuya hem de UV'lere sahip olmasını gerektirir ve `vertex colors` modu köşe renkleri gerektirir; seçilen mod için veri mevcut değilse, düğüm düz gölgeli işlemeye geri döner. `model_3d_info` ve `camera_info`, işlemenin görüntüleyici çerçevesiyle eşleşmesi için aynı Load3D / Preview3D görüntüleyiciden birlikte bağlanmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `görüntü` | Meshin işlenmiş görüntüsü. | IMAGE |
| `maske` | Meshin işlendiği yerlerde 1.0, diğer yerlerde 0.0 olan bir maske. | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderMesh/tr.md)

---
**Source fingerprint (SHA-256):** `d23e85a904520eb2dfed899eb3e6a9cf45c980df00c034503687ac4eccc66ac4`
