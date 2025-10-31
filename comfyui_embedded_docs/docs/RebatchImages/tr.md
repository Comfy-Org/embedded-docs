> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchImages/tr.md)

RebatchImages düğümü, bir grup görseli yeni bir grup konfigürasyonuna göre yeniden düzenlemek ve belirtilen şekilde grup boyutunu ayarlamak için tasarlanmıştır. Bu işlem, grup işlemlerinde görsel verilerin işlenmesini yönetmek ve optimize etmek için gereklidir; görsellerin verimli bir şekilde işlenmesi için istenen grup boyutuna göre düzenlenmesini sağlar.

## Girdiler

| Alan        | Veri Türü | Açıklama                                                                         |
|-------------|-------------|-------------------------------------------------------------------------------------|
| `images`    | `IMAGE`     | Yeniden gruplandırılacak görsellerin listesi. Bu parametre, yeniden gruplandırma işlemine tabi tutulacak girdi verilerini belirlemek için çok önemlidir. |
| `batch_size`| `INT`       | Çıktı gruplarının istenen boyutunu belirtir. Bu parametre, girdi görsellerinin nasıl gruplandırılıp işlendiğini doğrudan etkileyerek çıktının yapısını etkiler. |

## Çıktılar

| Alan   | Veri Türü | Açıklama                                                                   |
|--------|-------------|-------------------------------------------------------------------------------|
| `image`| `IMAGE`     | Çıktı, belirtilen grup boyutuna göre yeniden düzenlenmiş bir görsel grubu listesinden oluşur. Bu, görsel verilerin grup işlemlerinde esnek ve verimli bir şekilde işlenmesine olanak tanır. |