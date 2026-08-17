# Grok Video

Grok Video düğümü, metin açıklamasından kısa bir video oluşturur. Bir istem kullanarak sıfırdan bir video oluşturabilir veya isteğe bağlı olarak bir istemle yönlendirilen tek bir giriş görüntüsünü canlandırabilir. Düğüm, harici bir API'ye istek gönderir ve oluşturulan videoyu döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturma için kullanılacak model. | COMBO | Evet | "grok-imagine-video"<br>"grok-imagine-video-1.5" |
| `prompt` | İstenen videonun metin açıklaması. Bir giriş görüntüsü sağlandığında grok-imagine-video-1.5 için isteğe bağlıdır. | STRING | Evet | - |
| `resolution` | Çıktı videosunun çözünürlüğü. 1080p yalnızca grok-imagine-video-1.5 için kullanılabilir. | COMBO | Evet | "480p"<br>"720p"<br>"1080p" |
| `aspect_ratio` | Çıktı videosunun en-boy oranı (varsayılan: "auto"). | COMBO | Evet | "auto"<br>"16:9"<br>"4:3"<br>"3:2"<br>"1:1"<br>"2:3"<br>"3:4"<br>"9:16" |
| `duration` | Çıktı videosunun süresi saniye cinsinden (varsayılan: 6). | INT | Evet | 1 to 15 |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum; gerçek sonuçlar, tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 to 2147483647 |
| `image` | İsteğe bağlı başlangıç görüntüsü. Belirtilmezse, video yalnızca metin isteminden oluşturulur. | IMAGE | Hayır | - |

**Not:**
- 1080p çözünürlüğü yalnızca `grok-imagine-video-1.5` modeliyle kullanılabilir. `grok-imagine-video` ile seçilmesi bir hataya yol açar.
- Yalnızca bir giriş görüntüsü desteklenir. Birden fazla görüntü sağlanması bir hataya yol açar.
- `prompt`, model `grok-imagine-video-1.5` olarak ayarlanmadığı ve bir giriş görüntüsü sağlanmadığı sürece gereklidir. Gerekli olduğunda, istem boşluklar temizlendikten sonra en az 1 karakter uzunluğunda olmalıdır.
- `seed` yalnızca düğümün yeniden çalışıp çalışmayacağını belirler; oluşturulan sonuçlar, tohum değerinden bağımsız olarak deterministik değildir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `c708c8cd78749aa533db63e2bc5938ef14fa78cf95f8ba4628d0c586f8723297`
