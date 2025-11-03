> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmpp2mSde/tr.md)

Bu düğüm, DPMPP_2M_SDE modeli için bir örnekleyici oluşturmak üzere tasarlanmıştır ve belirli çözücü türleri, gürültü seviyeleri ve hesaplama cihazı tercihlerine dayalı örnekler oluşturulmasına olanak tanır. Örnekleyici yapılandırmasının karmaşıklıklarını soyutlayarak, özelleştirilmiş ayarlarla örnek oluşturma için sadeleştirilmiş bir arayüz sağlar.

## Girdiler

| Parametre       | Veri Türü    | Açıklama                                                                 |
|-----------------|-------------|-----------------------------------------------------------------------------|
| `solver_type`   | COMBO[STRING] | Örnekleme sürecinde kullanılacak çözücü türünü belirtir, 'midpoint' ve 'heun' arasında seçenekler sunar. Bu seçim, örnekleme sırasında uygulanan sayısal entegrasyon yöntemini etkiler. |
| `eta`           | `FLOAT`     | Sayısal entegrasyondaki adım boyutunu belirler ve örnekleme sürecinin detay seviyesini etkiler. Daha yüksek bir değer, daha büyük bir adım boyutunu gösterir. |
| `s_noise`       | `FLOAT`     | Örnekleme sürecinde eklenen gürültünün seviyesini kontrol eder ve oluşturulan örneklerin değişkenliğini etkiler. |
| `noise_device`  | COMBO[STRING] | Gürültü üretim işleminin yürütüleceği hesaplama cihazını ('gpu' veya 'cpu') belirtir; performansı ve verimliliği etkiler. |

## Çıktılar

| Parametre       | Veri Türü    | Açıklama                                                                 |
|-----------------|-------------|-----------------------------------------------------------------------------|
| `sampler`       | `SAMPLER`   | Çıktı, belirtilen parametrelere göre yapılandırılmış, örnek oluşturmaya hazır bir örnekleyicidir. |