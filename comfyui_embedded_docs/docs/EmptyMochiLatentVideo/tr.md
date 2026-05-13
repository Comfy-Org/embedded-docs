> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/tr.md)

EmptyMochiLatentVideo düğümü, belirtilen boyutlarda boş bir latent video tensörü oluşturur. Video oluşturma iş akışları için başlangıç noktası olarak kullanılabilecek sıfır dolu bir latent temsil üretir. Bu düğüm, latent video tensörü için genişlik, yükseklik, uzunluk ve toplu iş boyutunu tanımlamanıza olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `genişlik` | INT | Evet | 16 ile MAX_RESOLUTION arası | Latent videonun piksel cinsinden genişliği (varsayılan: 848, 16'ya bölünebilir olmalıdır) |
| `yükseklik` | INT | Evet | 16 ile MAX_RESOLUTION arası | Latent videonun piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalıdır) |
| `uzunluk` | INT | Evet | 7 ile MAX_RESOLUTION arası | Latent videodaki kare sayısı (varsayılan: 25, 1 çıkarıldıktan sonra 6'ya bölünebilir olmalıdır) |
| `toplu_boyut` | INT | Hayır | 1 ile 4096 arası | Bir toplu işlemde oluşturulacak latent video sayısı (varsayılan: 1) |

**Not:** Gerçek latent boyutları genişlik/8 ve yükseklik/8 olarak hesaplanır; zamansal boyut ise ((uzunluk - 1) // 6) + 1 olarak hesaplanır. `length` parametresi, `(length - 1)` ifadesinin 6'ya bölünebilir olmasını gerektirir; yani geçerli değerler 7, 13, 19, 25 vb. şeklindedir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `samples` | LATENT | Belirtilen boyutlarda, tamamı sıfırlardan oluşan boş bir latent video tensörü |

---
**Source fingerprint (SHA-256):** `6876a739355b2dcde42f8c02eb67405678798b818865ec1a73e19076b738554b`
