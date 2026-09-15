# ModelMergeCosmosPredict2_14B

ModelMergeCosmosPredict2_14B düğümü, iki AI modelini eşleşen iç bileşenlerini karıştırarak tek bir modelde birleştirir. Her embedder, blok ve son katman için ayrı bir ağırlık ayarlayarak ikinci modelin birinciye ne kadar karıştırılacağını kontrol etmenizi sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek temel model | MODEL | Evet | - |
| `model2` | Temel modele birleştirilecek ikincil model | MODEL | Evet | - |
| `pos_embedder.` | Konum gömücü karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `x_embedder.` | Girdi gömücü karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `t_embedder.` | Zaman gömücü karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `t_embedding_norm.` | Zaman gömme normalizasyonu karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.0.` | Blok 0 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.1.` | Blok 1 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.2.` | Blok 2 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.3.` | Blok 3 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.4.` | Blok 4 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.5.` | Blok 5 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.6.` | Blok 6 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.7.` | Blok 7 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.8.` | Blok 8 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.9.` | Blok 9 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.10.` | Blok 10 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.11.` | Blok 11 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.12.` | Blok 12 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.13.` | Blok 13 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.14.` | Blok 14 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.15.` | Blok 15 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.16.` | Blok 16 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.17.` | Blok 17 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.18.` | Blok 18 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.19.` | Blok 19 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.20.` | Blok 20 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.21.` | Blok 21 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.22.` | Blok 22 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.23.` | Blok 23 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.24.` | Blok 24 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.25.` | Blok 25 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.26.` | Blok 26 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.27.` | Blok 27 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.28.` | Blok 28 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.29.` | Blok 29 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.30.` | Blok 30 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.31.` | Blok 31 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.32.` | Blok 32 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.33.` | Blok 33 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.34.` | Blok 34 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.35.` | Blok 35 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `final_layer.` | Son katman karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

**Not:** Tüm karıştırma ağırlığı parametreleri 0.0 ile 1.0 arasında 0.01 adımlarla değer kabul eder; burada 0.0 ilgili bileşen için model2'den hiç katkı olmadığı, 1.0 ise model2'den tam katkı olduğu anlamına gelir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Her iki girdi modelinin özelliklerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_14B/tr.md)

---
**Source fingerprint (SHA-256):** `a5f34deda62dc03f22613517e43996b908a8673dc5da10d8f1b7f6411ece2f0a`
