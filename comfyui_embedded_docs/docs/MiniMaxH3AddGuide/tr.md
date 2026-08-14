# MiniMaxH3AddGuide

Bu düğüm, bir MiniMax H3 videosunun seçilen herhangi bir karesine bir görüntü, kısa bir klip, ses veya film müziği içeren bir klibi sabitler. Belirtilen kare dizinine koşullandırmaya bir kılavuz ana kare ekler ve aynı videoda birden fazla kareyi sabitlemek için bu düğümlerden birkaçını zincirleyebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|---------|
| `positive` | Kılavuz ana karenin eklendiği koşullandırma. | CONDITIONING | Evet | - |
| `latent` | Hedef videoyu tanımlayan MiniMax H3 ses-video latent değeri. MiniMax H3 AV latent değeri olmalıdır (iç içe, her biri 24 kanallı iki 5D tensör). | LATENT | Evet | - |
| `frame_idx` | Görüntünün veya klibin ilk karesinin sabitleneceği kare dizini. Negatif değerler videonun sonundan itibaren sayılır. (varsayılan: 0) | INT | Evet | -9999 ile 9999 arası |
| `vae` | Video VAE'si, bir görüntü bağlandığında gereklidir. | VAE | Hayır | - |
| `audio_vae` | Ses VAE'si, bir ses bağlandığında gereklidir. | VAE | Hayır | - |
| `image` | Sabitlenecek görüntü veya video kareleri. Çok kareli gruplar bir klip olarak sabitlenir ve modelin geçerli klip uzunluklarına kırpılır: 5, 22, 39... (17k + 5) kare. 5 kareden kısa gruplar yalnızca ilk görüntüyü kullanır. | IMAGE | Hayır | - |
| `audio` | Aynı kare dizininden başlayarak sabitlenecek film müziği, videonun kalan süresine kırpılır. | AUDIO | Hayır | - |

**Kısıtlamalar:**
- `image` veya `audio` girdilerinden en az biri sağlanmalıdır; aksi takdirde düğüm bir hata verir.
- `image` bağlandığında `vae` gereklidir.
- `audio` bağlandığında `audio_vae` gereklidir.
- 5 kareden az olan `image` grupları yalnızca ilk görüntüyü kullanır; 5 veya daha fazla kare içeren gruplar geçerli bir klip uzunluğuna (5, 22, 39, vb.) kırpılır.
- `frame_idx`, kılavuzu videonun kare aralığına yerleştirmelidir ve çok kareli bir klip videoya tamamen sığmalıdır; aksi takdirde düğüm bir hata verir.
- Ses bağlandığında, kare dizini videonun ses parçasının sonunun ötesinde olmamalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Kılavuz ana kare eklenmiş koşullandırma; çözümlenmiş kare dizinini ve sağlandıysa kodlanmış görüntü veya ses latent değerlerini içerir. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3AddGuide/tr.md)

---
**Source fingerprint (SHA-256):** `7a2f742421cc2655bd9c914258801e4538f1554a7c5e2b0836b2df1577f5a104`
