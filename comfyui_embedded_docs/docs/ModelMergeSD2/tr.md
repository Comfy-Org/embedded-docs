# ModelBirleştirmeSD2

ModelMergeSD2 düğümü, iki Stable Diffusion 2.x modelini eşleşen bileşenlerini karıştırarak birleştirir; zaman gömme, etiket gömme ve her girdi, orta ve çıktı bloğu için ayrı bir ağırlık sunar. Blok düzeni ModelMergeSD1 ile aynıdır, bu nedenle her iki düğüm de aynı oran kümesini sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model. İkinci modelin katkıda bulunmadığı her şey bu modelden korunur | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model. Ağırlıkları aşağıdaki oranlara göre karıştırılır | MODEL | Evet | - |
| `time_embed.` | Zaman gömme katmanı için karışım oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `label_emb.` | Etiket gömme katmanı için karışım oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `input_blocks.0.` ile `input_blocks.11.` arası | 12 girdi bloğunun her biri için karışım oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `middle_block.0.` ile `middle_block.2.` arası | 3 orta bloğun her biri için karışım oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `output_blocks.0.` ile `output_blocks.11.` arası | 12 çıktı bloğunun her biri için karışım oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `çıktı.` | Çıktı katmanı için karışım oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |

0.0 oranı, ilgili bileşeni `model1` içindeki haliyle korur; 1.0 oranı, onu tamamen `model2` modelinden alır; aradaki değerler ağırlıklı bir karışım üretir. Her iki girdi de aynı blok yapısına sahip Stable Diffusion 2.x modelleri olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Belirtilen oranlara göre her iki girdiyi birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD2/tr.md)

---
**Source fingerprint (SHA-256):** `b9d53f126139412fbd8b21be72e1dcdb02736519ab4dc9e28c7840d69acb7c87`
