> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaStrength/tr.md)

Bu düğüm, belirli bir koşullandırma kümesinin güç özelliğini değiştirmek, böylece koşullandırmanın üretim süreci üzerindeki etkisini veya yoğunluğunu ayarlamak için tasarlanmıştır.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Değiştirilecek koşullandırma kümesi; üretim sürecini etkileyen mevcut koşullandırma durumunu temsil eder. |
| `güç` | `FLOAT` | Koşullandırma kümesine uygulanacak güç değeri; etkisinin yoğunluğunu belirler. |

## Çıkışlar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Her bir öğe için güncellenmiş güç değerlerine sahip değiştirilmiş koşullandırma kümesi. |