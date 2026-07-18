# SyncLipSyncNode

Bu düğüm, sync.so API'sini kullanarak bir videodaki ağız hareketlerini yeni bir konuşma sesine yeniden senkronize eder. Yakın çekimleri, profilleri ve engelleri otomatik olarak işlerken konuşmacının ifadesini korur. Maliyet, çıktı süresine göre değişir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Yeniden senkronize edilecek konuşmacının görüntüsü. 4K'ya (4096x2160) kadar; 24/25/30 fps'lik sabit bir kare hızı en iyi sonucu verir. | VIDEO | Evet | - |
| `audio` | Ağzın senkronize edileceği konuşma sesi. | AUDIO | Evet | - |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |
| `model` | sync.so üretim modeli. | COMBO | Evet | Aşağıya bakın |

`model` parametresi, aşağıdaki alt parametreleri içeren dinamik bir birleşik giriştir:

| Alt Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---------------|-------------|-----------|----------|-------|
| `sync_mode` | Video ve ses arasındaki süre uyumsuzluğunun nasıl ele alınacağı; bu aynı zamanda çıktı uzunluğunu da belirler (varsayılan: "bounce"). | COMBO | Evet | `"bounce"`<br>`"cut_off"`<br>`"loop"`<br>`"silence"`<br>`"remap"` |
| `speaker_selection` | Birden fazla kişi görünür olduğunda hangi yüzün dudak senkronizasyonunun yapılacağı (varsayılan: "default"). | COMBO | Evet | `"default"`<br>`"auto-detect"`<br>`"coordinates"` |
| `speaker_frame` | Konuşmacıyı bulmak için kullanılan video karesi. Yalnızca `speaker_selection` "coordinates" olduğunda kullanılır (varsayılan: 0). | INT | Hayır | 0 ile 1000000 arası |
| `speaker_x` | Konuşmacının yüzünün X piksel koordinatı. Yalnızca `speaker_selection` "coordinates" olduğunda kullanılır (varsayılan: 0). | INT | Hayır | 0 ile 4096 arası |
| `speaker_y` | Konuşmacının yüzünün Y piksel koordinatı. Yalnızca `speaker_selection` "coordinates" olduğunda kullanılır (varsayılan: 0). | INT | Hayır | 0 ile 4096 arası |

**Senkronizasyon modu seçenekleri:**
- `bounce`: Video, ses bitene kadar ileri ve geri oynatılır (çıktı = ses uzunluğu)
- `loop`: Video, ses bitene kadar yeniden başlatılır (çıktı = ses uzunluğu)
- `remap`: Videoya sesle eşleşmesi için zaman esnetmesi uygulanır (çıktı = ses uzunluğu)
- `cut_off`: Daha uzun olan parça kırpılır (çıktı = daha kısa uzunluk)
- `silence`: Hiçbir şey kırpılmaz; daha kısa olan parça doldurulur (çıktı = daha uzun uzunluk)

**Konuşmacı seçimi seçenekleri:**
- `default`: Hangi yüzün dudak senkronizasyonunun yapılacağına modelin karar vermesine izin ver
- `auto-detect`: Etkin konuşmacıyı algıla ve takip et
- `coordinates`: `speaker_frame` tarafından seçilen karedeki piksel (`speaker_x`, `speaker_y`) koordinatlarındaki yüzü hedefle

**Kısıtlamalar:**
- Video çözünürlüğü 4K'yı (4096x2160) aşmamalıdır. Bu sınırın üzerindeki videolar bir hata verecektir.
- Ses süresi 600 saniyeyi (10 dakika) aşmamalıdır.
- `speaker_frame`, `speaker_x` ve `speaker_y` parametreleri yalnızca `speaker_selection` "coordinates" olarak ayarlandığında kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Ağız hareketleri sağlanan sesle eşleşecek şekilde yeniden senkronize edilmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SyncLipSyncNode/tr.md)

---
**Source fingerprint (SHA-256):** `b41f8c9bf0d55059f081a66af20636ec96462c3fd9caeb685cab10278f84678a`
