# WanHuMoGörüntüdenVideoya

WanHuMoImageToVideo düğümü, Wan HuMo video üretim hattı için koşullandırma verisi ve boş bir latent video hazırlar. Pozitif ve negatif koşullandırma girdilerine bir referans görüntüsü ve ses gömme vektörleri ekleyebilir ve istenen `width`, `height`, `length` ve `batch_size` değerlerine göre boyutlandırılmış sıfırla doldurulmuş bir latent oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video oluşturmayı istenen içeriğe doğru yönlendiren pozitif koşullandırma girdisi. | CONDITIONING | Evet | - |
| `negatif` | Video oluşturmayı istenmeyen içerikten uzaklaştıran negatif koşullandırma girdisi. | CONDITIONING | Evet | - |
| `vae` | Referans görüntülerini latent uzaya kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `genişlik` | Çıktı video karelerinin piksel cinsinden genişliği. Varsayılan: 832. | INT | Evet | 16 - MAX_RESOLUTION, adım 16 |
| `yükseklik` | Çıktı video karelerinin piksel cinsinden yüksekliği. Varsayılan: 480. | INT | Evet | 16 - MAX_RESOLUTION, adım 16 |
| `uzunluk` | Oluşturulan video dizisindeki kare sayısı. Varsayılan: 97. | INT | Evet | 1 - MAX_RESOLUTION, adım 4 |
| `toplu_iş_boyutu` | Aynı anda oluşturulacak video dizisi sayısı. Varsayılan: 1. | INT | Evet | 1 - 4096 |
| `ses_kodlayıcı_çıktısı` | Ses içeriğine göre video oluşturmayı etkileyebilen isteğe bağlı ses kodlama verisi. | AUDIOENCODEROUTPUT | Hayır | - |
| `referans_görsel` | Video oluşturmanın stilini ve içeriğini yönlendirmek için kullanılan isteğe bağlı referans görüntüsü. Gruptaki yalnızca ilk görüntü kullanılır. | IMAGE | Hayır | - |

**Not:** Bir referans görüntüsü sağlandığında, gruptaki ilk görüntü bilineer interpolasyon kullanılarak istenen `width` ve `height` değerlerine büyütülür ve VAE ile kodlanır. Bu referans latent, pozitif koşullandırmaya eklenir; aynı şekle sahip sıfırla doldurulmuş bir latent ise negatif koşullandırmaya eklenir. `audio_encoder_output` sağlandığında, ses gömme vektörleri enterpolasyon yapılır ve pozitif koşullandırmaya eklenir; sıfırla doldurulmuş bir ses gömme vektörü ise negatif koşullandırmaya eklenir. İsteğe bağlı girdilerden biri atlanırsa, sıfırla doldurulmuş yer tutucu tensörler kullanılır: `[batch_size, 16, 1, height // 8, width // 8]` şeklinde sıfır bir referans latent ve/veya `[batch_size, latent_t + 1, 8, 5, 1280]` şeklinde sıfır ses gömme vektörleri; burada `latent_t = ((length - 1) // 4) + 1`.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Referans görüntüsü ve/veya ses gömme vektörleri dahil edilmiş değiştirilmiş pozitif koşullandırma. | CONDITIONING |
| `negative` | Referans görüntüsü ve/veya ses gömme vektörleri dahil edilmiş değiştirilmiş negatif koşullandırma. | CONDITIONING |
| `latent` | Video dizisi için sıfırla başlatılmış latent gösterimi; `width`, `height`, `length` ve `batch_size` değerlerine göre boyutlandırılmıştır. Şekil: `[batch_size, 16, latent_t, height // 8, width // 8]`, burada `latent_t = ((length - 1) // 4) + 1`. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `db674a4a00729a8715988030083e2858f958cd21de73bbbe4ed6d76f5f539419`
