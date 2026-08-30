# Görüntüyü Kaydet (Gelişmiş)

**Save Image (Advanced)** düğümü, girdi görüntülerini dosya biçimi, bit derinliği ve renk uzayı üzerinde gelişmiş kontrol ile ComfyUI çıktı dizininize kaydeder. PNG, EXR veya AVIF dosyaları (animasyonlu AVIF dahil) olarak kaydetmeyi destekler ve kaydedilen dosyalara iş akışı meta verileri gömülebilir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `görüntüler` | Kaydedilecek görüntüler. | IMAGE | Evet | - |
| `dosya_adı_ön_eki` | Kaydedilecek dosyanın ön ekidir. `%date:yyyy-MM-dd%` veya `%Empty Latent Image.width%` gibi biçimlendirme belirteçleri içerebilir. (varsayılan: "ComfyUI") | STRING | Evet | - |
| `format` | Görüntünün kaydedileceği dosya biçimi. Bir biçim seçmek, o biçime özel ek seçenekleri görüntüler. | DYNAMIC_COMBO | Evet | `"png"`<br>`"exr"`<br>`"avif"` |

### PNG Girdileri

Bu seçenekler, `format` `"png"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `bit_depth` | Kaydedilen PNG dosyası için bit derinliği. (varsayılan: "8-bit") | COMBO | Evet (koşullu) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | Girdi tensörünün renk uzayı. PNG biçimi için yalnızca sRGB kullanılabilir. (varsayılan: "sRGB") | COMBO | Evet (koşullu) | `"sRGB"` |

### EXR Girdileri

Bu seçenekler, `format` `"exr"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `bit_depth` | Kaydedilen EXR dosyası için bit derinliği. (varsayılan: "32-bit float") | COMBO | Evet (koşullu) | `"32-bit float"` |
| `input_color_space` | Girdi tensörünün renk uzayı. EXR her zaman eşleşen gamutta sahne-doğrusal (scene-linear) olarak yazılır.<br>`"sRGB"` — girdi, sRGB kodlu Rec.709'dur; ters sRGB EOTF uygulanır.<br>`"HDR"` — girdi, HLG kodlu Rec.2020'dir (BT.2100); sahne-doğrusal ışık elde etmek için ters HLG OETF uygulanır.<br>`"linear"` — girdi zaten sahne-doğrusaldır (Rec.709 birincil renkleri); değiştirilmeden yazılır. Oluşturucu/birleştirici (renderer/compositor) çıktısı için bunu kullanın. (varsayılan: "sRGB") | COMBO | Evet (koşullu) | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

### AVIF Girdileri

Bu seçenekler, `format` `"avif"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `bit_depth` | Kaydedilen AVIF dosyası için bit derinliği. auto, sRGB için 8-bit YUV420 ve HDR için 10-bit YUV420 kullanır. (varsayılan: "auto") | COMBO | Evet (koşullu) | `"auto"`<br>`"8-bit YUV420"`<br>`"10-bit YUV420"` |
| `input_color_space` | Girdi görüntülerinin renk uzayı. HDR, BT.2020/HLG'yi; HDR PQ ise BT.2020/PQ'yu seçer. (varsayılan: "sRGB") | COMBO | Evet (koşullu) | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `crf` | Daha düşük değerler daha yüksek kalite ve daha büyük dosyalar üretir. (varsayılan: 18) | INT | Evet (koşullu) | 1 ila 63 |
| `save_mode` | AVIF dosyası için kaydetme modu. `"still images"`, gruptaki her görüntüyü ayrı bir durağan dosya olarak kaydeder; `"animated"`, grubun tamamını tek bir animasyonlu AVIF dosyası olarak kaydeder ve `fps` ile `loop_count` seçeneklerini gösterir. (varsayılan: "still images") | DYNAMIC_COMBO | Evet (koşullu) | `"still images"`<br>`"animated"` |

### AVIF Animasyon Seçenekleri

Bu seçenekler, `save_mode` `"animated"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `fps` | Animasyonun kare hızı. (varsayılan: 6.0) | FLOAT | Evet (koşullu) | 0.01 ila 1000.0 |
| `loop_count` | Animasyonun döngüye girme sayısı. 0, sonsuza kadar döngü yapar. (varsayılan: 0) | INT | Evet (koşullu) | 0 ila 1000 |

**Parametre Bağımlılıklarına İlişkin Notlar:**
- Biçime özel parametreler (`bit_depth`, `input_color_space` ve AVIF için ayrıca `crf` ile `save_mode`), yalnızca belirli bir `format` seçildiğinde kullanılabilir.
- PNG biçimi için yalnızca "8-bit" ve "16-bit" bit derinlikleri ve yalnızca "sRGB" renk uzayı kullanılabilir.
- EXR biçimi için yalnızca "32-bit float" bit derinliği; "sRGB", "HDR" veya "linear" renk uzayları kullanılabilir.
- AVIF biçimi için `fps` ve `loop_count` yalnızca `save_mode` `"animated"` olarak ayarlandığında kullanılabilir.
- PNG ve EXR görüntüleri 1 (gri tonlamalı), 3 (RGB) veya 4 (RGBA) kanala sahip olmalıdır; diğer kanal sayıları desteklenmez ve hata oluşturur.
- AVIF yalnızca 1 kanallı gri tonlamalı ve 3 kanallı RGB görüntüleri destekler; RGBA (alfa) görüntüleri desteklenmez ve hata oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Girdi görüntüleri, değiştirilmeden aktarılır. Düğümün arayüz çıktısı, her biri dosya adını, alt klasörü ve türü ("output") içeren kaydedilmiş görüntü sonuçlarının bir listesini sağlar. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `d3df3caca99d58d973d0bc2ff7c22c4626185d390ec2acf870d4014331c4c335`
