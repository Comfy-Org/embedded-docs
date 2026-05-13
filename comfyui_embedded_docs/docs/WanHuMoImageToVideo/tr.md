> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/tr.md)

WanHuMoImageToVideo düğümü, video kareleri için gizil (latent) temsiller oluşturarak görüntüleri video dizilerine dönüştürür. Koşullandırma girdilerini işler ve video oluşumunu etkilemek için referans görüntüleri ve ses katıştırmalarını (embeddings) dahil edebilir. Düğüm, video sentezi için uygun, değiştirilmiş koşullandırma verileri ve gizil temsiller çıktısı verir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pozitif` | CONDITIONING | Evet | - | Video oluşumunu istenen içeriğe yönlendiren pozitif koşullandırma girdisi |
| `negatif` | CONDITIONING | Evet | - | Video oluşumunu istenmeyen içerikten uzaklaştıran negatif koşullandırma girdisi |
| `vae` | VAE | Evet | - | Referans görüntüleri gizil uzaya kodlamak için kullanılan VAE modeli |
| `genişlik` | INT | Evet | 16 - MAX_RESOLUTION | Çıktı video karelerinin piksel cinsinden genişliği (varsayılan: 832, 16'ya bölünebilir olmalıdır) |
| `yükseklik` | INT | Evet | 16 - MAX_RESOLUTION | Çıktı video karelerinin piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalıdır) |
| `uzunluk` | INT | Evet | 1 - MAX_RESOLUTION | Oluşturulan video dizisindeki kare sayısı (varsayılan: 97, (length - 1) 4'e bölünebilir olmalıdır) |
| `toplu_iş_boyutu` | INT | Evet | 1 - 4096 | Aynı anda oluşturulacak video dizisi sayısı (varsayılan: 1) |
| `ses_kodlayıcı_çıktısı` | AUDIOENCODEROUTPUT | Hayır | - | Ses içeriğine göre video oluşumunu etkileyebilecek isteğe bağlı ses kodlama verisi |
| `referans_görsel` | IMAGE | Hayır | - | Video oluşum stilini ve içeriğini yönlendirmek için kullanılan isteğe bağlı referans görüntüsü |

**Not:** Bir referans görüntüsü sağlandığında, kodlanır ve hem pozitif hem de negatif koşullandırmaya eklenir. Ses kodlayıcı çıktısı sağlandığında, işlenir ve koşullandırma verilerine dahil edilir. Hiçbiri sağlanmazsa, hem referans gizilleri hem de ses katıştırmaları için sıfır dolu yer tutucu tensörler kullanılır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | Referans görüntü ve/veya ses katıştırmaları dahil edilmiş değiştirilmiş pozitif koşullandırma |
| `gizli_uzay` | CONDITIONING | Referans görüntü ve/veya ses katıştırmaları dahil edilmiş değiştirilmiş negatif koşullandırma |
| `latent` | LATENT | Video dizisi verilerini içeren oluşturulmuş gizil temsil |

---
**Source fingerprint (SHA-256):** `6301671d04748ce80c561a65df80c7ca146b91bcce8851872df40211af29fd39`
