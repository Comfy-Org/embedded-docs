SetFirstSigma düğümü, bir sigma değerleri dizisini, dizideki ilk sigma değerini özel bir değerle değiştirerek değiştirir. Girdi olarak mevcut bir sigma dizisi ve yeni bir sigma değeri alır; ardından yalnızca ilk öğesi değiştirilmiş, diğer tüm sigma değerleri aynı kalmış yeni bir sigma dizisi döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `sigmalar` | Değiştirilecek sigma değerlerinin girdi dizisi | SIGMAS | Evet | - |
| `sigma` | Dizide ilk öğe olarak ayarlanacak yeni sigma değeri (varsayılan: 136,0) | FLOAT | Evet | 0,0 ile 20000,0 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmalar` | İlk öğesi özel sigma değeriyle değiştirilmiş, değiştirilmiş sigma dizisi | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/tr.md)

---
**Source fingerprint (SHA-256):** `2414acd7f3f42032c12bae2c581de4721f4c1daa912255fa0956caaa567291d5`
