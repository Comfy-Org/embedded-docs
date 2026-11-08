# OpenAI GPT Image 2.6 SVG

## Genel Bakış

OpenAI GPT Image 2.6 SVG, OpenAI'nin GPT Image modelleriyle bir istemden düzenlenebilir SVG üretir. Sonuç vektör biçimlendirmesidir; bu nedenle şekiller ve metinler bir vektör düzenleyicide düzenlenebilir kalır. İki model kullanılabilir: `gpt-image-2.6-flare` ve `gpt-image-2.6-sunburst`.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | SVG için kullanılacak GPT Image modeli. | DYNAMIC_COMBO | Evet | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"` |

### gpt-image-2.6-flare ve gpt-image-2.6-sunburst Girdileri

Her iki model de aynı parametreleri paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model.prompt` | Çizilecek SVG'nin açıklaması. (varsayılan: `""`) | STRING | Evet | Yok |
| `model.size` | SVG'nin çizildiği referans görüntünün boyutu. (varsayılan: `"1024x1024"`) | COMBO | Evet | `"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `model.background` | Referans görüntünün arka planı. (varsayılan: `"auto"`) | COMBO | Evet | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | SVG'nin çizildiği referans görüntünün kalitesi. (varsayılan: `"low"`) | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.complexity` | Modelin referans görüntüyü oluşturmadan önce ne kadar planladığı. (varsayılan: `"high"`) | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"` |
| `model.seed` | Düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar tohum değerinden bağımsız olarak deterministik değildir. (varsayılan: `42`) | INT | Evet | 0 ile 2147483647 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `svg` | SVG biçimlendirmesi olarak oluşturulan vektör görüntü. | SVG |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageSVGNode/tr.md)

---
**Source fingerprint (SHA-256):** `8ac2f473b265d3b6857e6280a1c017301b124fc6d671ec83a59c677218062c90`
