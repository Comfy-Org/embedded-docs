# Flux2Scheduler

Flux2Scheduler düğümü, özellikle Flux modeli için uyarlanmış, gürültü giderme işlemi için bir dizi gürültü seviyesi (sigma) üretir. Bu düğüm, gürültü giderme adımlarının sayısına ve hedef görüntünün boyutlarına bağlı olarak bir zamanlama hesaplar; bu da görüntü oluşturma sırasında gürültü giderme ilerlemesini etkiler.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `adım` | Gerçekleştirilecek gürültü giderme adım sayısı. Daha yüksek bir değer genellikle daha ayrıntılı sonuçlar verir ancak işlemin daha uzun sürmesine neden olur (varsayılan: 20). | INT | Evet | 1 ila 4096 |
| `genişlik` | Oluşturulacak görüntünün piksel cinsinden genişliği. Bu değer, gürültü zamanlaması hesaplamasını etkiler (varsayılan: 1024). | INT | Evet | 16 ila 16384 |
| `yükseklik` | Oluşturulacak görüntünün piksel cinsinden yüksekliği. Bu değer, gürültü zamanlaması hesaplamasını etkiler (varsayılan: 1024). | INT | Evet | 16 ila 16384 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Örnekleyici için gürültü giderme zamanlamasını tanımlayan bir dizi gürültü seviyesi değeri (sigma). | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/tr.md)

---
**Source fingerprint (SHA-256):** `dbe44a6eb454dd61ab22df5770ad5ac559e03b20fd36d17d33730cdb835f7ede`
