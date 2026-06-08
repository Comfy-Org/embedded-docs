LaplaceScheduler düğümü, difüzyon örneklemesinde kullanılmak üzere bir Laplace dağılımını takip eden sigma değerleri dizisi oluşturur. Maksimumdan minimum değere kademeli olarak azalan bir gürültü seviyesi çizelgesi oluşturur ve ilerlemeyi kontrol etmek için Laplace dağılım parametrelerini kullanır. Bu zamanlayıcı, difüzyon modelleri için gürültü çizelgesini tanımlamak amacıyla özel örnekleme iş akışlarında yaygın olarak kullanılır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `adımlar` | Çizelgedeki örnekleme adım sayısı (varsayılan: 20) | INT | Evet | 1 ila 10000 |
| `sigma_maks` | Çizelgenin başlangıcındaki maksimum sigma değeri (varsayılan: 14,614642) | FLOAT | Evet | 0,0 ila 5000,0 |
| `sigma_min` | Çizelgenin sonundaki minimum sigma değeri (varsayılan: 0,0291675) | FLOAT | Evet | 0,0 ila 5000,0 |
| `mu` | Laplace dağılımı için ortalama parametresi (varsayılan: 0,0) | FLOAT | Evet | -10,0 ila 10,0 |
| `beta` | Laplace dağılımı için ölçek parametresi (varsayılan: 0,5) | FLOAT | Evet | 0,0 ila 10,0 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `SIGMAS` | Bir Laplace dağılımı çizelgesini takip eden sigma değerleri dizisi | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/tr.md)

---
**Source fingerprint (SHA-256):** `9d8cacb93d0bb1872a368821fd3cad5d6d373817a923436af9f62a7648d5d735`
