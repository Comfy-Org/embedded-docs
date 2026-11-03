# ByteDance İlk-Son-Kare'den Videoya

Bu düğüm, bir metin istemiyle birlikte ilk ve son kare görüntülerini kullanarak video oluşturur. Açıklamanızı ve iki ana kareyi alarak aralarında geçiş yapan eksiksiz bir video dizisi oluşturur. Düğüm, videonun çözünürlüğünü, en-boy oranını, süresini ve diğer oluşturma parametrelerini denetlemek için çeşitli seçenekler sunar.

**Not:** BytePlus, Seedance 1.5 Pro modelini 11 Kasım 2026'da kapatıyor; bu nedenle bu düğüm artık onu sunmuyor ve onunla kaydedilen iş akışları çalışmayı durduruyor. `seedance-1-0-pro-250528` bu düğümde kalan tek modeldir. Sesli video ve daha uzun klipler için [Seedance 2.5 iş ortağı düğümünü](https://docs.comfy.org/tr/tutorials/partner-nodes/bytedance/seedance-2-5) kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturmak için kullanılan model (varsayılan: `"seedance-1-0-pro-250528"`). | COMBO | Evet | `"seedance-1-0-pro-250528"` |
| `prompt` | Videoyu oluşturmak için kullanılan metin istemi. Boş olmamalı ve ayrılmış parametre anahtar sözcüklerini (`resolution`, `ratio`, `duration`, `seed`, `camerafixed`, `watermark`) içermemelidir. | STRING | Evet | - |
| `ilk_kare` | Video için kullanılacak ilk kare. 300x300 ile 6000x6000 piksel arasında ve en-boy oranı 0.4 ile 2.5 arasında olmalıdır. | IMAGE | Evet | - |
| `son_kare` | Video için kullanılacak son kare. 300x300 ile 6000x6000 piksel arasında ve en-boy oranı 0.4 ile 2.5 arasında olmalıdır. | IMAGE | Evet | - |
| `çözünürlük` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `en_boy_oranı` | Çıktı videosunun en-boy oranı. | COMBO | Evet | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `süre` | Çıktı videosunun saniye cinsinden süresi. (varsayılan: 5) | INT | Evet | 3 - 12 |
| `tohum` | Oluşturma için kullanılacak seed. (varsayılan: 0) | INT | Hayır | 0 - 2147483647 |
| `sabit_kamera` | Kameranın sabitlenip sabitlenmeyeceğini belirtir. Platform, isteminize kamerayı sabitleme talimatı ekler ancak gerçek etkiyi garanti etmez. (varsayılan: False) | BOOLEAN | Hayır | - |
| `filigran` | Videoya "AI generated" filigranı eklenip eklenmeyeceği. (varsayılan: False) | BOOLEAN | Hayır | - |
| `ses_oluştur` | Yapay zeka ile oluşturulmuş bir ses parçası ekler. Kalan modeller bu girdiyi yok sayar (varsayılan: False) | BOOLEAN | Hayır | - |

**Not:** Hem `first_frame` hem de `last_frame` 300x300 ile 6000x6000 piksel arasında olmalı ve en-boy oranı 0.4 ile 2.5 arasında olmalıdır. `prompt`, ayrılmış parametre anahtar sözcükleri içeriyorsa denetlenir ve reddedilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `ae0f3a34a21baad7f04f6917e98d16dc64496479a050896869ec6693a9a9ebaf`
