# Görüntüyü Kaydet (Gelişmiş)

**Save Image (Advanced)** düğümü, girdi görüntülerini dosya biçimi, bit derinliği ve renk uzayı üzerinde gelişmiş kontrolle ComfyUI çıktı dizininize kaydeder. PNG, EXR veya AVIF dosyaları (animasyonlu AVIF dahil) olarak kaydetmeyi destekler ve kaydedilen dosyalara iş akışı meta verilerini gömebilir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `images` | Kaydedilecek görüntüler. | IMAGE | Evet | - |
| `filename_prefix` | Kaydedilecek dosya için önek. `%date:yyyy-MM-dd%` veya `%Empty Latent Image.width%` gibi biçimlendirme belirteçleri içerebilir. (varsayılan: "ComfyUI") | STRING | Evet | - |
| `format` | Görüntünün kaydedileceği dosya biçimi. Bir biçim seçmek, o biçime özel ek seçenekleri gösterir. | DYNAMIC_COMBO | Evet | `"png"`<br>`"exr"`<br>`"avif"` |

### PNG Girdileri

Bu seçenekler `format` değeri `"png"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `bit_depth` | Kaydedilen PNG dosyası için bit derinliği. (varsayılan: "8-bit") | COMBO | Evet (koşullu) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | Girdi tensörünün renk uzayı. PNG biçimi için yalnızca sRGB kullanılabilir. (varsayılan: "sRGB") | COMBO | Evet (koşullu) | `"sRGB"` |
| `channels` | PNG'ye hangi kanalların yazılacağı. `"auto"` girdi kanallarını korur; gri tonlama RGB'yi parlaklığa dönüştürür ve alfa kanalını kaldırır; RGB, alfa olmadan rengi kaydeder; RGBA ise alfayı korur veya tamamen opak bir alfa ekler. (varsayılan: `"auto"`) | COMBO | Hayır | `"auto"`<br>`"grayscale (1 channel)"`<br>`"RGB (3 channels)"`<br>`"RGBA (4 channels)"` |

### EXR Girdileri

Bu seçenekler `format` değeri `"exr"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `bit_depth` | Kaydedilen EXR dosyası için bit derinliği. (varsayılan: "16-bit float") | COMBO | Evet (koşullu) | `"16-bit float"`<br>`"32-bit float"` |
| `input_color_space` | Girdi tensörünün renk uzayı. EXR her zaman eşleşen renk gamında sahne-doğrusal olarak yazılır.<br>`"sRGB"` — girdi sRGB ile kodlanmış Rec.709'dur; ters sRGB EOTF uygulanır.<br>`"HDR"` — girdi HLG ile kodlanmış Rec.2020 (BT.2100)'dir; sahne-doğrusal ışık elde etmek için ters HLG OETF uygulanır.<br>`"linear"` — girdi zaten sahne-doğrusaldır (Rec.709 ana renkleri); değiştirilmeden yazılır. Bunu renderer/kompozitör çıktısı için kullanın.<br>`"linear ACEScg"` — girdi zaten sahne-doğrusal ACEScg'dir (AP1 / D60); ACEScg renksellikleriyle değiştirilmeden yazılır. (varsayılan: "sRGB") | COMBO | Evet (koşullu) | `"sRGB"`<br>`"HDR"`<br>`"linear"`<br>`"linear ACEScg"` |

### AVIF Girdileri

Bu seçenekler `format` değeri `"avif"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `bit_depth` | Kaydedilen AVIF dosyası için bit derinliği. Otomatik, sRGB için 8-bit YUV420 ve HDR için 10-bit YUV420 kullanır. (varsayılan: "auto") | COMBO | Evet (koşullu) | `"auto"`<br>`"8-bit YUV420"`<br>`"10-bit YUV420"` |
| `input_color_space` | Girdi görüntülerinin renk uzayı. HDR, BT.2020/HLG'yi seçer; HDR PQ ise BT.2020/PQ'yu seçer. (varsayılan: "sRGB") | COMBO | Evet (koşullu) | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `crf` | Daha düşük değerler daha yüksek kalite ve daha büyük dosyalar üretir. (varsayılan: 18) | INT | Evet (koşullu) | 1 ile 63 arası |
| `save_mode` | AVIF dosyası için kaydetme modu. `"still images"` toplu işteki her görüntüyü ayrı bir durağan dosya olarak kaydeder; `"animated"` tüm toplu işi tek bir animasyonlu AVIF dosyası olarak kaydeder ve `fps` ile `loop_count` seçeneklerini gösterir. (varsayılan: "still images") | DYNAMIC_COMBO | Evet (koşullu) | `"still images"`<br>`"animated"` |

### AVIF Animasyonlu Seçenekler

Bu seçenekler `save_mode` değeri `"animated"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `fps` | Animasyonun kare hızı. (varsayılan: 6.0) | FLOAT | Evet (koşullu) | 0.01 ile 1000.0 arası |
| `loop_count` | Animasyonun döngü sayısı. 0 sonsuza kadar döngüye girer. (varsayılan: 0) | INT | Evet (koşullu) | 0 ile 1000 arası |

**Parametre Bağımlılıkları Hakkında Notlar:**
- Biçime özgü parametreler (`bit_depth`, `input_color_space` ve AVIF için ayrıca `crf` ile `save_mode`) yalnızca belirli bir `format` seçildiğinde kullanılabilir.
- PNG biçimi için yalnızca "8-bit" ve "16-bit" bit derinlikleri ile yalnızca "sRGB" renk uzayı kullanılabilir.
- EXR biçimi için "16-bit float" ve "32-bit float" bit derinliklerinin ikisi de "sRGB", "HDR", "linear" veya "linear ACEScg" renk uzaylarıyla kullanılabilir. "16-bit float" varsayılandır ve daha küçük dosyalar üretir.
- AVIF biçimi için `fps` ve `loop_count` yalnızca `save_mode` değeri `"animated"` olarak ayarlandığında kullanılabilir.
- PNG ve EXR görüntüleri 1 (gri tonlama), 3 (RGB) veya 4 (RGBA) kanala sahip olmalıdır; diğer kanal sayıları desteklenmez ve hata verir.
- AVIF yalnızca 1 kanallı gri tonlama ve 3 kanallı RGB görüntüleri destekler; RGBA (alfa) görüntüler desteklenmez ve hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Girdi görüntüleri, değiştirilmeden aktarılır. Düğümün arayüz çıktısı, her biri dosya adı, alt klasör ve tür ("output") içeren kaydedilmiş görüntü sonuçlarının bir listesini sağlar. Birden fazla görüntü içeren animasyonlu AVIF için arayüz çıktısı ayrıca bir `animated` işareti içerir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `4e8a92c5f1bba35bc4cdf8c858cc9a6fe57cf08436e2dc303d8204c726108216`
