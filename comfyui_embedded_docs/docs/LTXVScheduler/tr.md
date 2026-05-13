> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/tr.md)

LTXVScheduler düğümü, özel örnekleme süreçleri için sigma değerleri üretir. Girdi latenti içindeki token sayısına bağlı olarak gürültü planı parametrelerini hesaplar ve örnekleme planını oluşturmak için bir sigmoid dönüşümü uygular. Düğüm, isteğe bağlı olarak elde edilen sigmaları belirtilen bir terminal değerine uyacak şekilde esnetebilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `adımlar` | INT | Evet | 1-10000 | Örnekleme adım sayısı (varsayılan: 20) |
| `maks_kaydırma` | FLOAT | Evet | 0.0-100.0 | Sigma hesaplaması için maksimum kaydırma değeri (varsayılan: 2.05) |
| `temel_kaydırma` | FLOAT | Evet | 0.0-100.0 | Sigma hesaplaması için temel kaydırma değeri (varsayılan: 0.95) |
| `uzatma` | BOOLEAN | Evet | True/False | Sigmaları [terminal, 1] aralığında olacak şekilde esnet (varsayılan: True) |
| `terminal` | FLOAT | Evet | 0.0-0.99 | Esnetme sonrası sigmaların terminal değeri (varsayılan: 0.1) |
| `gizli` | LATENT | Hayır | - | Sigma ayarı için token sayısını hesaplamak amacıyla kullanılan isteğe bağlı latent girdisi |

**Not:** `latent` parametresi isteğe bağlıdır. Sağlanmadığında, düğüm hesaplamalar için varsayılan token sayısı olan 4096'yı kullanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `sigmas` | SIGMAS | Örnekleme süreci için oluşturulan sigma değerleri |

---
**Source fingerprint (SHA-256):** `3c7e8721fd75bfb0a253c38cd29e2ee1905bfe08193aa97dbaa959550aba34bc`
