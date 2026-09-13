# Kandinsky5ImageToVideo

Kandinsky5ImageToVideo düğümü, Kandinsky modelini kullanarak video oluşturma için koşullandırma ve latent verilerini hazırlar. İstenen genişlik, yükseklik, uzunluk ve toplu iş boyutuna göre boyutlandırılmış boş bir video latent oluşturur ve isteğe bağlı olarak, pozitif ve negatif koşullandırmayı güncelleyerek oluşturulan videonun ilk karelerini yönlendirmek için bir başlangıç görüntüsünü kodlayabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Video oluşturmayı yönlendirmek için kullanılan pozitif koşullandırma istemleri. | CONDITIONING | Evet | N/A |
| `negative` | Video oluşturmayı belirli kavramlardan uzaklaştırmak için kullanılan negatif koşullandırma istemleri. | CONDITIONING | Evet | N/A |
| `vae` | İsteğe bağlı başlangıç görüntüsünü latent uzayına kodlamak için kullanılan VAE modeli. | VAE | Evet | N/A |
| `width` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 768). | INT | Evet | 16 ila 16384 (adım 16) |
| `height` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 512). | INT | Evet | 16 ila 16384 (adım 16) |
| `length` | Videodaki kare sayısı (varsayılan: 121). | INT | Evet | 1 ila 16384 (adım 4) |
| `batch_size` | Aynı anda oluşturulacak video dizisi sayısı (varsayılan: 1). | INT | Evet | 1 ila 4096 |
| `start_image` | İsteğe bağlı bir başlangıç görüntüsü veya kare grubu. Sağlanırsa, kodlanır ve modelin çıktı latentlerinin gürültülü başlangıcının yerine kullanılır. | IMAGE | Hayır | N/A |

**Not:** Bir `start_image` sağlandığında, belirtilen `width` ve `height` değerlerine uyacak şekilde çift doğrusal interpolasyon kullanılarak otomatik olarak yeniden boyutlandırılır. Görüntü grubunun yalnızca ilk `length` karesi kodlama için kullanılır; fazladan kareler yok sayılır. Görüntü grubunda `length` değerinden daha az kare varsa, yalnızca o kareler kullanılır. Görüntünün yalnızca RGB kanalları kodlanır. Kodlanan latent daha sonra videonun başlangıç görünümünü yönlendirmek için hem `positive` hem de `negative` koşullandırmasına enjekte edilir ve temiz kodlanmış kareler modelin çıktı latentlerinin gürültülü başlangıcının yerine geçer.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Değiştirilmiş pozitif koşullandırma; bir `start_image` sağlandığında kodlanmış başlangıç görüntüsü verileriyle güncellenir. | CONDITIONING |
| `negative` | Değiştirilmiş negatif koşullandırma; bir `start_image` sağlandığında kodlanmış başlangıç görüntüsü verileriyle güncellenir. | CONDITIONING |
| `latent` | Boş video latent. Belirtilen boyutlar için şekillendirilmiş, sıfırlarla doldurulmuş bir latent tensörü. | LATENT |
| `cond_latent` | Temiz kodlanmış başlangıç görüntüleri; model çıktı latentlerinin gürültülü başlangıcının yerine geçmek için kullanılır. `start_image` sağlanmadığında boştur. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`
