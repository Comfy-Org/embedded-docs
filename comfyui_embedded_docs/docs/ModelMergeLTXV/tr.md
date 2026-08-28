# ModelBirleştirmeLTXV

ModelMergeLTXV düğümü, LTXV model mimarileri için özel olarak tasarlanmış gelişmiş model birleştirme işlemleri gerçekleştirir. Transformer blokları, projeksiyon katmanları ve diğer özel modüller dahil olmak üzere çeşitli model bileşenleri için enterpolasyon ağırlıklarını ayarlayarak iki farklı modeli birbirine karıştırmanıza olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `patchify_proj.` | Patchify projeksiyon katmanları için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `adaln_single.` | Adaptif katman normalizasyonu tek katmanları için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `caption_projection.` | Başlık projeksiyon katmanları için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.0.` | Transformer bloğu 0 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.1.` | Transformer bloğu 1 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.2.` | Transformer bloğu 2 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.3.` | Transformer bloğu 3 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.4.` | Transformer bloğu 4 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.5.` | Transformer bloğu 5 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.6.` | Transformer bloğu 6 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.7.` | Transformer bloğu 7 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.8.` | Transformer bloğu 8 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.9.` | Transformer bloğu 9 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.10.` | Transformer bloğu 10 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.11.` | Transformer bloğu 11 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.12.` | Transformer bloğu 12 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.13.` | Transformer bloğu 13 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.14.` | Transformer bloğu 14 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.15.` | Transformer bloğu 15 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.16.` | Transformer bloğu 16 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.17.` | Transformer bloğu 17 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.18.` | Transformer bloğu 18 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.19.` | Transformer bloğu 19 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.20.` | Transformer bloğu 20 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.21.` | Transformer bloğu 21 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.22.` | Transformer bloğu 22 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.23.` | Transformer bloğu 23 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.24.` | Transformer bloğu 24 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.25.` | Transformer bloğu 25 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.26.` | Transformer bloğu 26 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.27.` | Transformer bloğu 27 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `ölçek_kaydırma_tablosu` | Ölçek kaydırma tablosu için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |
| `proj_out.` | Projeksiyon çıktı katmanları için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Belirtilen enterpolasyon ağırlıklarına göre her iki girdi modelinin özelliklerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/tr.md)

---
**Source fingerprint (SHA-256):** `0ff5f93aee831259066679a27fff8f7cbd4a9686242091f1bc7dd3805725566e`
