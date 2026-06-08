Bu düğüm, DPMPP_2M_SDE modeli için bir örnekleyici oluşturmak üzere tasarlanmıştır; belirtilen çözücü türlerine, gürültü seviyelerine ve hesaplama cihazı tercihlerine göre örnekler oluşturulmasına olanak tanır. Örnekleyici yapılandırmasının karmaşıklığını soyutlayarak, özelleştirilmiş ayarlarla örnekler oluşturmak için kolaylaştırılmış bir arayüz sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `solver_type` | Örnekleme sürecinde kullanılacak çözücü türünü belirtir; 'midpoint' ve 'heun' arasında seçenekler sunar. Bu seçim, örnekleme sırasında uygulanan sayısal entegrasyon yöntemini etkiler. | COMBO[STRING] |
| `eta` | Sayısal entegrasyondaki adım boyutunu belirler, örnekleme sürecinin ayrıntı düzeyini etkiler. Daha yüksek bir değer, daha büyük bir adım boyutunu gösterir. | `FLOAT` |
| `s_noise` | Örnekleme sürecinde eklenen gürültü seviyesini kontrol eder, oluşturulan örneklerin değişkenliğini etkiler. | `FLOAT` |
| `noise_device` | Gürültü oluşturma sürecinin yürütüldüğü hesaplama cihazını ('gpu' veya 'cpu') belirtir; performans ve verimliliği etkiler. | COMBO[STRING] |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Çıktı, belirtilen parametrelere göre yapılandırılmış ve örnekler oluşturmaya hazır bir örnekleyicidir. | `SAMPLER` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmpp2mSde/tr.md)
