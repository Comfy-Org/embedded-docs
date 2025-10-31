> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/tr.md)

WanPhantomSubjectToVideo düğümü, koşullandırma girdilerini ve isteğe bağlı referans görüntülerini işleyerek video içeriği oluşturur. Video üretimi için gizli temsiller oluşturur ve sağlandığında girdi görüntülerinden görsel rehberlik dahil edebilir. Düğüm, video modelleri için zaman-boyutlu birleştirme ile koşullandırma verilerini hazırlar ve değiştirilmiş koşullandırmayı, üretilen gizli video verileriyle birlikte çıktı olarak verir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Video üretimini yönlendirmek için pozitif koşullandırma girdisi |
| `negative` | CONDITIONING | Evet | - | Belirli özelliklerden kaçınmak için negatif koşullandırma girdisi |
| `vae` | VAE | Evet | - | Görüntüler sağlandığında onları kodlamak için VAE modeli |
| `width` | INT | Hayır | 16'dan MAX_RESOLUTION'a | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, 16'ya bölünebilir olmalı) |
| `height` | INT | Hayır | 16'dan MAX_RESOLUTION'a | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalı) |
| `length` | INT | Hayır | 1'den MAX_RESOLUTION'a | Üretilen videodaki kare sayısı (varsayılan: 81, 4'e bölünebilir olmalı) |
| `batch_size` | INT | Hayır | 1'den 4096'ya | Aynı anda üretilecek video sayısı (varsayılan: 1) |
| `images` | IMAGE | Hayır | - | Zaman-boyutlu koşullandırma için isteğe bağlı referans görüntüleri |

**Not:** `images` sağlandığında, belirtilen `width` ve `height` değerleriyle eşleşecek şekilde otomatik olarak yukarı ölçeklenir ve işleme için yalnızca ilk `length` kare kullanılır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Görüntüler sağlandığında zaman-boyutlu birleştirme ile değiştirilmiş pozitif koşullandırma |
| `negative_text` | CONDITIONING | Görüntüler sağlandığında zaman-boyutlu birleştirme ile değiştirilmiş negatif koşullandırma |
| `negative_img_text` | CONDITIONING | Görüntüler sağlandığında zaman-boyutlu birleştirme sıfırlanmış negatif koşullandırma |
| `latent` | LATENT | Belirtilen boyutlar ve uzunlukta üretilmiş gizli video temsili |