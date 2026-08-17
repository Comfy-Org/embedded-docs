# Görüntüyü Kaydet (Gelişmiş)

**SaveImageAdvanced** düğümü, dosya formatı, bit derinliği ve renk uzayı üzerinde gelişmiş kontrol ile görüntüleri ComfyUI çıktı dizininize kaydeder. PNG veya EXR dosyaları olarak kaydetmeyi destekler ve iş akışı meta verilerini kaydedilen dosyalara embed edebilir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Kaydedilecek görüntüler. | IMAGE | Evet | - |
| `filename_prefix` | Kaydedilecek dosyanın öneki. `%date:yyyy-MM-dd%` veya `%Empty Latent Image.width%` gibi biçimlendirme belirteçleri içerebilir. (varsayılan: "ComfyUI") | STRING | Evet | - |
| `format` | Görüntünün kaydedileceği dosya formatı. Bir format seçmek, o format için ek seçenekler gösterir. | DYNAMIC_COMBO | Evet | `"png"`<br>`"exr"` |

### PNG Girdileri

Bu girdiler, `format` `"png"` olarak ayarlandığında gösterilir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `bit_depth` | Görüntü kaydedilirken kullanılan bit derinliği. (varsayılan: "8-bit") | COMBO | Evet (koşullu) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | Girdi tensörünün renk uzayı. (varsayılan: "sRGB") | COMBO | Evet (koşullu) | `"sRGB"` |

### EXR Girdileri

Bu girdiler, `format` `"exr"` olarak ayarlandığında gösterilir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `bit_depth` | Görüntü kaydedilirken kullanılan bit derinliği. (varsayılan: "32-bit float") | COMBO | Evet (koşullu) | `"32-bit float"` |
| `input_color_space` | Girdi tensörünün renk uzayı. EXR her zaman eşleşen gamutta sahne-doğrusal (scene-linear) olarak yazılır. (varsayılan: "sRGB") | COMBO | Evet (koşullu) | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

**Parametre Bağımlılıkları ve Dosya Davranışı Hakkında Notlar:**

- `bit_depth` ve `input_color_space` yalnızca bağlı oldukları `format` seçildiğinde görünür.
- PNG formatı için yalnızca `"8-bit"` ve `"16-bit"` bit derinlikleri ile yalnızca `"sRGB"` renk uzayı kullanılabilir. Renk uzayı seçimi PNG piksellerini değiştirmez — PNG dosyaları her zaman sRGB kodlu görüntüler olarak kaydedilir.
- EXR formatı için yalnızca `"32-bit float"` bit derinliği kullanılabilir; `"sRGB"`, `"HDR"` veya `"linear"` renk uzaylarıyla birlikte.
- EXR için `input_color_space` parametresi, kaydetmeden önce girdi tensörünün nasıl yorumlanacağını belirler:
  - `"sRGB"` — girdi, sRGB kodlu Rec.709'dur; ters sRGB EOTF uygulanır.
  - `"HDR"` — girdi, HLG kodlu Rec.2020'dir (BT.2100); sahne-doğrusal ışık elde etmek için ters HLG OETF uygulanır.
  - `"linear"` — girdi zaten sahne-doğrusaldır (Rec.709 ana renkler); değiştirilmeden yazılır. Renderer/birleştirici çıktısı için bunu kullanın.
- İş akışı meta verileri (istem ve ek PNG bilgisi), meta veri yazma `--disable-metadata` komut satırı bağımsız değişkeniyle devre dışı bırakılmadıkça kaydedilen PNG ve EXR dosyalarına embed edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `images` | Kaydedilen görüntüler (`images` girdisine iletilen görüntülerle aynı). Düğümün kullanıcı arayüzü sonucu, kaydedilen dosyaların bir listesini içerir; her dosya dosya adı, alt klasör ve tür ("output") ile raporlanır. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `b03a822a90cf50d30fbf4397ab280393951f08d2339dd48c0dbaf75d9c415bca`
