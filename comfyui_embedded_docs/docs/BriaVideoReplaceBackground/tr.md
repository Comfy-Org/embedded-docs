# Bria Video Arka Plan Değiştir

Bu düğüm, Bria'nın API'sini kullanarak bir videonun arka planını sağlanan bir görüntü veya video ile değiştirir. Çıktı, ön plan videosunun çözünürlüğünü ve kare hızını korur; farklı en boy oranına sahip bir arka plan, sığacak şekilde uzatılır, bu nedenle en boy oranlarının eşleşmesi bozulmamış sonuçlar üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `video` | Arka planı değiştirilen ön plan videosu. | VIDEO | Evet | - |
| `background_image` | Ön planın arkasına yerleştirilecek arka plan görüntüsü. Ya bir arka plan görüntüsü ya da bir arka plan videosu sağlayın, ikisini birden değil. | IMAGE | Hayır | - |
| `background_video` | Ön planın arkasına yerleştirilecek arka plan videosu. Ya bir arka plan görüntüsü ya da bir arka plan videosu sağlayın, ikisini birden değil. | VIDEO | Hayır | - |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0 ile 2147483647 arası |

**Not:** `background_image` veya `background_video` değerlerinden yalnızca birini sağlamalısınız — ikisini birden değil ve hiçbirini sağlamamak da geçerli değildir. Ön plan videosu 60 saniye veya daha kısa olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `video` | Arka planı değiştirilmiş sonuç videosu. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoReplaceBackground/tr.md)

---
**Source fingerprint (SHA-256):** `4eb9650e5ca88baf2a91a9309b87936b3d18b88e314a56ab4c73d06a9143c645`
