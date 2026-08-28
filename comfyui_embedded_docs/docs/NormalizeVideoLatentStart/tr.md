# NormalizeVideoLatentStart

Bu düğüm, bir video latentinin ilk birkaç karesini, kendilerinden sonra gelen karelere daha çok benzeyecek şekilde ayarlar. Videodaki daha sonraki bir dizi referans karesinden ortalama ve varyasyonu hesaplar ve aynı özellikleri başlangıç karelerine uygular. Bu, videonun başında daha yumuşak ve daha tutarlı bir görsel geçiş oluşturmaya yardımcı olur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `latent` | İşlenecek video latent gösterimi. | LATENT | Evet | - |
| `start_frame_count` | Baştan itibaren sayılan, normalleştirilecek latent kare sayısı (varsayılan: 4). | INT | Evet | 1 ile 16384 (max resolution) |
| `reference_frame_count` | Başlangıç karelerinden sonra referans olarak kullanılacak latent kare sayısı (varsayılan: 5). | INT | Evet | 1 ile 16384 (max resolution) |

**Not:** `reference_frame_count`, başlangıç karelerinden sonra mevcut olan kare sayısıyla otomatik olarak sınırlandırılır. Video latenti yalnızca 1 kare uzunluğundaysa hiçbir normalizasyon yapılmaz ve orijinal latent değiştirilmeden döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Başlangıç kareleri normalleştirilmiş, işlenmiş video latent gösterimi. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/tr.md)

---
**Source fingerprint (SHA-256):** `383e5a19ee4cd8bdea5983567ddbdc30bb09c373142a1a934cea985f1b9d1b0d`
