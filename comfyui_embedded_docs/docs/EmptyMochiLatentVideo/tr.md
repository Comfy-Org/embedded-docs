# BoşMochiGizliVideo

EmptyMochiLatentVideo, belirttiğiniz boyutlarla boş bir latent video tensörü oluşturur. Video oluşturma iş akışları için başlangıç noktası olarak kullanılabilecek, sıfırlarla doldurulmuş bir latent temsil üretir. Düğüm, latent video tensörünün genişliğini, yüksekliğini, uzunluğunu ve toplu iş boyutunu tanımlamanıza olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Latent videonun piksel cinsinden genişliği (varsayılan: 848, değerler 16'lık adımlarla artar) | INT | Evet | 16 - MAX_RESOLUTION |
| `yükseklik` | Latent videonun piksel cinsinden yüksekliği (varsayılan: 480, değerler 16'lık adımlarla artar) | INT | Evet | 16 - MAX_RESOLUTION |
| `uzunluk` | Latent videodaki kare sayısı (varsayılan: 25, değerler 7'den başlayarak 6'lık adımlarla artar) | INT | Evet | 7 - MAX_RESOLUTION |
| `toplu_boyut` | Bir toplu işte oluşturulacak latent video sayısı (varsayılan: 1) | INT | Hayır | 1 - 4096 |

**Not:** Gerçek latent boyutları width/8 ve height/8 olarak hesaplanır, zamansal boyut `((length - 1) // 6) + 1` olarak hesaplanır ve tensör 12 kanala sahiptir. `length` 7'den başlayarak 6'lık adımlarla ilerlediğinden geçerli değerler 7, 13, 19, 25 vb.'dir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Belirtilen boyutlara sahip, tamamen sıfırlardan oluşan boş bir latent video tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/tr.md)

---
**Source fingerprint (SHA-256):** `1774e1b54b429a946172ba9f609b433d99c0ca2ced2d9e0e3b0b85c82e5141b2`
