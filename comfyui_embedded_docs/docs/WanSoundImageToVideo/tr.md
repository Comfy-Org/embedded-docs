# WanSoundImageToVideo

WanSoundImageToVideo düğümü, Wan ses-video üretimi için koşullandırma ve boş bir latent video tensörü hazırlar. İsteğe bağlı olarak, oluşturulan videoyu yönlendirmek için ses kodlaması, bir referans görüntüsü, bir kontrol videosu ve bir hareket referansı ekleyebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Oluşturulan videoda hangi içeriğin görünmesi gerektiğini yönlendiren pozitif koşullandırma istemleri | CONDITIONING | Evet | - |
| `negatif` | Oluşturulan videoda hangi içerikten kaçınılması gerektiğini belirten negatif koşullandırma istemleri | CONDITIONING | Evet | - |
| `vae` | Referans görüntülerini, hareket referanslarını ve kontrol videosu karelerini latent temsillere kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı videosunun genişliği, piksel cinsinden (varsayılan: 832, adım: 16) | INT | Evet | 16 - MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun yüksekliği, piksel cinsinden (varsayılan: 480, adım: 16) | INT | Evet | 16 - MAX_RESOLUTION |
| `uzunluk` | Oluşturulan videodaki kare sayısı (varsayılan: 77, adım: 4) | INT | Evet | 1 - MAX_RESOLUTION |
| `toplu_iş_boyutu` | Aynı anda oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |
| `ses_kodlayıcı_çıktısı` | Ses özelliklerine göre video oluşturmayı etkileyebilen isteğe bağlı ses kodlaması. Sağlandığında, ses özellikleri enterpole edilir ve video oluşturmayı koşullandırmak için kullanılır. | AUDIO_ENCODER_OUTPUT | Hayır | - |
| `ref_image` | Video içeriği için görsel rehberlik sağlayan isteğe bağlı referans görüntüsü. Görüntü, belirtilen genişlik ve yükseklikle eşleşecek şekilde yeniden ölçeklendirilir ve ardından bir latent temsile kodlanır. Girdinin yalnızca ilk görüntüsü referans olarak kullanılır. | IMAGE | Hayır | - |
| `control_video` | Oluşturulan videonun hareketini ve yapısını yönlendiren isteğe bağlı kontrol videosu. Video yeniden ölçeklendirilir ve kodlanır, ardından çıktıyı koşullandırmak için kullanılır. Yalnızca ilk `length` kare kullanılır. | IMAGE | Hayır | - |
| `ref_motion` | Videodaki hareket desenleri için rehberlik sağlayan isteğe bağlı hareket referansı. Girdi 73'ten fazla kare içeriyorsa yalnızca son 73 kare kullanılır. 73'ten az kare sağlanırsa dizi nötr karelerle doldurulur. | IMAGE | Hayır | - |

Not: Tüm isteğe bağlı girdiler bağımsız olarak veya birlikte kullanılabilir. Düğüm, hangi isteğe bağlı girdilerin bağlandığına göre sağlanan `positive` ve `negative` koşullandırmasını değiştirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Video oluşturma için değiştirilmiş, işlenmiş pozitif koşullandırma; ilgili isteğe bağlı girdiler sağlandığında ses gömmeleri, referans latentleri, hareket referansları ve kontrol videosu koşullandırmasını içerir | CONDITIONING |
| `negative` | Video oluşturma için değiştirilmiş, işlenmiş negatif koşullandırma; ilgili isteğe bağlı girdiler sağlandığında ses gömmeleri (sıfıra ayarlanır), referans latentleri, hareket referansları ve kontrol videosu koşullandırmasını içerir | CONDITIONING |
| `latent` | Oluşturma için başlangıç noktası olarak kullanılan boş latent video tensörü. Latent tensörü `[batch_size, 16, latent_t, height/8, width/8]` şeklindedir; burada `latent_t`, `((length - 1) // 4) + 1` olarak hesaplanır. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `b1148cd00d8999dd6842e3c2fb13655fda8f20d5befed975a6d1652688b2807c`
