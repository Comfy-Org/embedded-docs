KSamplerAdvanced düğümü, gelişmiş yapılandırmalar ve teknikler sunarak örnekleme sürecini iyileştirmek için tasarlanmıştır. Temel KSampler işlevlerine kıyasla, bir modelden örnekler üretmek için daha sofistike seçenekler sunmayı amaçlar.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Örneklerin oluşturulacağı modeli belirtir; örnekleme sürecinde kritik bir rol oynar. | MODEL |
| `gürültü_ekle` | Örnekleme sürecine gürültü eklenip eklenmeyeceğini belirler; oluşturulan örneklerin çeşitliliğini ve kalitesini etkiler. | COMBO[STRING] |
| `gürültü_tohumu` | Gürültü oluşturma için tohum değerini ayarlar; örnekleme sürecinde tekrarlanabilirliği sağlar. | INT |
| `adımlar` | Örnekleme sürecinde atılacak adım sayısını tanımlar; çıktının detayını ve kalitesini etkiler. | INT |
| `cfg` | Koşullandırma faktörünü kontrol eder; örnekleme sürecinin yönünü ve alanını etkiler. | FLOAT |
| `örnekleyici_adı` | Kullanılacak belirli örnekleyiciyi seçer; örnekleme tekniğinin özelleştirilmesine olanak tanır. | COMBO[STRING] |
| `zamanlayıcı` | Örnekleme sürecini kontrol etmek için zamanlayıcıyı seçer; örneklerin ilerlemesini ve kalitesini etkiler. | COMBO[STRING] |
| `pozitif` | Örneklemeyi istenen niteliklere yönlendirmek için pozitif koşullandırmayı belirtir. | CONDITIONING |
| `negatif` | Örneklemeyi belirli niteliklerden uzaklaştırmak için negatif koşullandırmayı belirtir. | CONDITIONING |
| `gizli_görüntü` | Örnekleme sürecinde kullanılacak başlangıç gizli görüntüsünü sağlar; bir başlangıç noktası görevi görür. | LATENT |
| `başlangıç_adımı` | Örnekleme sürecinin başlangıç adımını belirler; örnekleme ilerlemesi üzerinde kontrol sağlar. | INT |
| `bitiş_adımı` | Örnekleme sürecinin bitiş adımını ayarlar; örneklemenin kapsamını tanımlar. | INT |
| `kalan_gürültüyle_dön` | Örneğin artık gürültüyle birlikte döndürülüp döndürülmeyeceğini belirtir; nihai çıktının görünümünü etkiler. | COMBO[STRING] |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Çıktı, uygulanan yapılandırmaları ve teknikleri yansıtarak modelden oluşturulan gizli görüntüyü temsil eder. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerAdvanced/tr.md)
