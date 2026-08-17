# WanInfiniteTalkToVideo

WanInfiniteTalkToVideo düğümü, sesten konuşan kafa videosu klibi oluşturur. Video difüzyon modelini bir veya iki konuşmacının ses özellikleriyle koşullandırır; isteğe bağlı olarak başlangıç görüntüsünü veya önceki kareleri bağlam olarak kullanır ve örnekleme için yamalı bir model, koşullandırma ve gizli video döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `mode` | Ses modu. `"single_speaker"` seçildiğinde bir ses girdisi kullanılır. `"two_speakers"` seçildiğinde aşağıda listelenen ikinci konuşmacı girdileri eklenir. | DYNAMIC_COMBO | Evet | `"single_speaker"`<br>`"two_speakers"` |
| `model` | Yamalanacak temel video difüzyon modeli. | MODEL | Evet | - |
| `model_patch` | Ses projeksiyon katmanlarını içeren model yaması. | MODELPATCH | Evet | - |
| `positive` | Video oluşturmayı yönlendirmek için kullanılan pozitif koşullandırma. | CONDITIONING | Evet | - |
| `negative` | Video oluşturmayı yönlendirmek için kullanılan negatif koşullandırma. | CONDITIONING | Evet | - |
| `vae` | Görüntüleri ve önceki kareleri gizli uzaya kodlamak için kullanılan VAE. | VAE | Evet | - |
| `width` | Oluşturulan videonun piksel cinsinden genişliği, 16'lık adımlarla. (varsayılan: 832) | INT | Evet | 16 - MAX_RESOLUTION (step 16) |
| `height` | Oluşturulan videonun piksel cinsinden yüksekliği, 16'lık adımlarla. (varsayılan: 480) | INT | Evet | 16 - MAX_RESOLUTION (step 16) |
| `length` | Oluşturulacak kare sayısı. (varsayılan: 81) | INT | Evet | 1 - MAX_RESOLUTION (step 4) |
| `audio_encoder_output_1` | İlk konuşmacı için ses kodlayıcı çıktısı; koşullandırma için kullanılan ses özelliklerini içerir. | AUDIOENCODEROUTPUT | Evet | - |
| `start_image` | Videonun başlangıcını başlatmak için kullanılan isteğe bağlı başlangıç görüntüsü. `width` ve `height` değerlerine yeniden boyutlandırılır. | IMAGE | Hayır | - |
| `clip_vision_output` | Hem pozitif hem negatif koşullandırmaya eklenen isteğe bağlı CLIP vision çıktısı. | CLIPVISIONOUTPUT | Hayır | - |
| `motion_frame_count` | Hareket bağlamı olarak kullanılacak önceki kare sayısı. (varsayılan: 9) | INT | Evet | 1 - 33 (step 1) |
| `audio_scale` | Ses koşullandırmasına uygulanan ölçekleme faktörü. (varsayılan: 1.0) | FLOAT | Evet | -10.0 - 10.0 (step 0.01) |
| `previous_frames` | Mevcut bir diziyi uzatmak için kullanılan isteğe bağlı önceki video kareleri. Düğüm, hareket bağlamı olarak son `motion_frame_count` karesini kullanır. | IMAGE | Hayır | - |

### Tek Konuşmacı Girdileri

`single_speaker` seçildiğinde herhangi bir ek girdi eklenmez.

### İki Konuşmacı Girdileri

Bu girdiler, `mode` değeri `"two_speakers"` olduğunda kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `audio_encoder_output_2` | İkinci konuşmacı için ses kodlayıcı çıktısı. Sağlandığında `mask_1` ve `mask_2` de sağlanmalıdır. | AUDIOENCODEROUTPUT | Hayır | - |
| `mask_1` | İlk konuşmacı için maske; iki ses girdisi kullanılıyorsa gereklidir. | MASK | Hayır | - |
| `mask_2` | İkinci konuşmacı için maske; iki ses girdisi kullanılıyorsa gereklidir. | MASK | Hayır | - |

**Parametre Kısıtlamaları:**

- `audio_encoder_output_2` sağlanırsa, hem `mask_1` hem de `mask_2` de sağlanmalıdır.
- Hem `mask_1` hem de `mask_2` sağlanırsa, `audio_encoder_output_2` de sağlanmalıdır.
- `previous_frames` sağlanırsa, en az `motion_frame_count` tarafından belirtilen sayıda kare içermelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Ses koşullandırma ve örnekleme sarmalayıcıları uygulanmış yamalı model. | MODEL |
| `positive` | Başlangıç görüntüsü veya CLIP vision bağlamıyla potansiyel olarak değiştirilmiş pozitif koşullandırma. | CONDITIONING |
| `negative` | Başlangıç görüntüsü veya CLIP vision bağlamıyla potansiyel olarak değiştirilmiş negatif koşullandırma. | CONDITIONING |
| `latent` | Oluşturulacak videoyu temsil eden sıfır başlangıçlı gizli tensör. | LATENT |
| `trim_image` | Önceki karelerden uzatırken baştan kırpılacak kare sayısı; yeni bir dizi başlatılırken 0. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `b7359490c1de86d9c82122bc227295b3b7f8a3493f629365ae0f22f9f34d9a66`
