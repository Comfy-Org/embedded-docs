> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/tr.md)

WanInfiniteTalkToVideo düğümü, ses girişinden video dizileri oluşturur. Bir veya iki konuşmacıdan alınan ses özellikleriyle koşullandırılmış bir video difüzyon modeli kullanarak, bir konuşan kafa videosunun potansiyel temsilini üretir. Düğüm, yeni bir dizi oluşturabilir veya hareket bağlamı için önceki kareleri kullanarak mevcut bir diziyi genişletebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `mod` | COMBO | Evet | `"single_speaker"`<br>`"two_speakers"` | Ses giriş modu. `"single_speaker"` tek bir ses girişi kullanır. `"two_speakers"` ikinci bir konuşmacı ve ilgili maskeler için girişleri etkinleştirir. |
| `model` | MODEL | Evet | - | Temel video difüzyon modeli. |
| `model_patch` | MODELPATCH | Evet | - | Ses projeksiyon katmanlarını içeren model yaması. |
| `pozitif` | CONDITIONING | Evet | - | Olumlu koşullandırma, üretimi yönlendirir. |
| `negatif` | CONDITIONING | Evet | - | Olumsuz koşullandırma, üretimi yönlendirir. |
| `vae` | VAE | Evet | - | Görüntüleri potansiyel uzaya kodlamak ve potansiyel uzaydan çözmek için kullanılan VAE. |
| `genişlik` | INT | Hayır | 16 - MAX_RESOLUTION | Çıktı videosunun piksel cinsinden genişliği. 16'ya bölünebilir olmalıdır. (varsayılan: 832) |
| `yükseklik` | INT | Hayır | 16 - MAX_RESOLUTION | Çıktı videosunun piksel cinsinden yüksekliği. 16'ya bölünebilir olmalıdır. (varsayılan: 480) |
| `uzunluk` | INT | Hayır | 1 - MAX_RESOLUTION | Oluşturulacak kare sayısı. (varsayılan: 81) |
| `clip_vision_output` | CLIPVISIONOUTPUT | Hayır | - | Ek koşullandırma için isteğe bağlı CLIP görüş çıktısı. |
| `başlangıç_görseli` | IMAGE | Hayır | - | Video dizisini başlatmak için isteğe bağlı bir başlangıç görüntüsü. |
| `audio_encoder_output_1` | AUDIOENCODEROUTPUT | Evet | - | İlk konuşmacı için özellikler içeren birincil ses kodlayıcı çıktısı. |
| `hareket_kare_sayısı` | INT | Hayır | 1 - 33 | Bir diziyi genişletirken hareket bağlamı olarak kullanılacak önceki kare sayısı. (varsayılan: 9) |
| `audio_scale` | FLOAT | Hayır | -10.0 - 10.0 | Ses koşullandırmasına uygulanan bir ölçekleme faktörü. (varsayılan: 1.0) |
| `önceki_kareler` | IMAGE | Hayır | - | Genişletilecek isteğe bağlı önceki video kareleri. |
| `audio_encoder_output_2` | AUDIOENCODEROUTPUT | Hayır | - | İkinci ses kodlayıcı çıktısı. `mod` `"two_speakers"` olarak ayarlandığında gereklidir. |
| `mask_1` | MASK | Hayır | - | İki ses girişi kullanılıyorsa gerekli olan, ilk konuşmacı için maske. |
| `mask_2` | MASK | Hayır | - | İki ses girişi kullanılıyorsa gerekli olan, ikinci konuşmacı için maske. |

**Parametre Kısıtlamaları:**

* `mode` `"two_speakers"` olarak ayarlandığında, `audio_encoder_output_2`, `mask_1` ve `mask_2` parametreleri zorunlu hale gelir.
* `audio_encoder_output_2` sağlanırsa, hem `mask_1` hem de `mask_2` de sağlanmalıdır.
* `mask_1` ve `mask_2` sağlanırsa, `audio_encoder_output_2` de sağlanmalıdır.
* `previous_frames` sağlanırsa, `motion_frame_count` tarafından belirtilen sayıda en az kare içermelidir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `pozitif` | MODEL | Ses koşullandırması uygulanmış yamalı model. |
| `negatif` | CONDITIONING | Potansiyel olarak ek bağlamla (örn. başlangıç görüntüsü, CLIP görüşü) değiştirilmiş olumlu koşullandırma. |
| `latent` | CONDITIONING | Potansiyel olarak ek bağlamla değiştirilmiş olumsuz koşullandırma. |
| `kırpılmış_görsel` | LATENT | Potansiyel uzayda oluşturulan video dizisi. |
| `trim_image` | INT | Bir dizi genişletilirken hareket bağlamının başlangıcından kırpılması gereken kare sayısı. |

---
**Source fingerprint (SHA-256):** `6bb976da5cac0b61edb7d4c9d206c7c7ea9ffc0e982034c23c7f2e891e972888`
