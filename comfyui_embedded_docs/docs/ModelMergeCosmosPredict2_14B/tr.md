# ModelMergeCosmosPredict2_14B

ModelMergeCosmosPredict2_14B düğümü, dahili bileşenlerini harmanlayarak iki yapay zeka modelini birleştirir. Belirli katmanlar ve bileşenler için ayarlanabilir ağırlık değerleri kullanarak, ikinci modelin her bir parçasının nihai birleşik sonucu ne kadar etkileyeceği üzerinde hassas kontrol sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek temel model | MODEL | Evet | - |
| `model2` | Temel modele birleştirilecek ikincil model | MODEL | Evet | - |
| `pos_embedder.` | Konum gömücü harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `x_embedder.` | Girdi gömücü harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `t_embedder.` | Zaman gömücü harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `t_embedding_norm.` | Zaman gömme normalizasyonu harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.0.` | Blok 0 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.1.` | Blok 1 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.2.` | Blok 2 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.3.` | Blok 3 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.4.` | Blok 4 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.5.` | Blok 5 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.6.` | Blok 6 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.7.` | Blok 7 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.8.` | Blok 8 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.9.` | Blok 9 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.10.` | Blok 10 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.11.` | Blok 11 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.12.` | Blok 12 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.13.` | Blok 13 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.14.` | Blok 14 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.15.` | Blok 15 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.16.` | Blok 16 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.17.` | Blok 17 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.18.` | Blok 18 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.19.` | Blok 19 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.20.` | Blok 20 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.21.` | Blok 21 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.22.` | Blok 22 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.23.` | Blok 23 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.24.` | Blok 24 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.25.` | Blok 25 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.26.` | Blok 26 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.27.` | Blok 27 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.28.` | Blok 28 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.29.` | Blok 29 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.30.` | Blok 30 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.31.` | Blok 31 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.32.` | Blok 32 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.33.` | Blok 33 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.34.` | Blok 34 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.35.` | Blok 35 harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `final_layer.` | Son katman harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

**Not:** Tüm harmanlama ağırlığı parametreleri, 0.0 ile 1.0 arasında 0.01 adımlarla değer kabul eder; 0.0, model2'nin ilgili bileşene hiçbir katkısı olmadığını, 1.0 ise model2'nin tam katkısı olduğunu ifade eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Her iki girdi modelinin özelliklerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_14B/tr.md)

---
**Source fingerprint (SHA-256):** `a5f34deda62dc03f22613517e43996b908a8673dc5da10d8f1b7f6411ece2f0a`
