# LaplaceZamanlayıcı

LaplaceScheduler düğümü, difüzyon örneklemesinde kullanılmak üzere Laplace dağılımını izleyen bir sigma değerleri dizisi üretir. Maksimumdan minimum değere kademeli olarak azalan bir gürültü seviyesi çizelgesi oluşturur ve ilerlemeyi kontrol etmek için Laplace dağılımı parametrelerini kullanır. Bu zamanlayıcı, özel örnekleme iş akışlarında difüzyon modelleri için gürültü çizelgesini tanımlamak amacıyla yaygın olarak kullanılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `adımlar` | Çizelgedeki örnekleme adım sayısı (varsayılan: 20) | INT | Evet | 1 ila 10000 |
| `sigma_maks` | Çizelgenin başlangıcındaki maksimum sigma değeri (varsayılan: 14.614642) | FLOAT | Evet | 0.0 ila 5000.0 |
| `sigma_min` | Çizelgenin sonundaki minimum sigma değeri (varsayılan: 0.0291675) | FLOAT | Evet | 0.0 ila 5000.0 |
| `mu` | Laplace dağılımı için ortalama parametresi (varsayılan: 0.0) | FLOAT | Evet | -10.0 ila 10.0 |
| `beta` | Laplace dağılımı için ölçek parametresi (varsayılan: 0.5) | FLOAT | Evet | 0.0 ila 10.0 |

Not: `sigma_max`, `sigma_min`, `mu` ve `beta` gelişmiş parametrelerdir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `SIGMAS` | Laplace dağılımı çizelgesini izleyen bir sigma değerleri dizisi | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/tr.md)

---
**Source fingerprint (SHA-256):** `8e5ca00f4797f863a2cf8b9b115ec27beb7f65981cbb04eb036150402fc19389`
