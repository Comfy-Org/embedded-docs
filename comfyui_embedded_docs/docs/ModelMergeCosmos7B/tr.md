# ModelBirleştirmeCosmos7B

ModelMergeCosmos7B düğümü, iki yapay zeka modelini belirli bileşenlerin ağırlıklı harmanlamasını kullanarak birleştirir. Modellerin farklı bölümlerinin nasıl birleştirileceği üzerinde, konum gömme katmanları, dönüştürücü blokları ve son katmanlar için ayrı ağırlıklar ayarlayarak ince taneli kontrol sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `pos_embedder.` | Konum gömme bileşeni ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `extra_pos_embedder.` | Ek konum gömme bileşeni ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `x_embedder.` | x gömme bileşeni ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `t_embedder.` | t gömme bileşeni ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `affline_norm.` | Afin normalizasyon bileşeni ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block0.` | Dönüştürücü bloğu 0 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block1.` | Dönüştürücü bloğu 1 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block2.` | Dönüştürücü bloğu 2 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block3.` | Dönüştürücü bloğu 3 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block4.` | Dönüştürücü bloğu 4 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block5.` | Dönüştürücü bloğu 5 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block6.` | Dönüştürücü bloğu 6 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block7.` | Dönüştürücü bloğu 7 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block8.` | Dönüştürücü bloğu 8 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block9.` | Dönüştürücü bloğu 9 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block10.` | Dönüştürücü bloğu 10 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block11.` | Dönüştürücü bloğu 11 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block12.` | Dönüştürücü bloğu 12 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block13.` | Dönüştürücü bloğu 13 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block14.` | Dönüştürücü bloğu 14 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block15.` | Dönüştürücü bloğu 15 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block16.` | Dönüştürücü bloğu 16 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block17.` | Dönüştürücü bloğu 17 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block18.` | Dönüştürücü bloğu 18 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block19.` | Dönüştürücü bloğu 19 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block20.` | Dönüştürücü bloğu 20 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block21.` | Dönüştürücü bloğu 21 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block22.` | Dönüştürücü bloğu 22 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block23.` | Dönüştürücü bloğu 23 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block24.` | Dönüştürücü bloğu 24 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block25.` | Dönüştürücü bloğu 25 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block26.` | Dönüştürücü bloğu 26 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block27.` | Dönüştürücü bloğu 27 ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `final_layer.` | Son katman bileşeni ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Her iki giriş modelinin özelliklerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos7B/tr.md)

---
**Source fingerprint (SHA-256):** `0721b047933179706c76f622efb5b7425aad530d302d8b33ec12dd68513dec0b`
