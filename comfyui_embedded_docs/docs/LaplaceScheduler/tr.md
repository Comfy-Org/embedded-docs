> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/tr.md)

LaplaceScheduler düğümü, difüzyon örneklemesinde kullanılmak üzere bir Laplace dağılımını takip eden sigma değerleri dizisi oluşturur. Maksimumdan minimum değere kademeli olarak azalan bir gürültü seviyesi çizelgesi oluşturur ve ilerlemeyi kontrol etmek için Laplace dağılım parametrelerini kullanır. Bu zamanlayıcı, difüzyon modelleri için gürültü çizelgesini tanımlamak amacıyla özel örnekleme iş akışlarında yaygın olarak kullanılır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `steps` | INT | Evet | 1 ila 10000 | Çizelgedeki örnekleme adım sayısı (varsayılan: 20) |
| `sigma_max` | FLOAT | Evet | 0,0 ila 5000,0 | Çizelgenin başlangıcındaki maksimum sigma değeri (varsayılan: 14,614642) |
| `sigma_min` | FLOAT | Evet | 0,0 ila 5000,0 | Çizelgenin sonundaki minimum sigma değeri (varsayılan: 0,0291675) |
| `mu` | FLOAT | Evet | -10,0 ila 10,0 | Laplace dağılımı için ortalama parametresi (varsayılan: 0,0) |
| `beta` | FLOAT | Evet | 0,0 ila 10,0 | Laplace dağılımı için ölçek parametresi (varsayılan: 0,5) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `SIGMAS` | SIGMAS | Bir Laplace dağılımı çizelgesini takip eden sigma değerleri dizisi |

---
**Source fingerprint (SHA-256):** `9d8cacb93d0bb1872a368821fd3cad5d6d373817a923436af9f62a7648d5d735`
