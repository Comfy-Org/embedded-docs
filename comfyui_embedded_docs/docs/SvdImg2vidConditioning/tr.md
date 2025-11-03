> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SvdImg2vidConditioning/tr.md)

Bu düğüm, video üretimi görevleri için koşullandırma verileri oluşturmak üzere tasarlanmıştır ve özellikle SVD_img2vid modelleri ile kullanıma uyarlanmıştır. Başlangıç görüntüleri, video parametreleri ve bir VAE modeli de dahil olmak üzere çeşitli girdiler alır ve video karelerinin üretimine rehberlik etmek için kullanılabilecek koşullandırma verilerini üretir.

## Girdiler

| Parametre             | Comfy Veri Türü   | Açıklama |
|----------------------|--------------------|-------------|
| `clip_vision`         | `CLIP_VISION`      | Başlangıç görüntüsünden görsel özellikleri kodlamak için kullanılan CLIP görü modelini temsil eder; video üretimi için görüntünün içeriğini ve bağlamını anlamada çok önemli bir rol oynar. |
| `init_image`          | `IMAGE`            | Videoyu oluşturmak için kullanılacak başlangıç görüntüsüdür ve video üretim süreci için başlangıç noktası görevi görür. |
| `vae`                 | `VAE`              | Başlangıç görüntüsünü, tutarlı ve sürekli video kareleri oluşturmayı kolaylaştırmak için bir gizli uzaya (latent space) kodlamak üzere kullanılan bir Varyasyonel Otokodlayıcı (Variational Autoencoder - VAE) modelidir. |
| `width`               | `INT`              | Oluşturulacak video karelerinin istenen genişliğidir; videonun çözünürlüğünün özelleştirilmesine olanak tanır. |
| `height`              | `INT`              | Oluşturulacak video karelerinin istenen yüksekliğidir; videonun en-boy oranı ve çözünürlüğü üzerinde kontrol sağlar. |
| `video_frames`        | `INT`              | Video için oluşturulacak kare sayısını belirtir; videonun uzunluğunu belirler. |
| `motion_bucket_id`    | `INT`              | Video üretiminde uygulanacak hareket türünü kategorilere ayırmak için kullanılan bir tanımlayıcıdır; dinamik ve ilgi çekici videoların oluşturulmasına yardımcı olur. |
| `fps`                 | `INT`              | Video için saniye başına düşen kare (fps) oranıdır; oluşturulan videonun akıcılığını ve gerçekçiliğini etkiler. |
| `augmentation_level`  | `FLOAT`            | Başlangıç görüntüsüne uygulanan artırma (augmentation) seviyesini kontrol eden bir parametredir; oluşturulan video karelerinin çeşitliliğini ve değişkenliğini etkiler. |

## Çıktılar

| Parametre     | Comfy Veri Türü   | Açıklama |
|---------------|--------------------|-------------|
| `positive`    | `CONDITIONING`     | Pozitif koşullandırma verileridir; video üretim sürecini istenen yönde yönlendirmek için kodlanmış özellikler ve parametrelerden oluşur. |
| `negative`    | `CONDITIONING`     | Negatif koşullandırma verileridir; pozitif koşullandırmaya bir tezat oluşturur ve oluşturulan videoda belirli desenlerden veya özelliklerden kaçınmak için kullanılabilir. |
| `latent`      | `LATENT`           | Videodaki her bir kare için oluşturulan gizli temsillerdir (latent representations); video üretim süreci için temel bir bileşen görevi görür. |