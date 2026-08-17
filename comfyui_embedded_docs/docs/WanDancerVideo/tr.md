# WanDancerVideo

WanDancerVideo, WanDancer modeli ile video üretimi için koşullandırma verilerini ve boş bir latent tensör hazırlar. Pozitif ve negatif koşullandırma alır ve bunları isteğe bağlı olarak bir başlangıç görüntüsü, bir maske, CLIP görüş gömmeleri ve ses özellikleriyle birleştirerek üretilen videoyu kontrol eder.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Video üretimini yönlendiren pozitif koşullandırma. | CONDITIONING | Evet |  |
| `negative` | Video üretimini yönlendiren negatif koşullandırma. | CONDITIONING | Evet |  |
| `vae` | Başlangıç görüntüsünü latent uzaya kodlamak için kullanılan VAE. | VAE | Evet |  |
| `width` | Üretilen videonun piksel cinsinden genişliği (varsayılan: 480). | INT | Evet | 16 to MAX_RESOLUTION (step: 16) |
| `height` | Üretilen videonun piksel cinsinden yüksekliği (varsayılan: 832). | INT | Evet | 16 to MAX_RESOLUTION (step: 16) |
| `length` | Üretilen videodaki kare sayısı. WanDancer için 149 olmalıdır (varsayılan: 149). | INT | Evet | 1 to MAX_RESOLUTION (step: 4) |
| `clip_vision_output` | İlk kare için CLIP görüş gömmeleri. | CLIP_VISION_OUTPUT | Hayır |  |
| `clip_vision_output_ref` | Referans görüntüsü için CLIP görüş gömmeleri. | CLIP_VISION_OUTPUT | Hayır |  |
| `start_image` | Kodlanacak başlangıç görüntüsü(leri), herhangi bir sayıda kare olabilir. | IMAGE | Hayır |  |
| `mask` | Başlangıç görüntüsü(leri) için görüntü koşullandırma maskesi. Beyaz korunur, siyah üretilir. Yerel üretimler için kullanılır. | MASK | Hayır |  |
| `audio_encoder_output` | Ses koşullu üretim için ses özellikleri, FPS ve ses enjeksiyon ölçeği sağlayan bir ses kodlayıcının çıktısı. | AUDIO_ENCODER_OUTPUT | Hayır |  |

**Parametre Kısıtlamaları Üzerine Not:**
- `start_image` sağlandığında, `width` × `height` boyutuna yeniden boyutlandırılır, `length` kareyle sınırlandırılır ve bir concat maskesiyle birlikte her iki koşullandırmaya eklenen bir latente kodlanır.
- `mask` yalnızca `start_image` de sağlandığında etkili olur. Maskede beyaz alanlar korunur, siyah alanlar üretilir. `mask` sağlanmadığında, başlangıç görüntüsü alanı koşullandırma rehberi olarak kullanılır ve geri kalan kareler üretilir.
- `clip_vision_output_ref` yalnızca `clip_vision_output` sağlandığında uygulanır.
- `audio_encoder_output`, ses özelliklerini, FPS'yi ve bir ses enjeksiyon ölçeğini (varsayılan 1.0) her iki koşullandırmaya ekler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Üzerine ek veriler (concat latent, CLIP görüş, ses) eklenmiş pozitif koşullandırma. | CONDITIONING |
| `negative` | Üzerine ek veriler (concat latent, CLIP görüş, ses) eklenmiş negatif koşullandırma. | CONDITIONING |
| `latent` | Belirtilen video uzunluğu, yüksekliği ve genişliğiyle eşleşen boyutlara sahip boş bir latent tensör. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/tr.md)

---
**Source fingerprint (SHA-256):** `086a0ec361cf7f7ae7ce9505b55d31d92b025c6c7c9cde192009e6664011ad05`
