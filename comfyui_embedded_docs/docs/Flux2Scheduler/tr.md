# Flux2Scheduler

Flux2Scheduler düğümü, gürültü giderme işlemi için Flux2 modeline özel olarak uyarlanmış bir dizi gürültü seviyesi (sigma) üretir. Gürültü giderme adımlarının sayısına ve hedef görüntünün boyutlarına dayalı olarak bir zamanlama hesaplar; bu da görüntü üretimi sırasında gürültü gidermenin ilerleyişini etkiler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `steps` | Gerçekleştirilecek gürültü giderme adımı sayısı. Daha yüksek bir değer genellikle daha ayrıntılı sonuçlar sağlar ancak işlemin daha uzun sürmesine neden olur (varsayılan: 20). | INT | Evet | 1 - 4096 |
| `width` | Üretilecek görüntünün piksel cinsinden genişliği. Bu değer gürültü zamanlaması hesaplamasını etkiler (varsayılan: 1024). | INT | Evet | 16 - 16384 (MAX_RESOLUTION) |
| `height` | Üretilecek görüntünün piksel cinsinden yüksekliği. Bu değer gürültü zamanlaması hesaplamasını etkiler (varsayılan: 1024). | INT | Evet | 16 - 16384 (MAX_RESOLUTION) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Örnekleyici için gürültü giderme zamanlamasını tanımlayan bir dizi gürültü seviyesi değeri (sigma). Çıktı, adım sayısından bir fazla değer içerir (`steps + 1`). | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/tr.md)

---
**Source fingerprint (SHA-256):** `9606177f37f7bc03aef524623f03b7f24bcdc3d9327dcdf74863fe2befeb2b65`
