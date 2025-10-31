> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaStrength/tr.md)

Bu düğüm, belirli bir koşullandırma setinin güç özelliğini değiştirmek için tasarlanmış olup, üretim süreci üzerindeki koşullandırmanın etkisinin veya yoğunluğunun ayarlanmasına olanak tanır.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Değiştirilecek koşullandırma seti; üretim sürecini etkileyen mevcut koşullandırma durumunu temsil eder. |
| `strength` | `FLOAT` | Koşullandırma setine uygulanacak güç değeri; koşullandırmanın etki yoğunluğunu belirler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Her bir öğe için güncellenmiş güç değerlerine sahip, değiştirilmiş koşullandırma seti. |