> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingDiscrete/tr.md)

Bu düğüm, ayrık örnekleme stratejisi uygulayarak bir modelin örnekleme davranışını değiştirmek için tasarlanmıştır. Epsilon, v_prediction, lcm veya x0 gibi farklı örnekleme yöntemlerinin seçimine olanak tanır ve isteğe bağlı olarak sıfır atış gürültü oranı (zsnr) ayarına dayalı olarak modelin gürültü azaltma stratejisini ayarlar.

## Girdiler

| Parametre | Veri Tipi | Python dtype     | Açıklama |
|-----------|--------------|-------------------|-------------|
| `model`   | MODEL     | `torch.nn.Module` | Ayrık örnekleme stratejisinin uygulanacağı model. Bu parametre, değişikliğe uğrayacak temel modeli tanımladığı için çok önemlidir. |
| `örnekleme`| COMBO[STRING] | `str`           | Modele uygulanacak ayrık örnekleme yöntemini belirtir. Yöntem seçimi, modelin örnekleri nasıl ürettiğini etkileyerek örnekleme için farklı stratejiler sunar. |
| `zsnr`    | `BOOLEAN`   | `bool`           | Etkinleştirildiğinde, modelin gürültü azaltma stratejisini sıfır atış gürültü oranına göre ayarlayan bir boolean bayrağı. Bu, üretilen örneklerin kalitesini ve özelliklerini etkileyebilir. |

## Çıktılar

| Parametre | Veri Tipi | Python dtype     | Açıklama |
|-----------|-------------|-------------------|-------------|
| `model`   | MODEL     | `torch.nn.Module` | Uygulanan ayrık örnekleme stratejisine sahip değiştirilmiş model. Bu model artık belirtilen yöntem ve ayarları kullanarak örnek üretebilecek şekilde donatılmıştır. |