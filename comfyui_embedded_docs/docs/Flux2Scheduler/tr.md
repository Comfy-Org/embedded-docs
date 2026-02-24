> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/tr.md)

Flux2Scheduler düğümü, Flux modeli için özel olarak tasarlanmış, gürültü giderme işlemi için bir gürültü seviyesi (sigmas) dizisi oluşturur. Görüntü oluşturma sırasında gürültü kaldırma ilerleyişini etkileyen, gürültü giderme adım sayısına ve hedef görüntünün boyutlarına dayalı bir zamanlama hesaplar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `steps` | INT | Evet | 1 - 4096 | Gerçekleştirilecek gürültü giderme adım sayısı. Daha yüksek bir değer genellikle daha detaylı sonuçlara yol açar ancak işlenmesi daha uzun sürer (varsayılan: 20). |
| `width` | INT | Evet | 16 - 16384 | Oluşturulacak görüntünün piksel cinsinden genişliği. Bu değer, gürültü zamanlama hesaplamasını etkiler (varsayılan: 1024). |
| `height` | INT | Evet | 16 - 16384 | Oluşturulacak görüntünün piksel cinsinden yüksekliği. Bu değer, gürültü zamanlama hesaplamasını etkiler (varsayılan: 1024). |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Örnekleyici için gürültü giderme zamanlamasını tanımlayan bir gürültü seviyesi değerleri (sigmas) dizisi. |
