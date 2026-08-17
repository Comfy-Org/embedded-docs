# WanHuMoGörüntüdenVideoya

WanHuMoImageToVideo düğümü, görüntüden videoya üretim için koşullandırma verilerini ve latent alanını hazırlar. Boş bir latent video tensörü oluşturur, isteğe bağlı olarak VAE ile bir referans görüntüsünü kodlar ve isteğe bağlı olarak ses kodlayıcı çıktısını video zamanlamalı koşullandırmaya dönüştürür. Düğüm, daha fazla video örneklemesi için pozitif ve negatif koşullandırma akışları ile birlikte bir latent tensör çıkarır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Video üretimini istenen içeriğe yönlendiren pozitif koşullandırma girdisi. | CONDITIONING | Evet | - |
| `negative` | Video üretimini istenmeyen içerikten uzaklaştıran negatif koşullandırma girdisi. | CONDITIONING | Evet | - |
| `vae` | Referans görüntüsünü latent alana kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `width` | Çıktı video karelerinin piksel cinsinden genişliği (varsayılan: 832; 16'ya bölünebilir olmalıdır). | INT | Evet | 16 to MAX_RESOLUTION (step 16) |
| `height` | Çıktı video karelerinin piksel cinsinden yüksekliği (varsayılan: 480; 16'ya bölünebilir olmalıdır). | INT | Evet | 16 to MAX_RESOLUTION (step 16) |
| `length` | Oluşturulan video dizisindeki kare sayısı (varsayılan: 97; `(length - 1)` ifadesi 4'e bölünebilir olmalıdır). | INT | Evet | 1 to MAX_RESOLUTION (step 4) |
| `batch_size` | Aynı anda oluşturulacak video dizisi sayısı (varsayılan: 1). | INT | Evet | 1 to 4096 |
| `audio_encoder_output` | Ses içeriğine dayalı olarak video üretimini etkilemek için kullanılan isteğe bağlı ses kodlayıcı çıktısı. | AUDIO_ENCODER_OUTPUT | Hayır | - |
| `ref_image` | Video üretim stilini ve içeriğini yönlendirmek için kullanılan isteğe bağlı referans görüntüsü. | IMAGE | Hayır | - |

**Not:** `ref_image` sağlandığında, `width` x `height` boyutuna yeniden boyutlandırılır, `vae` ile kodlanır ve pozitif ve negatif koşullandırmaya bir referans latent olarak eklenir. Referans görüntüsü sağlanmadığında, sıfır referans latentleri kullanılır. `audio_encoder_output` sağlandığında, ses embedding'leri işlenir ve her iki koşullandırma akışına bir ses embedding'i olarak eklenir; aksi takdirde sıfır ses embedding'i kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Referans latent ve ses embedding bilgisi eklenmiş pozitif koşullandırma. | CONDITIONING |
| `negative` | Referans latent ve ses embedding bilgisi eklenmiş negatif koşullandırma. | CONDITIONING |
| `latent` | Video dizisini temsil eden ve `batch_size`, `length`, `height` ve `width` değerlerine göre sıfırlarla başlatılan latent tensör. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `db674a4a00729a8715988030083e2858f958cd21de73bbbe4ed6d76f5f539419`
