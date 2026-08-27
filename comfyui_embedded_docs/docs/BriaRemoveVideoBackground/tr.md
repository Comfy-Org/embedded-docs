# Bria Video Arka Planı Kaldır

Bu düğüm, Bria AI hizmetini kullanarak bir videodan arka planı kaldırır. Girdi videosunu işler ve orijinal arka planı, seçtiğiniz düz bir renkle değiştirir. İşlem, harici bir API üzerinden gerçekleştirilir ve sonuç yeni bir video dosyası olarak döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Arka planın kaldırılacağı girdi video dosyası. | VIDEO | Evet | N/A |
| `arka plan rengi` | Çıktı videosu için arka plan rengi. | COMBO | Evet | `"Black"`<br>`"White"`<br>`"Gray"`<br>`"Red"`<br>`"Green"`<br>`"Blue"`<br>`"Yellow"`<br>`"Cyan"`<br>`"Magenta"`<br>`"Orange"` |
| `tohum` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0 ile 2147483647 arası |

**Not:** Girdi videosunun süresi 60 saniye veya daha az olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Arka planı kaldırılan ve seçilen renkle değiştirilen, H.264 codec'i ile MP4 olarak kodlanmış işlenmiş video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/tr.md)

---
**Source fingerprint (SHA-256):** `dbd6b7393f893be5a40322fc96b90bb3d5f1818bdda7b8109b28f48baac44d59`
