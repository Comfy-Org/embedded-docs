# ModelBirleştirmeCosmosTahmin2_2B

ModelMergeCosmosPredict2_2B düğümü, farklı model bileşenleri üzerinde ince ayar kontrolü sağlayan blok tabanlı bir yaklaşımla iki difüzyon modelini birleştirir. Konum gömücüleri, zaman gömücüleri, transformer blokları ve son katmanlar için enterpolasyon ağırlıklarını ayarlayarak iki modelin belirli bölümlerini harmanlamanıza olanak tanır. Bu, her modeldeki farklı mimari bileşenlerin birleştirilmiş sonuca nasıl katkıda bulunacağı üzerinde hassas kontrol sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `pos_embedder.` | Konum gömücü enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `x_embedder.` | Giriş gömücü enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `t_embedder.` | Zaman gömücü enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `t_embedding_norm.` | Zaman gömme normalizasyonu enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.0.` | Transformer bloğu 0 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.1.` | Transformer bloğu 1 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.2.` | Transformer bloğu 2 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.3.` | Transformer bloğu 3 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.4.` | Transformer bloğu 4 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.5.` | Transformer bloğu 5 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.6.` | Transformer bloğu 6 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.7.` | Transformer bloğu 7 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.8.` | Transformer bloğu 8 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.9.` | Transformer bloğu 9 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.10.` | Transformer bloğu 10 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.11.` | Transformer bloğu 11 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.12.` | Transformer bloğu 12 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.13.` | Transformer bloğu 13 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.14.` | Transformer bloğu 14 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.15.` | Transformer bloğu 15 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.16.` | Transformer bloğu 16 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.17.` | Transformer bloğu 17 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.18.` | Transformer bloğu 18 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.19.` | Transformer bloğu 19 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.20.` | Transformer bloğu 20 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.21.` | Transformer bloğu 21 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.22.` | Transformer bloğu 22 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.23.` | Transformer bloğu 23 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.24.` | Transformer bloğu 24 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.25.` | Transformer bloğu 25 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.26.` | Transformer bloğu 26 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.27.` | Transformer bloğu 27 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `final_layer.` | Son katman enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Her iki giriş modelinin özelliklerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_2B/tr.md)

---
**Source fingerprint (SHA-256):** `3586868201320ae9a326a08f6a9bd74511a5342bf8496e7efcb9f45cf4b7c55d`
