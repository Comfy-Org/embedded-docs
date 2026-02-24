> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/tr.md)

HunyuanVideo15ImageToVideo düğümü, HunyuanVideo 1.5 modeline dayalı video oluşturma için koşullandırma ve gizli uzay verilerini hazırlar. Bir video dizisi için başlangıç gizli temsilini oluşturur ve isteğe bağlı olarak oluşturma sürecini yönlendirmek için bir başlangıç görüntüsü veya bir CLIP görüntü çıktısı entegre edebilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Videoda ne olması gerektiğini tanımlayan pozitif koşullandırma istemleri. |
| `negative` | CONDITIONING | Evet | - | Videoda ne olmaması gerektiğini tanımlayan negatif koşullandırma istemleri. |
| `vae` | VAE | Evet | - | Başlangıç görüntüsünü gizli uzaya kodlamak için kullanılan VAE (Değişimli Otokodlayıcı) modeli. |
| `width` | INT | Hayır | 16'dan MAX_RESOLUTION'a | Çıktı video karelerinin piksel cinsinden genişliği. 16'ya bölünebilir olmalıdır. (varsayılan: 848) |
| `height` | INT | Hayır | 16'dan MAX_RESOLUTION'a | Çıktı video karelerinin piksel cinsinden yüksekliği. 16'ya bölünebilir olmalıdır. (varsayılan: 480) |
| `length` | INT | Hayır | 1'den MAX_RESOLUTION'a | Video dizisindeki toplam kare sayısı. (varsayılan: 33) |
| `batch_size` | INT | Hayır | 1'den 4096'ya | Tek bir partide oluşturulacak video dizisi sayısı. (varsayılan: 1) |
| `start_image` | IMAGE | Hayır | - | Video oluşturmayı başlatmak için isteğe bağlı bir başlangıç görüntüsü. Sağlanırsa, kodlanır ve ilk kareleri koşullandırmak için kullanılır. |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Hayır | - | Oluşturma için ek görsel koşullandırma sağlamak üzere isteğe bağlı CLIP görüntü yerleştirmeleri. |

**Not:** Bir `start_image` sağlandığında, belirtilen `width` ve `height` ile eşleşecek şekilde otomatik olarak çift doğrusal enterpolasyon kullanılarak yeniden boyutlandırılır. Görüntü partisinin ilk `length` karesi kullanılır. Kodlanan görüntü daha sonra, karşılık gelen bir `concat_mask` ile birlikte `concat_latent_image` olarak hem `positive` hem de `negative` koşullandırmasına eklenir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Kodlanmış başlangıç görüntüsünü veya CLIP görüntü çıktısını artık içerebilen, değiştirilmiş pozitif koşullandırma. |
| `negative` | CONDITIONING | Kodlanmış başlangıç görüntüsünü veya CLIP görüntü çıktısını artık içerebilen, değiştirilmiş negatif koşullandırma. |
| `latent` | LATENT | Belirtilen parti boyutu, video uzunluğu, genişlik ve yükseklik için yapılandırılmış boyutlara sahip boş bir gizli tensör. |
