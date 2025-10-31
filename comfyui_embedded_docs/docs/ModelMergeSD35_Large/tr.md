> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD35_Large/tr.md)

ModelMergeSD35_Large düğümü, iki Stable Diffusion 3.5 Large modelini farklı model bileşenlerinin etkisini ayarlayarak birleştirmenize olanak tanır. İkinci modelin her bir parçasının (gömme katmanlarından birleşik bloklara ve son katmanlara kadar) birleştirilmiş nihai modele ne kadar katkıda bulunacağı üzerinde hassas kontrol sağlar.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Evet | - | Birleştirme için temel olarak hizmet veren ana model |
| `model2` | MODEL | Evet | - | Bileşenlerinin ana modele karıştırılacağı ikincil model |
| `pos_embed.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den konum gömme katmanının ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `x_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den x gömme katmanının ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `context_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den bağlam gömme katmanının ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `y_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den y gömme katmanının ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `t_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den t gömme katmanının ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.0.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 0 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.1.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 1 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.2.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 2 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.3.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 3 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.4.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 4 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.5.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 5 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.6.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 6 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.7.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 7 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.8.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 8 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.9.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 9 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.10.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 10 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.11.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 11 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.12.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 12 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.13.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 13 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.14.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 14 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.15.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 15 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.16.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 16 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.17.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 17 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.18.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 18 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.19.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 19 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.20.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 20 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.21.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 21 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.22.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 22 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.23.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 23 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.24.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 24 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.25.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 25 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.26.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 26 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.27.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 27 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.28.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 28 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.29.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 29 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.30.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 30 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.31.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 31 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.32.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 32 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.33.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 33 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.34.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 34 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.35.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 35 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.36.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 36 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.37.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den 37 numaralı birleşik bloğun ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `final_layer.` | FLOAT | Evet | 0.0 - 1.0 | Model2'den son katmanın ne kadarının birleştirilmiş modele karıştırılacağını kontrol eder (varsayılan: 1.0) |

**Not:** Tüm karıştırma parametreleri 0.0 ile 1.0 arasında değerler kabul eder; burada 0.0 model2'den hiç katkı olmadığı, 1.0 ise ilgili bileşen için model2'den tam katkı olduğu anlamına gelir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Belirtilen karıştırma parametrelerine göre her iki girdi modelinden özelliklerin birleştirildiği ortaya çıkan birleştirilmiş model |