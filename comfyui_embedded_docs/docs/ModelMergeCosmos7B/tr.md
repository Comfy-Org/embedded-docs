> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos7B/tr.md)

ModelMergeCosmos7B düğümü, iki yapay zeka modelini belirli bileşenlerin ağırlıklı harmanlamasını kullanarak birleştirir. Modellerin farklı bölümlerinin nasıl birleştirileceği üzerinde, konum gömme katmanları, dönüştürücü blokları ve son katmanlar için ayrı ağırlıklar ayarlayarak ince taneli kontrol sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Evet | - | Birleştirilecek ilk model |
| `model2` | MODEL | Evet | - | Birleştirilecek ikinci model |
| `pos_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Konum gömme bileşeni ağırlığı (varsayılan: 1.0) |
| `extra_pos_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Ek konum gömme bileşeni ağırlığı (varsayılan: 1.0) |
| `x_embedder.` | FLOAT | Evet | 0.0 - 1.0 | x gömme bileşeni ağırlığı (varsayılan: 1.0) |
| `t_embedder.` | FLOAT | Evet | 0.0 - 1.0 | t gömme bileşeni ağırlığı (varsayılan: 1.0) |
| `affline_norm.` | FLOAT | Evet | 0.0 - 1.0 | Afin normalizasyon bileşeni ağırlığı (varsayılan: 1.0) |
| `blocks.block0.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 0 ağırlığı (varsayılan: 1.0) |
| `blocks.block1.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 1 ağırlığı (varsayılan: 1.0) |
| `blocks.block2.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 2 ağırlığı (varsayılan: 1.0) |
| `blocks.block3.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 3 ağırlığı (varsayılan: 1.0) |
| `blocks.block4.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 4 ağırlığı (varsayılan: 1.0) |
| `blocks.block5.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 5 ağırlığı (varsayılan: 1.0) |
| `blocks.block6.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 6 ağırlığı (varsayılan: 1.0) |
| `blocks.block7.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 7 ağırlığı (varsayılan: 1.0) |
| `blocks.block8.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 8 ağırlığı (varsayılan: 1.0) |
| `blocks.block9.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 9 ağırlığı (varsayılan: 1.0) |
| `blocks.block10.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 10 ağırlığı (varsayılan: 1.0) |
| `blocks.block11.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 11 ağırlığı (varsayılan: 1.0) |
| `blocks.block12.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 12 ağırlığı (varsayılan: 1.0) |
| `blocks.block13.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 13 ağırlığı (varsayılan: 1.0) |
| `blocks.block14.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 14 ağırlığı (varsayılan: 1.0) |
| `blocks.block15.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 15 ağırlığı (varsayılan: 1.0) |
| `blocks.block16.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 16 ağırlığı (varsayılan: 1.0) |
| `blocks.block17.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 17 ağırlığı (varsayılan: 1.0) |
| `blocks.block18.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 18 ağırlığı (varsayılan: 1.0) |
| `blocks.block19.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 19 ağırlığı (varsayılan: 1.0) |
| `blocks.block20.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 20 ağırlığı (varsayılan: 1.0) |
| `blocks.block21.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 21 ağırlığı (varsayılan: 1.0) |
| `blocks.block22.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 22 ağırlığı (varsayılan: 1.0) |
| `blocks.block23.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 23 ağırlığı (varsayılan: 1.0) |
| `blocks.block24.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 24 ağırlığı (varsayılan: 1.0) |
| `blocks.block25.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 25 ağırlığı (varsayılan: 1.0) |
| `blocks.block26.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 26 ağırlığı (varsayılan: 1.0) |
| `blocks.block27.` | FLOAT | Evet | 0.0 - 1.0 | Dönüştürücü bloğu 27 ağırlığı (varsayılan: 1.0) |
| `final_layer.` | FLOAT | Evet | 0.0 - 1.0 | Son katman bileşeni ağırlığı (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Her iki giriş modelinin özelliklerini birleştiren birleştirilmiş model |

---
**Source fingerprint (SHA-256):** `0721b047933179706c76f622efb5b7425aad530d302d8b33ec12dd68513dec0b`
