> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/tr.md)

LTXVScheduler düğümü, özel örnekleme işlemleri için sigma değerleri üretir. Girdi gizli değişkenindeki token sayısına dayalı olarak gürültü zamanlama parametrelerini hesaplar ve örnekleme zamanlaması oluşturmak için bir sigmoid dönüşümü uygular. Düğüm isteğe bağlı olarak, elde edilen sigmaları belirli bir terminal değeriyle eşleşecek şekilde uzatabilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `adımlar` | INT | Evet | 1-10000 | Örnekleme adım sayısı (varsayılan: 20) |
| `maks_kaydırma` | FLOAT | Evet | 0.0-100.0 | Sigma hesaplaması için maksimum kaydırma değeri (varsayılan: 2.05) |
| `temel_kaydırma` | FLOAT | Evet | 0.0-100.0 | Sigma hesaplaması için temel kaydırma değeri (varsayılan: 0.95) |
| `uzatma` | BOOLEAN | Evet | Doğru/Yanlış | Sigmaları [terminal, 1] aralığına uzatır (varsayılan: Doğru) |
| `terminal` | FLOAT | Evet | 0.0-0.99 | Uzatma işleminden sonra sigmaların terminal değeri (varsayılan: 0.1) |
| `gizli` | LATENT | Hayır | - | Sigma ayarlaması için token sayısını hesaplamak üzere kullanılan isteğe bağlı gizli değişken girdisi |

**Not:** `latent` parametresi isteğe bağlıdır. Sağlanmadığında, düğüm hesaplamalar için varsayılan olarak 4096 token sayısını kullanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Örnekleme işlemi için oluşturulan sigma değerleri |