> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCrop/tr.md)

LatentCrop düğümü, görüntülerin gizli (latent) temsilleri üzerinde kırpma işlemleri gerçekleştirmek için tasarlanmıştır. Kırpma boyutlarının ve konumunun belirtilmesine olanak tanıyarak, gizli uzayda hedefli değişiklikler yapılmasını sağlar.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | 'samples' parametresi, kırpılacak gizli temsilleri temsil eder. Kırpma işleminin gerçekleştirileceği veriyi tanımlamak için kritik öneme sahiptir. |
| `width`   | `INT`       | Kırpma alanının genişliğini belirtir. Çıktı gizli temsilinin boyutlarını doğrudan etkiler. |
| `height`  | `INT`       | Kırpma alanının yüksekliğini belirtir. Ortaya çıkan kırpılmış gizli temsilin boyutunu etkiler. |
| `x`       | `INT`       | Kırpma alanının başlangıç x koordinatını belirler. Kırpmanın orijinal gizli temsil içindeki konumunu etkiler. |
| `y`       | `INT`       | Kırpma alanının başlangıç y koordinatını belirler. Kırpmanın orijinal gizli temsil içindeki konumunu ayarlar. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Çıktı, belirtilen kırpma işleminin uygulandığı değiştirilmiş bir gizli temsildir. |