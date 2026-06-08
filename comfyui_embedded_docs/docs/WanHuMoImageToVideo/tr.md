WanHuMoImageToVideo düğümü, video kareleri için gizil (latent) temsiller oluşturarak görüntüleri video dizilerine dönüştürür. Koşullandırma girdilerini işler ve video oluşumunu etkilemek için referans görüntüleri ve ses katıştırmalarını (embeddings) dahil edebilir. Düğüm, video sentezi için uygun, değiştirilmiş koşullandırma verileri ve gizil temsiller çıktısı verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video oluşumunu istenen içeriğe yönlendiren pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negatif` | Video oluşumunu istenmeyen içerikten uzaklaştıran negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `vae` | Referans görüntüleri gizil uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı video karelerinin piksel cinsinden genişliği (varsayılan: 832, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 - MAX_RESOLUTION |
| `yükseklik` | Çıktı video karelerinin piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 - MAX_RESOLUTION |
| `uzunluk` | Oluşturulan video dizisindeki kare sayısı (varsayılan: 97, (length - 1) 4'e bölünebilir olmalıdır) | INT | Evet | 1 - MAX_RESOLUTION |
| `toplu_iş_boyutu` | Aynı anda oluşturulacak video dizisi sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |
| `ses_kodlayıcı_çıktısı` | Ses içeriğine göre video oluşumunu etkileyebilecek isteğe bağlı ses kodlama verisi | AUDIOENCODEROUTPUT | Hayır | - |
| `referans_görsel` | Video oluşum stilini ve içeriğini yönlendirmek için kullanılan isteğe bağlı referans görüntüsü | IMAGE | Hayır | - |

**Not:** Bir referans görüntüsü sağlandığında, kodlanır ve hem pozitif hem de negatif koşullandırmaya eklenir. Ses kodlayıcı çıktısı sağlandığında, işlenir ve koşullandırma verilerine dahil edilir. Hiçbiri sağlanmazsa, hem referans gizilleri hem de ses katıştırmaları için sıfır dolu yer tutucu tensörler kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `negatif` | Referans görüntü ve/veya ses katıştırmaları dahil edilmiş değiştirilmiş pozitif koşullandırma | CONDITIONING |
| `gizli_uzay` | Referans görüntü ve/veya ses katıştırmaları dahil edilmiş değiştirilmiş negatif koşullandırma | CONDITIONING |
| `latent` | Video dizisi verilerini içeren oluşturulmuş gizil temsil | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `6301671d04748ce80c561a65df80c7ca146b91bcce8851872df40211af29fd39`
