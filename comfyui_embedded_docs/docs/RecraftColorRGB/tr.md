# Recraft Renk RGB

Kırmızı, yeşil ve mavi değerlerini ayrı ayrı belirterek bir Recraft rengi oluşturun. Bu düğüm, RGB tamsayı değerlerini (0-255) alır ve bunları diğer Recraft işlemlerinde kullanılabilecek bir Recraft rengi biçimine dönüştürür. İsteğe bağlı olarak, mevcut bir Recraft renk zincirini yeni renkle genişletmek için de sağlayabilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `k` | Rengin kırmızı değeri (varsayılan: 0) | INT | Evet | 0-255 |
| `y` | Rengin yeşil değeri (varsayılan: 0) | INT | Evet | 0-255 |
| `m` | Rengin mavi değeri (varsayılan: 0) | INT | Evet | 0-255 |
| `recraft_rengi` | Yeni RGB rengiyle genişletilecek isteğe bağlı mevcut Recraft renk zinciri | COLOR | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `recraft_rengi` | Belirtilen RGB değerlerini içeren oluşturulmuş Recraft renk nesnesi veya mevcut bir renk zinciri sağlanmışsa genişletilmiş renk zinciri | COLOR |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftColorRGB/tr.md)

---
**Source fingerprint (SHA-256):** `8c3503632d085fa4c1771f92f17008b7b051e9604d9e7d1e7d352cbbbd22dddc`
