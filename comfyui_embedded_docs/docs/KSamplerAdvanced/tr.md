> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerAdvanced/tr.md)

KSamplerAdvanced düğümü, gelişmiş yapılandırmalar ve teknikler sunarak örnekleme sürecini iyileştirmek için tasarlanmıştır. Temel KSampler işlevlerine kıyasla, bir modelden örnekler üretmek için daha sofistike seçenekler sunmayı amaçlar.

## Girişler

| Parametre | Veri Türü | Açıklama |
|----------------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `model` | MODEL | Örneklerin oluşturulacağı modeli belirtir; örnekleme sürecinde kritik bir rol oynar. |
| `gürültü_ekle` | COMBO[STRING] | Örnekleme sürecine gürültü eklenip eklenmeyeceğini belirler; oluşturulan örneklerin çeşitliliğini ve kalitesini etkiler. |
| `gürültü_tohumu` | INT | Gürültü oluşturma için tohum değerini ayarlar; örnekleme sürecinde tekrarlanabilirliği sağlar. |
| `adımlar` | INT | Örnekleme sürecinde atılacak adım sayısını tanımlar; çıktının detayını ve kalitesini etkiler. |
| `cfg` | FLOAT | Koşullandırma faktörünü kontrol eder; örnekleme sürecinin yönünü ve alanını etkiler. |
| `örnekleyici_adı` | COMBO[STRING] | Kullanılacak belirli örnekleyiciyi seçer; örnekleme tekniğinin özelleştirilmesine olanak tanır. |
| `zamanlayıcı` | COMBO[STRING] | Örnekleme sürecini kontrol etmek için zamanlayıcıyı seçer; örneklerin ilerlemesini ve kalitesini etkiler. |
| `pozitif` | CONDITIONING | Örneklemeyi istenen niteliklere yönlendirmek için pozitif koşullandırmayı belirtir. |
| `negatif` | CONDITIONING | Örneklemeyi belirli niteliklerden uzaklaştırmak için negatif koşullandırmayı belirtir. |
| `gizli_görüntü` | LATENT | Örnekleme sürecinde kullanılacak başlangıç gizli görüntüsünü sağlar; bir başlangıç noktası görevi görür. |
| `başlangıç_adımı` | INT | Örnekleme sürecinin başlangıç adımını belirler; örnekleme ilerlemesi üzerinde kontrol sağlar. |
| `bitiş_adımı` | INT | Örnekleme sürecinin bitiş adımını ayarlar; örneklemenin kapsamını tanımlar. |
| `kalan_gürültüyle_dön` | COMBO[STRING] | Örneğin artık gürültüyle birlikte döndürülüp döndürülmeyeceğini belirtir; nihai çıktının görünümünü etkiler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-------------|-------------|------------------------------------------------------------------------------------------------------------------------------|
| `latent` | LATENT | Çıktı, uygulanan yapılandırmaları ve teknikleri yansıtarak modelden oluşturulan gizli görüntüyü temsil eder. |