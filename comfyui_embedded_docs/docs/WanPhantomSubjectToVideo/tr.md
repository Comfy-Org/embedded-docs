> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/tr.md)

WanPhantomSubjectToVideo düğümü, koşullandırma girdilerini ve isteğe bağlı referans görüntülerini işleyerek video içeriği oluşturur. Video oluşturma için gizli temsiller oluşturur ve sağlandığında girdi görüntülerinden görsel yönlendirme ekleyebilir. Düğüm, video modelleri için zaman boyutlu birleştirme ile koşullandırma verilerini hazırlar ve oluşturulan gizli video verileriyle birlikte değiştirilmiş koşullandırmayı çıktı olarak verir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `pozitif` | CONDITIONING | Evet | - | Video oluşturmayı yönlendirmek için pozitif koşullandırma girdisi |
| `negatif` | CONDITIONING | Evet | - | Belirli özelliklerden kaçınmak için negatif koşullandırma girdisi |
| `vae` | VAE | Evet | - | Sağlandığında görüntüleri kodlamak için VAE modeli |
| `genişlik` | INT | Evet | 16 ile MAX_RESOLUTION | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, 16'ya bölünebilir olmalıdır) |
| `yükseklik` | INT | Evet | 16 ile MAX_RESOLUTION | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalıdır) |
| `uzunluk` | INT | Evet | 1 ile MAX_RESOLUTION | Oluşturulan videodaki kare sayısı (varsayılan: 81, 4'e bölünebilir olmalıdır) |
| `toplu_iş_boyutu` | INT | Evet | 1 ile 4096 | Aynı anda oluşturulacak video sayısı (varsayılan: 1) |
| `görseller` | IMAGE | Hayır | - | Zaman boyutlu koşullandırma için isteğe bağlı referans görüntüleri |

**Not:** `images` sağlandığında, belirtilen `width` ve `height` değerlerine uyacak şekilde otomatik olarak yükseltilir ve işleme için yalnızca ilk `length` karesi kullanılır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `negatif_metin` | CONDITIONING | Görüntüler sağlandığında zaman boyutlu birleştirme ile değiştirilmiş pozitif koşullandırma |
| `negatif_img_metin` | CONDITIONING | Görüntüler sağlandığında zaman boyutlu birleştirme ile değiştirilmiş negatif koşullandırma |
| `gizli` | CONDITIONING | Görüntüler sağlandığında sıfırlanmış zaman boyutlu birleştirme ile negatif koşullandırma |
| `latent` | LATENT | Belirtilen boyutlar ve uzunluk ile oluşturulmuş gizli video temsili |

---
**Source fingerprint (SHA-256):** `2e3e8277dca9e998220fc5939c2cc72fdc15e80cc4b95daa33f5b92e2270dd73`
