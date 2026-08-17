# LTXVZamanlayıcı

LTXVScheduler düğümü, özel örnekleme süreçleri için sigma değerleri üretir. Girdi latentindeki token sayısına bağlı olarak gürültü planı parametrelerini hesaplar ve örnekleme planını oluşturmak için bir sigmoid dönüşümü uygular. Düğüm, isteğe bağlı olarak elde edilen sigmaları belirtilen bir terminal değerine uyacak şekilde uzatabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `steps` | Örnekleme adım sayısı (varsayılan: 20) | INT | Evet | 1-10000 |
| `max_shift` | Sigma hesaplaması için maksimum kaydırma değeri (varsayılan: 2.05) | FLOAT | Evet | 0.0-100.0 |
| `base_shift` | Sigma hesaplaması için temel kaydırma değeri (varsayılan: 0.95) | FLOAT | Evet | 0.0-100.0 |
| `stretch` | Sigmaları [terminal, 1] aralığında olacak şekilde uzat (varsayılan: True) | BOOLEAN | Evet | True/False |
| `terminal` | Uzatma sonrası sigmaların terminal değeri (varsayılan: 0.1) | FLOAT | Evet | 0.0-0.99 |
| `latent` | Sigma ayarlaması için token sayısını hesaplamakta kullanılan isteğe bağlı latent girdisi | LATENT | Hayır | - |

**Not:** `latent` parametresi isteğe bağlıdır. Sağlanmadığında, düğüm hesaplamalar için varsayılan 4096 token sayısını kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Örnekleme süreci için üretilen sigma değerleri | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/tr.md)

---
**Source fingerprint (SHA-256):** `5b4907e905e27a951c332c400e24023ef089df7a5f4a17b1fc8ba42a41302399`
