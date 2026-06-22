# ByteDance İlk-Son-Kare'den Videoya

Bu belge, yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/en.md)

Bu düğüm, bir metin istemi ile birlikte ilk ve son kare görüntülerini kullanarak bir video oluşturur. Tanımınızı ve iki ana kareyi alarak, bunlar arasında geçiş yapan eksiksiz bir video dizisi oluşturur. Düğüm, videonun çözünürlüğünü, en boy oranını, süresini ve diğer oluşturma parametrelerini kontrol etmek için çeşitli seçenekler sunar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak model (varsayılan: `"seedance-1-0-lite-i2v-250428"`). | COMBO | Evet | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-i2v-250428"` |
| `prompt` | Videoyu oluşturmak için kullanılan metin istemi. | STRING | Evet | - |
| `ilk_kare` | Video için kullanılacak ilk kare. 300x300 ile 6000x6000 piksel arasında olmalı ve en boy oranı 0,4 ile 2,5 arasında olmalıdır. | IMAGE | Evet | - |
| `son_kare` | Video için kullanılacak son kare. 300x300 ile 6000x6000 piksel arasında olmalı ve en boy oranı 0,4 ile 2,5 arasında olmalıdır. | IMAGE | Evet | - |
| `çözünürlük` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `en_boy_oranı` | Çıktı videosunun en boy oranı (varsayılan: `"adaptive"`). | COMBO | Evet | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `süre` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). Not: `seedance-1-5-pro-251215` modeli için desteklenen minimum süre 4 saniyedir. | INT | Evet | 3 - 12 |
| `tohum` | Oluşturma için kullanılacak tohum değeri (varsayılan: 0). | INT | Hayır | 0 - 2147483647 |
| `sabit_kamera` | Kameranın sabitlenip sabitlenmeyeceğini belirtir. Platform, isteminize kamerayı sabitlemek için bir talimat ekler, ancak gerçek etkiyi garanti etmez (varsayılan: False). | BOOLEAN | Hayır | - |
| `filigran` | Videoya "AI tarafından oluşturuldu" filigranı eklenip eklenmeyeceği (varsayılan: False). | BOOLEAN | Hayır | - |
| `ses_oluştur` | Bu parametre, `seedance-1-5-pro-251215` dışındaki tüm modeller için yok sayılır (varsayılan: False). | BOOLEAN | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `2da7b8ad2bc818a21988c028155ba2b466452a1655ac506fcef01c143dda7450`
