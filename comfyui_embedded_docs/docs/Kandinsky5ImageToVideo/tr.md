# Kandinsky5ImageToVideo

Kandinsky5ImageToVideo düğümü, Kandinsky modelini kullanarak video oluşturma için koşullandırma ve gizli uzay verilerini hazırlar. Boş bir video gizli tensörü oluşturur ve isteğe bağlı olarak, oluşturulan videonun ilk karelerini yönlendirmek için bir başlangıç görüntüsünü kodlayarak pozitif ve negatif koşullandırmayı buna göre değiştirebilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video oluşturmayı yönlendirecek pozitif koşullandırma istemleri. | CONDITIONING | Evet | Yok |
| `negatif` | Video oluşturmayı belirli kavramlardan uzaklaştıracak negatif koşullandırma istemleri. | CONDITIONING | Evet | Yok |
| `vae` | İsteğe bağlı başlangıç görüntüsünü gizli uzaya kodlamak için kullanılan VAE modeli. | VAE | Evet | Yok |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 768). | INT | Hayır | 16 ila 8192 (adım 16) |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 512). | INT | Hayır | 16 ila 8192 (adım 16) |
| `uzunluk` | Videodaki kare sayısı (varsayılan: 121). | INT | Hayır | 1 ila 8192 (adım 4) |
| `toplu_boyutu` | Aynı anda oluşturulacak video dizisi sayısı (varsayılan: 1). | INT | Hayır | 1 ila 4096 |
| `başlangıç_görseli` | İsteğe bağlı bir başlangıç görüntüsü. Sağlanırsa, kodlanır ve modelin çıktı gizli değişkenlerinin gürültülü başlangıcını değiştirmek için kullanılır. | IMAGE | Hayır | Yok |

**Not:** Bir `start_image` sağlandığında, çift doğrusal enterpolasyon kullanılarak belirtilen `width` ve `height` değerlerine otomatik olarak yeniden boyutlandırılır. Görüntü grubunun ilk `length` karesi kodlama için kullanılır. Kodlanmış gizli değişken daha sonra videonun ilk görünümünü yönlendirmek için hem `positive` hem de `negative` koşullandırmaya enjekte edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Kodlanmış başlangıç görüntü verileriyle potansiyel olarak güncellenmiş, değiştirilmiş pozitif koşullandırma. | CONDITIONING |
| `negatif` | Kodlanmış başlangıç görüntü verileriyle potansiyel olarak güncellenmiş, değiştirilmiş negatif koşullandırma. | CONDITIONING |
| `latent` | Belirtilen boyutlar için şekillendirilmiş, sıfırlarla dolu boş bir video gizli tensörü. | LATENT |
| `cond_latent` | Sağlanan başlangıç görüntülerinin temiz, kodlanmış gizli temsili. Bu, oluşturulan video gizli değişkenlerinin gürültülü başlangıcını değiştirmek için dahili olarak kullanılır. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `19d3b60be18f5adcd659563329988bce2511a1b27b33fd0ab3a9d93e265557f2`
