> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/tr.md)

Bu düğüm, Bria AI servisini kullanarak bir videodan arka planı kaldırır. Giriş videosunu işler ve orijinal arka planı seçtiğiniz düz bir renkle değiştirir. İşlem harici bir API üzerinden gerçekleştirilir ve sonuç yeni bir video dosyası olarak döndürülür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Evet | Yok | Arka planının kaldırılacağı giriş video dosyası. |
| `background_color` | STRING | Evet | `"Siyah"`<br>`"Beyaz"`<br>`"Gri"`<br>`"Kırmızı"`<br>`"Yeşil"`<br>`"Mavi"`<br>`"Sarı"`<br>`"Camgöbeği"`<br>`"Eflatun"`<br>`"Turuncu"` | Çıktı videosu için yeni arka plan olarak kullanılacak düz renk. |
| `seed` | INT | Hayır | 0 ile 2147483647 | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eden bir seed değeri. Seed değerinden bağımsız olarak sonuçlar deterministik değildir. (varsayılan: 0) |

**Not:** Giriş videosunun süresi 60 saniye veya daha kısa olmalıdır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Arka planı kaldırılmış ve seçilen renkle değiştirilmiş işlenmiş video dosyası. |
