Bu düğüm, Bria AI hizmetini kullanarak bir videonun arka planını kaldırır. Giriş videosunu işler ve orijinal arka planı seçtiğiniz düz bir renkle değiştirir. İşlem harici bir API aracılığıyla gerçekleştirilir ve sonuç yeni bir video dosyası olarak döndürülür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Arka planı kaldırılacak giriş video dosyası. | VIDEO | Evet | Yok |
| `arka plan rengi` | Çıkış videosu için yeni arka plan olarak kullanılacak düz renk. | STRING | Evet | `"Siyah"`<br>`"Beyaz"`<br>`"Gri"`<br>`"Kırmızı"`<br>`"Yeşil"`<br>`"Mavi"`<br>`"Sarı"`<br>`"Camgöbeği"`<br>`"Eflatun"`<br>`"Turuncu"` |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eden tohum değeri. Tohum değerinden bağımsız olarak sonuçlar deterministik değildir. (varsayılan: 0) | INT | Hayır | 0 ile 2147483647 arası |

**Not:** Giriş videosunun süresi 60 saniye veya daha kısa olmalıdır.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Arka planı kaldırılmış ve seçilen renkle değiştirilmiş işlenmiş video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/tr.md)

---
**Source fingerprint (SHA-256):** `51499fc006d3fd3fd45f8aad686d92537d399255b3a583fd54b77c5a0698a068`
