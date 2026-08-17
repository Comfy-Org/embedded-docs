# OpenAI GPT Görüntü 2

Bu düğüm, OpenAI GPT Image API'sini kullanarak görüntüler üretir. Birkaç GPT Image modelini, düzenleme için isteğe bağlı referans görüntülerini ve iç boyama (inpainting) için isteğe bağlı bir maskeyi destekler. Referans görüntüler sağlandığında düğüm API'ye bir düzenleme isteği gönderir; aksi takdirde düz bir üretim isteği gönderir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak OpenAI GPT Image modeli. Bir model seçmek, o modele özgü ek parametreleri ortaya çıkarır. | DYNAMIC_COMBO | Evet | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `prompt` | GPT Image için metin istemi (varsayılan: ""). | STRING | Evet | N/A |
| `n` | Üretilecek görüntü sayısı (varsayılan: 1). | INT | Evet | 1 ila 8 |
| `seed` | Tekrarlanabilirlik için tohum değeri (varsayılan: 0). Henüz arka uçta uygulanmamıştır. | INT | Evet | 0 ila 2147483647 |

### gpt-image-2 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model.size` | Görüntü boyutu. Özel genişlik ve yüksekliği kullanmak için "Custom" seçin (varsayılan: "auto"). | COMBO | Evet | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Yalnızca `size` değeri "Custom" olduğunda kullanılır. 16'nın katı olmalıdır (varsayılan: 1024). | INT | Hayır | 1024 ila 3840 |
| `model.custom_height` | Yalnızca `size` değeri "Custom" olduğunda kullanılır. 16'nın katı olmalıdır (varsayılan: 1024). | INT | Hayır | 1024 ila 3840 |
| `model.background` | Görüntüyü arka planlı veya arka plansız döndürür (varsayılan: "auto"). | COMBO | Evet | `"auto"`<br>`"opaque"` |
| `model.quality` | Görüntü kalitesi, maliyeti ve üretim süresini etkiler (varsayılan: "low"). | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"` |

### gpt-image-1.5 ve gpt-image-1 Girdileri

Bu iki model aynı modele özgü parametre setini paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model.size` | Görüntü boyutu (varsayılan: "auto"). | COMBO | Evet | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `model.background` | Görüntüyü arka planlı veya arka plansız döndürür (varsayılan: "auto"). | COMBO | Evet | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Görüntü kalitesi, maliyeti ve üretim süresini etkiler (varsayılan: "low"). | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"` |

### Referans Girdileri

Bu girdiler tüm modeller için kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model.images` | Görüntü düzenleme için isteğe bağlı referans görüntü(ler). Genişletilebilir yuva: en fazla 16 görüntü bağlayın (`image_1` ile `image_16` arası). | IMAGE | Hayır | 0 ila 16 görüntü |
| `model.mask` | İç boyama (inpainting) için isteğe bağlı maske (beyaz alanlar değiştirilir). Tam olarak bir referans görüntü gerektirir. | MASK | Hayır | N/A |

**Parametre Kısıtlamaları ve Sınırlamalar:**

- `model.size` değeri "Custom" olduğunda (yalnızca gpt-image-2), `model.custom_width` ve `model.custom_height` 16'nın katı olmalı, en uzun kenar 3840 pikseli aşmamalı, en-boy oranı 3:1'i aşmamalı ve toplam piksel sayısı 655,360 ile 8,294,400 arasında olmalıdır.
- Bir maske tam olarak bir referans görüntü gerektirir. Maske, girdi görüntüsü olmadan kullanılamaz ve birden fazla girdi görüntüsüyle birlikte kullanılamaz.
- Maske sağlandığında, maske yüksekliği ve genişliği, girdi görüntüsünün yüksekliği ve genişliğiyle eşleşmelidir.
- Referans görüntüler, API'ye gönderilmeden önce en fazla 2048 x 2048 toplam piksele küçültülür.
- `seed` parametresi henüz arka uçta uygulanmamıştır.
- API tek bir yanıtta farklı boyutlara sahip görüntüler döndürürse, tüm görüntüler ilk görüntünün boyutlarına uyacak şekilde yeniden boyutlandırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Üretilen görüntü veya görüntüler, (N, H, W, C) şeklinde tek bir batch tensöründe istiflenir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `fb3491f949151fbd3f5825ec9f9ae124019767d083f56966ef34af278aef50c0`
