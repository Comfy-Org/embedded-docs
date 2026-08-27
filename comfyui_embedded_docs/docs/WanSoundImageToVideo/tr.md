# WanSoundImageToVideo

WanSoundImageToVideo düğümü, isteğe bağlı ses koşullandırmasıyla görüntülerden video içeriği üretir. Video latentleri oluşturmak için pozitif ve negatif koşullandırma istemlerini bir VAE modeliyle birlikte alır ve video üretim sürecini yönlendirmek için referans görüntüleri, ses kodlamasını, kontrol videolarını ve hareket referanslarını dahil edebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Üretilen videoda ne görünmesi gerektiğini yönlendiren pozitif koşullandırma istemleri | CONDITIONING | Evet | - |
| `negatif` | Üretilen videoda nelerin bulunmaması gerektiğini belirten negatif koşullandırma istemleri | CONDITIONING | Evet | - |
| `vae` | Video latent temsillerini kodlamak ve çözmek için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 to MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 to MAX_RESOLUTION |
| `uzunluk` | Üretilen videodaki kare sayısı (varsayılan: 77, 4'e bölünebilir olmalıdır) | INT | Evet | 1 to MAX_RESOLUTION |
| `toplu_iş_boyutu` | Aynı anda üretilecek video sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `ses_kodlayıcı_çıktısı` | Ses özelliklerine dayalı olarak video üretimini etkileyebilen isteğe bağlı ses kodlaması. Sağlandığında, ses özellikleri enterpole edilir ve video üretimini koşullandırmak için kullanılır. | AUDIO_ENCODER_OUTPUT | Hayır | - |
| `ref_image` | Video içeriği için görsel rehberlik sağlayan isteğe bağlı referans görüntüsü. Görüntü, belirtilen genişlik ve yüksekliğe uyacak şekilde büyütülür, ardından bir latent temsile kodlanır. Girdinin yalnızca ilk görüntüsü referans olarak kullanılır. | IMAGE | Hayır | - |
| `control_video` | Üretilen videonun hareketini ve yapısını yönlendiren isteğe bağlı kontrol videosu. Video büyütülür ve kodlanır, ardından çıktıyı koşullandırmak için kullanılır. Yalnızca ilk `length` kare kullanılır. | IMAGE | Hayır | - |
| `ref_motion` | Videodaki hareket desenleri için rehberlik sağlayan isteğe bağlı hareket referansı. Girdi 73'ten fazla kare içeriyorsa, yalnızca son 73 kare kullanılır. 73'ten az kare sağlanırsa, dizi nötr karelerle doldurulur. | IMAGE | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Video üretimi için değiştirilmiş, ses gömmeleri, referans latentleri, hareket referansları ve kontrol videosu koşullandırması içeren işlenmiş pozitif koşullandırma | CONDITIONING |
| `negative` | Video üretimi için değiştirilmiş, ses gömmeleri (sıfıra ayarlanmış), referans latentleri, hareket referansları ve kontrol videosu koşullandırması içeren işlenmiş negatif koşullandırma | CONDITIONING |
| `latent` | Son video karelerine çözülebilen latent uzayda üretilmiş video temsilidir. Latent tensörü [batch_size, 16, latent_t, height/8, width/8] biçimindedir; burada latent_t, length parametresinden türetilir | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `b1148cd00d8999dd6842e3c2fb13655fda8f20d5befed975a6d1652688b2807c`
