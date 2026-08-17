# Kandinsky5ImageToVideo

Kandinsky5ImageToVideo düğümü, Kandinsky modelini kullanarak video üretimi için koşullandırma ve latent uzay verilerini hazırlar. Boş bir video latent tensörü oluşturur ve isteğe bağlı olarak, üretilen videonun ilk karelerini yönlendirmek için bir başlangıç görüntüsünü kodlayarak pozitif ve negatif koşullandırmayı buna göre değiştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Video üretimini yönlendiren pozitif koşullandırma prompt'ları. | CONDITIONING | Evet | N/A |
| `negative` | Video üretimini belirli kavramlardan uzaklaştıran negatif koşullandırma prompt'ları. | CONDITIONING | Evet | N/A |
| `vae` | İsteğe bağlı başlangıç görüntüsünü latent uzaya kodlamak için kullanılan VAE modeli. | VAE | Evet | N/A |
| `width` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 768). | INT | Evet | 16 ila 8192 (adım 16) |
| `height` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 512). | INT | Evet | 16 ila 8192 (adım 16) |
| `length` | Videodaki kare sayısı (varsayılan: 121). | INT | Evet | 1 ila 8192 (adım 4) |
| `batch_size` | Aynı anda üretilecek video dizisi sayısı (varsayılan: 1). | INT | Evet | 1 ila 4096 |
| `start_image` | İsteğe bağlı bir başlangıç görüntüsü. Sağlanırsa kodlanır ve modelin çıktı latent'lerinin gürültülü başlangıcını değiştirmek için kullanılır. | IMAGE | Hayır | N/A |

**Not:** Bir `start_image` sağlandığında, belirtilen `width` ve `height` değerlerine uyacak şekilde çift doğrusal (bilinear) enterpolasyon kullanılarak yeniden boyutlandırılır. Görüntünün yalnızca ilk `length` karesi kodlama için kullanılır. Kodlanan latent daha sonra, başlangıç karelerini işaretleyen bir maske ile birlikte hem `positive` hem de `negative` koşullandırmaya enjekte edilir; böylece temiz kodlanmış görüntü, üretilen videonun gürültülü başlangıcının yerini alır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Kodlanmış başlangıç görüntüsü verileriyle güncellenmiş olabilecek değiştirilmiş pozitif koşullandırma. | CONDITIONING |
| `negative` | Kodlanmış başlangıç görüntüsü verileriyle güncellenmiş olabilecek değiştirilmiş negatif koşullandırma. | CONDITIONING |
| `latent` | Belirtilen `batch_size`, `length`, `height` ve `width` değerlerine göre şekillendirilmiş, sıfırlarla dolu boş bir video latent tensörü. | LATENT |
| `cond_latent` | Sağlanan başlangıç görüntülerinin temiz, kodlanmış latent temsili. Modelin çıktı latent'lerinin gürültülü başlangıcını değiştirmek için kullanılır. `start_image` sağlanmadığında boştur. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`
