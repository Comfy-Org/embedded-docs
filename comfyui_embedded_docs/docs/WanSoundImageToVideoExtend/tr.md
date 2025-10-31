> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/tr.md)

WanSoundImageToVideoExtend düğümü, ses koşullandırması ve referans görüntüleri dahil ederek görüntüden videoya üretimi genişletir. Pozitif ve negatif koşullandırmaları video latents verileri ve isteğe bağlı ses gömme verileriyle alarak genişletilmiş video dizileri oluşturur. Düğüm bu girdileri işleyerek, ses ipuçlarıyla senkronize edilebilen tutarlı video çıktıları üretir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Videoda neyin yer alması gerektiğini yönlendiren pozitif koşullandırma istemleri |
| `negative` | CONDITIONING | Evet | - | Videodan neyin çıkarılması gerektiğini belirten negatif koşullandırma istemleri |
| `vae` | VAE | Evet | - | Video karelerini kodlamak ve kodunu çözmek için kullanılan Varyasyonel Otokodlayıcı |
| `length` | INT | Evet | 1 to MAX_RESOLUTION | Video dizisi için oluşturulacak kare sayısı (varsayılan: 77, adım: 4) |
| `video_latent` | LATENT | Evet | - | Uzatma için başlangıç noktası olarak hizmet eden başlangıç video latent temsili |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | Hayır | - | Ses özelliklerine dayalı olarak video üretimini etkileyebilecek isteğe bağlı ses gömme verileri |
| `ref_image` | IMAGE | Hayır | - | Video üretimi için görsel rehberlik sağlayan isteğe bağlı referans görüntü |
| `control_video` | IMAGE | Hayır | - | Oluşturulan videonun hareketini ve stilini yönlendirebilecek isteğe bağlı kontrol videosu |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Video bağlamı uygulanmış işlenmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Video bağlamı uygulanmış işlenmiş negatif koşullandırma |
| `latent` | LATENT | Genişletilmiş video dizisini içeren oluşturulmuş video latent temsili |