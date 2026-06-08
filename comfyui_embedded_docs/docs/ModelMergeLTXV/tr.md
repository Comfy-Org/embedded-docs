ModelMergeLTXV düğümü, özellikle LTXV model mimarileri için tasarlanmış gelişmiş model birleştirme işlemlerini gerçekleştirir. Dönüştürücü blokları, projeksiyon katmanları ve diğer özelleştirilmiş modüller dahil olmak üzere çeşitli model bileşenleri için enterpolasyon ağırlıklarını ayarlayarak iki farklı modeli birbiriyle harmanlamanıza olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `patchify_proj.` | Yamalama projeksiyon katmanları için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `adaln_single.` | Uyarlanabilir katman normalizasyonu tek katmanları için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `caption_projection.` | Altyazı projeksiyon katmanları için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.0.` | Dönüştürücü bloğu 0 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.1.` | Dönüştürücü bloğu 1 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.2.` | Dönüştürücü bloğu 2 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.3.` | Dönüştürücü bloğu 3 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.4.` | Dönüştürücü bloğu 4 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.5.` | Dönüştürücü bloğu 5 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.6.` | Dönüştürücü bloğu 6 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.7.` | Dönüştürücü bloğu 7 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.8.` | Dönüştürücü bloğu 8 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.9.` | Dönüştürücü bloğu 9 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.10.` | Dönüştürücü bloğu 10 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.11.` | Dönüştürücü bloğu 11 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.12.` | Dönüştürücü bloğu 12 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.13.` | Dönüştürücü bloğu 13 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.14.` | Dönüştürücü bloğu 14 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.15.` | Dönüştürücü bloğu 15 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.16.` | Dönüştürücü bloğu 16 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.17.` | Dönüştürücü bloğu 17 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.18.` | Dönüştürücü bloğu 18 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.19.` | Dönüştürücü bloğu 19 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.20.` | Dönüştürücü bloğu 20 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.21.` | Dönüştürücü bloğu 21 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.22.` | Dönüştürücü bloğu 22 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.23.` | Dönüştürücü bloğu 23 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.24.` | Dönüştürücü bloğu 24 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.25.` | Dönüştürücü bloğu 25 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.26.` | Dönüştürücü bloğu 26 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `transformer_blocks.27.` | Dönüştürücü bloğu 27 için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `ölçek_kaydırma_tablosu` | Ölçek kaydırma tablosu için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `proj_out.` | Projeksiyon çıktı katmanları için enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Belirtilen enterpolasyon ağırlıklarına göre her iki giriş modelinin özelliklerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/tr.md)

---
**Source fingerprint (SHA-256):** `29ef8750b6e88f71abca10c8aaad5d75c9c32afec057af78842ca82441438922`
