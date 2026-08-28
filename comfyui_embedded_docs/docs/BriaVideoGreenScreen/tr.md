# Bria Video Green Screen

Bu düğüm, Bria API kullanarak bir videonun arka planını düz bir kroma anahtar (chroma-key) ekranıyla değiştirir. Giriş videosunu işler ve orijinal arka planın kaldırılıp tek tip yeşil veya mavi ekran rengiyle değiştirildiği yeni bir video döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | İşlenecek giriş videosu | VIDEO | Evet | Video dosyası |
| `green_shade` | Ön planın arkasına uygulanan düz kroma anahtar tonu: broadcast_green (#00B140), chroma_green (#00FF00) veya blue_screen (#0000FF). | COMBO | Evet | `"broadcast_green"`<br>`"chroma_green"`<br>`"blue_screen"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir (varsayılan: 0) | INT | Evet | 0 ile 2147483647 |

**Not:** Giriş videosu 60 saniyeden uzun olmamalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Orijinal arka planın seçilen kroma anahtar tonuyla değiştirildiği işlenmiş video (MP4, H.264) | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoGreenScreen/tr.md)

---
**Source fingerprint (SHA-256):** `70d2951d0adbbe7492b2bc97d04be6591b65f040ca4b414754ad6365c5db45cf`
