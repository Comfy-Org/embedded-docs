# SesKodlayıcıKodla

AudioEncoderEncode düğümü, bir ses kodlayıcı modeli kullanarak ses verilerini kodlayarak işler. Ses girişini alır ve koşullandırma hattında daha ileri işlemler için kullanılabilen kodlanmış bir temsile dönüştürür. Bu düğüm, ham ses dalga formlarını ses tabanlı makine öğrenimi uygulamaları için uygun bir biçime dönüştürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `audio_encoder` | Ses girişini işlemek için kullanılan ses kodlayıcı modeli | AUDIO_ENCODER | Evet | - |
| `audio` | Dalga formu ve örnekleme hızı bilgisi içeren ses verisi | AUDIO | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Ses kodlayıcı tarafından üretilen kodlanmış ses temsili | AUDIO_ENCODER_OUTPUT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/tr.md)

---
**Source fingerprint (SHA-256):** `85f77152ccc1e3f4687e2b655283e69e03d90b862d6a676dcb89ea973dd70a63`
