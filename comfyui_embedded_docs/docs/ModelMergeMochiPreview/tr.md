> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMochiPreview/tr.md)

Bu düğüm, blok tabanlı bir yaklaşım kullanarak iki yapay zeka modelini birleştirir ve farklı model bileşenleri üzerinde ince ayar yapma imkanı sağlar. Konumsal frekanslar, gömme katmanları ve bireysel dönüştürücü blokları dahil olmak üzere belirli bölümler için enterpolasyon ağırlıklarını ayarlayarak modelleri harmanlamanıza olanak tanır. Birleştirme işlemi, belirtilen ağırlık değerlerine göre her iki girdi modelinin mimarilerini ve parametrelerini birleştirir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Evet | - | Birleştirilecek ilk model |
| `model2` | MODEL | Evet | - | Birleştirilecek ikinci model |
| `pos_frequencies.` | FLOAT | Evet | 0.0 - 1.0 | Konumsal frekans enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `t_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Zaman gömücü enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `t5_y_embedder.` | FLOAT | Evet | 0.0 - 1.0 | T5-Y gömücü enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `t5_yproj.` | FLOAT | Evet | 0.0 - 1.0 | T5-Y izdüşüm enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.0.` | FLOAT | Evet | 0.0 - 1.0 | Blok 0 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.1.` | FLOAT | Evet | 0.0 - 1.0 | Blok 1 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.2.` | FLOAT | Evet | 0.0 - 1.0 | Blok 2 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.3.` | FLOAT | Evet | 0.0 - 1.0 | Blok 3 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.4.` | FLOAT | Evet | 0.0 - 1.0 | Blok 4 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.5.` | FLOAT | Evet | 0.0 - 1.0 | Blok 5 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.6.` | FLOAT | Evet | 0.0 - 1.0 | Blok 6 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.7.` | FLOAT | Evet | 0.0 - 1.0 | Blok 7 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.8.` | FLOAT | Evet | 0.0 - 1.0 | Blok 8 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.9.` | FLOAT | Evet | 0.0 - 1.0 | Blok 9 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.10.` | FLOAT | Evet | 0.0 - 1.0 | Blok 10 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.11.` | FLOAT | Evet | 0.0 - 1.0 | Blok 11 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.12.` | FLOAT | Evet | 0.0 - 1.0 | Blok 12 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.13.` | FLOAT | Evet | 0.0 - 1.0 | Blok 13 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.14.` | FLOAT | Evet | 0.0 - 1.0 | Blok 14 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.15.` | FLOAT | Evet | 0.0 - 1.0 | Blok 15 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.16.` | FLOAT | Evet | 0.0 - 1.0 | Blok 16 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.17.` | FLOAT | Evet | 0.0 - 1.0 | Blok 17 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.18.` | FLOAT | Evet | 0.0 - 1.0 | Blok 18 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.19.` | FLOAT | Evet | 0.0 - 1.0 | Blok 19 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.20.` | FLOAT | Evet | 0.0 - 1.0 | Blok 20 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.21.` | FLOAT | Evet | 0.0 - 1.0 | Blok 21 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.22.` | FLOAT | Evet | 0.0 - 1.0 | Blok 22 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.23.` | FLOAT | Evet | 0.0 - 1.0 | Blok 23 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.24.` | FLOAT | Evet | 0.0 - 1.0 | Blok 24 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.25.` | FLOAT | Evet | 0.0 - 1.0 | Blok 25 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.26.` | FLOAT | Evet | 0.0 - 1.0 | Blok 26 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.27.` | FLOAT | Evet | 0.0 - 1.0 | Blok 27 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.28.` | FLOAT | Evet | 0.0 - 1.0 | Blok 28 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.29.` | FLOAT | Evet | 0.0 - 1.0 | Blok 29 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.30.` | FLOAT | Evet | 0.0 - 1.0 | Blok 30 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.31.` | FLOAT | Evet | 0.0 - 1.0 | Blok 31 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.32.` | FLOAT | Evet | 0.0 - 1.0 | Blok 32 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.33.` | FLOAT | Evet | 0.0 - 1.0 | Blok 33 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.34.` | FLOAT | Evet | 0.0 - 1.0 | Blok 34 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.35.` | FLOAT | Evet | 0.0 - 1.0 | Blok 35 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.36.` | FLOAT | Evet | 0.0 - 1.0 | Blok 36 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.37.` | FLOAT | Evet | 0.0 - 1.0 | Blok 37 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.38.` | FLOAT | Evet | 0.0 - 1.0 | Blok 38 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.39.` | FLOAT | Evet | 0.0 - 1.0 | Blok 39 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.40.` | FLOAT | Evet | 0.0 - 1.0 | Blok 40 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.41.` | FLOAT | Evet | 0.0 - 1.0 | Blok 41 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.42.` | FLOAT | Evet | 0.0 - 1.0 | Blok 42 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.43.` | FLOAT | Evet | 0.0 - 1.0 | Blok 43 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.44.` | FLOAT | Evet | 0.0 - 1.0 | Blok 44 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.45.` | FLOAT | Evet | 0.0 - 1.0 | Blok 45 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.46.` | FLOAT | Evet | 0.0 - 1.0 | Blok 46 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `blocks.47.` | FLOAT | Evet | 0.0 - 1.0 | Blok 47 enterpolasyonu için ağırlık (varsayılan: 1.0) |
| `final_layer.` | FLOAT | Evet | 0.0 - 1.0 | Son katman enterpolasyonu için ağırlık (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Belirtilen ağırlıklara göre her iki girdi modelinin özelliklerini birleştiren birleştirilmiş model |

---
**Source fingerprint (SHA-256):** `aebf536f3f89ca8c81141ac871b1b612082c3bd38a29984168b05eccf0cb57e3`
