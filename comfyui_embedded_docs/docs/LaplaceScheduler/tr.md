> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/tr.md)

LaplaceScheduler düğümü, difüzyon örneklemesi için Laplace dağılımını takip eden bir sigma değerleri dizisi oluşturur. Maksimum değerden minimum değere doğru kademeli olarak azalan gürültü seviyeleri programı oluşturur ve ilerlemeyi kontrol etmek için Laplace dağılımı parametrelerini kullanır. Bu programlayıcı, difüzyon modelleri için gürültü programını tanımlamak üzere özel örnekleme iş akışlarında yaygın olarak kullanılır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `adımlar` | INT | Evet | 1 - 10000 | Programdaki örnekleme adımlarının sayısı (varsayılan: 20) |
| `sigma_maks` | FLOAT | Evet | 0.0 - 5000.0 | Programın başındaki maksimum sigma değeri (varsayılan: 14.614642) |
| `sigma_min` | FLOAT | Evet | 0.0 - 5000.0 | Programın sonundaki minimum sigma değeri (varsayılan: 0.0291675) |
| `mu` | FLOAT | Evet | -10.0 - 10.0 | Laplace dağılımı için ortalama parametresi (varsayılan: 0.0) |
| `beta` | FLOAT | Evet | 0.0 - 10.0 | Laplace dağılımı için ölçek parametresi (varsayılan: 0.5) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `SIGMAS` | SIGMAS | Laplace dağılım programını takip eden bir sigma değerleri dizisi |