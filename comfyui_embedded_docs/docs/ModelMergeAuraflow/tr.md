# ModelBirleştirmeAuraflow

ModelMergeAuraflow düğümü, çeşitli model bileşenleri için belirli karıştırma ağırlıklarını ayarlayarak iki farklı modeli birbirine karıştırmanıza olanak tanır. Modellerin farklı bölümlerinin başlangıç katmanlarından son çıktılara kadar nasıl birleştirileceği üzerinde ince ayar düzeyinde kontrol sağlar. Bu düğüm, birleştirme süreci üzerinde hassas kontrol ile özel model kombinasyonları oluşturmak için özellikle kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `init_x_linear.` | Başlangıç doğrusal dönüşümü için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `konumsal_kodlama` | Konumsal kodlama bileşenleri için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `cond_seq_linear.` | Koşullu dizi doğrusal katmanları için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `kayıt_jetonları` | Token kayıt bileşenleri için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `t_embedder.` | Zaman gömme bileşenleri için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `double_layers.0.` | Çift katman grubu 0 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `double_layers.1.` | Çift katman grubu 1 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `double_layers.2.` | Çift katman grubu 2 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `double_layers.3.` | Çift katman grubu 3 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.0.` | Tek katman 0 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.1.` | Tek katman 1 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.2.` | Tek katman 2 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.3.` | Tek katman 3 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.4.` | Tek katman 4 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.5.` | Tek katman 5 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.6.` | Tek katman 6 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.7.` | Tek katman 7 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.8.` | Tek katman 8 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.9.` | Tek katman 9 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.10.` | Tek katman 10 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.11.` | Tek katman 11 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.12.` | Tek katman 12 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.13.` | Tek katman 13 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.14.` | Tek katman 14 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.15.` | Tek katman 15 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.16.` | Tek katman 16 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.17.` | Tek katman 17 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.18.` | Tek katman 18 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.19.` | Tek katman 19 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.20.` | Tek katman 20 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.21.` | Tek katman 21 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.22.` | Tek katman 22 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.23.` | Tek katman 23 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.24.` | Tek katman 24 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.25.` | Tek katman 25 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.26.` | Tek katman 26 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.27.` | Tek katman 27 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.28.` | Tek katman 28 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.29.` | Tek katman 29 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.30.` | Tek katman 30 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `single_layers.31.` | Tek katman 31 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `modF.` | modF bileşenleri için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `final_linear.` | Son doğrusal dönüşüm için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Belirtilen karıştırma ağırlıklarına göre her iki girdi modelinin özelliklerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAuraflow/tr.md)

---
**Source fingerprint (SHA-256):** `e9d3d81b2a3f81b082f9dc9f662f4e51df66f1f077e2899a1fea9a7061c4a97b`
