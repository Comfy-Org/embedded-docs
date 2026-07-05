# WanSoundImageToVideo

WanSoundImageToVideo düğümü, isteğe bağlı ses koşullandırmasıyla görüntülerden video içeriği oluşturur. Video gizil değişkenlerini (latent) oluşturmak için pozitif ve negatif koşullandırma istemlerini bir VAE modeliyle birlikte alır; video oluşturma sürecini yönlendirmek için referans görüntüleri, ses kodlamasını, kontrol videolarını ve hareket referanslarını entegre edebilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Oluşturulan videoda hangi içeriğin görünmesi gerektiğini yönlendiren pozitif koşullandırma istemleri | CONDITIONING | Evet | - |
| `negatif` | Oluşturulan videoda hangi içeriğin kaçınılması gerektiğini belirten negatif koşullandırma istemleri | CONDITIONING | Evet | - |
| `vae` | Video gizil temsillerini kodlamak ve çözmek için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 ile MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 ile MAX_RESOLUTION |
| `uzunluk` | Oluşturulan videodaki kare sayısı (varsayılan: 77, 4'e bölünebilir olmalıdır) | INT | Evet | 1 ile MAX_RESOLUTION |
| `toplu_iş_boyutu` | Aynı anda oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `ses_kodlayıcı_çıktısı` | Ses özelliklerine dayalı olarak video oluşturmayı etkileyebilecek isteğe bağlı ses kodlaması | AUDIOENCODEROUTPUT | Hayır | - |
| `ref_image` | Video içeriği için görsel rehberlik sağlayan isteğe bağlı referans görüntüsü | IMAGE | Hayır | - |
| `control_video` | Oluşturulan videonun hareketini ve yapısını yönlendiren isteğe bağlı kontrol videosu | IMAGE | Hayır | - |
| `ref_motion` | Videodaki hareket desenleri için rehberlik sağlayan isteğe bağlı hareket referansı | IMAGE | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Video oluşturma için değiştirilmiş, işlenmiş pozitif koşullandırma | CONDITIONING |
| `negative` | Video oluşturma için değiştirilmiş, işlenmiş negatif koşullandırma | CONDITIONING |
| `latent` | Son video karelerine çözülebilen, gizil uzayda oluşturulmuş video temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `f80f82b8671294a14ecfecf91bc13febae0c91c5efa438467a4413d52dc82d3f`
