# İçBoyaModelKoşullandırma

InpaintModelConditioning düğümü, rötuş (inpainting) modelleri için koşullandırma sürecini kolaylaştırmak, çeşitli koşullandırma girdilerinin entegrasyonunu ve manipülasyonunu sağlayarak rötuş çıktısını özelleştirmek üzere tasarlanmıştır. Belirli model kontrol noktalarını yükleme, stil veya kontrol ağı modelleri uygulama ile koşullandırma öğelerini kodlama ve birleştirme gibi geniş bir işlev yelpazesini kapsar; böylece rötuş görevlerini özelleştirmek için kapsamlı bir araç görevi görür.

## Girdiler

| Parametre | Açıklama | Comfy Veri Türü |
| --- | --- | --- |
| `pozitif` | Rötuş modeline uygulanacak pozitif koşullandırma bilgisini veya parametrelerini temsil eder. Bu girdi, rötuş işleminin gerçekleştirilmesi gereken bağlamı veya kısıtlamaları tanımlamak için çok önemlidir ve nihai çıktıyı önemli ölçüde etkiler. | `CONDITIONING` |
| `negatif` | Rötuş modeline uygulanacak negatif koşullandırma bilgisini veya parametrelerini temsil eder. Bu girdi, rötuş işlemi sırasında kaçınılması gereken koşulları veya bağlamları belirtmek için gereklidir ve böylece nihai çıktıyı etkiler. | `CONDITIONING` |
| `vae` | Koşullandırma sürecinde kullanılacak VAE modelini belirtir. Bu girdi, kullanılacak VAE modelinin belirli mimarisini ve parametrelerini belirlemek için çok önemlidir. | `VAE` |
| `pikseller` | Rötuş yapılacak görüntünün piksel verilerini temsil eder. Bu girdi, rötuş görevi için gerekli görsel bağlamı sağlamak açısından gereklidir. | `IMAGE` |
| `maske` | Görüntüye uygulanacak ve rötuş yapılacak alanları gösteren maskeyi belirtir. Bu girdi, görüntü içinde rötuş gerektiren belirli bölgeleri tanımlamak için çok önemlidir. | `MASK` |


| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | İşlem sonrası değiştirilmiş pozitif koşullandırma bilgisi, rötuş modeline uygulanmaya hazırdır. Bu çıktı, rötuş sürecini belirtilen pozitif koşullara göre yönlendirmek için gereklidir. | `CONDITIONING` |
| `negative` | İşlem sonrası değiştirilmiş negatif koşullandırma bilgisi, rötuş modeline uygulanmaya hazırdır. Bu çıktı, rötuş sürecini belirtilen negatif koşullara göre yönlendirmek için gereklidir. | `CONDITIONING` |
| `latent` | Koşullandırma sürecinden elde edilen gizli (latent) temsildir. Bu çıktı, rötuş yapılan görüntünün temel özelliklerini ve karakteristiklerini anlamak için çok önemlidir. | `LATENT` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InpaintModelConditioning/tr.md)
