# Grok Video

Grok Video düğümü, metin açıklamasından kısa bir video oluşturur. Bir istem kullanarak sıfırdan video oluşturabilir veya tek bir girdi görüntüsünden video üretebilir. Düğüm, isteği harici bir API'ye gönderir ve oluşturulan videoyu döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturma için kullanılacak model. | COMBO | Evet | `"grok-imagine-video"`<br>`"grok-imagine-video-1.5"` |
| `istem` | İstenen videonun metin açıklaması. Bir girdi görüntüsü sağlandığında grok-imagine-video-1.5 için isteğe bağlıdır. | STRING | Evet | - |
| `çözünürlük` | Çıktı videosunun çözünürlüğü. 1080p yalnızca grok-imagine-video-1.5 için kullanılabilir. | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `en boy oranı` | Çıktı videosunun en-boy oranı. | COMBO | Evet | `"auto"`<br>`"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `süre` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 6). | INT | Evet | 1 ila 15 |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 ila 2147483647 |
| `görüntü` | İsteğe bağlı başlangıç görüntüsü. Atlanırsa video yalnızca metin isteminden oluşturulur. | IMAGE | Hayır | - |

**Not:** Bir `image` sağlandığında yalnızca bir girdi görüntüsü desteklenir; birden fazla görüntü sağlanması hataya neden olur. Hiçbir görüntü sağlanmadığında veya `grok-imagine-video` kullanılırken bir görüntü olsa bile `prompt` boşluklar kaldırıldıktan sonra boş olmamalıdır. `grok-imagine-video-1.5` için `prompt` yalnızca bir girdi görüntüsü sağlandığında isteğe bağlıdır. `1080p` çözünürlüğü yalnızca `grok-imagine-video-1.5` için kullanılabilir. `aspect_ratio` `"auto"` olarak ayarlandığında en-boy oranı servis tarafından otomatik olarak seçilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `c7d07b7bf9a776892873698abb97c7d936c7770aab397d031a287b7ecfad0b71`
