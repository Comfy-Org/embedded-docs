# MiniMax H3 için Kılavuz Ekle

Bu düğüm, bir görüntüyü, kısa bir klibi, sesi veya ses parçasıyla birlikte bir klibi MiniMax H3 videosunun herhangi bir karesine sabitler. Seçilen kare indeksinde koşullandırmaya bir kılavuz anahtar karesi ekler ve aynı videoda birkaç kareyi sabitlemek için birkaç düğümü zincirleyebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `positive` | Kılavuz anahtar karesinin eklendiği koşullandırma. | CONDITIONING | Evet | - |
| `vae` | Görüntü bağlandığında gerekli olan video VAE'si. | VAE | Hayır | - |
| `audio_vae` | Ses bağlandığında gerekli olan ses VAE'si. | VAE | Hayır | - |
| `latent` | Hedef videoyu tanımlayan MiniMax H3 ses-video latent değeri. MiniMax H3 AV latent olmalıdır (iç içe, iki adet 5D tensör içerir; video tensörü 24 kanallıdır). | LATENT | Evet | - |
| `image` | Sabitlenecek görüntü veya video kareleri. Çok kareli gruplar bir klip olarak sabitlenir ve modelin geçerli klip uzunluklarına kırpılır: 5, 22, 39... (17k + 5) kare. 5 kareden kısa gruplarda yalnızca ilk görüntü kullanılır. | IMAGE | Hayır | - |
| `audio` | Aynı kare indeksinden başlayarak sabitlenecek ses parçası; videonun kalan süresine kırpılır. | AUDIO | Hayır | - |
| `frame_idx` | Görüntünün veya klibin ilk karesinin sabitleneceği kare indeksi. Negatif değerler videonun sonundan itibaren sayılır. (varsayılan: 0) | INT | Evet | -9999 ile 9999 |

**Kısıtlamalar:**
- En az bir `image` veya `audio` sağlanmalıdır; aksi halde düğüm bir hata verir.
- `image` bağlandığında `vae` gereklidir.
- `audio` bağlandığında `audio_vae` gereklidir.
- 5 kareden az `image` grubu yalnızca ilk görüntüyü kullanır; 5 veya daha fazla kare içeren gruplar geçerli bir klip uzunluğuna (5, 22, 39 vb.) kırpılır.
- `frame_idx`, kılavuzu videonun kare aralığı içine yerleştirmelidir ve çok kareli bir klip videoya tamamen sığmalıdır; aksi halde düğüm bir hata verir.
- Ses bağlandığında, kare indeksi videonun ses parçasının sonunu geçmemelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Kılavuz anahtar karesi eklenmiş koşullandırma; çözümlenmiş kare indeksini ve sağlandığında kodlanmış görüntü veya ses latentlerini içerir. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3AddGuide/tr.md)

---
**Source fingerprint (SHA-256):** `7a2f742421cc2655bd9c914258801e4538f1554a7c5e2b0836b2df1577f5a104`
