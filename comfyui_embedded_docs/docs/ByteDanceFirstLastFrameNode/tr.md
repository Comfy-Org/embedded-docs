# ByteDance İlk-Son-Kare'den Videoya

Bu düğüm, bir metin istemiyle birlikte ilk ve son kare görüntülerini kullanarak video oluşturur. Açıklamanızı ve iki ana kareyi alarak aralarında geçiş yapan eksiksiz bir video dizisi oluşturur. Düğüm, videonun çözünürlüğünü, en-boy oranını, süresini ve diğer oluşturma parametrelerini denetlemek için çeşitli seçenekler sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturmak için kullanılan model (varsayılan: `"seedance-1-5-pro-251215"`). | COMBO | Evet | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"` |
| `prompt` | Videoyu oluşturmak için kullanılan metin istemi. Boş olmamalı ve ayrılmış parametre anahtar sözcüklerini (`resolution`, `ratio`, `duration`, `seed`, `camerafixed`, `watermark`) içermemelidir. | STRING | Evet | - |
| `first_frame` | Video için kullanılacak ilk kare. 300x300 ile 6000x6000 piksel arasında ve en-boy oranı 0.4 ile 2.5 arasında olmalıdır. | IMAGE | Evet | - |
| `last_frame` | Video için kullanılacak son kare. 300x300 ile 6000x6000 piksel arasında ve en-boy oranı 0.4 ile 2.5 arasında olmalıdır. | IMAGE | Evet | - |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. | COMBO | Evet | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi. `seedance-1-5-pro-251215` kullanılırken minimum süre 4 saniyedir. (varsayılan: 5) | INT | Evet | 3 - 12 |
| `seed` | Oluşturma için kullanılacak seed. (varsayılan: 0) | INT | Hayır | 0 - 2147483647 |
| `camera_fixed` | Kameranın sabitlenip sabitlenmeyeceğini belirtir. Platform, isteminize kamerayı sabitleme talimatı ekler ancak gerçek etkiyi garanti etmez. (varsayılan: False) | BOOLEAN | Hayır | - |
| `watermark` | Videoya "AI generated" filigranı eklenip eklenmeyeceği. (varsayılan: False) | BOOLEAN | Hayır | - |
| `generate_audio` | Bu parametre `seedance-1-5-pro-251215` dışındaki tüm modeller için yok sayılır. (varsayılan: False) | BOOLEAN | Hayır | - |

**Not:** `seedance-1-5-pro-251215` modeli için `duration` 4 saniye veya daha büyük olmalıdır. Hem `first_frame` hem de `last_frame` 300x300 ile 6000x6000 piksel arasında olmalı ve en-boy oranı 0.4 ile 2.5 arasında olmalıdır. `prompt`, ayrılmış parametre anahtar sözcükleri içeriyorsa denetlenir ve reddedilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `ae0f3a34a21baad7f04f6917e98d16dc64496479a050896869ec6693a9a9ebaf`
