# ÖzelÖrnekleyici

SamplerCustom düğümü, çeşitli uygulamalar için esnek ve özelleştirilebilir bir örnekleme mekanizması sağlamak üzere tasarlanmıştır. Kullanıcıların kendi özel ihtiyaçlarına göre farklı örnekleme stratejileri seçmesine ve yapılandırmasına olanak tanıyarak örnekleme sürecinin uyarlanabilirliğini ve verimliliğini artırır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | 'model' giriş türü, örnekleme için kullanılacak modeli belirtir ve örnekleme davranışı ile çıktısının belirlenmesinde önemli bir rol oynar. | `MODEL` |
| `gürültü_ekle` | 'add_noise' giriş türü, kullanıcıların örnekleme sürecine gürültü eklenip eklenmeyeceğini belirlemesine olanak tanır ve üretilen örneklerin çeşitliliğini ve özelliklerini etkiler. | `BOOLEAN` |
| `gürültü_tohumu` | 'noise_seed' giriş türü, gürültü üretimi için bir tohum değeri sağlayarak, gürültü eklendiğinde örnekleme sürecinde tekrarlanabilirlik ve tutarlılık sağlar. | `INT` |
| `cfg` | 'cfg' giriş türü, örnekleme süreci için yapılandırmayı ayarlayarak örnekleme parametrelerinin ve davranışının ince ayarının yapılmasına olanak tanır. | `FLOAT` |
| `pozitif` | 'positive' giriş türü, olumlu koşullandırma bilgisini temsil eder ve örnekleme sürecini belirtilen olumlu niteliklerle uyumlu örnekler üretmeye yönlendirir. | `CONDITIONING` |
| `negatif` | 'negative' giriş türü, olumsuz koşullandırma bilgisini temsil eder ve örnekleme sürecini belirtilen olumsuz nitelikleri sergileyen örnekler üretmekten uzaklaştırır. | `CONDITIONING` |
| `örnekleyici` | 'sampler' giriş türü, kullanılacak belirli örnekleme stratejisini seçer ve üretilen örneklerin doğasını ve kalitesini doğrudan etkiler. | `SAMPLER` |
| `sigmalar` | 'sigmas' giriş türü, örnekleme sürecinde kullanılacak gürültü seviyelerini tanımlar ve örnek uzayının keşfini ile çıktının çeşitliliğini etkiler. | `SIGMAS` |
| `gizli_görüntü` | 'latent_image' giriş türü, örnekleme süreci için bir başlangıç gizli görüntüsü sağlar ve örnek üretimi için bir başlangıç noktası görevi görür. | `LATENT` |


| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | 'output', örnekleme sürecinin birincil sonucunu temsil eder ve üretilen örnekleri içerir. | `LATENT` |
| `denoised_output` | 'denoised_output', bir gürültü giderme işlemi uygulandıktan sonraki örnekleri temsil eder ve potansiyel olarak üretilen örneklerin netliğini ve kalitesini artırır. | `LATENT` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustom/tr.md)
