> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustom/tr.md)

SamplerCustom düğümü, çeşitli uygulamalar için esnek ve özelleştirilebilir bir örnekleme mekanizması sağlamak üzere tasarlanmıştır. Kullanıcıların kendi özel ihtiyaçlarına göre farklı örnekleme stratejileri seçmesine ve yapılandırmasına olanak tanıyarak örnekleme sürecinin uyarlanabilirliğini ve verimliliğini artırır.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|--------------|-------------|
| `model`   | `MODEL`      | 'model' giriş türü, örnekleme için kullanılacak modeli belirtir ve örnekleme davranışı ile çıktısının belirlenmesinde önemli bir rol oynar. |
| `add_noise` | `BOOLEAN`    | 'add_noise' giriş türü, kullanıcıların örnekleme sürecine gürültü eklenip eklenmeyeceğini belirlemesine olanak tanır ve üretilen örneklerin çeşitliliğini ve özelliklerini etkiler. |
| `noise_seed` | `INT`        | 'noise_seed' giriş türü, gürültü üretimi için bir tohum değeri sağlayarak, gürültü eklendiğinde örnekleme sürecinde tekrarlanabilirlik ve tutarlılık sağlar. |
| `cfg`     | `FLOAT`      | 'cfg' giriş türü, örnekleme süreci için yapılandırmayı ayarlayarak örnekleme parametrelerinin ve davranışının ince ayarının yapılmasına olanak tanır. |
| `positive` | `CONDITIONING` | 'positive' giriş türü, olumlu koşullandırma bilgisini temsil eder ve örnekleme sürecini belirtilen olumlu niteliklerle uyumlu örnekler üretmeye yönlendirir. |
| `negative` | `CONDITIONING` | 'negative' giriş türü, olumsuz koşullandırma bilgisini temsil eder ve örnekleme sürecini belirtilen olumsuz nitelikleri sergileyen örnekler üretmekten uzaklaştırır. |
| `sampler` | `SAMPLER`    | 'sampler' giriş türü, kullanılacak belirli örnekleme stratejisini seçer ve üretilen örneklerin doğasını ve kalitesini doğrudan etkiler. |
| `sigmas`  | `SIGMAS`     | 'sigmas' giriş türü, örnekleme sürecinde kullanılacak gürültü seviyelerini tanımlar ve örnek uzayının keşfini ile çıktının çeşitliliğini etkiler. |
| `latent_image` | `LATENT` | 'latent_image' giriş türü, örnekleme süreci için bir başlangıç gizli görüntüsü sağlar ve örnek üretimi için bir başlangıç noktası görevi görür. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|--------------|-------------|
| `output`  | `LATENT`     | 'output', örnekleme sürecinin birincil sonucunu temsil eder ve üretilen örnekleri içerir. |
| `denoised_output` | `LATENT` | 'denoised_output', bir gürültü giderme işlemi uygulandıktan sonraki örnekleri temsil eder ve potansiyel olarak üretilen örneklerin netliğini ve kalitesini artırır. |