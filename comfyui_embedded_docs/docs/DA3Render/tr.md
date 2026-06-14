# Render Depth Anything 3

Bu düğüm, Depth Anything 3 geometri verilerinden bir görselleştirme oluşturur. Seçilen çıktı moduna bağlı olarak derinlik haritaları, güven haritaları veya gökyüzü maskeleri çıktı olarak verebilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `da3_geometry` | Derinlik, isteğe bağlı olarak gökyüzü ve güven tensörlerini içeren Depth Anything 3 geometri veri paketi | DA3_GEOMETRY | Evet | - |
| `output` | Oluşturulacak görselleştirme türü. Seçenekler: depth, depth_colored, sky_mask ve confidence. Her seçeneğin kendine ait alt parametreleri vardır. | COMBO | Evet | `"depth"`<br>`"depth_colored"`<br>`"sky_mask"`<br>`"confidence"` |

### `output` seçenekleri için alt parametreler

`output` değeri `"depth"` veya `"depth_colored"` olarak ayarlandığında:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `normalization` | Derinlik normalizasyon yöntemi. v2_style, algısal olarak dengeli sonuçlar için ortalama/standart sapma normalizasyonu kullanır (varsayılan). min_max, maksimum kontrast için tüm derinlik aralığını [0, 1] aralığına genişletir. raw, Metrik model için metrik birimleri ölçeklemeden korur. | COMBO | Evet | `"v2_style"`<br>`"min_max"`<br>`"raw"` |
| `apply_sky_clip` | Normalizasyon öncesinde gökyüzü bölgesi derinliğini ön plan derinliğinin 99. yüzdelik dilimine kırpar. da3_geometry girişinde bir sky anahtarı gerektirir (yalnızca Mono/Metric modeller için). Varsayılan: False | BOOLEAN | Evet | True<br>False |

`output` değeri `"sky_mask"` olarak ayarlandığında:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `colored` | Gökyüzü maskesine Turbo renk haritasını uygular. Varsayılan: False | BOOLEAN | Evet | True<br>False |

`output` değeri `"confidence"` olarak ayarlandığında:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `colored` | Güven haritasına Turbo renk haritasını uygular. Varsayılan: False | BOOLEAN | Evet | True<br>False |

### Parametre Kısıtlamaları

- `apply_sky_clip` True olarak ayarlandığında, `da3_geometry` girişi bir gökyüzü tensörü içermelidir. Bu yalnızca Mono veya Metric modeller kullanıldığında geçerlidir. Gökyüzü tensörü eksikse, düğüm bir hata verecektir.
- `sky_mask` çıktı seçeneği, `da3_geometry` girişinde bir gökyüzü tensörü gerektirir. Bu yalnızca Mono veya Metric modellerle kullanılabilir.
- `confidence` çıktı seçeneği, `da3_geometry` girişinde bir güven tensörü gerektirir. Bu yalnızca Small veya Base modellerle kullanılabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `IMAGE` | Oluşturulan görselleştirme bir görüntü tensörü olarak. Derinlik çıktıları için gri tonlamalı veya renkli bir derinlik haritası döndürür. sky_mask ve confidence için, colored parametresine bağlı olarak gri tonlamalı veya renkli bir görselleştirme döndürür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3Render/tr.md)

---
**Source fingerprint (SHA-256):** `54d4cde95a916cac26c8a2e19c5623e794d46c0d7652f1c8204f9f2a0deabe0c`
