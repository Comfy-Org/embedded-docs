> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_2B/tr.md)

ModelMergeCosmosPredict2_2B düğümü, iki difüzyon modelini, farklı model bileşenleri üzerinde ayrıntılı kontrol sağlayan blok tabanlı bir yaklaşımla birleştirir. Konum yerleştiricileri, zaman yerleştiricileri, transformatör blokları ve son katmanlar için enterpolasyon ağırlıklarını ayarlayarak iki modelin belirli bölümlerini harmanlamanıza olanak tanır. Bu, her bir modelden farklı mimari bileşenlerin nihai birleştirilmiş sonuca nasıl katkıda bulunduğu üzerinde hassas kontrol sağlar.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Evet | - | Birleştirilecek ilk model |
| `model2` | MODEL | Evet | - | Birleştirilecek ikinci model |
| `pos_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Konum yerleştirici enterpolasyon ağırlığı (varsayılan: 1.0) |
| `x_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Girdi yerleştirici enterpolasyon ağırlığı (varsayılan: 1.0) |
| `t_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Zaman yerleştirici enterpolasyon ağırlığı (varsayılan: 1.0) |
| `t_embedding_norm.` | FLOAT | Evet | 0.0 - 1.0 | Zaman gömmesi normalleştirme enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.0.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 0 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.1.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 1 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.2.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 2 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.3.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 3 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.4.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 4 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.5.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 5 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.6.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 6 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.7.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 7 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.8.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 8 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.9.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 9 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.10.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 10 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.11.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 11 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.12.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 12 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.13.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 13 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.14.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 14 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.15.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 15 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.16.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 16 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.17.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 17 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.18.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 18 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.19.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 19 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.20.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 20 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.21.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 21 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.22.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 22 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.23.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 23 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.24.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 24 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.25.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 25 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.26.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 26 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `blocks.27.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 27 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `final_layer.` | FLOAT | Evet | 0.0 - 1.0 | Son katman enterpolasyon ağırlığı (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Her iki girdi modelinin özelliklerini birleştiren birleştirilmiş model |