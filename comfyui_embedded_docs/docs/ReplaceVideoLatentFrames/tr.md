# ReplaceVideoLatentFrames

ReplaceVideoLatentFrames, hedef latent videodaki bir kare aralığını, kaynak latent videodaki karelerle, belirtilen bir kare indeksinden başlayarak değiştirir. Kaynak latent sağlanmazsa, hedef latent değiştirilmeden döndürülür. Düğüm negatif indeksleri destekler ve kaynak kareler hedefe sığmadığında bir uyarı günlüğe kaydeder.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `destination` | Karelerin değiştirileceği hedef latent. | LATENT | Evet | - |
| `source` | Hedef latente eklenecek kareleri sağlayan kaynak latent. Sağlanmazsa, hedef latent değiştirilmeden döndürülür. | LATENT | Hayır | - |
| `index` | Kaynak latent karelerinin hedef latente yerleştirileceği hedef latentteki başlangıç kare indeksi. Negatif değerler sondan sayar (varsayılan: 0). | INT | Evet | -MAX_RESOLUTION to MAX_RESOLUTION |

**Kısıtlamalar:**

* Negatif bir `index`, hedef kare sayısına eklenerek ayarlanır; böylece hedef latenin sonundan geriye doğru sayar.
* `index` hedef kare sayısının ötesine işaret ediyorsa veya kaynak kareler `index`'ten başlayarak hedefe sığmıyorsa, bir uyarı günlüğe kaydedilir ve hedef latent değiştirilmeden döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Kare değiştirme işlemi sonrasında elde edilen latent video. Değiştirme gerçekleştirilemezse, hedef latent değiştirilmeden döndürülür. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/tr.md)

---
**Source fingerprint (SHA-256):** `5b98d875bdeaec63521bff19fecbc5510036c8b4f90322d8296b216688b557bf`
