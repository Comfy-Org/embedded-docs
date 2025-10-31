> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCrop/tr.md)

LatentCrop düğümü, görüntülerin gizli temsilleri üzerinde kırpma işlemleri gerçekleştirmek için tasarlanmıştır. Kırpma boyutlarının ve konumunun belirlenmesine olanak tanıyarak, gizli uzayda hedeflenmiş değişiklikler yapılmasını sağlar.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | 'samples' parametresi, kırpılacak olan gizli temsilleri ifade eder. Kırpma işleminin gerçekleştirileceği veriyi tanımlamak için çok önemlidir. |
| `width`   | `INT`       | Kırpma alanının genişliğini belirtir. Çıktı gizli temsilinin boyutlarını doğrudan etkiler. |
| `height`  | `INT`       | Kırpma alanının yüksekliğini belirterek, ortaya çıkan kırpılmış gizli temsilin boyutunu etkiler. |
| `x`       | `INT`       | Kırpma alanının başlangıç x-koordinatını belirler ve kırpma işleminin orijinal gizli temsil içindeki konumunu etkiler. |
| `y`       | `INT`       | Kırpma alanının başlangıç y-koordinatını belirleyerek, kırpma işleminin orijinal gizli temsil içindeki konumunu ayarlar. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Çıktı, belirtilen kırpma işleminin uygulandığı değiştirilmiş bir gizli temsildir. |