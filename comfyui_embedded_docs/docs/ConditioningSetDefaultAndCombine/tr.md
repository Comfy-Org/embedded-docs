> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetDefaultAndCombine/tr.md)

Bu düğüm, kanca tabanlı bir sistem kullanarak koşullandırma verilerini varsayılan koşullandırma verileriyle birleştirir. Birincil koşullandırma girişi ve bir varsayılan koşullandırma girişi alır, ardından bunları belirtilen kanca yapılandırmasına göre birleştirir. Sonuç, her iki kaynağı da içeren tek bir koşullandırma çıktısıdır.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `cond` | CONDITIONING | Gerekli | - | - | İşlenecek birincil koşullandırma girişi |
| `cond_DEFAULT` | CONDITIONING | Gerekli | - | - | Birincil koşullandırma ile birleştirilecek varsayılan koşullandırma verisi |
| `hooks` | HOOKS | İsteğe Bağlı | - | - | Koşullandırma verilerinin nasıl işlendiğini ve birleştirildiğini kontrol eden isteğe bağlı kanca yapılandırması |

## Çıkışlar

| Çıkış Adı | Veri Türu | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Birincil ve varsayılan koşullandırma girişlerinin birleştirilmesi sonucu oluşan birleşik koşullandırma verisi |