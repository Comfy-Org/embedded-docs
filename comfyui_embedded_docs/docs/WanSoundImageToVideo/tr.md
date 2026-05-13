> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/tr.md)

WanSoundImageToVideo düğümü, isteğe bağlı ses koşullandırmasıyla görüntülerden video içeriği oluşturur. Video gizil değişkenlerini (latent) oluşturmak için pozitif ve negatif koşullandırma istemlerini bir VAE modeliyle birlikte alır; video oluşturma sürecini yönlendirmek için referans görüntüleri, ses kodlamasını, kontrol videolarını ve hareket referanslarını entegre edebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-----------|
| `pozitif` | CONDITIONING | Evet | - | Oluşturulan videoda hangi içeriğin görünmesi gerektiğini yönlendiren pozitif koşullandırma istemleri |
| `negatif` | CONDITIONING | Evet | - | Oluşturulan videoda hangi içeriğin kaçınılması gerektiğini belirten negatif koşullandırma istemleri |
| `vae` | VAE | Evet | - | Video gizil temsillerini kodlamak ve çözmek için kullanılan VAE modeli |
| `genişlik` | INT | Evet | 16 ile MAX_RESOLUTION | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, 16'ya bölünebilir olmalıdır) |
| `yükseklik` | INT | Evet | 16 ile MAX_RESOLUTION | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalıdır) |
| `uzunluk` | INT | Evet | 1 ile MAX_RESOLUTION | Oluşturulan videodaki kare sayısı (varsayılan: 77, 4'e bölünebilir olmalıdır) |
| `toplu_iş_boyutu` | INT | Evet | 1 ile 4096 | Aynı anda oluşturulacak video sayısı (varsayılan: 1) |
| `ses_kodlayıcı_çıktısı` | AUDIOENCODEROUTPUT | Hayır | - | Ses özelliklerine dayalı olarak video oluşturmayı etkileyebilecek isteğe bağlı ses kodlaması |
| `ref_image` | IMAGE | Hayır | - | Video içeriği için görsel rehberlik sağlayan isteğe bağlı referans görüntüsü |
| `control_video` | IMAGE | Hayır | - | Oluşturulan videonun hareketini ve yapısını yönlendiren isteğe bağlı kontrol videosu |
| `ref_motion` | IMAGE | Hayır | - | Videodaki hareket desenleri için rehberlik sağlayan isteğe bağlı hareket referansı |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `negative` | CONDITIONING | Video oluşturma için değiştirilmiş, işlenmiş pozitif koşullandırma |
| `latent` | CONDITIONING | Video oluşturma için değiştirilmiş, işlenmiş negatif koşullandırma |
| `latent` | LATENT | Son video karelerine çözülebilen, gizil uzayda oluşturulmuş video temsili |

---
**Source fingerprint (SHA-256):** `f80f82b8671294a14ecfecf91bc13febae0c91c5efa438467a4413d52dc82d3f`
