# TextEncodeBooguEdit

Bu düğüm, Boogu ile görüntü düzenleme için koşullandırmayı (conditioning) hazırlar. Referans görüntüleri işleyerek hem pozitif hem negatif koşullandırma çıktıları oluşturur. Referans görüntü iki kez kullanılır: görüntüden gelen görsel token'lar, düzenleme talimatını güçlendirmek için yalnızca pozitif koşullandırmaya eklenirken, bir VAE referans latent'i, CFG altında birbirini iptal edecek şekilde hem pozitif hem negatif koşullandırmaya eklenir ve orijinal görüntü kimliği korunur; tokenleştirici, görüntülerin varlığına ve boş negatif istemlere göre uygun sistem istemini otomatik olarak seçer.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | Metin kodlama için kullanılan CLIP modeli | CLIP | Evet | |
| `prompt` | İstenen düzenlemeyi tanımlayan metin istemi. Çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet | |
| `negative_prompt` | Düzenlemede kaçınılması gerekenleri tanımlayan metin istemi. Negatif koşullandırmayı bırakmak için boş bırakılabilir. Gelişmiş parametre. | STRING | Evet | |
| `vae` | Referans görüntüleri gizli uzaya (latent space) kodlamak için kullanılan VAE modeli. Koşullandırma çıktılarına referans latent'leri eklemek için gereklidir. | VAE | Hayır | |
| `images` | Düzenlenecek referans görüntü(ler). Boogu, örnek başına bir referansa odaklanır; daha fazlasına izin verilir. | IMAGE | Hayır | En fazla 16 görüntü |
Referans latent'ler, yalnızca `vae` en az bir referans `image` ile birlikte sağlandığında her iki koşullandırma çıktısına da eklenir. `vae` atlanırsa, pozitif çıktı yine de referans görüntülerden görsel token'ları alır, ancak hiçbir çıktı referans latent içermez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Görsel belirteçlerle birlikte metin istemini ve referans gizli değişkenlerini içeren koşullandırma | CONDITIONING |
| `negative` | Negatif metin istemini ve referans gizli değişkenlerini içeren koşullandırma | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeBooguEdit/tr.md)

---
**Source fingerprint (SHA-256):** `170979acf5b2e9f25f96231a4b23a4376cfddcd4bda2fdd6e03528417e6931b0`
