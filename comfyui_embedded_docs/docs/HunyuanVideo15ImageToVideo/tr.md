HunyuanVideo15ImageToVideo düğümü, HunyuanVideo 1.5 modeline dayalı video oluşturma için koşullandırma ve gizli uzay verilerini hazırlar. Bir video dizisi için başlangıç gizli temsili oluşturur ve isteğe bağlı olarak oluşturma sürecini yönlendirmek için bir başlangıç görüntüsü veya CLIP görüş çıktısı entegre edebilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Videonun ne içermesi gerektiğini açıklayan pozitif koşullandırma istemleri. | CONDITIONING | Evet | - |
| `negatif` | Videonun ne içermemesi gerektiğini açıklayan negatif koşullandırma istemleri. | CONDITIONING | Evet | - |
| `vae` | Başlangıç görüntüsünü gizli uzaya kodlamak için kullanılan VAE (Değişken Otomatik Kodlayıcı) modeli. | VAE | Evet | - |
| `genişlik` | Çıktı video karelerinin piksel cinsinden genişliği. 16'ya bölünebilir olmalıdır. (varsayılan: 848) | INT | Hayır | 16 ila MAKS_ÇÖZÜNÜRLÜK |
| `yükseklik` | Çıktı video karelerinin piksel cinsinden yüksekliği. 16'ya bölünebilir olmalıdır. (varsayılan: 480) | INT | Hayır | 16 ila MAKS_ÇÖZÜNÜRLÜK |
| `uzunluk` | Video dizisindeki toplam kare sayısı. 4'ün katı olmalıdır. (varsayılan: 33) | INT | Hayır | 1 ila MAKS_ÇÖZÜNÜRLÜK |
| `toplu_boyutu` | Tek bir grupta oluşturulacak video dizisi sayısı. (varsayılan: 1) | INT | Hayır | 1 ila 4096 |
| `başlangıç_görseli` | Video oluşturmayı başlatmak için isteğe bağlı bir başlangıç görüntüsü. Sağlanırsa, kodlanır ve ilk kareleri koşullandırmak için kullanılır. Görüntünün yalnızca ilk `uzunluk` karesi kullanılır. | IMAGE | Hayır | - |
| `clip_vision_output` | Oluşturma için ek görsel koşullandırma sağlamak amacıyla isteğe bağlı CLIP görüş yerleştirmeleri. | CLIP_VISION_OUTPUT | Hayır | - |

**Not:** Bir `start_image` sağlandığında, çift doğrusal enterpolasyon kullanılarak belirtilen `width` ve `height` değerlerine otomatik olarak yeniden boyutlandırılır. Görüntü grubunun ilk `length` karesi kullanılır. Kodlanmış görüntü daha sonra, karşılık gelen bir `concat_mask` ile birlikte `concat_latent_image` olarak hem `positive` hem de `negative` koşullandırmaya eklenir. Maske, başlangıç görüntüsünün kapsadığı kareler için 0.0, kalan kareler için 1.0 olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `negatif` | Artık kodlanmış başlangıç görüntüsünü veya CLIP görüş çıktısını içerebilen değiştirilmiş pozitif koşullandırma. | CONDITIONING |
| `latent` | Artık kodlanmış başlangıç görüntüsünü veya CLIP görüş çıktısını içerebilen değiştirilmiş negatif koşullandırma. | CONDITIONING |
| `latent` | Belirtilen grup boyutu, video uzunluğu, genişlik ve yükseklik için yapılandırılmış boyutlara sahip boş bir gizli tensör. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `2f41bbb080672683fb1755be575f08c79ca03e324df66953eb40631581197d47`
