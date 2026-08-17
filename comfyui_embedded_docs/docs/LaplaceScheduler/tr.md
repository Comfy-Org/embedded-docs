# LaplaceZamanlayıcı

LaplaceScheduler düğümü, difüzyon örneklemesinde kullanılmak üzere Laplace dağılımını takip eden bir sigma değerleri dizisi üretir. Maksimumdan minimuma doğru kademeli olarak azalan bir gürültü seviyeleri programı oluşturur ve ilerlemeyi kontrol etmek için Laplace dağılım parametrelerini kullanır. Bu zamanlayıcı, difüzyon modelleri için gürültü programını tanımlamak üzere özel örnekleme iş akışlarında yaygın olarak kullanılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `steps` | Programdaki örnekleme adım sayısı (varsayılan: 20) | INT | Evet | 1 to 10000 |
| `sigma_max` | Programın başlangıcındaki maksimum sigma değeri (varsayılan: 14.614642) | FLOAT | Evet | 0.0 to 5000.0 |
| `sigma_min` | Programın sonundaki minimum sigma değeri (varsayılan: 0.0291675) | FLOAT | Evet | 0.0 to 5000.0 |
| `mu` | Laplace dağılımı için ortalama parametresi (varsayılan: 0.0) | FLOAT | Evet | -10.0 to 10.0 |
| `beta` | Laplace dağılımı için ölçek parametresi (varsayılan: 0.5) | FLOAT | Evet | 0.0 to 10.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `SIGMAS` | Laplace dağılımı programını takip eden bir sigma değerleri dizisi | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/tr.md)

---
**Source fingerprint (SHA-256):** `8e5ca00f4797f863a2cf8b9b115ec27beb7f65981cbb04eb036150402fc19389`
