# Kandinsky5ImageToVideo

Kandinsky5ImageToVideo düğümü, Kandinsky modelini kullanarak video oluşturma için conditioning ve latent uzay verilerini hazırlar. Boş bir video latent tensörü oluşturur ve isteğe bağlı olarak, oluşturulan videonun ilk karelerini yönlendirmek için bir başlangıç görüntüsünü kodlayarak positive ve negative conditioning'i buna göre değiştirir.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video oluşturmayı yönlendiren pozitif conditioning istemleri. | CONDITIONING | Evet | N/A |
| `negatif` | Video oluşturmayı belirli kavramlardan uzaklaştıran negatif conditioning istemleri. | CONDITIONING | Evet | N/A |
| `vae` | İsteğe bağlı başlangıç görüntüsünü latent uzaya kodlamak için kullanılan VAE modeli. | VAE | Evet | N/A |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 768). | INT | Evet | 16 ila 16384 (adım 16) |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 512). | INT | Evet | 16 ila 16384 (adım 16) |
| `uzunluk` | Videodaki kare sayısı (varsayılan: 121). | INT | Evet | 1 ila 16384 (adım 4) |
| `toplu_boyutu` | Aynı anda oluşturulacak video dizisi sayısı (varsayılan: 1). | INT | Evet | 1 ila 4096 |
| `başlangıç_görseli` | İsteğe bağlı bir başlangıç görüntüsü veya kare dizisi. Sağlanırsa kodlanır ve modelin çıktı latentlerinin gürültülü başlangıcını değiştirmek için kullanılır. | IMAGE | Hayır | N/A |

**Not:** Bir `start_image` sağlandığında, belirtilen `width` ve `height` değerlerine uyacak şekilde çift doğrusal (bilinear) enterpolasyon kullanılarak otomatik olarak yeniden boyutlandırılır. Görüntü dizisinin yalnızca ilk `length` karesi kodlama için kullanılır; ek kareler yok sayılır. Görüntü dizisinde `length` değerinden az kare varsa, yalnızca bu kareler kullanılır. Görüntünün yalnızca RGB kanalları kodlanır. Kodlanan latent daha sonra videonun ilk görünümünü yönlendirmek için hem `positive` hem de `negative` conditioning'e enjekte edilir ve temiz kodlanmış kareler, modelin çıktı latentlerinin gürültülü başlangıcını değiştirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `pozitif` | Kodlanmış başlangıç görüntüsü verileriyle güncellenmiş olabilen değiştirilmiş pozitif conditioning. | CONDITIONING |
| `negatif` | Kodlanmış başlangıç görüntüsü verileriyle güncellenmiş olabilen değiştirilmiş negatif conditioning. | CONDITIONING |
| `latent` | Boş video latent'i. Belirtilen boyutlara göre şekillendirilmiş, sıfırlarla doldurulmuş bir latent tensörü. | LATENT |
| `cond_latent` | Temiz kodlanmış başlangıç görüntüleri; model çıktı latentlerinin gürültülü başlangıcını değiştirmek için kullanılır. `start_image` sağlanmadığında boştur. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`
