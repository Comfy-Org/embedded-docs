# Bria Video Arka Plan Değiştir

Bu düğüm, Bria API'sini kullanarak bir videonun arka planını sağlanan bir görsel veya videoyla değiştirir. Çıktı, ön plan videosunun çözünürlüğünü ve kare hızını korur; farklı en boy oranına sahip bir arka plan sığacak şekilde uzatılır, bu nedenle eşleşen en boy oranları bozulmamış sonuçlar üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Arka planı değiştirilen ön plan videosu. | VIDEO | Evet | - |
| `background_image` | Ön planın arkasına yerleştirilecek arka plan görseli. Ya bir arka plan görseli ya da bir arka plan videosu sağlayın, ikisini birden değil. | IMAGE | Hayır | - |
| `background_video` | Ön planın arkasına yerleştirilecek arka plan videosu. Ya bir arka plan görseli ya da bir arka plan videosu sağlayın, ikisini birden değil. | VIDEO | Hayır | - |
| `seed` | Seed, düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0 ile 2147483647 |

**Not:** `background_image` veya `background_video` öğelerinden yalnızca birini sağlamalısınız — ikisini birden değil ve hiçbirini de sağlamamalısınız. Ön plan videosu ve arka plan videosu (kullanılıyorsa) her biri 60 saniye veya daha kısa olmalıdır. `background_image` kullanıldığında, alfa kanalı işleme alınmadan önce kaldırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Arka planı değiştirilmiş son video, MP4 (H.264) olarak kodlanmıştır. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoReplaceBackground/tr.md)

---
**Source fingerprint (SHA-256):** `c487cf7dd434b8523ce64f241c2171c82bb5e0abdc5c3ca3e8b1a1259aeab490`
