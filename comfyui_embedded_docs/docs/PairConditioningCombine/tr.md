> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/tr.md)

PairConditioningCombine düğümü, iki koşullandırma verisi çiftini (pozitif ve negatif) tek bir çift halinde birleştirir. İki ayrı koşullandırma çiftini girdi olarak alır ve ComfyUI'nin dahili koşullandırma birleştirme mantığını kullanarak bunları birleştirir. Bu düğüm deneyseldir ve öncelikle gelişmiş koşullandırma manipülasyonu iş akışlarında kullanılır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pozitif_A` | CONDITIONING | Evet | - | İlk pozitif koşullandırma girdisi |
| `negatif_A` | CONDITIONING | Evet | - | İlk negatif koşullandırma girdisi |
| `pozitif_B` | CONDITIONING | Evet | - | İkinci pozitif koşullandırma girdisi |
| `negatif_B` | CONDITIONING | Evet | - | İkinci negatif koşullandırma girdisi |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | Birleştirilmiş pozitif koşullandırma çıktısı |
| `negative` | CONDITIONING | Birleştirilmiş negatif koşullandırma çıktısı |