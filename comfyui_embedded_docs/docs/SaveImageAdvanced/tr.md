# Görüntüyü Kaydet (Gelişmiş)

**Save Image (Advanced)** düğümü, girdi görüntülerini dosya biçimi, bit derinliği ve renk uzayı üzerinde gelişmiş kontrol ile ComfyUI çıktı dizininize kaydeder. PNG veya EXR dosyaları olarak kaydetmeyi destekler ve kaydedilen dosyalara iş akışı meta verilerini gömer.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntüler` | Kaydedilecek görüntüler. | IMAGE | Evet | - |
| `dosya_adı_ön_eki` | Kaydedilecek dosyanın önekidir. `%date:yyyy-MM-dd%` veya `%Empty Latent Image.width%` gibi biçimlendirme belirteçleri içerebilir. (varsayılan: "ComfyUI") | STRING | Evet | - |
| `format` | Görüntünün kaydedileceği dosya biçimidir. Bir biçim seçmek, o biçim için ek seçenekler gösterir. | DYNAMIC_COMBO | Evet | `"png"`<br>`"exr"` |

### PNG Girdileri

Bu seçenekler, `format` `"png"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `bit_depth` | Kaydedilen PNG dosyasının bit derinliğidir. (varsayılan: "8-bit") | COMBO | Evet (koşullu) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | Girdi tensörünün renk uzayıdır. PNG biçimi için yalnızca sRGB kullanılabilir. (varsayılan: "sRGB") | COMBO | Evet (koşullu) | `"sRGB"` |

### EXR Girdileri

Bu seçenekler, `format` `"exr"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `bit_depth` | Kaydedilen EXR dosyasının bit derinliğidir. (varsayılan: "32-bit float") | COMBO | Evet (koşullu) | `"32-bit float"` |
| `input_color_space` | Girdi tensörünün renk uzayıdır. EXR her zaman eşleşen renk gamında sahne-doğrusal olarak yazılır.<br>`"sRGB"` — girdi, sRGB kodlu Rec.709'dur; ters sRGB EOTF uygulanır.<br>`"HDR"` — girdi, HLG kodlu Rec.2020 (BT.2100)'dir; sahne-doğrusal ışık elde etmek için ters HLG OETF uygulanır.<br>`"linear"` — girdi zaten sahne-doğrusaldır (Rec.709 ana renkleri); değiştirilmeden yazılır. Bunu, işleyici/birleştirici (renderer/compositor) çıktısı için kullanın. (varsayılan: "sRGB") | COMBO | Evet (koşullu) | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

**Parametre Bağımlılıkları Hakkında Notlar:**
- `bit_depth` ve `input_color_space` parametreleri yalnızca belirli bir `format` seçildiğinde kullanılabilir.
- PNG biçimi için yalnızca "8-bit" ve "16-bit" bit derinlikleri ve yalnızca "sRGB" renk uzayı kullanılabilir.
- EXR biçimi için yalnızca "32-bit float" bit derinliği kullanılabilir; "sRGB", "HDR" veya "linear" renk uzaylarıyla birlikte.
- Görüntüler 1 (gri tonlamalı), 3 (RGB) veya 4 (RGBA) kanala sahip olmalıdır; diğer kanal sayıları desteklenmez ve hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Girdi görüntüleri, değiştirilmeden aktarılır. Düğümün arayüz çıktısı, her biri dosya adı, alt klasör ve tür ("output") içeren kaydedilmiş görüntü sonuçlarının bir listesini sağlar. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `b03a822a90cf50d30fbf4397ab280393951f08d2339dd48c0dbaf75d9c415bca`
