> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/tr.md)

Kandinsky5ImageToVideo düğümü, Kandinsky modelini kullanarak video oluşturma için koşullandırma ve gizli uzay verilerini hazırlar. Boş bir video gizli tensörü oluşturur ve isteğe bağlı olarak, oluşturulan videonun ilk karelerini yönlendirmek için bir başlangıç görüntüsünü kodlayarak pozitif ve negatif koşullandırmayı buna göre değiştirebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pozitif` | CONDITIONING | Evet | Yok | Video oluşturmayı yönlendirecek pozitif koşullandırma istemleri. |
| `negatif` | CONDITIONING | Evet | Yok | Video oluşturmayı belirli kavramlardan uzaklaştıracak negatif koşullandırma istemleri. |
| `vae` | VAE | Evet | Yok | İsteğe bağlı başlangıç görüntüsünü gizli uzaya kodlamak için kullanılan VAE modeli. |
| `genişlik` | INT | Hayır | 16 ila 8192 (adım 16) | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 768). |
| `yükseklik` | INT | Hayır | 16 ila 8192 (adım 16) | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 512). |
| `uzunluk` | INT | Hayır | 1 ila 8192 (adım 4) | Videodaki kare sayısı (varsayılan: 121). |
| `toplu_boyutu` | INT | Hayır | 1 ila 4096 | Aynı anda oluşturulacak video dizisi sayısı (varsayılan: 1). |
| `başlangıç_görseli` | IMAGE | Hayır | Yok | İsteğe bağlı bir başlangıç görüntüsü. Sağlanırsa, kodlanır ve modelin çıktı gizli değişkenlerinin gürültülü başlangıcını değiştirmek için kullanılır. |

**Not:** Bir `start_image` sağlandığında, çift doğrusal enterpolasyon kullanılarak belirtilen `width` ve `height` değerlerine otomatik olarak yeniden boyutlandırılır. Görüntü grubunun ilk `length` karesi kodlama için kullanılır. Kodlanmış gizli değişken daha sonra videonun ilk görünümünü yönlendirmek için hem `positive` hem de `negative` koşullandırmaya enjekte edilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | Kodlanmış başlangıç görüntü verileriyle potansiyel olarak güncellenmiş, değiştirilmiş pozitif koşullandırma. |
| `latent` | CONDITIONING | Kodlanmış başlangıç görüntü verileriyle potansiyel olarak güncellenmiş, değiştirilmiş negatif koşullandırma. |
| `cond_latent` | LATENT | Belirtilen boyutlar için şekillendirilmiş, sıfırlarla dolu boş bir video gizli tensörü. |
| `cond_latent` | LATENT | Sağlanan başlangıç görüntülerinin temiz, kodlanmış gizli temsili. Bu, oluşturulan video gizli değişkenlerinin gürültülü başlangıcını değiştirmek için dahili olarak kullanılır. |

---
**Source fingerprint (SHA-256):** `19d3b60be18f5adcd659563329988bce2511a1b27b33fd0ab3a9d93e265557f2`
