# ReplaceVideoLatentFrames

ReplaceVideoLatentFrames düğümü, kaynak latent videodaki kareleri, belirtilen bir kare indeksinden başlayarak hedef latent videoya ekler. Kaynak latent sağlanmazsa, hedef latent değiştirilmeden döndürülür. Düğüm negatif indekslemeyi destekler ve kaynak kareler hedefe sığmazsa bir uyarı verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `destination` | Karelerin değiştirileceği hedef latent. | LATENT | Evet | - |
| `source` | Hedef latente eklenecek kareleri sağlayan kaynak latent. Sağlanmazsa, hedef latent değiştirilmeden döndürülür. | LATENT | Hayır | - |
| `index` | Kaynak latent karelerinin yerleştirileceği hedef latentteki başlangıç latent kare indeksi. Negatif değerler sondan sayar (varsayılan: 0). | INT | Evet | -MAX_RESOLUTION ile MAX_RESOLUTION (adım: 1) |

**Kısıtlamalar:**

* `index`, hedef latentin kare sayısının sınırları içinde olmalıdır. Değilse, bir uyarı kaydedilir ve hedef değiştirilmeden döndürülür.
* Kaynak latent kareleri, belirtilen `index`'ten başlayarak hedef latent karelerine sığmalıdır. Sığmazsa, bir uyarı kaydedilir ve hedef değiştirilmeden döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Kare değiştirme işleminden sonra ortaya çıkan latent video. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/tr.md)

---
**Source fingerprint (SHA-256):** `5b98d875bdeaec63521bff19fecbc5510036c8b4f90322d8296b216688b557bf`
