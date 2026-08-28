# SesKodlayıcıKodla

AudioEncoderEncode düğümü, bir ses kodlayıcı modeli kullanarak ses verisini kodlanmış bir temsiline dönüştürür. Bir ses kodlayıcı ve ham ses girdisi alır, ardından sesten dalga biçimini ve örnekleme hızını çıkararak koşullandırma hattında daha fazla işleme uygun kodlanmış bir çıktı üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `ses_kodlayıcı` | Ses girdisini işlemek için kullanılan ses kodlayıcı modeli | AUDIO_ENCODER | Evet | - |
| `ses` | Dalga biçimi ve örnekleme hızı bilgisi içeren ses verisi | AUDIO | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Ses kodlayıcı tarafından üretilen kodlanmış ses temsili | AUDIO_ENCODER_OUTPUT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/tr.md)

---
**Source fingerprint (SHA-256):** `85f77152ccc1e3f4687e2b655283e69e03d90b862d6a676dcb89ea973dd70a63`
