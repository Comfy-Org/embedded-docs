# ModelBirleştirmeSD35_Büyük

ModelMergeSD35_Large düğümü, farklı model bileşenlerinin etkisini ayarlayarak iki Stable Diffusion 3.5 Large modelini birleştirmenize olanak tanır. İkinci modelin her bir parçasının nihai birleştirilmiş modele ne kadar katkıda bulunacağı üzerinde; embedding katmanlarından ortak bloklara ve son katmana kadar hassas kontrol sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirme için temel görevi gören taban model | MODEL | Evet | - |
| `model2` | Bileşenleri taban model ile karıştırılacak ikincil model | MODEL | Evet | - |
| `pos_embed.` | model2'deki konum embedding bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `x_embedder.` | model2'deki x embedder bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `context_embedder.` | model2'deki context embedder bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `y_embedder.` | model2'deki y embedder bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `t_embedder.` | model2'deki t embedder bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.0.` | model2'deki ortak blok 0 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.1.` | model2'deki ortak blok 1 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.2.` | model2'deki ortak blok 2 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.3.` | model2'deki ortak blok 3 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.4.` | model2'deki ortak blok 4 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.5.` | model2'deki ortak blok 5 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.6.` | model2'deki ortak blok 6 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.7.` | model2'deki ortak blok 7 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.8.` | model2'deki ortak blok 8 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.9.` | model2'deki ortak blok 9 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.10.` | model2'deki ortak blok 10 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.11.` | model2'deki ortak blok 11 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.12.` | model2'deki ortak blok 12 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.13.` | model2'deki ortak blok 13 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.14.` | model2'deki ortak blok 14 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.15.` | model2'deki ortak blok 15 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.16.` | model2'deki ortak blok 16 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.17.` | model2'deki ortak blok 17 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.18.` | model2'deki ortak blok 18 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.19.` | model2'deki ortak blok 19 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.20.` | model2'deki ortak blok 20 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.21.` | model2'deki ortak blok 21 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.22.` | model2'deki ortak blok 22 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.23.` | model2'deki ortak blok 23 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.24.` | model2'deki ortak blok 24 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.25.` | model2'deki ortak blok 25 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.26.` | model2'deki ortak blok 26 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.27.` | model2'deki ortak blok 27 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.28.` | model2'deki ortak blok 28 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.29.` | model2'deki ortak blok 29 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.30.` | model2'deki ortak blok 30 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.31.` | model2'deki ortak blok 31 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.32.` | model2'deki ortak blok 32 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.33.` | model2'deki ortak blok 33 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.34.` | model2'deki ortak blok 34 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.35.` | model2'deki ortak blok 35 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.36.` | model2'deki ortak blok 36 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `joint_blocks.37.` | model2'deki ortak blok 37 bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `final_layer.` | model2'deki son katman bileşeninin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |

**Not:** Tüm karıştırma parametreleri 0.0 ile 1.0 arasında değer kabul eder; 0.0, model2'nin ilgili bileşen için hiçbir katkı sağlamadığını, 1.0 ise model2'nin o bileşen için tam katkı sağladığı anlamına gelir. Değerler 0.01'lik adımlarla artar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Belirtilen karıştırma parametrelerine göre her iki girdi modelinin özelliklerini birleştiren sonuç model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD35_Large/tr.md)

---
**Source fingerprint (SHA-256):** `c489c710e18d01adcf4320d9c010ed587ca5e12babb468448f56d79acdc40f6c`
