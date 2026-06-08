WanInfiniteTalkToVideo düğümü, ses girişinden video dizileri oluşturur. Bir veya iki konuşmacıdan alınan ses özellikleriyle koşullandırılmış bir video difüzyon modeli kullanarak, bir konuşan kafa videosunun potansiyel temsilini üretir. Düğüm, yeni bir dizi oluşturabilir veya hareket bağlamı için önceki kareleri kullanarak mevcut bir diziyi genişletebilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `mod` | Ses giriş modu. `"single_speaker"` tek bir ses girişi kullanır. `"two_speakers"` ikinci bir konuşmacı ve ilgili maskeler için girişleri etkinleştirir. | COMBO | Evet | `"single_speaker"`<br>`"two_speakers"` |
| `model` | Temel video difüzyon modeli. | MODEL | Evet | - |
| `model_patch` | Ses projeksiyon katmanlarını içeren model yaması. | MODELPATCH | Evet | - |
| `pozitif` | Olumlu koşullandırma, üretimi yönlendirir. | CONDITIONING | Evet | - |
| `negatif` | Olumsuz koşullandırma, üretimi yönlendirir. | CONDITIONING | Evet | - |
| `vae` | Görüntüleri potansiyel uzaya kodlamak ve potansiyel uzaydan çözmek için kullanılan VAE. | VAE | Evet | - |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği. 16'ya bölünebilir olmalıdır. (varsayılan: 832) | INT | Hayır | 16 - MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği. 16'ya bölünebilir olmalıdır. (varsayılan: 480) | INT | Hayır | 16 - MAX_RESOLUTION |
| `uzunluk` | Oluşturulacak kare sayısı. (varsayılan: 81) | INT | Hayır | 1 - MAX_RESOLUTION |
| `clip_vision_output` | Ek koşullandırma için isteğe bağlı CLIP görüş çıktısı. | CLIPVISIONOUTPUT | Hayır | - |
| `başlangıç_görseli` | Video dizisini başlatmak için isteğe bağlı bir başlangıç görüntüsü. | IMAGE | Hayır | - |
| `audio_encoder_output_1` | İlk konuşmacı için özellikler içeren birincil ses kodlayıcı çıktısı. | AUDIOENCODEROUTPUT | Evet | - |
| `hareket_kare_sayısı` | Bir diziyi genişletirken hareket bağlamı olarak kullanılacak önceki kare sayısı. (varsayılan: 9) | INT | Hayır | 1 - 33 |
| `audio_scale` | Ses koşullandırmasına uygulanan bir ölçekleme faktörü. (varsayılan: 1.0) | FLOAT | Hayır | -10.0 - 10.0 |
| `önceki_kareler` | Genişletilecek isteğe bağlı önceki video kareleri. | IMAGE | Hayır | - |
| `audio_encoder_output_2` | İkinci ses kodlayıcı çıktısı. `mod` `"two_speakers"` olarak ayarlandığında gereklidir. | AUDIOENCODEROUTPUT | Hayır | - |
| `mask_1` | İki ses girişi kullanılıyorsa gerekli olan, ilk konuşmacı için maske. | MASK | Hayır | - |
| `mask_2` | İki ses girişi kullanılıyorsa gerekli olan, ikinci konuşmacı için maske. | MASK | Hayır | - |

**Parametre Kısıtlamaları:**

* `mode` `"two_speakers"` olarak ayarlandığında, `audio_encoder_output_2`, `mask_1` ve `mask_2` parametreleri zorunlu hale gelir.
* `audio_encoder_output_2` sağlanırsa, hem `mask_1` hem de `mask_2` de sağlanmalıdır.
* `mask_1` ve `mask_2` sağlanırsa, `audio_encoder_output_2` de sağlanmalıdır.
* `previous_frames` sağlanırsa, `motion_frame_count` tarafından belirtilen sayıda en az kare içermelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Ses koşullandırması uygulanmış yamalı model. | MODEL |
| `negatif` | Potansiyel olarak ek bağlamla (örn. başlangıç görüntüsü, CLIP görüşü) değiştirilmiş olumlu koşullandırma. | CONDITIONING |
| `latent` | Potansiyel olarak ek bağlamla değiştirilmiş olumsuz koşullandırma. | CONDITIONING |
| `kırpılmış_görsel` | Potansiyel uzayda oluşturulan video dizisi. | LATENT |
| `trim_image` | Bir dizi genişletilirken hareket bağlamının başlangıcından kırpılması gereken kare sayısı. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `6bb976da5cac0b61edb7d4c9d206c7c7ea9ffc0e982034c23c7f2e891e972888`
