> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/tr.md)

AudioEncoderEncode düğümü, bir ses kodlayıcı modeli kullanarak ses verilerini kodlayarak işler. Ses girişini alır ve koşullandırma hattında daha ileri işlemler için kullanılabilecek kodlanmış bir temsile dönüştürür. Bu düğüm, ham ses dalga formlarını ses tabanlı makine öğrenimi uygulamalarına uygun bir formata dönüştürür.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|------------|--------|----------|
| `audio_encoder` | AUDIO_ENCODER | Zorunlu | - | - | Ses girişini işlemek için kullanılan ses kodlayıcı modeli |
| `audio` | AUDIO | Zorunlu | - | - | Dalga formu ve örnekleme hızı bilgilerini içeren ses verisi |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | AUDIO_ENCODER_OUTPUT | Ses kodlayıcı tarafından oluşturulan kodlanmış ses temsili |

---
**Source fingerprint (SHA-256):** `8de45c157937ee95fbaef06aaefe478db7be8b16088d92720d977fe3d14eee39`
