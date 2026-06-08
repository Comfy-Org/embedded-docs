ReplaceVideoLatentFrames düğümü, kaynak bir latent videodaki kareleri, hedef latent videoya belirtilen bir kare indeksinden başlayarak ekler. Kaynak latent sağlanmazsa, hedef latent değiştirilmeden döndürülür. Düğüm, negatif indekslemeyi işler ve kaynak kareler hedefe sığmazsa bir uyarı verir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `destination` | Karelerin değiştirileceği hedef latent. | LATENT | Evet | - |
| `source` | Hedef latente eklenecek kareleri sağlayan kaynak latent. Sağlanmazsa, hedef latent değiştirilmeden döndürülür. | LATENT | Hayır | - |
| `index` | Kaynak latent karelerinin hedef latente yerleştirileceği başlangıç latent kare indeksi. Negatif değerler sondan itibaren sayar (varsayılan: 0). | INT | Evet | -MAX_RESOLUTION ile MAX_RESOLUTION arası |

**Kısıtlamalar:**

* `index`, hedef latentin kare sayısı sınırları içinde olmalıdır. Değilse, bir uyarı kaydedilir ve hedef latent değiştirilmeden döndürülür.
* Kaynak latent kareleri, belirtilen `index`'ten başlayarak hedef latent karelerine sığmalıdır. Sığmazlarsa, bir uyarı kaydedilir ve hedef latent değiştirilmeden döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Kare değiştirme işleminden sonra elde edilen latent video. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/tr.md)

---
**Source fingerprint (SHA-256):** `b4e2b3dcdaa5c400fefc30262ae05cd1849896e6cb6bbb3a1bd6ce4d31583e23`
