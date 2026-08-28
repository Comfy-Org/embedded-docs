# LTXV Referans Ses (ID-LoRA)

LTXV Reference Audio, bir konuşmacının ses kimliğini referans bir ses klibinden üretilen sese aktarır. Referans sesi koşullandırmaya kodlar ve isteğe bağlı olarak modele kimlik rehberliği ekler; bu, her adımda referans olmadan ek bir ileri geçiş çalıştırarak konuşmacı kimliği etkisini güçlendirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kimlik rehberliği ile yamalanacak model. | MODEL | Evet | - |
| `pozitif` | Pozitif koşullandırma girdisi. | CONDITIONING | Evet | - |
| `negatif` | Negatif koşullandırma girdisi. | CONDITIONING | Evet | - |
| `referans_ses` | Konuşmacı kimliği aktarılacak referans ses klibi. ~5 saniye önerilir (eğitim süresi). Daha kısa veya daha uzun klipler ses kimliği aktarımını bozabilir. | AUDIO | Evet | - |
| `audio_vae` | Kodlama için LTXV Audio VAE. | VAE | Evet | - |
| `kimlik_rehberliği_ölçeği` | Kimlik rehberliğinin gücü. Her adımda referans olmadan ek bir ileri geçiş çalıştırarak konuşmacı kimliğini güçlendirir. Devre dışı bırakmak için 0'a ayarlayın (ek geçiş yok). (varsayılan: 3.0) | FLOAT | Evet | 0.0 - 100.0 |
| `başlangıç_yüzdesi` | Kimlik rehberliğinin etkin olduğu sigma aralığının başlangıcı. (varsayılan: 0.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bitiş_yüzdesi` | Kimlik rehberliğinin etkin olduğu sigma aralığının sonu. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

Not: Kimlik rehberliği yalnızca `identity_guidance_scale` 0'dan büyük olduğunda ve mevcut örnekleme adımı `start_percent` ve `end_percent` tarafından tanımlanan aralık içinde olduğunda uygulanır. Referans ses, ses VAE'sinin örnekleme hızından farklıysa, referans ses VAE'nin örnekleme hızına yeniden örneklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Kimlik rehberliği işlevi ile yamalanmış model. | MODEL |
| `pozitif` | Kodlanmış referans ses verisini artık içeren pozitif koşullandırma. | CONDITIONING |
| `negatif` | Kodlanmış referans ses verisini artık içeren negatif koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/tr.md)

---
**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`
