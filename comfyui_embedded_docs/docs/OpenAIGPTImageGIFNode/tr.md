# OpenAI GPT Image 2.6 GIF

## Genel Bakış

OpenAI GPT Image 2.6 GIF, bir istemden OpenAI'nin GPT Image modelleriyle animasyonlu GIF oluşturur ve bunu kare grubu ile kare hızı olarak döndürür; böylece doğrudan bir video veya animasyonlu görüntü kaydetme düğümüne aktarılabilir. İki model mevcuttur: `gpt-image-2.6-flare` ve `gpt-image-2.6-sunburst`.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Animasyon için kullanılacak GPT Image modeli. | DYNAMIC_COMBO | Evet | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"` |

### gpt-image-2.6-flare ve gpt-image-2.6-sunburst Girdileri

Her iki model de aynı parametreleri paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model.prompt` | Neyin canlandırılacağı. (varsayılan: `""`) | STRING | Evet | N/A |
| `model.size` | Her karenin boyutu. Daha büyük boyutlar yalnızca daha düşük kare sayılarıyla sığar. (varsayılan: `"512x512"`) | COMBO | Evet | `"384x384"`<br>`"512x512"`<br>`"640x640"`<br>`"720x720"`<br>`"768x768"`<br>`"960x960"`<br>`"512x288"`<br>`"288x512"`<br>`"1024x576"`<br>`"576x1024"`<br>`"1280x720"`<br>`"720x1280"` |
| `model.frame_count` | Kare sayısı. Kareler adımlarla faturalandırılır: 2 ile 8, 9, 10 ile 12, 13 ile 16. (varsayılan: `9`) | INT | Evet | 2 ile 16 arası |
| `model.frame_duration_ms` | Her karenin ne kadar süre gösterileceği, milisaniye cinsinden. (varsayılan: `200`) | INT | Evet | 20 ile 2000 arası (adım 10) |
| `model.background` | Kare arka planı. Saydamlık, vp9 kullanan Save WEBM, Save Animated WEBP ve Save Animated PNG tarafından korunur. (varsayılan: `"opaque"`) | COMBO | Evet | `"opaque"`<br>`"transparent"` |
| `model.quality` | Görüntü kalitesi. Daha yüksek seviyeler daha maliyetlidir ve daha uzun sürer. (varsayılan: `"low"`) | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.complexity` | Modelin, oluşturmadan önce animasyonu ne ölçüde planladığı. (varsayılan: `"high"`) | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"` |
| `model.seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: `42`) | INT | Evet | 0 ile 2147483647 arası |

**Parametre Kısıtlamaları ve Sınırlamaları:**

- Kare hızı `model.frame_duration_ms` üzerinden hesaplanır: 200 ms, 5 fps verir.
- Büyük bir `model.size` ile yüksek bir `model.frame_count` birlikte kullanılamaz ve fiyat rozetinde "Size too large for this frame count" gösterir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `frames` | Video veya animasyonlu görüntü kaydetme düğümüne hazır, kare grubu olarak animasyon. | IMAGE |
| `fps` | Döndürülen GIF'in kare süresinden okunan saniyedeki kare sayısı. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageGIFNode/tr.md)

---
**Source fingerprint (SHA-256):** `e47ebaef90f8b2618ef3c2659778f75ac9763013dcc515ba5650764ce49da951`
