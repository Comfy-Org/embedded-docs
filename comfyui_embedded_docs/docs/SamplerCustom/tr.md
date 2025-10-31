> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustom/tr.md)

SamplerCustom düğümü, çeşitli uygulamalar için esnek ve özelleştirilebilir bir örnekleme mekanizması sağlamak üzere tasarlanmıştır. Kullanıcıların, örnekleme sürecinin uyarlanabilirliğini ve verimliliğini artıran, kendi özel ihtiyaçlarına uygun farklı örnekleme stratejilerini seçmesine ve yapılandırmasına olanak tanır.

## Girdiler

| Parametre | Veri Tipi | Açıklama |
|-----------|-----------|-------------|
| `model`   | `MODEL`   | 'model' girdi tipi, örnekleme için kullanılacak modeli belirtir ve örnekleme davranışını ile çıktısını belirlemede kritik bir rol oynar. |
| `add_noise` | `BOOLEAN` | 'add_noise' girdi tipi, örnekleme sürecine gürültü eklenip eklenmeyeceğini belirlemeye olanak tanır; bu, üretilen örneklerin çeşitliliğini ve özelliklerini etkiler. |
| `noise_seed` | `INT`     | 'noise_seed' girdi tipi, gürültü üretimi için bir tohum değeri sağlar ve gürültü eklenirken örnekleme sürecinde tekrarlanabilirliği ve tutarlılığı garanti eder. |
| `cfg`     | `FLOAT`   | 'cfg' girdi tipi, örnekleme süreci için yapılandırmayı ayarlar ve örnekleme parametrelerinin ile davranışının ince ayar yapılmasına olanak tanır. |
| `positive` | `CONDITIONING` | 'positive' girdi tipi, olumlu koşullandırma bilgisini temsil eder ve örnekleme sürecini, belirtilen olumlu niteliklerle uyumlu örnekler üretmeye yönlendirir. |
| `negative` | `CONDITIONING` | 'negative' girdi tipi, olumsuz koşullandırma bilgisini temsil eder ve örnekleme sürecini, belirtilen olumsuz nitelikleri sergileyen örnekler üretmekten uzaklaştırır. |
| `sampler` | `SAMPLER` | 'sampler' girdi tipi, kullanılacak belirli örnekleme stratejisini seçer ve üretilen örneklerin doğasını ile kalitesini doğrudan etkiler. |
| `sigmas`  | `SIGMAS`  | 'sigmas' girdi tipi, örnekleme sürecinde kullanılacak gürültü seviyelerini tanımlar ve örnek uzayının keşfedilmesini ile çıktının çeşitliliğini etkiler. |
| `latent_image` | `LATENT` | 'latent_image' girdi tipi, örnekleme süreci için bir başlangıç gizli (latent) görüntüsü sağlar ve örnek üretimi için bir başlangıç noktası görevi görür. |

## Çıktılar

| Parametre | Veri Tipi | Açıklama |
|-----------|-----------|-------------|
| `output`  | `LATENT`  | 'output', örnekleme sürecinin birincil sonucunu temsil eder ve üretilen örnekleri içerir. |
| `denoised_output` | `LATENT` | 'denoised_output', bir gürültü giderme işlemi uygulandıktan sonraki örnekleri temsil eder ve üretilen örneklerin netliğini ile kalitesini potansiyel olarak artırır. |