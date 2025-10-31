> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/tr.md)

AudioEncoderLoader düğümü, mevcut ses kodlayıcı dosyalarınızdan ses kodlayıcı modellerini yükler. Bir ses kodlayıcı dosya adını girdi olarak alır ve iş akışınızda ses işleme görevleri için kullanılabilecek yüklenmiş bir ses kodlayıcı modeli döndürür.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `audio_encoder_name` | STRING | COMBO | - | Mevcut ses kodlayıcı dosyaları | audio_encoders klasörünüzden hangi ses kodlayıcı model dosyasının yükleneceğini seçer |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `audio_encoder` | AUDIO_ENCODER | Ses işleme iş akışlarında kullanılmak üzere yüklenmiş ses kodlayıcı modelini döndürür |