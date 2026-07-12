# Sınır Kutuları Oluştur

Bu düğüm, bir görüntüdeki nesneler veya metin bölgeleri etrafında sınırlayıcı kutular çizmek için bir tuval arayüzü sağlar. Sınırlayıcı kutu koordinatlarını piksel uzayında, Ideogram istem biçimlendirmesiyle uyumlu yapılandırılmış öğe verilerini ve çizilen kutuları etiketler ve renk paletleriyle gösteren bir önizleme görüntüsü çıktısı olarak verir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `arka plan` | Tuval ve önizlemede arka plan olarak kullanılan isteğe bağlı görüntü. | IMAGE | Hayır | - |
| `bboxes` | Tuvale başlatmak için sınırlayıcı kutular, öğeler veya bir JSON dizesi. Yeni bir yukarı akış değeri tuvale başlatır; tuval üzerinde yapılan düzenlemeler öncelik kazanır ve yukarı akış değeri tekrar değişene kadar korunur. | BOUNDING_BOX, ARRAY, STRING | Hayır | - |
| `genişlik` | Tuvalin ve sınırlayıcı kutular için piksel ızgarasının genişliği (varsayılan: 1024). | INT | Evet | 64 ila 16384 (adım: 16) |
| `yükseklik` | Tuvalin ve sınırlayıcı kutular için piksel ızgarasının yüksekliği (varsayılan: 1024). | INT | Evet | 64 ila 16384 (adım: 16) |
| `düzenleyici durumu` | Sınırlayıcı kutular çizin ve her kutunun türünü, metnini, açıklamasını, renk paletini ayarlayın. Arka plan öğesiyle başlayın ve ön planla bitirin. | BOUNDING_BOXES | Evet | - |
| `last_incoming` | Tuval tarafından yönetilen iç durum: tuvale en son başlatan yukarı akış bboxes değeri. Bir sonraki çalıştırmada tuvale bboxes girişinden yeniden başlatmak için boş bırakın. | BOUNDING_BOXES | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `önizleme` | Etiketler, renk paleti örnekleri ve açıklayıcı metinler dahil olmak üzere tüm sınırlayıcı kutuların işlenmiş olduğu tuvale ait bir RGB görüntüsü. | IMAGE |
| `sınır kutuları` | Her bir kutu için x, y, genişlik ve yükseklik değerlerini içeren, piksel koordinatlarında bir sınırlayıcı kutu listesi. | BOUNDING_BOX |
| `öğeler` | Her biri tür, sınırlayıcı kutu koordinatları (normalleştirilmiş 0-1000), metin (metin türü için), açıklama ve renk paleti içeren yapılandırılmış bir öğe nesneleri dizisi. | ARRAY |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateBoundingBoxes/tr.md)

---
**Source fingerprint (SHA-256):** `dc5545dffefdccf14f3919ff4d9966dbfd1a497dcd64e1863556d5728659ee94`
