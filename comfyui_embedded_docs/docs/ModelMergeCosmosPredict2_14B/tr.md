> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_14B/tr.md)

ModelMergeCosmosPredict2_14B düğümü, iki yapay zeka modelini birleştirerek farklı model bileşenlerinin etkisini ayarlamanıza olanak tanır. İkinci modelin her bir parçasının, birleştirilmiş nihai modele ne kadar katkıda bulunacağını, belirli model katmanları ve bileşenleri için harmanlama ağırlıkları kullanarak hassas bir şekilde kontrol etmenizi sağlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Evet | - | Birleştirilecek temel model |
| `model2` | MODEL | Evet | - | Temel modele birleştirilecek ikincil model |
| `pos_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Konum yerleştirici harmanlama ağırlığı (varsayılan: 1.0) |
| `x_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Girdi yerleştirici harmanlama ağırlığı (varsayılan: 1.0) |
| `t_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Zaman yerleştirici harmanlama ağırlığı (varsayılan: 1.0) |
| `t_embedding_norm.` | FLOAT | Evet | 0.0 - 1.0 | Zaman yerleştirme normalleştirme harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.0.` | FLOAT | Evet | 0.0 - 1.0 | Blok 0 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.1.` | FLOAT | Evet | 0.0 - 1.0 | Blok 1 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.2.` | FLOAT | Evet | 0.0 - 1.0 | Blok 2 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.3.` | FLOAT | Evet | 0.0 - 1.0 | Blok 3 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.4.` | FLOAT | Evet | 0.0 - 1.0 | Blok 4 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.5.` | FLOAT | Evet | 0.0 - 1.0 | Blok 5 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.6.` | FLOAT | Evet | 0.0 - 1.0 | Blok 6 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.7.` | FLOAT | Evet | 0.0 - 1.0 | Blok 7 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.8.` | FLOAT | Evet | 0.0 - 1.0 | Blok 8 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.9.` | FLOAT | Evet | 0.0 - 1.0 | Blok 9 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.10.` | FLOAT | Evet | 0.0 - 1.0 | Blok 10 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.11.` | FLOAT | Evet | 0.0 - 1.0 | Blok 11 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.12.` | FLOAT | Evet | 0.0 - 1.0 | Blok 12 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.13.` | FLOAT | Evet | 0.0 - 1.0 | Blok 13 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.14.` | FLOAT | Evet | 0.0 - 1.0 | Blok 14 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.15.` | FLOAT | Evet | 0.0 - 1.0 | Blok 15 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.16.` | FLOAT | Evet | 0.0 - 1.0 | Blok 16 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.17.` | FLOAT | Evet | 0.0 - 1.0 | Blok 17 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.18.` | FLOAT | Evet | 0.0 - 1.0 | Blok 18 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.19.` | FLOAT | Evet | 0.0 - 1.0 | Blok 19 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.20.` | FLOAT | Evet | 0.0 - 1.0 | Blok 20 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.21.` | FLOAT | Evet | 0.0 - 1.0 | Blok 21 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.22.` | FLOAT | Evet | 0.0 - 1.0 | Blok 22 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.23.` | FLOAT | Evet | 0.0 - 1.0 | Blok 23 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.24.` | FLOAT | Evet | 0.0 - 1.0 | Blok 24 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.25.` | FLOAT | Evet | 0.0 - 1.0 | Blok 25 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.26.` | FLOAT | Evet | 0.0 - 1.0 | Blok 26 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.27.` | FLOAT | Evet | 0.0 - 1.0 | Blok 27 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.28.` | FLOAT | Evet | 0.0 - 1.0 | Blok 28 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.29.` | FLOAT | Evet | 0.0 - 1.0 | Blok 29 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.30.` | FLOAT | Evet | 0.0 - 1.0 | Blok 30 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.31.` | FLOAT | Evet | 0.0 - 1.0 | Blok 31 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.32.` | FLOAT | Evet | 0.0 - 1.0 | Blok 32 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.33.` | FLOAT | Evet | 0.0 - 1.0 | Blok 33 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.34.` | FLOAT | Evet | 0.0 - 1.0 | Blok 34 harmanlama ağırlığı (varsayılan: 1.0) |
| `blocks.35.` | FLOAT | Evet | 0.0 - 1.0 | Blok 35 harmanlama ağırlığı (varsayılan: 1.0) |
| `final_layer.` | FLOAT | Evet | 0.0 - 1.0 | Son katman harmanlama ağırlığı (varsayılan: 1.0) |

**Not:** Tüm harmanlama ağırlığı parametreleri 0.0 ile 1.0 arasında değerler kabul eder; burada 0.0, model2'den hiç katkı olmadığı, 1.0 ise o belirli bileşen için model2'den tam katkı olduğu anlamına gelir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Her iki girdi modelinin özelliklerini birleştiren birleştirilmiş model |