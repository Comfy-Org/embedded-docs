> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmppSde/tr.md)

Bu düğüm, DPM++ SDE (Stokastik Diferansiyel Denklem) modeli için bir örnekleyici oluşturmak üzere tasarlanmıştır. Hem CPU hem de GPU yürütme ortamlarına uyum sağlayarak, örnekleyicinin uygulamasını mevcut donanıma göre optimize eder.

## Girişler

| Parametre | Veri Türü | Açıklama |
|----------------|-------------|-------------|
| `eta` | FLOAT | SDE çözücüsü için adım boyutunu belirler, örnekleme sürecinin ayrıntı düzeyini etkiler. |
| `s_noise` | FLOAT | Örnekleme sürecinde uygulanacak gürültü seviyesini belirler, oluşturulan örneklerin çeşitliliğini etkiler. |
| `r` | FLOAT | Örnekleme sürecindeki gürültü azaltma oranını kontrol eder, oluşturulan örneklerin netliğini ve kalitesini etkiler. |
| `noise_device` | COMBO[STRING] | Örnekleyici için yürütme ortamını (CPU veya GPU) seçer, mevcut donanıma göre performansı optimize eder. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|----------------|-------------|-------------|
| `sampler` | SAMPLER | Belirtilen parametrelerle yapılandırılmış, örnekleme işlemlerinde kullanıma hazır oluşturulan örnekleyici. |