# Ağı Renderla

Bu düğüm, tek bir görünümü ışın izleme (ray-casting) ile işleyerek bir 3B mesh'i 2B görüntüye dönüştürür. Dokulu mesh'i, vertex renklerini, düz gölgeli bir yüzeyi, yüzey normallerini veya derinliği çıktı olarak verebilir. Kamera ve isteğe bağlı model dönüşümü bir Load3D / Preview3D görüntüleyicisinden gelebilir; kamera bağlı değilse varsayılan bir önden görünüm otomatik olarak çerçevelenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `mesh` | İşlenecek 3B mesh. | MESH | Evet | — |
| `mode` | Neyin işleneceği. auto: varsa doku, yoksa vertex renkleri, yoksa gölgeli kil. (varsayılan: "auto") | COMBO | Evet | `"auto"`<br>`"texture"`<br>`"vertex colors"`<br>`"solid"`<br>`"normal"`<br>`"depth"` |
| `width` | İşlenen görüntünün piksel cinsinden genişliği. (varsayılan: 1024) | INT | Evet | 64 - 4096 (adım 8) |
| `height` | İşlenen görüntünün piksel cinsinden yüksekliği. (varsayılan: 1024) | INT | Evet | 64 - 4096 (adım 8) |
| `background` | Mesh'in kapsamadığı pikseller için kullanılan arka plan rengi. (varsayılan: "#000000") | COLOR | Evet | — |
| `model_3d_info` | Aynı Load3D / Preview3D görüntüleyicisinden gelen model dönüşümü. Görüntüleyici çerçevelemesiyle eşleşmesi için `camera_info` ile bağlayın. | LOAD3D_MODEL_INFO | Hayır | — |
| `camera_info` | Bir Load3D / Preview3D görüntüleyicisinden veya bir Create Camera Info düğümünden gelen kamera. Hiçbiri bağlı değilse varsayılan bir önden görünüm otomatik olarak çerçevelenir. | LOAD3D_CAMERA | Hayır | — |

Not: Toplu bir mesh'in yalnızca ilk öğesi işlenir — mesh batch'i birden fazla öğe içeriyorsa düğüm bir uyarı kaydeder ve ilkini kullanır. `texture` modu, mesh'in hem bir dokuya hem de UV'lere sahip olmasını gerektirir; `vertex colors` modu ise vertex renklerini gerektirir; seçilen mod için veriler mevcut değilse düğüm, düz gölgeli işlemeye geri döner. `normal` modu, mevcutsa mesh'in yumuşak vertex normallerini, aksi halde yüz başına normali kullanır. `depth` modunda, daha yakın yüzeyler daha parlak görünür (yakın = beyaz) ve mesh'in kapsamadığı pikseller siyah kalır. `model_3d_info` ve `camera_info`, aynı Load3D / Preview3D görüntüleyicisinden birlikte bağlanmak üzere tasarlanmıştır, böylece işleme görüntüleyicinin çerçevelemesiyle eşleşir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `image` | Mesh'in işlenmiş görüntüsü. | IMAGE |
| `mask` | Mesh'in işlendiği yerlerde 1.0, diğer yerlerde 0.0 olan bir maske. | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderMesh/tr.md)

---
**Source fingerprint (SHA-256):** `d23e85a904520eb2dfed899eb3e6a9cf45c980df00c034503687ac4eccc66ac4`
