# ModelBirleştirmeSD1

ModelMergeSD1 düğümü, iki Stable Diffusion 1.x modelini, her model bileşeninin sonuca katkısını ayarlayarak birbirine karıştırır. Zaman gömme, etiket gömme ve her girdi, orta ve çıktı bloğu üzerinde ayrı ayrı kontrol sağlayarak belirli kullanım durumları için ince ayarlı model birleştirmeye olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `time_embed.` | Zaman gömme katmanı karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `label_emb.` | Etiket gömme katmanı karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `input_blocks.0.` | Girdi bloğu 0 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `input_blocks.1.` | Girdi bloğu 1 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `input_blocks.2.` | Girdi bloğu 2 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `input_blocks.3.` | Girdi bloğu 3 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `input_blocks.4.` | Girdi bloğu 4 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `input_blocks.5.` | Girdi bloğu 5 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `input_blocks.6.` | Girdi bloğu 6 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `input_blocks.7.` | Girdi bloğu 7 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `input_blocks.8.` | Girdi bloğu 8 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `input_blocks.9.` | Girdi bloğu 9 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `input_blocks.10.` | Girdi bloğu 10 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `input_blocks.11.` | Girdi bloğu 11 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `middle_block.0.` | Orta blok 0 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `middle_block.1.` | Orta blok 1 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `middle_block.2.` | Orta blok 2 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `output_blocks.0.` | Çıktı bloğu 0 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `output_blocks.1.` | Çıktı bloğu 1 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `output_blocks.2.` | Çıktı bloğu 2 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `output_blocks.3.` | Çıktı bloğu 3 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `output_blocks.4.` | Çıktı bloğu 4 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `output_blocks.5.` | Çıktı bloğu 5 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `output_blocks.6.` | Çıktı bloğu 6 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `output_blocks.7.` | Çıktı bloğu 7 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `output_blocks.8.` | Çıktı bloğu 8 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `output_blocks.9.` | Çıktı bloğu 9 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `output_blocks.10.` | Çıktı bloğu 10 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `output_blocks.11.` | Çıktı bloğu 11 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `çıktı.` | Çıktı katmanı karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |

Tüm karıştırma ağırlıkları 0.0 ile 1.0 arasında değer kabul eder ve varsayılan olarak 1.0 değerine ayarlıdır; bu, ayarlama yapılmadığı sürece ilk modelin her bileşeninin tamamen kullanıldığı anlamına gelir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Her iki girdi modelinin özelliklerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD1/tr.md)

---
**Source fingerprint (SHA-256):** `b9d53f126139412fbd8b21be72e1dcdb02736519ab4dc9e28c7840d69acb7c87`
