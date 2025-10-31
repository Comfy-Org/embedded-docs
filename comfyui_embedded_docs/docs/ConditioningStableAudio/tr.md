> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/tr.md)

ConditioningStableAudio düğümü, ses üretimi için hem pozitif hem de negatif koşullandırma girişlerine zamanlama bilgisi ekler. Ses içeriğinin ne zaman ve ne kadar süreyle üretileceğini kontrol etmeye yardımcı olan başlangıç zamanı ve toplam süre parametrelerini ayarlar. Bu düğüm, mevcut koşullandırma verilerini ses özel zamanlama üst verileri ekleyerek değiştirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Ses zamanlama bilgisi ile değiştirilecek pozitif koşullandırma girişi |
| `negative` | CONDITIONING | Evet | - | Ses zamanlama bilgisi ile değiştirilecek negatif koşullandırma girişi |
| `seconds_start` | FLOAT | Evet | 0.0 - 1000.0 | Ses üretimi için saniye cinsinden başlangıç zamanı (varsayılan: 0.0) |
| `seconds_total` | FLOAT | Evet | 0.0 - 1000.0 | Ses üretimi için saniye cinsinden toplam süre (varsayılan: 47.0) |

## Çıkışlar

| Çıkış Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Ses zamanlama bilgisi uygulanmış değiştirilmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Ses zamanlama bilgisi uygulanmış değiştirilmiş negatif koşullandırma |