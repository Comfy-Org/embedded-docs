# Bria Video Green Screen

Bu düğüm, Bria API'sini kullanarak bir videonun arka planını düz bir kroma anahtar ekranıyla değiştirir. Giriş videosunu işler ve orijinal arka planın kaldırılıp yerine düz yeşil veya mavi ekran rengi getirildiği yeni bir video döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|----------|--------|
| `video` | İşlenecek giriş videosu | VIDEO | Evet | Video dosyası |
| `green_shade` | Ön planın arkasına uygulanan düz kroma anahtar tonu: broadcast_green (#00B140), chroma_green (#00FF00) veya blue_screen (#0000FF) | STRING | Evet | `"broadcast_green"`<br>`"chroma_green"`<br>`"blue_screen"` |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0) | INT | Evet | 0 ile 2147483647 arası |

**Not:** Giriş videosu 60 saniyeyi geçmemelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `video` | Orijinal arka planın seçilen kroma anahtar tonuyla değiştirildiği işlenmiş video | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoGreenScreen/tr.md)

---
**Source fingerprint (SHA-256):** `663b41bf51bd8d871a59e756f226e4bf6244bb616ebcd2e8ccfa426137f2a05b`
