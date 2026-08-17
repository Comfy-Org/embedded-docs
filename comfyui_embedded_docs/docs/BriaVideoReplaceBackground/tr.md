# Bria Video Arka Plan Değiştir

Bria kullanarak bir videonun arka planını sağlanan bir görsel veya video ile değiştirin. Çıktı, ön planın çözünürlüğünü ve kare hızını korur; farklı bir en-boy oranına sahip arka plan sığacak şekilde esnetilir, bu nedenle bozulmamış sonuçlar için eşleştirin.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Arka planı değiştirilen ön plan videosu. | VIDEO | Evet | - |
| `background_image` | Ön planın arkasına yerleştirilecek arka plan görseli. Bir arka plan görseli veya bir arka plan videosu sağlayın; ikisini birden değil. | IMAGE | Hayır | - |
| `background_video` | Ön planın arkasına yerleştirilecek arka plan videosu. Bir arka plan görseli veya bir arka plan videosu sağlayın; ikisini birden değil. | VIDEO | Hayır | - |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0 to 2147483647 |

**Not:** Tam olarak `background_image` veya `background_video` değerlerinden birini sağlamalısınız — ikisini birden değil, hiçbirini de değil. Hem ön plan hem de arka plan videoları 60 saniye veya daha kısa olmalıdır. Bir arka plan görseli sağlanırsa, alfa (şeffaflık) kanalı yüklemeden önce kaldırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Arka planı değiştirilmiş sonuç videosu. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoReplaceBackground/tr.md)

---
**Source fingerprint (SHA-256):** `c487cf7dd434b8523ce64f241c2171c82bb5e0abdc5c3ca3e8b1a1259aeab490`
