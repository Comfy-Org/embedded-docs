> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultAndCombine/tr.md)

PairConditioningSetDefaultAndCombine düğümü, varsayılan koşullandırma değerlerini ayarlar ve bunları giriş koşullandırma verileriyle birleştirir. Pozitif ve negatif koşullandırma girişlerini ve bunların varsayılan karşılıklarını alır, ardından ComfyUI'nin kanca sistemi aracılığıyla bunları işleyerek varsayılan değerleri içeren nihai koşullandırma çıktıları üretir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | İşlenecek birincil pozitif koşullandırma girişi |
| `negative` | CONDITIONING | Evet | - | İşlenecek birincil negatif koşullandırma girişi |
| `positive_DEFAULT` | CONDITIONING | Evet | - | Yedek olarak kullanılacak varsayılan pozitif koşullandırma değerleri |
| `negative_DEFAULT` | CONDITIONING | Evet | - | Yedek olarak kullanılacak varsayılan negatif koşullandırma değerleri |
| `hooks` | HOOKS | Hayır | - | Özel işleme mantığı için isteğe bağlı kanca grubu |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Varsayılan değerlerle birleştirilmiş işlenmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Varsayılan değerlerle birleştirilmiş işlenmiş negatif koşullandırma |