# VideoGizliDeğişkeniniKırp

TrimVideoLatent düğümü, bir latent video temsilinin başlangıcından kareler kaldırır. Bir latent video örneği alır ve baştan belirtilen sayıda kareyi kırparak videonun geri kalan kısmını döndürür. Bu, ilk kareleri kaldırarak video dizilerini kısaltmanıza olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `samples` | Kırpılacak video karelerini içeren girdi latent video temsili | LATENT | Evet | - |
| `trim_amount` | Videonun başlangıcından kaldırılacak kare sayısı (varsayılan: 0) | INT | Evet | 0 to 99999 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Belirtilen sayıda kare başlangıçtan kaldırılmış, kırpılmış latent video temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimVideoLatent/tr.md)

---
**Source fingerprint (SHA-256):** `33b7a899f2002e9a7008f2ca93de853c08dd0629a4c6867fb42aae4ec2eb864b`
