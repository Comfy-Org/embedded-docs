# WanHuMoGörüntüdenVideoya

WanHuMoImageToVideo düğümü, video kareleri için latent temsiller üreterek görüntüleri video dizilerine dönüştürür. Koşullama girdilerini işler ve video üretimini etkilemek için referans görüntüleri ve ses gömme vektörlerini dahil edebilir. Düğüm, video sentezi için uygun değiştirilmiş koşullama verileri ve latent temsilleri çıktı olarak verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video üretimini istenen içeriğe yönlendiren pozitif koşullama girdisi | CONDITIONING | Evet | - |
| `negatif` | Video üretimini istenmeyen içerikten uzaklaştıran negatif koşullama girdisi | CONDITIONING | Evet | - |
| `vae` | Referans görüntüleri latent uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı video karelerinin piksel cinsinden genişliği (varsayılan: 832, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 to MAX_RESOLUTION |
| `yükseklik` | Çıktı video karelerinin piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 to MAX_RESOLUTION |
| `uzunluk` | Oluşturulan video dizisindeki kare sayısı (varsayılan: 97, (length - 1) 4'e bölünebilir olacak şekilde olmalıdır) | INT | Evet | 1 to MAX_RESOLUTION |
| `toplu_iş_boyutu` | Aynı anda oluşturulacak video dizisi sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `ses_kodlayıcı_çıktısı` | Ses içeriğine dayalı olarak video üretimini etkileyebilen isteğe bağlı ses kodlama verisi | AUDIOENCODEROUTPUT | Hayır | - |
| `referans_görsel` | Video üretiminin stilini ve içeriğini yönlendirmek için kullanılan isteğe bağlı referans görüntüsü | IMAGE | Hayır | - |

**Not:** Bir referans görüntü sağlandığında, pozitif koşullamaya eklenen bir latent olarak kodlanır; aynı şekle sahip sıfır dolu bir latent ise negatif koşullamaya eklenir. Ses kodlayıcı çıktısı sağlandığında, ses gömme vektörleri enterpole edilir ve pozitif koşullamaya eklenir; sıfır dolu bir ses gömme vektörü ise negatif koşullamaya eklenir. İsteğe bağlı girdiler atlanırsa, hem referans latentleri hem de ses gömme vektörleri için sıfır dolu yer tutucu tensörler kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Referans görüntü ve/veya ses gömme vektörleri dahil edilmiş değiştirilmiş pozitif koşullama | CONDITIONING |
| `negatif` | Referans görüntü ve/veya ses gömme vektörleri dahil edilmiş değiştirilmiş negatif koşullama | CONDITIONING |
| `gizli_uzay` | Video dizisi için latent temsil; sıfırla başlatılır ve `width`, `height` ve `length` ayarlarına göre boyutlandırılır | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `db674a4a00729a8715988030083e2858f958cd21de73bbbe4ed6d76f5f539419`
