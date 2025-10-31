> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimVideoLatent/tr.md)

TrimVideoLatent düğümü, video latent temsilinin başından kareleri kaldırır. Bir latent video örneği alır ve başından belirtilen sayıda kareyi kesip atarak videonun kalan kısmını döndürür. Bu, başlangıç karelerini kaldırarak video dizilerini kısaltmanıza olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `örnekler` | LATENT | Evet | - | Kırpılacak video karelerini içeren girdi latent video temsili |
| `kırpma_miktarı` | INT | Hayır | 0 ila 99999 | Videonun başından kaldırılacak kare sayısı (varsayılan: 0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | LATENT | Başından belirtilen sayıda kare kaldırılmış, kırpılmış latent video temsili |