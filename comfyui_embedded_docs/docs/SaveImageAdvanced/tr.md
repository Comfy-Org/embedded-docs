# SaveImageAdvanced

**SaveImageAdvanced** düğümü, görüntüleri dosya biçimi, bit derinliği ve renk uzayı üzerinde gelişmiş kontrole sahip olarak ComfyUI çıktı dizininize kaydeder. PNG veya EXR dosyaları olarak kaydetmeyi destekler ve kaydedilen dosyalara iş akışı meta verileri ekleyebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntüler` | Kaydedilecek görüntüler. | IMAGE | Evet | - |
| `dosya_adı_ön_eki` | Kaydedilecek dosyanın ön eki. `%date:yyyy-MM-dd%` veya `%Empty Latent Image.width%` gibi biçimlendirme belirteçleri içerebilir. (varsayılan: "ComfyUI") | STRING | Evet | - |
| `format` | Görüntünün kaydedileceği dosya biçimi. Bir biçim seçmek, o biçim için ek seçenekleri görüntüler. | COMBO | Evet | `"png"`<br>`"exr"` |
| `bit_depth` | Seçilen biçim için bit derinliği. Bu parametre, bir biçim seçildiğinde görünür. (varsayılan: PNG için "8-bit", EXR için "32-bit float") | COMBO | Evet (koşullu) | PNG için: `"8-bit"`<br>`"16-bit"`<br>EXR için: `"32-bit float"` |
| `input_color_space` | Girdi tensörünün renk uzayı. PNG için yalnızca sRGB kullanılabilir. EXR için görüntü her zaman eşleşen gamutta sahne-doğrusal olarak yazılır. (varsayılan: "sRGB") | COMBO | Evet (koşullu) | PNG için: `"sRGB"`<br>EXR için: `"sRGB"`<br>`"HDR"`<br>`"linear"` |

**Parametre Bağımlılıkları Hakkında Notlar:**
- `bit_depth` ve `input_color_space` parametreleri yalnızca belirli bir `format` seçildiğinde kullanılabilir.
- PNG biçimi için yalnızca "8-bit" ve "16-bit" bit derinlikleri ve yalnızca "sRGB" renk uzayı kullanılabilir.
- EXR biçimi için yalnızca "32-bit float" bit derinliği, "sRGB", "HDR" veya "linear" renk uzayları ile kullanılabilir.
- EXR için `input_color_space` parametresi, girdi tensörünün nasıl yorumlanacağını belirler:
  - `"sRGB"` — girdi sRGB kodlu Rec.709'dur; ters sRGB EOTF uygulanır.
  - `"HDR"` — girdi HLG kodlu Rec.2020'dir (BT.2100); sahne-doğrusal ışık elde etmek için ters HLG OETF uygulanır.
  - `"linear"` — girdi zaten sahne-doğrusaldır (Rec.709 birincil renkler); değiştirilmeden yazılır. İşleyici/birleştirici çıktısı için kullanın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntüler` | Her biri dosya adı, alt klasör ve tür ("output") içeren kaydedilmiş görüntü sonuçlarının listesi. Bu çıktı, kullanıcı arayüzü görüntüleme amaçları için kullanılır. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `61e52bab8c28437cf648e4790823c15dbe0f758478635b0bd8b5cce785421fe5`
