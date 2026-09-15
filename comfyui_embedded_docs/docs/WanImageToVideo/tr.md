# WanGörüntüdenVideoya

WanImageToVideo düğümü, video üretimi için koşullandırma ve latent temsilleri hazırlar. Video için boş bir latent uzayı oluşturur ve üretimi yönlendirmek için isteğe bağlı olarak bir başlangıç görüntüsünü ve CLIP görü çıktısını dahil edebilir. Hem pozitif hem de negatif koşullandırma girdileri, sağlanan görüntü ve görü verisiyle güncellenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Üretimi yönlendirmek için kullanılan pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negatif` | Üretimi yönlendirmek için kullanılan negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `vae` | Görüntüleri latent uzayına kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Üretilen videonun genişliği (varsayılan: 832, adım: 16) | INT | Evet | 16 - MAX_RESOLUTION |
| `yükseklik` | Üretilen videonun yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 - MAX_RESOLUTION |
| `uzunluk` | Videodaki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 - MAX_RESOLUTION |
| `toplu_boyut` | Tek bir toplu işte üretilecek video sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |
| `clip_görü_çıktısı` | Hem pozitif hem de negatif girdilere ek koşullandırma olarak eklenen isteğe bağlı CLIP görü çıktısı | CLIP_VISION_OUTPUT | Hayır | - |
| `başlangıç_görüntüsü` | Videoyu başlatmak için kullanılan isteğe bağlı başlangıç görüntüsü. Sağlandığında, belirtilen `width` ve `height` boyutlarına yeniden boyutlandırılır ve kare dizisinin başına yerleştirilir; `length` değerinin ötesindeki kareler yok sayılır. Kalan kareler nötr gri (0.5) değerleriyle doldurulur. | IMAGE | Hayır | - |

**Not:** `start_image` sağlandığında, kare dizisi VAE ile kodlanır ve koşullandırmaya bir maske uygulanır. Maske, başlangıç görüntüsünün kapsadığı kareler için 0, kalan kareler için 1 olarak ayarlanır; böylece üretim sağlanan görüntüden devam eder. Kodlama sırasında görüntünün yalnızca ilk üç renk kanalı (RGB) kullanılır. Hem pozitif hem de negatif koşullandırma aynı birleştirilmiş latent görüntüyü, maskeyi ve (sağlanmışsa) CLIP görü çıktısını alır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Görüntü ve görü verisiyle güncellenmiş pozitif koşullandırma | CONDITIONING |
| `negative` | Görüntü ve görü verisiyle güncellenmiş negatif koşullandırma | CONDITIONING |
| `latent` | Video üretimine hazır, [batch_size, 16, ((length-1)//4)+1, height//8, width//8] şeklinde boş latent tensör | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `46779f9f2f3da16826b7b547761a96597a3b6b43ce51a9c13367987642f3d5b7`
