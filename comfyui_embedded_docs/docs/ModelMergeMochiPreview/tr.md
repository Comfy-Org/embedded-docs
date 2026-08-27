# ModelBirleştirmeMochiÖnizleme

Bu düğüm, blok tabanlı bir yaklaşım kullanarak iki yapay zeka modelini birleştirir ve farklı model bileşenleri üzerinde ince ayar yapma imkanı sağlar. Konumsal frekanslar, gömme katmanları ve bireysel dönüştürücü blokları dahil olmak üzere belirli bölümler için enterpolasyon ağırlıklarını ayarlayarak modelleri harmanlamanıza olanak tanır. Birleştirme işlemi, belirtilen ağırlık değerlerine göre her iki girdi modelinin mimarilerini ve parametrelerini birleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `pos_frequencies.` | Konumsal frekans enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `t_embedder.` | Zaman gömücü enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `t5_y_embedder.` | T5-Y gömücü enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `t5_yproj.` | T5-Y izdüşüm enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.0.` | Blok 0 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.1.` | Blok 1 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.2.` | Blok 2 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.3.` | Blok 3 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.4.` | Blok 4 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.5.` | Blok 5 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.6.` | Blok 6 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.7.` | Blok 7 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.8.` | Blok 8 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.9.` | Blok 9 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.10.` | Blok 10 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.11.` | Blok 11 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.12.` | Blok 12 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.13.` | Blok 13 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.14.` | Blok 14 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.15.` | Blok 15 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.16.` | Blok 16 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.17.` | Blok 17 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.18.` | Blok 18 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.19.` | Blok 19 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.20.` | Blok 20 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.21.` | Blok 21 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.22.` | Blok 22 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.23.` | Blok 23 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.24.` | Blok 24 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.25.` | Blok 25 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.26.` | Blok 26 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.27.` | Blok 27 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.28.` | Blok 28 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.29.` | Blok 29 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.30.` | Blok 30 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.31.` | Blok 31 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.32.` | Blok 32 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.33.` | Blok 33 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.34.` | Blok 34 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.35.` | Blok 35 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.36.` | Blok 36 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.37.` | Blok 37 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.38.` | Blok 38 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.39.` | Blok 39 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.40.` | Blok 40 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.41.` | Blok 41 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.42.` | Blok 42 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.43.` | Blok 43 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.44.` | Blok 44 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.45.` | Blok 45 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.46.` | Blok 46 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.47.` | Blok 47 enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `final_layer.` | Son katman enterpolasyonu için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Belirtilen ağırlıklara göre her iki girdi modelinin özelliklerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMochiPreview/tr.md)

---
**Source fingerprint (SHA-256):** `aebf536f3f89ca8c81141ac871b1b612082c3bd38a29984168b05eccf0cb57e3`
