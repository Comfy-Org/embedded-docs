# HunyuanVideo15ImageToVideo

HunyuanVideo15ImageToVideo düğümü, HunyuanVideo 1.5 modeline dayalı video oluşturma için koşullandırma ve latent uzay verilerini hazırlar. Bir video dizisi için başlangıç latent temsili oluşturur ve isteğe bağlı olarak oluşturma sürecini yönlendirmek için bir başlangıç görüntüsü veya CLIP görüş çıktısını entegre edebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Videonun ne içermesi gerektiğini tanımlayan pozitif koşullandırma istemleridir. | CONDITIONING | Evet | - |
| `negative` | Videonun neyi içermemesi gerektiğini tanımlayan negatif koşullandırma istemleridir. | CONDITIONING | Evet | - |
| `vae` | Başlangıç görüntüsünü latent uzaya kodlamak için kullanılan VAE (Varyasyonel Otomatik Kodlayıcı) modelidir. | VAE | Evet | - |
| `width` | Çıktı video karelerinin piksel cinsinden genişliği. 16'ya bölünebilir olmalıdır. (varsayılan: 848) | INT | Evet | 16 to MAX_RESOLUTION, step: 16 |
| `height` | Çıktı video karelerinin piksel cinsinden yüksekliği. 16'ya bölünebilir olmalıdır. (varsayılan: 480) | INT | Evet | 16 to MAX_RESOLUTION, step: 16 |
| `length` | Video dizisindeki toplam kare sayısı. Değer 4'lük adımlarla artar. (varsayılan: 33) | INT | Evet | 1 to MAX_RESOLUTION, step: 4 |
| `batch_size` | Tek bir partide oluşturulacak video dizisi sayısı. (varsayılan: 1) | INT | Evet | 1 to 4096 |
| `start_image` | Video oluşturmayı başlatmak için isteğe bağlı bir başlangıç görüntüsü. Sağlanırsa kodlanır ve ilk kareleri koşullandırmak için kullanılır. Görüntünün yalnızca ilk `length` karesi kullanılır. | IMAGE | Hayır | - |
| `clip_vision_output` | Oluşturma için ek görsel koşullandırma sağlayan isteğe bağlı CLIP görüş vektör gösterimleri. | CLIP_VISION_OUTPUT | Hayır | - |

**Not:** Bir `start_image` sağlandığında, belirtilen `width` ve `height` değerlerine uyacak şekilde çift doğrusal (bilinear) enterpolasyon kullanılarak otomatik olarak yeniden boyutlandırılır ve yalnızca RGB kanalları kullanılır. Görüntü partisinin ilk `length` karesi kullanılır. Kodlanan görüntü daha sonra bir `concat_latent_image` ve buna karşılık gelen bir `concat_mask` olarak hem `positive` hem de `negative` koşullandırmasına eklenir. Maske, başlangıç görüntüsünün kapsadığı kareler için 0.0, kalan kareler için 1.0 olarak ayarlanır. Bir `clip_vision_output` sağlandığında, bu da hem `positive` hem de `negative` koşullandırmasına eklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Artık kodlanmış başlangıç görüntüsünü veya CLIP görüş çıktısını içerebilen değiştirilmiş pozitif koşullandırma. | CONDITIONING |
| `negative` | Artık kodlanmış başlangıç görüntüsünü veya CLIP görüş çıktısını içerebilen değiştirilmiş negatif koşullandırma. | CONDITIONING |
| `latent` | Belirtilen parti boyutu, video uzunluğu, genişlik ve yükseklik için yapılandırılmış boyutlara sahip boş bir latent tensör. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `dbedf7f378ae9613c8f47fe9876a4576c815055b4cdb6bf687b7575fcd7ea80a`
