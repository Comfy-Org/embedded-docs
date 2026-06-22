# WanPhantomSubjectToVideo

WanPhantomSubjectToVideo düğümü, koşullandırma girdilerini ve isteğe bağlı referans görüntülerini işleyerek video içeriği oluşturur. Video oluşturma için gizli temsiller oluşturur ve sağlandığında girdi görüntülerinden görsel yönlendirme ekleyebilir. Düğüm, video modelleri için zaman boyutlu birleştirme ile koşullandırma verilerini hazırlar ve oluşturulan gizli video verileriyle birlikte değiştirilmiş koşullandırmayı çıktı olarak verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video oluşturmayı yönlendirmek için pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negatif` | Belirli özelliklerden kaçınmak için negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `vae` | Sağlandığında görüntüleri kodlamak için VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 ile MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 ile MAX_RESOLUTION |
| `uzunluk` | Oluşturulan videodaki kare sayısı (varsayılan: 81, 4'e bölünebilir olmalıdır) | INT | Evet | 1 ile MAX_RESOLUTION |
| `toplu_iş_boyutu` | Aynı anda oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `görseller` | Zaman boyutlu koşullandırma için isteğe bağlı referans görüntüleri | IMAGE | Hayır | - |

**Not:** `images` sağlandığında, belirtilen `width` ve `height` değerlerine uyacak şekilde otomatik olarak yükseltilir ve işleme için yalnızca ilk `length` karesi kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `negatif_metin` | Görüntüler sağlandığında zaman boyutlu birleştirme ile değiştirilmiş pozitif koşullandırma | CONDITIONING |
| `negatif_img_metin` | Görüntüler sağlandığında zaman boyutlu birleştirme ile değiştirilmiş negatif koşullandırma | CONDITIONING |
| `gizli` | Görüntüler sağlandığında sıfırlanmış zaman boyutlu birleştirme ile negatif koşullandırma | CONDITIONING |
| `latent` | Belirtilen boyutlar ve uzunluk ile oluşturulmuş gizli video temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `2e3e8277dca9e998220fc5939c2cc72fdc15e80cc4b95daa33f5b92e2270dd73`
