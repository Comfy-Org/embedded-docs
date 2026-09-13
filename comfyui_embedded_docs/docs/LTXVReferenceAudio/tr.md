# LTXV Referans Ses (ID-LoRA)

LTXV Reference Audio, bir referans ses klibindeki konuşmacının ses kimliğini üretilen sese aktarır. Referans sesi koşullandırmaya kodlar ve isteğe bağlı olarak modeli kimlik rehberliğiyle yamalar; bu, konuşmacı kimliği etkisini güçlendirmek için her adımda referans olmadan ekstra bir ileri geçiş çalıştırır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kimlik rehberliğiyle yamalanacak model. | MODEL | Evet | - |
| `positive` | Pozitif koşullandırma girdisi. | CONDITIONING | Evet | - |
| `negative` | Negatif koşullandırma girdisi. | CONDITIONING | Evet | - |
| `reference_audio` | Konuşmacı kimliği aktarılacak referans ses klibi. ~5 saniye önerilir (eğitim süresi). Daha kısa veya daha uzun klipler ses kimliği aktarımını bozabilir. | AUDIO | Evet | - |
| `audio_vae` | Kodlama için LTXV Audio VAE. | VAE | Evet | - |
| `identity_guidance_scale` | Kimlik rehberliğinin gücü. Konuşmacı kimliğini güçlendirmek için her adımda referans olmadan ekstra bir ileri geçiş çalıştırır. Devre dışı bırakmak için 0 yapın (ekstra geçiş yok). (varsayılan: 3.0) | FLOAT | Evet | 0.0 - 100.0 |
| `start_percent` | Kimlik rehberliğinin etkin olduğu sigma aralığının başlangıcı. (varsayılan: 0.0) | FLOAT | Evet | 0.0 - 1.0 |
| `end_percent` | Kimlik rehberliğinin etkin olduğu sigma aralığının sonu. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

Not: Kimlik rehberliği yalnızca `identity_guidance_scale` 0'dan büyük olduğunda ve geçerli örnekleme adımı `start_percent` ile `end_percent` tarafından tanımlanan aralıkta olduğunda uygulanır. İkisi farklıysa referans ses, ses VAE'sinin örnekleme hızına yeniden örneklenir.

Not: `start_percent` ve `end_percent` gelişmiş parametrelerdir; yalnızca arayüzde gelişmiş seçenekler etkinleştirildiğinde gösterilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Kimlik rehberliği işleviyle yamalanmış model. | MODEL |
| `positive` | Artık kodlanmış referans ses verisini içeren pozitif koşullandırma. | CONDITIONING |
| `negative` | Artık kodlanmış referans ses verisini içeren negatif koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/tr.md)

---
**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`
