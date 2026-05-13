> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SvdImg2vidConditioning/tr.md)

Bu düğüm, video oluşturma görevleri için koşullandırma verileri üretmek üzere tasarlanmıştır ve özellikle SVD_img2vid modelleriyle kullanılmak üzere uyarlanmıştır. Başlangıç görüntüleri, video parametreleri ve bir VAE modeli dahil olmak üzere çeşitli girdiler alarak, video karelerinin oluşturulmasını yönlendirmek için kullanılabilecek koşullandırma verileri üretir.

## Girdiler

| Parametre            | Comfy dtype        | Açıklama |
|----------------------|--------------------|-------------|
| `clip_vision`         | `CLIP_VISION`      | Başlangıç görüntüsünden görsel özellikleri kodlamak için kullanılan CLIP görme modelini temsil eder; video oluşturma için görüntünün içeriğini ve bağlamını anlamada çok önemli bir rol oynar. |
| `init_image`          | `IMAGE`            | Videonun oluşturulacağı başlangıç görüntüsüdür ve video oluşturma süreci için başlangıç noktası görevi görür. |
| `vae`                 | `VAE`              | Başlangıç görüntüsünü bir gizli uzaya kodlamak için kullanılan bir Varyasyonel Otomatik Kodlayıcı (VAE) modelidir; tutarlı ve sürekli video karelerinin oluşturulmasını kolaylaştırır. |
| `width`               | `INT`              | Oluşturulacak video karelerinin istenen genişliğidir; videonun çözünürlüğünün özelleştirilmesine olanak tanır. |
| `height`              | `INT`              | Video karelerinin istenen yüksekliğidir; videonun en boy oranı ve çözünürlüğü üzerinde kontrol sağlar. |
| `video_frames`        | `INT`              | Video için oluşturulacak kare sayısını belirtir; videonun uzunluğunu belirler. |
| `motion_bucket_id`    | `INT`              | Video oluşturmada uygulanacak hareket türünü kategorize etmek için bir tanımlayıcıdır; dinamik ve ilgi çekici videoların oluşturulmasına yardımcı olur. |
| `fps`                 | `INT`              | Video için saniyedeki kare sayısıdır (fps); oluşturulan videonun akıcılığını ve gerçekçiliğini etkiler. |
| `augmentation_level`  | `FLOAT`            | Başlangıç görüntüsüne uygulanan büyütme seviyesini kontrol eden bir parametredir; oluşturulan video karelerinin çeşitliliğini ve değişkenliğini etkiler. |

## Çıktılar

| Parametre     | Comfy dtype        | Açıklama |
|---------------|--------------------|-------------|
| `positive`    | `CONDITIONING`     | Pozitif koşullandırma verileridir; video oluşturma sürecini istenen bir yönde yönlendirmek için kodlanmış özellikler ve parametrelerden oluşur. |
| `negative`    | `CONDITIONING`     | Negatif koşullandırma verileridir; pozitif koşullandırmaya bir zıtlık sağlar ve oluşturulan videoda belirli desenlerden veya özelliklerden kaçınmak için kullanılabilir. |
| `latent`      | `LATENT`           | Videonun her karesi için oluşturulan gizli temsillerdir; video oluşturma süreci için temel bir bileşen görevi görür. |