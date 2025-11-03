> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/tr.md)

ModelMergeLTXV düğümü, LTXV model mimarileri için özel olarak tasarlanmış gelişmiş model birleştirme işlemleri gerçekleştirir. Transformer blokları, projeksiyon katmanları ve diğer özelleştirilmiş modüller dahil olmak üzere çeşitli model bileşenleri için enterpolasyon ağırlıklarını ayarlayarak iki farklı modeli harmanlamanıza olanak tanır.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Evet | - | Birleştirilecek ilk model |
| `model2` | MODEL | Evet | - | Birleştirilecek ikinci model |
| `patchify_proj.` | FLOAT | Evet | 0.0 - 1.0 | Patchify projeksiyon katmanları için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `adaln_single.` | FLOAT | Evet | 0.0 - 1.0 | Uyarlamalı katman normalleştirme tekli katmanları için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `caption_projection.` | FLOAT | Evet | 0.0 - 1.0 | Altyazı projeksiyon katmanları için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.0.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 0 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.1.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 1 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.2.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 2 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.3.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 3 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.4.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 4 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.5.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 5 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.6.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 6 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.7.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 7 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.8.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 8 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.9.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 9 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.10.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 10 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.11.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 11 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.12.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 12 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.13.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 13 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.14.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 14 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.15.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 15 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.16.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 16 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.17.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 17 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.18.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 18 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.19.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 19 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.20.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 20 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.21.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 21 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.22.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 22 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.23.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 23 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.24.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 24 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.25.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 25 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.26.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 26 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.27.` | FLOAT | Evet | 0.0 - 1.0 | Transformer bloğu 27 için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `ölçek_kaydırma_tablosu` | FLOAT | Evet | 0.0 - 1.0 | Ölçek kaydırma tablosu için enterpolasyon ağırlığı (varsayılan: 1.0) |
| `proj_out.` | FLOAT | Evet | 0.0 - 1.0 | Projeksiyon çıkış katmanları için enterpolasyon ağırlığı (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Belirtilen enterpolasyon ağırlıklarına göre her iki girdi modelinden özellikleri birleştiren birleştirilmiş model |