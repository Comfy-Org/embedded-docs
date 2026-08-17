# BoşMochiGizliVideo

EmptyMochiLatentVideo düğümü, belirtilen boyutlarda boş bir latent video tensörü oluşturur. Video üretim iş akışları için başlangıç noktası olarak kullanılabilen sıfırlarla doldurulmuş bir latent temsil üretir. Düğüm, latent video tensörü için genişlik, yükseklik, uzunluk ve batch boyutunu tanımlamanıza olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `width` | Latent videonun piksel cinsinden genişliği (varsayılan: 848, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 ila MAX_RESOLUTION |
| `height` | Latent videonun piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 ila MAX_RESOLUTION |
| `length` | Latent videodaki kare sayısı (varsayılan: 25, `(length - 1)` ifadesi 6'ya bölünebilir olmalıdır) | INT | Evet | 7 ila MAX_RESOLUTION |
| `batch_size` | Bir batch içinde üretilecek latent video sayısı (varsayılan: 1) | INT | Hayır | 1 ila 4096 |

**Not:** Düğüm, girdinin uzamsal ve zamansal boyutlarını sıkıştırır. Latent genişlik ve yükseklik, `width / 8` ve `height / 8` olarak hesaplanır ve zamansal boyut `((length - 1) // 6) + 1` olarak hesaplanır. `length` parametresi, `(length - 1)` ifadesinin 6'ya bölünebilir olmasını gerektirir; yani geçerli değerler 7, 13, 19, 25 vb.'dir. Ortaya çıkan latent tensör, 12 kanala ve `(batch_size, 12, ((length - 1) // 6) + 1, height // 8, width // 8)` şeklinde bir nihai boyuta sahiptir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Belirtilen boyutlarda, tümü sıfırlardan oluşan boş bir latent video tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/tr.md)

---
**Source fingerprint (SHA-256):** `1774e1b54b429a946172ba9f609b433d99c0ca2ced2d9e0e3b0b85c82e5141b2`
