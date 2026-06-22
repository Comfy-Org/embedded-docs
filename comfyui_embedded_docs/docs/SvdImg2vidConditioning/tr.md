# SvdImg2vidConditioning

Bu düğüm, video oluşturma görevleri için koşullandırma verileri üretmek üzere tasarlanmıştır ve özellikle SVD_img2vid modelleriyle kullanılmak üzere uyarlanmıştır. Başlangıç görüntüleri, video parametreleri ve bir VAE modeli dahil olmak üzere çeşitli girdiler alarak, video karelerinin oluşturulmasını yönlendirmek için kullanılabilecek koşullandırma verileri üretir.

## Girdiler

| Parametre | Açıklama | Comfy dtype |
| --- | --- | --- |
| `clip_vision` | Başlangıç görüntüsünden görsel özellikleri kodlamak için kullanılan CLIP görme modelini temsil eder; video oluşturma için görüntünün içeriğini ve bağlamını anlamada çok önemli bir rol oynar. | `CLIP_VISION` |
| `init_image` | Videonun oluşturulacağı başlangıç görüntüsüdür ve video oluşturma süreci için başlangıç noktası görevi görür. | `IMAGE` |
| `vae` | Başlangıç görüntüsünü bir gizli uzaya kodlamak için kullanılan bir Varyasyonel Otomatik Kodlayıcı (VAE) modelidir; tutarlı ve sürekli video karelerinin oluşturulmasını kolaylaştırır. | `VAE` |
| `width` | Oluşturulacak video karelerinin istenen genişliğidir; videonun çözünürlüğünün özelleştirilmesine olanak tanır. | `INT` |
| `height` | Video karelerinin istenen yüksekliğidir; videonun en boy oranı ve çözünürlüğü üzerinde kontrol sağlar. | `INT` |
| `video_frames` | Video için oluşturulacak kare sayısını belirtir; videonun uzunluğunu belirler. | `INT` |
| `motion_bucket_id` | Video oluşturmada uygulanacak hareket türünü kategorize etmek için bir tanımlayıcıdır; dinamik ve ilgi çekici videoların oluşturulmasına yardımcı olur. | `INT` |
| `fps` | Video için saniyedeki kare sayısıdır (fps); oluşturulan videonun akıcılığını ve gerçekçiliğini etkiler. | `INT` |
| `augmentation_level` | Başlangıç görüntüsüne uygulanan büyütme seviyesini kontrol eden bir parametredir; oluşturulan video karelerinin çeşitliliğini ve değişkenliğini etkiler. | `FLOAT` |

## Çıktılar

| Parametre | Açıklama | Comfy dtype |
| --- | --- | --- |
| `positive` | Pozitif koşullandırma verileridir; video oluşturma sürecini istenen bir yönde yönlendirmek için kodlanmış özellikler ve parametrelerden oluşur. | `CONDITIONING` |
| `negative` | Negatif koşullandırma verileridir; pozitif koşullandırmaya bir zıtlık sağlar ve oluşturulan videoda belirli desenlerden veya özelliklerden kaçınmak için kullanılabilir. | `CONDITIONING` |
| `latent` | Videonun her karesi için oluşturulan gizli temsillerdir; video oluşturma süreci için temel bir bileşen görevi görür. | `LATENT` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SvdImg2vidConditioning/tr.md)
