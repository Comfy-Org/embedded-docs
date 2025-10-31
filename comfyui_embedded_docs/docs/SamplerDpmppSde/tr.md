> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmppSde/tr.md)

Bu düğüm, DPM++ SDE (Stokastik Diferansiyel Denklem) modeli için bir örnekleyici oluşturmak üzere tasarlanmıştır. Hem CPU hem de GPU yürütme ortamlarına uyum sağlar ve mevcut donanıma bağlı olarak örnekleyici uygulamasını optimize eder.

## Girdiler

| Parametre      | Veri Tipi | Açıklama |
|----------------|-------------|-------------|
| `eta`          | FLOAT       | SDE çözücüsü için adım boyutunu belirtir ve örnekleme sürecinin ayrıntı düzeyini etkiler.|
| `s_noise`      | FLOAT       | Örnekleme sürecinde uygulanacak gürültü seviyesini belirler ve oluşturulan örneklerin çeşitliliğini etkiler.|
| `r`            | FLOAT       | Örnekleme sürecindeki gürültü azaltma oranını kontrol eder ve oluşturulan örneklerin netliğini ve kalitesini etkiler.|
| `noise_device` | COMBO[STRING]| Örnekleyici için yürütme ortamını (CPU veya GPU) seçer ve mevcut donanıma bağlı olarak performansı optimize eder.|

## Çıktılar

| Parametre    | Veri Tipi | Açıklama |
|----------------|-------------|-------------|
| `sampler`    | SAMPLER     | Belirtilen parametrelerle yapılandırılmış, örnekleme işlemlerinde kullanıma hazır olarak oluşturulan örnekleyici. |