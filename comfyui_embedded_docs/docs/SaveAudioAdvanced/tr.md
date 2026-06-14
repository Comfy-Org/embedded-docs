# Ses Kaydet (Gelişmiş)

Giriş sesini ComfyUI çıktı dizininize kaydeder. Bu düğüm, FLAC, MP3 ve Opus dahil olmak üzere çeşitli formatlarda, yapılandırılabilir kalite ayarlarıyla ses dışa aktarmanıza olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ses` | Kaydedilecek ses. | AUDIO | Evet | - |
| `dosya_adı_ön_eki` | Kaydedilecek dosya için ön ek. %date:yyyy-MM-dd% gibi biçimlendirme belirteçleri içerebilir. (varsayılan: "audio/ComfyUI") | STRING | Evet | - |
| `format` | Sesin kaydedileceği dosya biçimi. | COMBO | Evet | "flac"<br>"mp3"<br>"opus" |

Biçim olarak "mp3" seçildiğinde, aşağıdaki seçeneklerle birlikte bir `quality` alt parametresi kullanılabilir hale gelir: "V0", "128k", "320k" (varsayılan: "V0").

Biçim olarak "opus" seçildiğinde, aşağıdaki seçeneklerle birlikte bir `quality` alt parametresi kullanılabilir hale gelir: "64k", "96k", "128k", "192k", "320k" (varsayılan: "128k").

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|-------------|-----------|
| `ui` | Kaydedilen ses dosyası bilgilerini içeren kullanıcı arayüzü çıktısı. | UI |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `98314263dd84c562e7c02ba89f3d10551fcb898ac784af2aa397ca8357e4aae8`
