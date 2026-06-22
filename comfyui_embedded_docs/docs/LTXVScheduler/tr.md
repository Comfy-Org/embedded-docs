# LTXVZamanlayıcı

LTXVScheduler düğümü, özel örnekleme süreçleri için sigma değerleri üretir. Girdi latenti içindeki token sayısına bağlı olarak gürültü planı parametrelerini hesaplar ve örnekleme planını oluşturmak için bir sigmoid dönüşümü uygular. Düğüm, isteğe bağlı olarak elde edilen sigmaları belirtilen bir terminal değerine uyacak şekilde esnetebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `adımlar` | Örnekleme adım sayısı (varsayılan: 20) | INT | Evet | 1-10000 |
| `maks_kaydırma` | Sigma hesaplaması için maksimum kaydırma değeri (varsayılan: 2.05) | FLOAT | Evet | 0.0-100.0 |
| `temel_kaydırma` | Sigma hesaplaması için temel kaydırma değeri (varsayılan: 0.95) | FLOAT | Evet | 0.0-100.0 |
| `uzatma` | Sigmaları [terminal, 1] aralığında olacak şekilde esnet (varsayılan: True) | BOOLEAN | Evet | True/False |
| `terminal` | Esnetme sonrası sigmaların terminal değeri (varsayılan: 0.1) | FLOAT | Evet | 0.0-0.99 |
| `gizli` | Sigma ayarı için token sayısını hesaplamak amacıyla kullanılan isteğe bağlı latent girdisi | LATENT | Hayır | - |

**Not:** `latent` parametresi isteğe bağlıdır. Sağlanmadığında, düğüm hesaplamalar için varsayılan token sayısı olan 4096'yı kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Örnekleme süreci için oluşturulan sigma değerleri | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/tr.md)

---
**Source fingerprint (SHA-256):** `3c7e8721fd75bfb0a253c38cd29e2ee1905bfe08193aa97dbaa959550aba34bc`
