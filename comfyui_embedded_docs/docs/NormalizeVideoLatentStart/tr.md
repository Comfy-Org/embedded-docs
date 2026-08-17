# NormalizeVideoLatentStart

Bu düğüm, bir video latentinin ilk birkaç karesini, sonraki karelere daha çok benzeyecek şekilde ayarlar. Videodaki daha sonraki bir dizi referans kareden ortalama ve varyasyonu hesaplar ve aynı özellikleri başlangıç karelerine uygular. Bu, bir videonun başında daha yumuşak ve daha tutarlı bir görsel geçiş oluşturmaya yardımcı olur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `latent` | İşlenecek video latent temsili. | LATENT | Evet | - |
| `start_frame_count` | Başlangıçtan itibaren normalize edilecek latent kare sayısı (varsayılan: 4). | INT | Evet | 1 ila 16384 (maksimum çözünürlük) |
| `reference_frame_count` | Başlangıç karelerinden sonra referans olarak kullanılacak latent kare sayısı (varsayılan: 5). | INT | Evet | 1 ila 16384 (maksimum çözünürlük) |

**Not:** `reference_frame_count` otomatik olarak başlangıç karelerinden sonra kullanılabilir kare sayısıyla sınırlandırılır. Video latent yalnızca 1 kare uzunluğundaysa, normalizasyon yapılmaz ve orijinal latent değiştirilmeden döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Başlangıç kareleri normalize edilmiş işlenmiş video latent. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/tr.md)

---
**Source fingerprint (SHA-256):** `383e5a19ee4cd8bdea5983567ddbdc30bb09c373142a1a934cea985f1b9d1b0d`
