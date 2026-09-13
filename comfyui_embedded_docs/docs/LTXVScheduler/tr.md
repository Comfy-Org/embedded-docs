# LTXVZamanlayıcı

LTXVScheduler düğümü, özel bir örnekleme süreci için sigma değerleri üretir. Gürültü çizelgesini, sağlanan latentteki token sayısından hesaplar veya hiçbir latent bağlı olmadığında varsayılan olarak 4096 token kullanır; ayrıca isteğe bağlı olarak, son değer belirtilen `terminal` değeriyle eşleşecek şekilde sigma değerlerini gerebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `adımlar` | Örnekleme adımı sayısı (varsayılan: 20) | INT | Evet | 1-10000 |
| `maks_kaydırma` | Sigma hesaplamasında kullanılan maksimum kaydırma değeri (varsayılan: 2.05) | FLOAT | Evet | 0.0-100.0 (step: 0.01) |
| `temel_kaydırma` | Sigma hesaplamasında kullanılan temel kaydırma değeri (varsayılan: 0.95) | FLOAT | Evet | 0.0-100.0 (step: 0.01) |
| `uzatma` | Sigma değerlerini [terminal, 1] aralığında olacak şekilde gerin (varsayılan: True) | BOOLEAN | Evet | True/False |
| `terminal` | Gerinme sonrasında sigma değerlerinin terminal değeri (varsayılan: 0.1). Yalnızca `stretch` etkinleştirildiğinde kullanılır. | FLOAT | Evet | 0.0-0.99 (step: 0.01) |
| `gizli` | Sigma ayarı için token sayısını hesaplamakta kullanılan isteğe bağlı latent girdisi. Sağlanmadığında varsayılan 4096 token sayısı kullanılır. | LATENT | Hayır | - |

**Not:** `stretch` etkinleştirildiğinde, sıfır olmayan sigma değerleri yeniden ölçeklendirilir; böylece son sıfır olmayan sigma değeri, `terminal` değerine eşit olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Örnekleme süreci için üretilen sigma değerleri | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/tr.md)

---
**Source fingerprint (SHA-256):** `5b4907e905e27a951c332c400e24023ef089df7a5f4a17b1fc8ba42a41302399`
