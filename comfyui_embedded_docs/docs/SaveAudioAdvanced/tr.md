# Ses Kaydet (Gelişmiş)

Sesi, ComfyUI çıktı dizininize kaydeder. Bu düğüm; FLAC, MP3 ve Opus dahil çeşitli biçimlerde, yapılandırılabilir kalite ayarlarıyla ses dışa aktarmanızı sağlar.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ses` | Kaydedilecek ses. | AUDIO | Evet | - |
| `dosya_adı_ön_eki` | Kaydedilecek dosyanın ön eki. %date:yyyy-MM-dd% gibi biçimlendirme belirteçleri içerebilir. (varsayılan: "audio/ComfyUI") | STRING | Evet | - |
| `format` | Sesin kaydedileceği dosya biçimi. | DYNAMIC_COMBO | Evet | "flac"<br>"mp3"<br>"opus" |

### MP3 Girdileri

Biçim olarak "mp3" seçildiğinde aşağıdaki ayar kullanılabilir hale gelir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `quality` | Çıktı MP3 dosyasının kodlama kalitesi. (varsayılan: "V0") | COMBO | Hayır | "V0"<br>"128k"<br>"320k" |

### Opus Girdileri

Biçim olarak "opus" seçildiğinde aşağıdaki ayar kullanılabilir hale gelir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `quality` | Çıktı Opus dosyasının kodlama kalitesi. (varsayılan: "128k") | COMBO | Hayır | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

Not: `quality` ayarı yalnızca ilgili biçim seçildiğinde kullanılabilir. "flac" seçildiğinde ek bir kalite ayarı bulunmaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Giriş sesi, kaydedildikten sonra değiştirilmeden geçirilir. | AUDIO |

Düğüm ayrıca, kaydedilen ses dosyası bilgilerini içeren UI bilgisi döndürür.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `5f3af49670b485bbd31f0ed0c5667c12e9b9b23014cadcf64442a486255d0e6d`
