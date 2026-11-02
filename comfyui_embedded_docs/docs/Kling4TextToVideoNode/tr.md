# Kling 4.0 Text to Video

Kling 4.0 modeliyle metin isteminden ses dahil bir video oluşturur. Bu düğüm, istemi ve üretim ayarlarını Kling API'sine gönderir, görevin tamamlanmasını bekler ve tamamlanan videoyu döndürür. Yalnızca bir açıklamadan, referans medya olmadan klip oluşturulması gerektiğinde kullanın.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Model seçici. Yalnızca `"kling-4.0"` kullanılabilir; seçildiğinde aşağıdaki girdiler görünür. | DYNAMIC_COMBO | Evet | `"kling-4.0"` |

### kling-4.0 Girdileri

Bu girdiler `model` `"kling-4.0"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak videonun metin açıklaması. 1 ile 26000 karakter arasında olmalıdır. | STRING | Evet | 1 - 26000 karakter |
| `resolution` | Çıktı videosunun çözünürlüğü. Varsayılan: `"720p"`. | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. Varsayılan: `"16:9"`. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu. Varsayılan: 5. | INT | Evet | 3 - 30 |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 - 2147483647 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Görev tamamlandığında sağlayıcıdan indirilen oluşturulmuş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4TextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `3835dcb7d83d843ea7f6c5dc691b48759d9c3e7a7baeead3d0f92817e73d6079`
