# WanInfiniteTalkToVideo

WanInfiniteTalkToVideo, ses girdisinden video dizileri oluşturur. Bir veya iki konuşmacıdan çıkarılan ses özellikleriyle koşullandırılmış bir video difüzyon modeli kullanarak, konuşan bir kafa videosunun gizli temsilini üretir. Düğüm, yeni bir dizi oluşturabilir veya önceki kareleri hareket bağlamı olarak kullanarak mevcut bir diziyi uzatabilir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `mod` | Ses giriş modu. `single_speaker` tek bir ses girdisi kullanır. `two_speakers`, İki Konuşmacı Girdileri bölümünde listelenen ek ses girdisini ve maskeleri etkinleştirir. | DYNAMIC_COMBO | Evet | `"single_speaker"`<br>`"two_speakers"` |
| `model` | Temel video difüzyon modeli. | MODEL | Evet | - |
| `model_patch` | Ses projeksiyon katmanlarını içeren model yaması. | MODEL_PATCH | Evet | - |
| `pozitif` | Üretimi yönlendiren pozitif koşullandırma. | CONDITIONING | Evet | - |
| `negatif` | Üretimi yönlendiren negatif koşullandırma. | CONDITIONING | Evet | - |
| `vae` | Görüntüleri gizli uzaya kodlamak ve gizli uzaydan çözmek için kullanılan VAE. | VAE | Evet | - |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği. 16'ya bölünebilir olmalıdır. (varsayılan: 832) | INT | Evet | 16 - MAX_RESOLUTION (step 16) |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği. 16'ya bölünebilir olmalıdır. (varsayılan: 480) | INT | Evet | 16 - MAX_RESOLUTION (step 16) |
| `uzunluk` | Oluşturulacak kare sayısı. (varsayılan: 81) | INT | Evet | 1 - MAX_RESOLUTION (step 4) |
| `clip_vision_output` | Ek koşullandırma için isteğe bağlı CLIP görüş çıktısı. | CLIP_VISION_OUTPUT | Hayır | - |
| `başlangıç_görseli` | Video dizisini başlatmak için isteğe bağlı başlangıç görüntüsü. | IMAGE | Hayır | - |
| `audio_encoder_output_1` | İlk konuşmacı için özellikler içeren birincil ses kodlayıcı çıktısı. | AUDIO_ENCODER_OUTPUT | Evet | - |
| `hareket_kare_sayısı` | Hareket bağlamı olarak kullanılacak önceki kare sayısı. (varsayılan: 9) | INT | Evet | 1 - 33 |
| `audio_scale` | Ses koşullandırmasına uygulanan ölçekleme faktörü. (varsayılan: 1.0) | FLOAT | Evet | -10.0 - 10.0 |
| `önceki_kareler` | Uzatma için isteğe bağlı önceki video kareleri. Son `motion_frame_count` kare, hareket bağlamı olarak kullanılır. | IMAGE | Hayır | - |

### İki Konuşmacı Girdileri

Bu bölümdeki girdiler, `mode` değeri `"two_speakers"` olarak ayarlandığında gösterilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `audio_encoder_output_2` | İkinci konuşmacı için özellikler içeren ikinci ses kodlayıcı çıktısı. | AUDIO_ENCODER_OUTPUT | Hayır | - |
| `mask_1` | İlk konuşmacı için maske, iki ses girdisi kullanılıyorsa gereklidir. | MASK | Hayır | - |
| `mask_2` | İkinci konuşmacı için maske, iki ses girdisi kullanılıyorsa gereklidir. | MASK | Hayır | - |

**Parametre Kısıtlamaları:**

- `mode` değeri `"two_speakers"` olarak ayarlandığında, ikinci konuşmacı kurulumu için `audio_encoder_output_2`, `mask_1` ve `mask_2` gereklidir.
- `audio_encoder_output_2` sağlanmışsa, hem `mask_1` hem de `mask_2` de sağlanmalıdır.
- Hem `mask_1` hem de `mask_2` sağlanmışsa, `audio_encoder_output_2` de sağlanmalıdır.
- `previous_frames` sağlanmışsa, `motion_frame_count` tarafından belirtilen en az sayıda kare içermelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Ses koşullandırması uygulanmış yamalı model. | MODEL |
| `pozitif` | Başlangıç görüntüsü veya CLIP görüş çıktısı gibi ek bağlamla potansiyel olarak değiştirilmiş pozitif koşullandırma. | CONDITIONING |
| `negatif` | Potansiyel olarak ek bağlamla değiştirilmiş negatif koşullandırma. | CONDITIONING |
| `latent` | Gizli uzayda üretilen video dizisi. | LATENT |
| `kırpılmış_görsel` | Bir dizi uzatılırken hareket bağlamının başlangıcından kırpılması gereken kare sayısı. `previous_frames` sağlandığında `motion_frame_count` değerine eşittir, aksi halde 0. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `b7359490c1de86d9c82122bc227295b3b7f8a3493f629365ae0f22f9f34d9a66`
