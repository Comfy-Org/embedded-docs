> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftColorRGB/tr.md)

Kırmızı, yeşil ve mavi değerlerini ayrı ayrı belirterek bir Recraft rengi oluşturun. Bu düğüm, RGB tamsayı değerlerini (0-255) alır ve bunları diğer Recraft işlemlerinde kullanılabilecek bir Recraft rengi biçimine dönüştürür. İsteğe bağlı olarak, mevcut bir Recraft renk zincirini yeni renkle genişletmek için de sağlayabilirsiniz.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `k` | INT | Evet | 0-255 | Rengin kırmızı değeri (varsayılan: 0) |
| `y` | INT | Evet | 0-255 | Rengin yeşil değeri (varsayılan: 0) |
| `m` | INT | Evet | 0-255 | Rengin mavi değeri (varsayılan: 0) |
| `recraft_rengi` | COLOR | Hayır | - | Yeni RGB rengiyle genişletilecek isteğe bağlı mevcut Recraft renk zinciri |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `recraft_rengi` | COLOR | Belirtilen RGB değerlerini içeren oluşturulmuş Recraft renk nesnesi veya mevcut bir renk zinciri sağlanmışsa genişletilmiş renk zinciri |

---
**Source fingerprint (SHA-256):** `8c3503632d085fa4c1771f92f17008b7b051e9604d9e7d1e7d352cbbbd22dddc`
