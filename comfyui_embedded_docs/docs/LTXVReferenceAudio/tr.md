> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/tr.md)

LTXV Referans Ses düğümü, ses üretiminde konuşmacı kimlik aktarımı için kullanılır. Referans ses klibini model için koşullandırmaya kodlayarak, üretilen sesin konuşmacının ses özelliklerini benimsemesini sağlar. Ayrıca, konuşmacı kimlik etkisini güçlendirmek için ek bir işlem adımı çalıştıran kimlik yönlendirmesi uygulayabilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Kimlik yönlendirmesi ile yamalanacak model. |
| `positive` | CONDITIONING | Evet | - | Pozitif koşullandırma girişi. |
| `negative` | CONDITIONING | Evet | - | Negatif koşullandırma girişi. |
| `reference_audio` | SES | Evet | - | Konuşmacı kimliği aktarılacak referans ses klibi. ~5 saniye önerilir (eğitim süresi). Daha kısa veya daha uzun klipler ses kimlik aktarımını bozabilir. |
| `audio_vae` | VAE | Evet | - | Referans sesi kodlamak için LTXV Ses VAE'si. |
| `identity_guidance_scale` | FLOAT | Hayır | 0.0 - 100.0 | Kimlik yönlendirmesinin gücü. Konuşmacı kimliğini güçlendirmek için her adımda referans olmadan ek bir ileri geçiş çalıştırır. Devre dışı bırakmak için 0'a ayarlayın (ek geçiş yok). (varsayılan: 3.0) |
| `start_percent` | FLOAT | Hayır | 0.0 - 1.0 | Kimlik yönlendirmesinin aktif olduğu sigma aralığının başlangıcı. (varsayılan: 0.0) |
| `end_percent` | FLOAT | Hayır | 0.0 - 1.0 | Kimlik yönlendirmesinin aktif olduğu sigma aralığının sonu. (varsayılan: 1.0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Kimlik yönlendirme işlevi ile yamalanmış model. |
| `positive` | CONDITIONING | Artık kodlanmış referans ses verilerini içeren pozitif koşullandırma. |
| `negative` | CONDITIONING | Artık kodlanmış referans ses verilerini içeren negatif koşullandırma. |