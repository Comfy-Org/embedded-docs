> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ThresholdMask/tr.md)

ThresholdMask düğümü, bir maskeyi bir eşik değeri uygulayarak ikili maskeye dönüştürür. Girdi maskesindeki her pikseli belirtilen eşik değeriyle karşılaştırır ve eşiğin üzerindeki piksellerin 1 (beyaz), eşiğin altında veya eşit olan piksellerin ise 0 (siyah) olduğu yeni bir maske oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `mask` | MASK | Evet | - | İşlenecek girdi maskesi |
| `value` | FLOAT | Evet | 0.0 - 1.0 | İkilileştirme için eşik değeri (varsayılan: 0.5) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `mask` | MASK | Eşikleme işlemi sonrasında elde edilen ikili maske |