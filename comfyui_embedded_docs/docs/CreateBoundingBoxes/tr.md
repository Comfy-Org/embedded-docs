# Sınır Kutuları Oluştur

Bu düğüm, bir görüntüdeki nesnelerin veya metin bölgelerinin etrafına sınırlayıcı kutular çizmek için bir tuval arayüzü sağlar. Sınırlayıcı kutu koordinatlarını piksel cinsinden, Ideogram istem biçimlendirmesiyle uyumlu yapılandırılmış öğe verilerini ve çizilen kutuları etiketler ve renk paletleriyle gösteren bir önizleme görüntüsünü çıktı olarak verir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `arka plan` | Tuval ve önizlemede arka plan olarak kullanılan isteğe bağlı görüntü. | IMAGE | Hayır | - |
| `genişlik` | Tuvalin ve sınırlayıcı kutular için piksel ızgarasının genişliği (varsayılan: 1024). | INT | Evet | 64 ile 16384 arası (adım: 16) |
| `yükseklik` | Tuvalin ve sınırlayıcı kutular için piksel ızgarasının yüksekliği (varsayılan: 1024). | INT | Evet | 64 ile 16384 arası (adım: 16) |
| `düzenleyici durumu` | Sınırlayıcı kutular çizin ve her kutunun türünü, metnini, açıklamasını, renk paletini ayarlayın. Önce arka plan öğesiyle, en son ön planla başlayın. | BOUNDING_BOXES | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `sınır kutuları` | Etiketler, renk paleti örnekleri ve açıklayıcı metinler dahil olmak üzere, işlenmiş tüm sınırlayıcı kutuları gösteren bir RGB görüntüsü. | IMAGE |
| `öğeler` | Her biri x, y, genişlik ve yükseklik değerlerini içeren, piksel koordinatlarındaki sınırlayıcı kutuların listesi. | BOUNDING_BOX |
| `elements` | Her biri tür, sınırlayıcı kutu koordinatları (normalleştirilmiş 0-1000), metin (metin türü için), açıklama ve renk paleti içeren yapılandırılmış bir öğe nesneleri dizisi. | ARRAY |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateBoundingBoxes/tr.md)

---
**Source fingerprint (SHA-256):** `a63939f13edc6c6507590a390dcd6d0a3321febb5831baab1655d9952228612c`
