> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAuraflow/tr.md)

ModelMergeAuraflow düğümü, iki farklı modeli çeşitli model bileşenleri için belirli karıştırma ağırlıklarını ayarlayarak birleştirmenize olanak tanır. Modelin ilk katmanlarından son çıktılara kadar farklı bölümlerin nasıl birleştirileceği üzerinde hassas kontrol sağlar. Bu düğüm, birleştirme süreci üzerinde hassas kontrol ile özel model kombinasyonları oluşturmak için özellikle kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Evet | - | Birleştirilecek ilk model |
| `model2` | MODEL | Evet | - | Birleştirilecek ikinci model |
| `init_x_linear.` | FLOAT | Evet | 0.0 - 1.0 | Başlangıç doğrusal dönüşüm için karıştırma ağırlığı (varsayılan: 1.0) |
| `konumsal_kodlama` | FLOAT | Evet | 0.0 - 1.0 | Konumsal kodlama bileşenleri için karıştırma ağırlığı (varsayılan: 1.0) |
| `cond_seq_linear.` | FLOAT | Evet | 0.0 - 1.0 | Koşullu dizi doğrusal katmanları için karıştırma ağırlığı (varsayılan: 1.0) |
| `kayıt_jetonları` | FLOAT | Evet | 0.0 - 1.0 | Token kayıt bileşenleri için karıştırma ağırlığı (varsayılan: 1.0) |
| `t_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Zaman gömme bileşenleri için karıştırma ağırlığı (varsayılan: 1.0) |
| `double_layers.0.` | FLOAT | Evet | 0.0 - 1.0 | Çift katman grubu 0 için karıştırma ağırlığı (varsayılan: 1.0) |
| `double_layers.1.` | FLOAT | Evet | 0.0 - 1.0 | Çift katman grubu 1 için karıştırma ağırlığı (varsayılan: 1.0) |
| `double_layers.2.` | FLOAT | Evet | 0.0 - 1.0 | Çift katman grubu 2 için karıştırma ağırlığı (varsayılan: 1.0) |
| `double_layers.3.` | FLOAT | Evet | 0.0 - 1.0 | Çift katman grubu 3 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.0.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 0 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.1.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 1 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.2.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 2 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.3.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 3 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.4.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 4 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.5.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 5 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.6.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 6 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.7.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 7 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.8.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 8 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.9.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 9 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.10.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 10 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.11.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 11 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.12.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 12 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.13.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 13 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.14.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 14 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.15.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 15 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.16.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 16 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.17.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 17 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.18.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 18 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.19.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 19 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.20.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 20 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.21.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 21 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.22.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 22 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.23.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 23 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.24.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 24 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.25.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 25 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.26.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 26 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.27.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 27 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.28.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 28 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.29.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 29 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.30.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 30 için karıştırma ağırlığı (varsayılan: 1.0) |
| `single_layers.31.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 31 için karıştırma ağırlığı (varsayılan: 1.0) |
| `modF.` | FLOAT | Evet | 0.0 - 1.0 | modF bileşenleri için karıştırma ağırlığı (varsayılan: 1.0) |
| `final_linear.` | FLOAT | Evet | 0.0 - 1.0 | Son doğrusal dönüşüm için karıştırma ağırlığı (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Belirtilen karıştırma ağırlıklarına göre her iki girdi modelinden özelliklerin birleştirildiği model |