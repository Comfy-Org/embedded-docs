# Sınır Kutuları Oluştur

Bu düğüm, bir görüntüdeki nesnelerin veya metin bölgelerinin etrafına sınırlayıcı kutular çizmek için bir tuval arayüzü sağlar. Sınırlayıcı kutu koordinatlarını piksel cinsinden, Ideogram istem biçimlendirmesiyle uyumlu yapılandırılmış öğe verilerini ve çizilen kutuları etiketler ve renk paletleriyle gösteren bir önizleme görüntüsünü çıktı olarak verir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `arka plan` | Tuval ve önizlemede arka plan olarak kullanılan isteğe bağlı görüntü. | IMAGE | Hayır | - |
| `bboxes` | Kanvası başlatmak için sınırlayıcı kutular, öğeler veya bir JSON dizesi. Yeni bir yukarı akış değeri kanvası başlatır; kanvas üzerinde yapılan düzenlemeler önceliklidir ve yukarı akış değeri tekrar değişene kadar korunur. | BOUNDING_BOX, ARRAY, STRING | Hayır | - |
| `genişlik` | Tuvalin ve sınırlayıcı kutular için piksel ızgarasının genişliği (varsayılan: 1024). | INT | Evet | 64 ile 16384 arası (adım: 16) |
| `yükseklik` | Tuvalin ve sınırlayıcı kutular için piksel ızgarasının yüksekliği (varsayılan: 1024). | INT | Evet | 64 ile 16384 arası (adım: 16) |
| `düzenleyici durumu` | Sınırlayıcı kutular çizin ve her kutunun türünü, metnini, açıklamasını, renk paletini ayarlayın. Önce arka plan öğesiyle, en son ön planla başlayın. | BOUNDING_BOXES | Evet | - |
| `last_incoming` | Kanvas tarafından yönetilen iç durum: kanvası en son başlatan yukarı akış bboxes değeri. Bir sonraki çalıştırmada kanvası bboxes girişinden yeniden başlatmak için boş bırakın. | BOUNDING_BOXES | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `önizleme` | Etiketler, renk paleti örnekleri ve açıklayıcı metinler dahil olmak üzere, işlenmiş tüm sınırlayıcı kutuları gösteren bir RGB görüntüsü. | IMAGE |
| `sınır kutuları` | Her biri x, y, genişlik ve yükseklik değerlerini içeren, piksel koordinatlarındaki sınırlayıcı kutuların listesi. | BOUNDING_BOX |
| `öğeler` | Her biri tür, sınırlayıcı kutu koordinatları (normalleştirilmiş 0-1000), metin (metin türü için), açıklama ve renk paleti içeren yapılandırılmış bir öğe nesneleri dizisi. | ARRAY |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateBoundingBoxes/tr.md)

---
**Source fingerprint (SHA-256):** `dc5545dffefdccf14f3919ff4d9966dbfd1a497dcd64e1863556d5728659ee94`
