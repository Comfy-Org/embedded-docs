# BoşMochiGizliVideo

EmptyMochiLatentVideo, belirttiğiniz boyutlarda boş bir latent video tensörü oluşturur. Video oluşturma iş akışları için başlangıç noktası olarak kullanılabilen, sıfırlarla doldurulmuş bir latent gösterim üretir. Düğüm, latent video tensörünün genişliğini, yüksekliğini, uzunluğunu ve yığın boyutunu tanımlamanıza olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Latent videonun piksel cinsinden genişliği (varsayılan: 848, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 to MAX_RESOLUTION |
| `yükseklik` | Latent videonun piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 to MAX_RESOLUTION |
| `uzunluk` | Latent videodaki kare sayısı (varsayılan: 25, `(length - 1)` ifadesi 6'ya bölünebilmelidir) | INT | Evet | 7 to MAX_RESOLUTION |
| `toplu_boyut` | Bir yığında (batch) oluşturulacak latent video sayısı (varsayılan: 1) | INT | Hayır | 1 ile 4096 |

**Not:** Gerçek latent boyutları width/8 ve height/8 olarak hesaplanır, zamansal boyut `((length - 1) // 6) + 1` olarak hesaplanır ve tensör 12 kanala sahiptir. `length` parametresi, `(length - 1)` ifadesinin 6'ya bölünebilmesini sağlamalıdır; yani geçerli değerler 7, 13, 19, 25 vb. şeklindedir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Belirtilen boyutlarda, tamamı sıfırlardan oluşan boş latent video tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/tr.md)

---
**Source fingerprint (SHA-256):** `1774e1b54b429a946172ba9f609b433d99c0ca2ced2d9e0e3b0b85c82e5141b2`
