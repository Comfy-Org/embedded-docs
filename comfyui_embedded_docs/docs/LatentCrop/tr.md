# Gizli Değişkeni Kırp

LatentCrop düğümü, görüntülerin gizli (latent) temsilleri üzerinde kırpma işlemleri gerçekleştirmek için tasarlanmıştır. Kırpma boyutlarının ve konumunun belirtilmesine olanak tanıyarak, gizli uzayda hedefli değişiklikler yapılmasını sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `örnekler` | 'samples' parametresi, kırpılacak gizli temsilleri temsil eder. Kırpma işleminin gerçekleştirileceği veriyi tanımlamak için kritik öneme sahiptir. | `LATENT` |
| `genişlik` | Kırpma alanının genişliğini belirtir. Çıktı gizli temsilinin boyutlarını doğrudan etkiler. | `INT` |
| `yükseklik` | Kırpma alanının yüksekliğini belirtir. Ortaya çıkan kırpılmış gizli temsilin boyutunu etkiler. | `INT` |
| `x` | Kırpma alanının başlangıç x koordinatını belirler. Kırpmanın orijinal gizli temsil içindeki konumunu etkiler. | `INT` |
| `y` | Kırpma alanının başlangıç y koordinatını belirler. Kırpmanın orijinal gizli temsil içindeki konumunu ayarlar. | `INT` |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Çıktı, belirtilen kırpma işleminin uygulandığı değiştirilmiş bir gizli temsildir. | `LATENT` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCrop/tr.md)
