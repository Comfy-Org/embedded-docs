> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/tr.md)

AudioEncoderEncode düğümü, ses verilerini bir ses kodlayıcı modeli kullanarak kodlayarak işler. Ses girişini alır ve koşullandırma işlem hattında ileri işlemler için kullanılabilecek kodlanmış bir temsile dönüştürür. Bu düğüm, ham ses dalga formlarını ses tabanlı makine öğrenimi uygulamaları için uygun bir formata dönüştürür.

## Girişler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `audio_encoder` | AUDIO_ENCODER | Gerekli | - | - | Ses girişini işlemek için kullanılan ses kodlayıcı modeli |
| `audio` | AUDIO | Gerekli | - | - | Dalga formu ve örnekleme hızı bilgilerini içeren ses verisi |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | AUDIO_ENCODER_OUTPUT | Ses kodlayıcı tarafından oluşturulan kodlanmış ses temsili |