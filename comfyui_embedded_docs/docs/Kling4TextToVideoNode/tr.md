# Kling 4.0 Metinden Videoya

Kling 4.0 modeliyle metin isteminden ses dahil olacak şekilde video oluşturur. Bu düğüm, istemi ve oluşturma ayarlarını Kling API'sine gönderir, görevin tamamlanmasını bekler ve tamamlanan videoyu döndürür. Yalnızca bir açıklamadan, referans medya olmadan klip oluşturulması gerektiğinde kullanın.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Model seçici. `"kling-4.0"` 4K HDR ve 30 saniyeye kadar destekler; `"kling-4.0-flash"` 720p ve 20 saniye ile sınırlıdır. Bir model seçildiğinde aşağıda o modelin girdileri görünür. | DYNAMIC_COMBO | Evet | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### kling-4.0 Girdileri

Bu girdiler `model` `"kling-4.0"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak videonun metin açıklaması. 1 ile 26000 karakter arasında olmalıdır. | STRING | Evet | 1 ile 26000 karakter arası |
| `resolution` | Çıktı videosunun çözünürlüğü; adında `HDR` bulunan bir seçenek HDR video döndürür. Varsayılan: `"720p"`. | COMBO | Evet | `"720p"`<br>`"1080p"`<br>`"4k"`<br>`"1080p HDR"`<br>`"4k HDR"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. Varsayılan: `"16:9"`. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu. Varsayılan: 5. | INT | Evet | 3 ile 30 arası |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

### kling-4.0-flash Girdileri

Bu girdiler `model` `"kling-4.0-flash"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak videonun metin açıklaması. 1 ile 26000 karakter arasında olmalıdır. | STRING | Evet | 1 ile 26000 karakter arası |
| `resolution` | Çıktı videosunun çözünürlüğü. Flash yalnızca 720p oluşturur. Varsayılan: `"720p"`. | COMBO | Evet | `"720p"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. Varsayılan: `"16:9"`. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu. Varsayılan: 5. | INT | Evet | 3 ile 20 arası |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Görev tamamlandığında sağlayıcıdan indirilen oluşturulmuş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4TextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `7a5d99aa6f5fdb923ce9e2c89f64e92d46fad14d28002a033ddedc24c7d27894`
