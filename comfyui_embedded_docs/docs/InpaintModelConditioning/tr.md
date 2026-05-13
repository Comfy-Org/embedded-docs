> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InpaintModelConditioning/tr.md)

InpaintModelConditioning düğümü, rötuş (inpainting) modelleri için koşullandırma sürecini kolaylaştırmak, çeşitli koşullandırma girdilerinin entegrasyonunu ve manipülasyonunu sağlayarak rötuş çıktısını özelleştirmek üzere tasarlanmıştır. Belirli model kontrol noktalarını yükleme, stil veya kontrol ağı modelleri uygulama ile koşullandırma öğelerini kodlama ve birleştirme gibi geniş bir işlev yelpazesini kapsar; böylece rötuş görevlerini özelleştirmek için kapsamlı bir araç görevi görür.

## Girdiler

| Parametre | Comfy Veri Türü | Açıklama |
|-----------|-----------------|----------|
| `pozitif`| `CONDITIONING`  | Rötuş modeline uygulanacak pozitif koşullandırma bilgisini veya parametrelerini temsil eder. Bu girdi, rötuş işleminin gerçekleştirilmesi gereken bağlamı veya kısıtlamaları tanımlamak için çok önemlidir ve nihai çıktıyı önemli ölçüde etkiler. |
| `negatif`| `CONDITIONING`  | Rötuş modeline uygulanacak negatif koşullandırma bilgisini veya parametrelerini temsil eder. Bu girdi, rötuş işlemi sırasında kaçınılması gereken koşulları veya bağlamları belirtmek için gereklidir ve böylece nihai çıktıyı etkiler. |
| `vae`     | `VAE`           | Koşullandırma sürecinde kullanılacak VAE modelini belirtir. Bu girdi, kullanılacak VAE modelinin belirli mimarisini ve parametrelerini belirlemek için çok önemlidir. |
| `pikseller`  | `IMAGE`         | Rötuş yapılacak görüntünün piksel verilerini temsil eder. Bu girdi, rötuş görevi için gerekli görsel bağlamı sağlamak açısından gereklidir. |
| `maske`    | `MASK`          | Görüntüye uygulanacak ve rötuş yapılacak alanları gösteren maskeyi belirtir. Bu girdi, görüntü içinde rötuş gerektiren belirli bölgeleri tanımlamak için çok önemlidir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|--------------|----------|
| `negatif`| `CONDITIONING` | İşlem sonrası değiştirilmiş pozitif koşullandırma bilgisi, rötuş modeline uygulanmaya hazırdır. Bu çıktı, rötuş sürecini belirtilen pozitif koşullara göre yönlendirmek için gereklidir. |
| `gizli`| `CONDITIONING` | İşlem sonrası değiştirilmiş negatif koşullandırma bilgisi, rötuş modeline uygulanmaya hazırdır. Bu çıktı, rötuş sürecini belirtilen negatif koşullara göre yönlendirmek için gereklidir. |
| `latent`  | `LATENT`       | Koşullandırma sürecinden elde edilen gizli (latent) temsildir. Bu çıktı, rötuş yapılan görüntünün temel özelliklerini ve karakteristiklerini anlamak için çok önemlidir. |