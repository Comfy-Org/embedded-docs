# WanDancerVideo

WanDancerVideo düğümü, WanDancer modeli ile video üretimi için koşullandırma verilerini ve boş bir latent tensör hazırlar. İsteğe bağlı başlangıç görsellerini, maskeleri, CLIP vision embedding'lerini ve ses özelliklerini pozitif ve negatif koşullandırmaya ekleyerek üretilen videoyu yönlendirmelerini sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video üretimini yönlendirmek için pozitif koşullandırma. | CONDITIONING | Evet |  |
| `negatif` | Video üretimini yönlendirmek için negatif koşullandırma. | CONDITIONING | Evet |  |
| `vae` | Başlangıç görselini latent uzaya kodlamak için kullanılan VAE. | VAE | Evet |  |
| `genişlik` | Üretilen videonun piksel cinsinden genişliği (varsayılan: 480). | INT | Evet | 16 to MAX_RESOLUTION (step: 16) |
| `yükseklik` | Üretilen videonun piksel cinsinden yüksekliği (varsayılan: 832). | INT | Evet | 16 to MAX_RESOLUTION (step: 16) |
| `uzunluk` | Üretilen videodaki kare sayısı. WanDancer için 149 olarak kalmalıdır (varsayılan: 149). | INT | Evet | 1 to MAX_RESOLUTION (step: 4) |
| `clip_vision_output` | İlk kare için CLIP vision embedding'leri. | CLIP_VISION_OUTPUT | Hayır |  |
| `clip_vision_output_ref` | Referans görsel için CLIP vision embedding'leri. | CLIP_VISION_OUTPUT | Hayır |  |
| `başlangıç görseli` | Kodlanacak başlangıç görsel(ler)i; herhangi bir sayıda kare olabilir. | IMAGE | Hayır |  |
| `mask` | Başlangıç görsel(ler)i için görüntü koşullandırma maskesi. Beyaz korunur, siyah üretilir. Yerel üretimler için kullanılır. | MASK | Hayır |  |
| `audio_encoder_output` | Ses özelliklerini, kare hızını ve enjeksiyon ölçeği değerlerini sağlayan bir ses kodlayıcı çıktısı; sağlandığında koşullandırmaya eklenir. | AUDIO_ENCODER_OUTPUT | Hayır |  |

### Parametre Davranışına İlişkin Notlar

- `start_image` isteğe bağlıdır. Sağlandığında `width` ve `height` değerlerine yeniden boyutlandırılır, `vae` tarafından kodlanır ve hem pozitif hem de negatif koşullandırmaya eklenir. `start_image`, `length` değerinden daha fazla kareye sahipse fazla kareler atılır. Daha az kareye sahipse eksik kareler sıfır değerleriyle doldurulur.
- `mask` yalnızca `start_image` de sağlandığında etki eder. Beyaz alanlar korunur, siyah alanlar üretilir.
- `clip_vision_output_ref` yalnızca `clip_vision_output` da sağlandığında etki eder.
- `audio_encoder_output`, sağlandığında ses embedding'lerini, kare hızını ve enjeksiyon ölçeğini hem pozitif hem de negatif koşullandırmaya ekler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Başlangıç görseli latent'i, maske, CLIP vision veya ses verileri eklenmiş pozitif koşullandırma. | CONDITIONING |
| `negatif` | Başlangıç görseli latent'i, maske, CLIP vision veya ses verileri eklenmiş negatif koşullandırma. | CONDITIONING |
| `latent` | İstenen video uzunluğu, yüksekliği ve genişliğine göre boyutlandırılmış boş bir latent tensör. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/tr.md)

---
**Source fingerprint (SHA-256):** `086a0ec361cf7f7ae7ce9505b55d31d92b025c6c7c9cde192009e6664011ad05`
