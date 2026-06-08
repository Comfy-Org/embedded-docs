**LTXV Referans Ses Düğümü**, ses üretiminde konuşmacı kimlik aktarımı için kullanılır. Bir referans ses klibini model için koşullandırmaya kodlayarak, üretilen sesin konuşmacının ses özelliklerini benimsemesini sağlar. Ayrıca, konuşmacı kimlik etkisini güçlendirmek için ek bir işlem adımı çalıştıran kimlik yönlendirmesi uygulayabilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kimlik yönlendirmesi ile yamalanacak model. | MODEL | Evet | - |
| `pozitif` | Pozitif koşullandırma girişi. | CONDITIONING | Evet | - |
| `negatif` | Negatif koşullandırma girişi. | CONDITIONING | Evet | - |
| `referans_ses` | Konuşmacı kimliği aktarılacak referans ses klibi. Yaklaşık 5 saniye önerilir (eğitim süresi). Daha kısa veya daha uzun klipler ses kimliği aktarımını bozabilir. | SES | Evet | - |
| `audio_vae` | Referans sesi kodlamak için LTXV Ses VAE'si. | VAE | Evet | - |
| `kimlik_rehberliği_ölçeği` | Kimlik yönlendirmesinin gücü. Konuşmacı kimliğini güçlendirmek için her adımda referans olmadan ek bir ileri geçiş çalıştırır. Devre dışı bırakmak için 0 olarak ayarlayın (ek geçiş yok). (varsayılan: 3.0) | FLOAT | Hayır | 0.0 - 100.0 |
| `başlangıç_yüzdesi` | Kimlik yönlendirmesinin etkin olduğu sigma aralığının başlangıcı. (varsayılan: 0.0) | FLOAT | Hayır | 0.0 - 1.0 |
| `bitiş_yüzdesi` | Kimlik yönlendirmesinin etkin olduğu sigma aralığının sonu. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 1.0 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Kimlik yönlendirme işlevi ile yamalanmış model. | MODEL |
| `pozitif` | Artık kodlanmış referans ses verilerini içeren pozitif koşullandırma. | CONDITIONING |
| `negatif` | Artık kodlanmış referans ses verilerini içeren negatif koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/tr.md)

---
**Source fingerprint (SHA-256):** `0b87fb135ba8e752f4114cb47152503b0ec548eefcaa03f99f1cbdda6664874c`
