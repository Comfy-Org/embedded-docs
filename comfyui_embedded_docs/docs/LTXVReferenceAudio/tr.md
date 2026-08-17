# LTXV Referans Ses (ID-LoRA)

LTXV Reference Audio düğümü, ses üretiminde ID-LoRA konuşmacı kimliği aktarımı için bir referans ses klibi ayarlar. Klibi koşullandırmaya kodlar; böylece üretilen ses, konuşmacının ses özelliklerini benimser. İsteğe bağlı olarak modeli kimlik rehberliği ile yamalar; bu işlem, referans olmadan ek bir ileri geçiş çalıştırarak konuşmacı kimliği etkisini güçlendirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kimlik rehberliği ile yamalanacak model. | MODEL | Evet | - |
| `positive` | Pozitif koşullandırma girdisi. | CONDITIONING | Evet | - |
| `negative` | Negatif koşullandırma girdisi. | CONDITIONING | Evet | - |
| `reference_audio` | Kimliği aktarılacak referans ses klibi. Yaklaşık 5 saniye önerilir (eğitim süresi). Daha kısa veya daha uzun klipler ses kimliği aktarımını bozabilir. | AUDIO | Evet | - |
| `audio_vae` | Kodlama için LTXV Ses VAE'si. | VAE | Evet | - |
| `identity_guidance_scale` | Kimlik rehberliğinin gücü. Her adımda referans olmadan ek bir ileri geçiş çalıştırarak konuşmacı kimliğini güçlendirir. Devre dışı bırakmak için 0'a ayarlayın (ek geçiş yok). (varsayılan: 3.0) | FLOAT | Hayır | 0.0 - 100.0 |
| `start_percent` | Kimlik rehberliğinin aktif olduğu sigma aralığının başlangıcı. (varsayılan: 0.0) | FLOAT | Hayır | 0.0 - 1.0 |
| `end_percent` | Kimlik rehberliğinin aktif olduğu sigma aralığının sonu. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 1.0 |

Not: Kimlik rehberliği yalnızca `start_percent` ve `end_percent` tarafından tanımlanan aralıktaki sigma değerleri için aktiftir; bu aralığın dışında gürültü giderme çıktısı değiştirilmeden bırakılır. Referans ses hem pozitif hem de negatif koşullandırmaya eklenir. Referans sesin örnekleme hızı, ses VAE'sinin örnekleme hızından farklıysa, ses VAE'ye uyacak şekilde otomatik olarak yeniden örneklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Kimlik rehberliği işleviyle yamalanmış model. | MODEL |
| `positive` | Artık kodlanmış referans ses verilerini içeren pozitif koşullandırma. | CONDITIONING |
| `negative` | Artık kodlanmış referans ses verilerini içeren negatif koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/tr.md)

---
**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`
