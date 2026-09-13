# Görüntüyü Kaydet (Gelişmiş)

The **Save Image (Advanced)** node saves the input images to your ComfyUI output directory with advanced control over file format, bit depth, and color space. It supports saving as PNG, EXR, or AVIF files (including animated AVIF) and can embed workflow metadata into the saved files.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `images` | Kaydedilecek görüntüler. | IMAGE | Evet | - |
| `filename_prefix` | Kaydedilecek dosya için ön ek. `%date:yyyy-MM-dd%` veya `%Empty Latent Image.width%` gibi biçimlendirme belirteçleri içerebilir. (varsayılan: "ComfyUI") | STRING | Evet | - |
| `format` | Görüntünün kaydedileceği dosya biçimi. Bir biçim seçildiğinde o biçime yönelik ek seçenekler görünür. | DYNAMIC_COMBO | Evet | `"png"`<br>`"exr"`<br>`"avif"` |

### PNG Girdileri

Bu seçenekler `format` `"png"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `bit_depth` | Kaydedilen PNG dosyası için bit derinliği. (varsayılan: "8-bit") | COMBO | Evet (koşullu) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | Giriş tensörünün renk uzayı. PNG biçimi için yalnızca sRGB kullanılabilir. (varsayılan: "sRGB") | COMBO | Evet (koşullu) | `"sRGB"` |

### EXR Girdileri

Bu seçenekler `format` `"exr"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `bit_depth` | Kaydedilen EXR dosyası için bit derinliği. (varsayılan: "32-bit float") | COMBO | Evet (koşullu) | `"32-bit float"` |
| `input_color_space` | Giriş tensörünün renk uzayı. EXR, eşleşen renk gamında her zaman sahne-doğrusal olarak yazılır.<br>`"sRGB"` — giriş sRGB kodlu Rec.709'dur; ters sRGB EOTF uygulanır.<br>`"HDR"` — giriş HLG kodlu Rec.2020'dir (BT.2100); sahne-doğrusal ışık elde etmek için ters HLG OETF uygulanır.<br>`"linear"` — giriş zaten sahne-doğrusaldır (Rec.709 ana renkleri); değiştirilmeden yazılır. Bunu renderer/compositor çıktısı için kullanın. (varsayılan: "sRGB") | COMBO | Evet (koşullu) | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

### AVIF Girdileri

Bu seçenekler `format` `"avif"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `bit_depth` | Kaydedilen AVIF dosyası için bit derinliği. Auto, sRGB için 8-bit YUV420 ve HDR için 10-bit YUV420 kullanır. (varsayılan: "auto") | COMBO | Evet (koşullu) | `"auto"`<br>`"8-bit YUV420"`<br>`"10-bit YUV420"` |
| `input_color_space` | Giriş görüntülerinin renk uzayı. HDR, BT.2020/HLG'yi seçer; HDR PQ ise BT.2020/PQ'yu seçer. (varsayılan: "sRGB") | COMBO | Evet (koşullu) | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `crf` | Daha düşük değerler daha yüksek kalite ve daha büyük dosyalar üretir. (varsayılan: 18) | INT | Evet (koşullu) | 1 ile 63 |
| `save_mode` | AVIF dosyası için kaydetme modu. `"still images"` toplu işteki her görüntüyü ayrı bir sabit görüntü dosyası olarak kaydeder; `"animated"` tüm toplu işi tek bir animasyonlu AVIF dosyası olarak kaydeder ve `fps` ile `loop_count` seçeneklerini görünür kılar. (varsayılan: "still images") | DYNAMIC_COMBO | Evet (koşullu) | `"still images"`<br>`"animated"` |

### AVIF Animasyon Seçenekleri

Bu seçenekler `save_mode` `"animated"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `fps` | Animasyonun kare hızı. (varsayılan: 6.0) | FLOAT | Evet (koşullu) | 0.01 ile 1000.0 |
| `loop_count` | Animasyonun kaç kez döngüye gireceği. 0 sonsuza kadar döngüye girer. (varsayılan: 0) | INT | Evet (koşullu) | 0 ile 1000 |

**Parametre Bağımlılıklarıyla İlgili Notlar:**
- Biçime özgü parametreler (`bit_depth`, `input_color_space` ve AVIF için ayrıca `crf` ile `save_mode`), yalnızca belirli bir `format` seçildiğinde kullanılabilir.
- PNG biçimi için yalnızca "8-bit" ve "16-bit" bit derinlikleri ve yalnızca "sRGB" renk uzayı kullanılabilir.
- EXR biçimi için yalnızca "32-bit float" bit derinliği kullanılabilir; "sRGB", "HDR" veya "linear" renk uzaylarıyla birlikte.
- AVIF biçimi için `fps` ve `loop_count`, yalnızca `save_mode` `"animated"` olarak ayarlandığında kullanılabilir.
- PNG ve EXR görüntüleri 1 (gri tonlama), 3 (RGB) veya 4 (RGBA) kanala sahip olmalıdır; diğer kanal sayıları desteklenmez ve hata verir.
- AVIF yalnızca 1 kanallı gri tonlamalı ve 3 kanallı RGB görüntüleri destekler; RGBA (alfa) görüntüler desteklenmez ve hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Giriş görüntüleri, değiştirilmeden geçirilir. Düğümün UI çıktısı, her biri dosya adı, alt klasör ve tür ("output") içeren kaydedilmiş görüntü sonuçlarının listesini sağlar. Birden fazla görüntü içeren animasyonlu AVIF için UI çıktısı ayrıca bir `animated` işareti içerir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `d3df3caca99d58d973d0bc2ff7c22c4626185d390ec2acf870d4014331c4c335`
