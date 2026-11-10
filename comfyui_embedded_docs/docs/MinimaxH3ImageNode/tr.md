# MiniMax H3 Image

MiniMax H3 Image ile metinden görüntüler oluşturur veya en fazla 16 referans görüntüyü düzenler ve birleştirir. İstem, referanslara bağlantı sırasına göre `@Image1`, `@Image2` ve benzeri şekilde atıfta bulunur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | `MiniMax-H3-Image` veya daha hızlı çalıştırmalar için `MiniMax-H3-Image-Highspeed`. Varsayılan: `"MiniMax-H3-Image"`. | COMBO | Evet | `"MiniMax-H3-Image"`<br>`"MiniMax-H3-Image-Highspeed"` |
| `prompt` | Ne oluşturulacağı veya referansların nasıl düzenleneceği. Referans görüntüler bağlıyken en fazla 8.000 karakter olabilir. Varsayılan: boş. | STRING | Evet | 1 ile 8000 karakter arası |
| `size` | `2K` ve `4K` boyutu bir en-boy oranından türetir; `custom` tam bir genişlik ve yükseklik ayarlar. Varsayılan: `"2K"`. | DYNAMIC_COMBO | Evet | `"2K"`<br>`"4K"`<br>`"custom"` |
| `enhance_prompt` | MiniMax, oluşturmadan önce istemi ayrıntılı bir sahne açıklamasına yeniden yazar. Görüntü düzenlemeleri her zaman iyileştirilir. Kapalıyken sabit bir en-boy oranı veya özel bir boyut seçin. Varsayılan: true. | BOOLEAN | Hayır | true<br>false |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Hayır | 0 ile 2147483647 arası |
| `images` | Düzenlenecek veya birleştirilecek referans görüntüler; istemde bağlantı sırasına göre `@Image1` ile `@Image16` arası şeklinde belirtilir. | AUTOGROW | Hayır | En fazla 16 görüntü |

### Boyut "2K" ve "4K" Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | `auto` ile MiniMax oranı istemden seçer veya bir referans görüntü bağlıysa onu takip eder. `enhance_prompt` kapalıyken metinden görüntüye işlemi sabit bir oran gerektirir. Varsayılan: `"auto"`. | COMBO | Evet | Birden çok seçenek mevcut |

### Boyut "custom" Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `width` | Piksel cinsinden çıktı genişliği. Varsayılan: 2048. | INT | Evet | 512 ile 7680 arası (adım: 16) |
| `height` | Piksel cinsinden çıktı yüksekliği. Varsayılan: 2048. | INT | Evet | 512 ile 7680 arası (adım: 16) |

Not: Özel bir boyut için genişlik çarpı yükseklik 655.360 ile 20.000.000 piksel arasında olmalı ve en-boy oranı en fazla 3:1 olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Oluşturulan veya düzenlenen görüntü, PNG olarak. | IMAGE |
| `revised_prompt` | İstem iyileştirme açıkken MiniMax'in kullandığı yeniden yazılmış istem. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxH3ImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `723eb4c2d3b303ece041f98bd5b773c669affb9a7b3da0c08ffcac4ee89f8e11`
