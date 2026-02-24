> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/tr.md)

Kandinsky5ImageToVideo düğümü, Kandinsky modelini kullanarak video üretimi için koşullandırma ve gizli uzay verilerini hazırlar. Boş bir video gizli tensörü oluşturur ve isteğe bağlı olarak bir başlangıç görüntüsünü kodlayarak üretilen videonun ilk karelerine rehberlik edebilir ve buna göre pozitif ve negatif koşullandırmayı değiştirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | Yok | Video üretimine rehberlik edecek pozitif koşullandırma istemleri. |
| `negative` | CONDITIONING | Evet | Yok | Video üretimini belirli kavramlardan uzaklaştıracak negatif koşullandırma istemleri. |
| `vae` | VAE | Evet | Yok | İsteğe bağlı başlangıç görüntüsünü gizli uzaya kodlamak için kullanılan VAE modeli. |
| `width` | INT | Hayır | 16 ila 8192 (adım 16) | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 768). |
| `height` | INT | Hayır | 16 ila 8192 (adım 16) | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 512). |
| `length` | INT | Hayır | 1 ila 8192 (adım 4) | Videodaki kare sayısı (varsayılan: 121). |
| `batch_size` | INT | Hayır | 1 ila 4096 | Aynı anda üretilecek video dizisi sayısı (varsayılan: 1). |
| `start_image` | IMAGE | Hayır | Yok | İsteğe bağlı bir başlangıç görüntüsü. Sağlanırsa, kodlanır ve modelin çıktı gizli değerlerinin gürültülü başlangıcını değiştirmek için kullanılır. |

**Not:** Bir `start_image` sağlandığında, belirtilen `width` ve `height` değerleriyle eşleşecek şekilde otomatik olarak çift doğrusal enterpolasyon kullanılarak yeniden boyutlandırılır. Görüntü grubunun ilk `length` karesi kodlama için kullanılır. Kodlanmış gizli değer daha sonra, videonun başlangıç görünümüne rehberlik etmesi için hem `positive` hem de `negative` koşullandırmaya enjekte edilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Kodlanmış başlangıç görüntüsü verileriyle potansiyel olarak güncellenmiş, değiştirilmiş pozitif koşullandırma. |
| `negative` | CONDITIONING | Kodlanmış başlangıç görüntüsü verileriyle potansiyel olarak güncellenmiş, değiştirilmiş negatif koşullandırma. |
| `latent` | LATENT | Belirtilen boyutlar için şekillendirilmiş, sıfırlarla dolu boş bir video gizli tensörü. |
| `cond_latent` | LATENT | Sağlanan başlangıç görüntülerinin temiz, kodlanmış gizli temsili. Bu, üretilen video gizli değerlerinin gürültülü başlangıcını değiştirmek için dahili olarak kullanılır. |
