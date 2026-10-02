# Grok Video

Grok Video düğümü, bir metin açıklamasından kısa bir video oluşturur. Bir istem kullanarak sıfırdan video oluşturabilir veya tek bir girdi görüntüsünden video üretebilir. Düğüm, isteği harici bir API'ye gönderir ve oluşturulan videoyu döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturma için kullanılacak model (varsayılan: `"grok-imagine-video-1.5-lite"`). | COMBO | Evet | `"grok-imagine-video"`<br>`"grok-imagine-video-1.5"`<br>`"grok-imagine-video-1.5-lite"` |
| `istem` | İstenen videonun metin açıklaması. Bir girdi görüntüsü sağlandığında `grok-imagine-video-1.5` modelleri için isteğe bağlıdır. | STRING | Evet | - |
| `çözünürlük` | Çıktı videosunun çözünürlüğü. `1080p`, `grok-imagine-video` için kullanılamaz. | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `en boy oranı` | Çıktı videosunun en-boy oranı. Bir girdi görüntüsü sağlandığında yok sayılır; video, görüntünün en-boy oranını izler. | COMBO | Evet | `"auto"`<br>`"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `süre` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 6). | INT | Evet | 1 - 15 |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 - 2147483647 |
| `görüntü` | İsteğe bağlı başlangıç görüntüsü. Atlanırsa, video yalnızca metin isteminden oluşturulur. | IMAGE | Hayır | - |

**Not:** Bir `image` sağlandığında yalnızca bir girdi görüntüsü desteklenir; birden fazla görüntü sağlanması hataya neden olur. Görüntü sağlanmadığında veya bir görüntü olsa bile `grok-imagine-video` kullanıldığında, `prompt` boşluklar temizlendikten sonra boş olmamalıdır. `grok-imagine-video-1.5` modelleri için `prompt` yalnızca bir girdi görüntüsü sağlandığında isteğe bağlıdır. `1080p` çözünürlüğü `grok-imagine-video` için kullanılamaz. `aspect_ratio` `"auto"` olarak ayarlandığında, en-boy oranı hizmet tarafından otomatik olarak seçilir; bir girdi görüntüsü sağlandığında `aspect_ratio` yok sayılır ve video, görüntünün en-boy oranını izler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `ed5a1c39598a319d5b350b19f39a352dedd1150471695d25f7637fc0f8735d02`
