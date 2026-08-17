# WanPhantomSubjectToVideo

The WanPhantomSubjectToVideo düğümü, koşullandırma girdilerini ve isteğe bağlı referans görüntülerini işleyerek video içeriği üretir. Video üretimi için latent temsiller oluşturur ve sağlandığında giriş görüntülerinden görsel rehberlik ekleyebilir. Düğüm, Wan video modelleri için zamansal boyutlu birleştirme ile koşullandırma verilerini hazırlar ve değiştirilmiş koşullandırmanın yanı sıra üretilen latent video verisini çıktı olarak verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Video üretimini yönlendirmek için pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negative` | Belirli özelliklerden kaçınmak için negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `vae` | Sağlandığında görüntüleri kodlamak için VAE modeli | VAE | Evet | - |
| `width` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, 16'ya bölünebilmelidir) | INT | Evet | 16 - MAX_RESOLUTION |
| `height` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilmelidir) | INT | Evet | 16 - MAX_RESOLUTION |
| `length` | Üretilen videodaki kare sayısı (varsayılan: 81, 4'e bölünebilmelidir) | INT | Evet | 1 - MAX_RESOLUTION |
| `batch_size` | Aynı anda üretilecek video sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |
| `images` | Zamansal boyutlu koşullandırma için isteğe bağlı referans görüntüleri | IMAGE | Hayır | - |

**Not:** `images` sağlandığında, görüntüler belirtilen `width` ve `height` ile eşleşecek şekilde otomatik olarak büyütülür ve işleme için yalnızca ilk `length` kare kullanılır. Her görüntü, VAE tarafından kodlanmadan önce ilk 3 renk kanalına indirgenir. `images` sağlanmadığında, koşullandırma girdileri değiştirilmeden geçer.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Görüntüler sağlandığında zamansal boyutlu birleştirme ile değiştirilmiş pozitif koşullandırma | CONDITIONING |
| `negative_text` | Görüntüler sağlandığında zamansal boyutlu birleştirme ile değiştirilmiş negatif koşullandırma | CONDITIONING |
| `negative_img_text` | Görüntüler sağlandığında sıfırlanmış zamansal boyutlu birleştirme ile negatif koşullandırma | CONDITIONING |
| `latent` | 16 kanallı, zamansal boyutu ((length - 1) // 4) + 1 ve uzamsal boyutları height // 8 ve width // 8 olan sıfır dolu latent video gösterimi | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
