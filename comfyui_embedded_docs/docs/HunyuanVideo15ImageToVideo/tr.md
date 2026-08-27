# HunyuanVideo15ImageToVideo

HunyuanVideo15ImageToVideo düğümü, HunyuanVideo 1.5 modeline dayalı video üretimi için koşullandırma ve latent uzay verilerini hazırlar. Bir video dizisi için başlangıç latent temsili oluşturur ve isteğe bağlı olarak üretim sürecini yönlendirmek için bir başlangıç görüntüsü veya CLIP görüş çıktısı entegre edebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Videonun ne içermesi gerektiğini tanımlayan pozitif koşullandırma istemleridir. | CONDITIONING | Evet | - |
| `negatif` | Videonun neyi içermemesi gerektiğini tanımlayan negatif koşullandırma istemleridir. | CONDITIONING | Evet | - |
| `vae` | Başlangıç görüntüsünü latent uzaya kodlamak için kullanılan VAE (Varyasyonel Otomatik Kodlayıcı) modelidir. | VAE | Evet | - |
| `genişlik` | Çıktı video karelerinin piksel cinsinden genişliği. 16'ya bölünebilir olmalıdır. (varsayılan: 848) | INT | Evet | 16 ile MAX_RESOLUTION, adım: 16 |
| `yükseklik` | Çıktı video karelerinin piksel cinsinden yüksekliği. 16'ya bölünebilir olmalıdır. (varsayılan: 480) | INT | Evet | 16 ile MAX_RESOLUTION, adım: 16 |
| `uzunluk` | Video dizisindeki toplam kare sayısı. Değerler 1'den başlayarak 4'er adımlarla artar (1, 5, 9, 13, ...). (varsayılan: 33) | INT | Evet | 1 ile MAX_RESOLUTION, adım: 4 |
| `toplu_boyutu` | Tek bir batch'te üretilecek video dizisi sayısı. (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `başlangıç_görseli` | Video üretimini başlatmak için isteğe bağlı bir başlangıç görüntüsü. Sağlanırsa kodlanır ve ilk kareleri koşullandırmak için kullanılır. Görüntünün yalnızca ilk `length` karesi kullanılır. | IMAGE | Hayır | - |
| `clip_vision_output` | Üretim için ek görsel koşullandırma sağlayan isteğe bağlı CLIP görüş gömmeleridir. | CLIP_VISION_OUTPUT | Hayır | - |

**Not:** Bir `start_image` sağlandığında, belirtilen `width` ve `height` değerlerine uyacak şekilde çift doğrusal (bilinear) enterpolasyon kullanılarak otomatik olarak yeniden boyutlandırılır. Görüntü batch'inin yalnızca ilk `length` karesi kullanılır ve her karenin yalnızca ilk 3 renk kanalı kodlanır. Kodlanan görüntü daha sonra bir `concat_latent_image` ve buna karşılık gelen bir `concat_mask` olarak hem `positive` hem de `negative` koşullandırmaya eklenir. Maske, başlangıç görüntüsünün kapsadığı kareler için 0.0, geri kalan kareler için 1.0 olarak ayarlanır. Bir `clip_vision_output` sağlandığında, bu da hem `positive` hem de `negative` koşullandırmaya eklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Kodlanmış başlangıç görüntüsünü veya CLIP görüş çıktısını artık içerebilen değiştirilmiş pozitif koşullandırmadır. | CONDITIONING |
| `negatif` | Kodlanmış başlangıç görüntüsünü veya CLIP görüş çıktısını artık içerebilen değiştirilmiş negatif koşullandırmadır. | CONDITIONING |
| `latent` | Belirtilen batch boyutu, video uzunluğu, genişliği ve yüksekliği için yapılandırılmış boyutlara sahip boş bir latent tensörüdür. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `dbedf7f378ae9613c8f47fe9876a4576c815055b4cdb6bf687b7575fcd7ea80a`
