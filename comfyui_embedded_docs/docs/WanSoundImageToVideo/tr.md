# WanSoundImageToVideo

WanSoundImageToVideo düğümü, isteğe bağlı ses koşullandırmasıyla görüntülerden video üretimini hazırlar. Koşullandırma girdilerini ve boş bir latent tensörü oluşturmak için pozitif ve negatif koşullandırma promptlarını bir VAE modeliyle birlikte alır ve video üretim sürecini yönlendirmek için referans görüntüleri, ses kodlamasını, kontrol videolarını ve hareket referanslarını dahil edebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Üretilen videoda hangi içeriğin görünmesi gerektiğini yönlendiren pozitif koşullandırma promptları | CONDITIONING | Evet | - |
| `negative` | Üretilen videoda hangi içerikten kaçınılması gerektiğini belirten negatif koşullandırma promptları | CONDITIONING | Evet | - |
| `vae` | Video latent temsillerini kodlamak ve çözmek için kullanılan VAE modeli | VAE | Evet | - |
| `width` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 ila MAX_RESOLUTION (adım: 16) |
| `height` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 ila MAX_RESOLUTION (adım: 16) |
| `length` | Üretilen videodaki kare sayısı (varsayılan: 77, 4'e bölünebilir olmalıdır) | INT | Evet | 1 ila MAX_RESOLUTION (adım: 4) |
| `batch_size` | Aynı anda üretilecek video sayısı (varsayılan: 1) | INT | Evet | 1 ila 4096 |
| `audio_encoder_output` | Ses özelliklerine göre video üretimini etkileyebilen isteğe bağlı ses kodlaması. Sağlandığında, ses özellikleri enterpole edilir ve video üretimini koşullandırmak için kullanılır. | AUDIOENCODEROUTPUT | Hayır | - |
| `ref_image` | Video içeriği için görsel rehberlik sağlayan isteğe bağlı referans görüntüsü. Görüntü, belirtilen genişlik ve yüksekliğe uyacak şekilde ölçeklenir ve ardından bir latent temsile kodlanır. Girdi grubundaki yalnızca ilk görüntü kullanılır. | IMAGE | Hayır | - |
| `control_video` | Üretilen videonun hareketini ve yapısını yönlendiren isteğe bağlı kontrol videosu. Video ölçeklenir ve kodlanır, ardından çıktıyı koşullandırmak için kullanılır. Yalnızca ilk `length` kare kullanılır. | IMAGE | Hayır | - |
| `ref_motion` | Videodaki hareket desenleri için rehberlik sağlayan isteğe bağlı hareket referansı. Girdide 73'ten fazla kare varsa, yalnızca son 73 kare kullanılır. 73'ten az kare sağlanırsa, dizi nötr karelerle doldurulur. | IMAGE | Hayır | - |

**Not:** İsteğe bağlı girdiler (`audio_encoder_output`, `ref_image`, `control_video`, `ref_motion`) bağımsız olarak veya birlikte kullanılabilir. Kontrol videosu koşullandırması her zaman uygulanır; `control_video` sağlanmadığında, boş (sıfır) bir kontrol videosu kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Video üretimi için değiştirilmiş işlenmiş pozitif koşullandırma. İlgili isteğe bağlı girdiler sağlandığında, ses gömmelerini, referans latentlerini, hareket referanslarını ve kontrol videosu koşullandırmasını içerir. | CONDITIONING |
| `negative` | Video üretimi için değiştirilmiş işlenmiş negatif koşullandırma. İlgili isteğe bağlı girdiler sağlandığında, ses gömmelerini (sıfıra ayarlanmış), referans latentlerini, hareket referanslarını ve kontrol videosu koşullandırmasını içerir. | CONDITIONING |
| `latent` | Video üretimi için başlangıç noktası görevi gören boş latent tensör. Latent, [batch_size, 16, latent_t, height/8, width/8] şeklindedir; burada latent_t = ((length - 1) // 4) + 1'dir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `b1148cd00d8999dd6842e3c2fb13655fda8f20d5befed975a6d1652688b2807c`
