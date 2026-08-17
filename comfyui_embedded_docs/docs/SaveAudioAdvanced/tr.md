# Ses Kaydet (Gelişmiş)

Ses Kaydet (Gelişmiş)

Girdi sesini ComfyUI çıktı dizininize kaydeder. Ses dosyalarını FLAC, MP3 veya Opus formatında dışa aktarabilir; MP3 ve Opus dosyaları için seçilebilir kalite ayarları sunar.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `format` | Sesin kaydedileceği dosya biçimi. | DYNAMIC_COMBO | Evet | "flac"<br>"mp3"<br>"opus" |
| `audio` | Kaydedilecek ses. | AUDIO | Evet | - |
| `filename_prefix` | Kaydedilecek dosya için önek. %date:yyyy-MM-dd% gibi biçimlendirme belirteçleri içerebilir. (varsayılan: "audio/ComfyUI") | STRING | Evet | - |

### flac Girdileri

`flac` biçimi ek ayar gerektirmez.

### mp3 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `quality` | MP3 dosyaları için kodlama kalitesi. (varsayılan: "V0") | COMBO | Evet | "V0"<br>"128k"<br>"320k" |

### opus Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `quality` | Opus dosyaları için kodlama kalitesi. (varsayılan: "128k") | COMBO | Evet | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

**Not:** `quality` ayarı yalnızca `format` `mp3` veya `opus` olduğunda gösterilir. Eğer `quality` değeri sağlanmazsa, ses seçilen biçimin varsayılan kalitesiyle kaydedilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Girdi sesi, kaydedildikten sonra geçirilir. | AUDIO |
| `ui` | Kaydedilen ses dosyası bilgilerini içeren UI çıktısı. | UI |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `5f3af49670b485bbd31f0ed0c5667c12e9b9b23014cadcf64442a486255d0e6d`
