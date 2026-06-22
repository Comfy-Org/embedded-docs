# ModelÖrneklemeAyrık

Bu düğüm, bir modele ayrık örnekleme stratejisi uygulayarak modelin örnekleme davranışını değiştirmek için tasarlanmıştır. Epsilon, v_prediction, lcm veya x0 gibi farklı örnekleme yöntemlerinin seçilmesine olanak tanır ve isteğe bağlı olarak modelin gürültü azaltma stratejisini sıfır atışlı gürültü oranı (zsnr) ayarına göre düzenler.

## Girişler

| Parametre | Açıklama | Veri Türü | Python dtype |
| --- | --- | --- | --- |
| `model` | Ayrık örnekleme stratejisinin uygulanacağı model. Bu parametre, değişikliğe uğrayacak temel modeli tanımladığı için kritik öneme sahiptir. | MODEL | `torch.nn.Module` |
| `örnekleme` | Modele uygulanacak ayrık örnekleme yöntemini belirtir. Yöntem seçimi, modelin örnekleri nasıl oluşturduğunu etkiler ve örnekleme için farklı stratejiler sunar. | COMBO[STRING] | `str` |
| `zsnr` | Etkinleştirildiğinde, modelin gürültü azaltma stratejisini sıfır atışlı gürültü oranına göre ayarlayan bir boolean işaretidir. Bu, oluşturulan örneklerin kalitesini ve özelliklerini etkileyebilir. | `BOOLEAN` | `bool` |

## Çıktılar

| Parametre | Açıklama | Veri Türü | Python dtype |
| --- | --- | --- | --- |
| `model` | Uygulanan ayrık örnekleme stratejisiyle değiştirilmiş model. Bu model artık belirtilen yöntem ve ayarlamaları kullanarak örnekler oluşturabilecek şekilde donatılmıştır. | MODEL | `torch.nn.Module` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingDiscrete/tr.md)
