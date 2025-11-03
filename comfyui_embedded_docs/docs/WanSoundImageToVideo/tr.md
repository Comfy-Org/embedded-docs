> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/tr.md)

WanSoundImageToVideo düğümü, görüntülerden isteğe bağlı ses koşullandırması ile video içeriği oluşturur. Video latents oluşturmak için olumlu ve olumsuz koşullandırma prompt'larını ve bir VAE modeli alır; ayrıca video oluşturma sürecine rehberlik etmek için referans görüntüleri, ses kodlaması, kontrol videoları ve hareket referanslarını dahil edebilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Oluşturulan videoda hangi içeriğin görünmesi gerektiğine rehberlik eden olumlu koşullandırma prompt'ları |
| `negative` | CONDITIONING | Evet | - | Oluşturulan videoda hangi içeriğin bulunmaması gerektiğini belirten olumsuz koşullandırma prompt'ları |
| `vae` | VAE | Evet | - | Video latent temsillerini kodlamak ve kodunu çözmek için kullanılan VAE modeli |
| `width` | INT | Evet | 16 - MAX_RESOLUTION | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, 16'ya bölünebilir olmalı) |
| `height` | INT | Evet | 16 - MAX_RESOLUTION | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalı) |
| `length` | INT | Evet | 1 - MAX_RESOLUTION | Oluşturulan videodaki kare sayısı (varsayılan: 77, 4'e bölünebilir olmalı) |
| `batch_size` | INT | Evet | 1 - 4096 | Aynı anda oluşturulacak video sayısı (varsayılan: 1) |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | Hayır | - | Ses özelliklerine dayanarak video oluşturmayı etkileyebilecek isteğe bağlı ses kodlaması |
| `ref_image` | IMAGE | Hayır | - | Video içeriği için görsel rehberlik sağlayan isteğe bağlı referans görüntüsü |
| `control_video` | IMAGE | Hayır | - | Oluşturulan videonun hareketini ve yapısını yönlendiren isteğe bağlı kontrol videosu |
| `ref_motion` | IMAGE | Hayır | - | Videodaki hareket desenleri için rehberlik sağlayan isteğe bağlı hareket referansı |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Video oluşturma için değiştirilmiş, işlenmiş olumlu koşullandırma |
| `negative` | CONDITIONING | Video oluşturma için değiştirilmiş, işlenmiş olumsuz koşullandırma |
| `latent` | LATENT | Nihai video karelerine dönüştürülebilecek, latent uzayda oluşturulmuş video temsili |