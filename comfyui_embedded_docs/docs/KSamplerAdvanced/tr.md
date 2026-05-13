> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerAdvanced/tr.md)

KSamplerAdvanced düğümü, gelişmiş yapılandırmalar ve teknikler sunarak örnekleme sürecini iyileştirmek için tasarlanmıştır. Temel KSampler işlevlerine kıyasla, bir modelden örnekler üretmek için daha sofistike seçenekler sunmayı amaçlar.

## Girişler

| Parametre | Veri Türü | Açıklama |
|----------------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `model` | MODEL | Örneklerin oluşturulacağı modeli belirtir; örnekleme sürecinde kritik bir rol oynar. |
| `add_noise` | COMBO[STRING] | Örnekleme sürecine gürültü eklenip eklenmeyeceğini belirler; oluşturulan örneklerin çeşitliliğini ve kalitesini etkiler. |
| `noise_seed` | INT | Gürültü oluşturma için tohum değerini ayarlar; örnekleme sürecinde tekrarlanabilirliği sağlar. |
| `steps` | INT | Örnekleme sürecinde atılacak adım sayısını tanımlar; çıktının detayını ve kalitesini etkiler. |
| `cfg` | FLOAT | Koşullandırma faktörünü kontrol eder; örnekleme sürecinin yönünü ve alanını etkiler. |
| `sampler_name` | COMBO[STRING] | Kullanılacak belirli örnekleyiciyi seçer; örnekleme tekniğinin özelleştirilmesine olanak tanır. |
| `scheduler` | COMBO[STRING] | Örnekleme sürecini kontrol etmek için zamanlayıcıyı seçer; örneklerin ilerlemesini ve kalitesini etkiler. |
| `positive` | CONDITIONING | Örneklemeyi istenen niteliklere yönlendirmek için pozitif koşullandırmayı belirtir. |
| `negative` | CONDITIONING | Örneklemeyi belirli niteliklerden uzaklaştırmak için negatif koşullandırmayı belirtir. |
| `latent_image` | LATENT | Örnekleme sürecinde kullanılacak başlangıç gizli görüntüsünü sağlar; bir başlangıç noktası görevi görür. |
| `start_at_step` | INT | Örnekleme sürecinin başlangıç adımını belirler; örnekleme ilerlemesi üzerinde kontrol sağlar. |
| `end_at_step` | INT | Örnekleme sürecinin bitiş adımını ayarlar; örneklemenin kapsamını tanımlar. |
| `return_with_leftover_noise` | COMBO[STRING] | Örneğin artık gürültüyle birlikte döndürülüp döndürülmeyeceğini belirtir; nihai çıktının görünümünü etkiler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-------------|-------------|------------------------------------------------------------------------------------------------------------------------------|
| `latent` | LATENT | Çıktı, uygulanan yapılandırmaları ve teknikleri yansıtarak modelden oluşturulan gizli görüntüyü temsil eder. |