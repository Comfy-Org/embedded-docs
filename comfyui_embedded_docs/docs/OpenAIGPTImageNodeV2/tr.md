# OpenAI GPT Image 2.6

Bu düğüm, OpenAI'nin GPT Image API'sini kullanarak görüntüler üretir. Altı modeli destekler — `gpt-image-2.6-flare`, `gpt-image-2.6-sunburst`, `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-2` ve `gpt-image-1.5` — görüntü düzenleme için referans görüntüler eklemenize olanak tanır ve bir görüntünün hangi kısımlarının değiştirileceğini belirtmek için maske kullanabilir.

## Girdiler

### Ortak Girdiler

Bu girdiler her zaman görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak OpenAI GPT Image modeli. Bir model seçmek, o modele özgü ek parametreleri gösterir. | DYNAMIC_COMBO | Evet | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"`<br>`"gpt-image-2.5-flare"`<br>`"gpt-image-2.5-sunburst"`<br>`"gpt-image-2"`<br>`"gpt-image-1.5"` |
| `istem` | GPT Image için metin istemi (varsayılan: `""`). | STRING | Evet | Yok |
| `n` | Kaç görüntü üretileceği (varsayılan: `1`). | INT | Evet | 1 ile 8 arası |
| `tohum` | Yeniden üretilebilirlik için tohum (varsayılan: `0`). Arka uçta henüz uygulanmadı. | INT | Evet | 0 ile 2147483647 arası |

### gpt-image-2.6-flare ve gpt-image-2.6-sunburst Girdileri

Bu girdiler, `model` değeri `gpt-image-2.6-flare` veya `gpt-image-2.6-sunburst` olarak ayarlandığında görünür. Her iki model de aynı parametre kümesini paylaşır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `boyut` | Görüntü boyutu. Özel genişlik ve yüksekliği kullanmak için "Custom" seçeneğini seçin (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `özel_genişlik` | Yalnızca `model.size` değeri "Custom" olduğunda kullanılır. 16'nın katı olmalıdır (varsayılan: `1024`). | INT | Hayır | 480 ile 3840 arası (adım 16) |
| `özel_yükseklik` | Yalnızca `model.size` değeri "Custom" olduğunda kullanılır. 16'nın katı olmalıdır (varsayılan: `1024`). | INT | Hayır | 480 ile 3840 arası (adım 16) |
| `arka_plan` | Görüntüyü arka planlı veya arka plansız döndürür (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `kalite` | Görüntü kalitesi; maliyeti ve üretim süresini etkiler (varsayılan: `"low"`). | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.images` | Görüntü düzenleme için isteğe bağlı referans görüntü(ler). En fazla 16 görüntü. Ayrıntılar için Referans Girdileri bölümüne bakın. | IMAGE | Hayır | 0 ile 16 arası |
| `model.mask` | İnpaunting için isteğe bağlı maske (beyaz alanlar değiştirilecektir). Tam olarak bir referans görüntü gerektirir. | MASK | Hayır | Yok |
| `model.complexity` | Modelin görüntüyü oluşturmadan önce ne kadar planladığı. Düşük değerler daha hızlı döner, yüksek değerler daha fazla planlama yapar. Varsayılan: `"high"`. | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"` |

### gpt-image-2 Girdileri

Bu girdiler, `model` değeri `gpt-image-2` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `boyut` | Görüntü boyutu. Özel genişlik ve yüksekliği kullanmak için "Custom" seçeneğini seçin (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `özel_genişlik` | Yalnızca `model.size` değeri "Custom" olduğunda kullanılır. 16'nın katı olmalıdır (varsayılan: `1024`). | INT | Hayır | 480 ile 3840 arası (adım 16) |
| `özel_yükseklik` | Yalnızca `model.size` değeri "Custom" olduğunda kullanılır. 16'nın katı olmalıdır (varsayılan: `1024`). | INT | Hayır | 480 ile 3840 arası (adım 16) |
| `arka_plan` | Görüntüyü arka planlı veya arka plansız döndürür (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"opaque"` |
| `kalite` | Görüntü kalitesi; maliyeti ve üretim süresini etkiler (varsayılan: `"low"`). | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Görüntü düzenleme için isteğe bağlı referans görüntü(ler). En fazla 16 görüntü. Ayrıntılar için Referans Girdileri bölümüne bakın. | IMAGE | Hayır | 0 ile 16 arası |
| `model.mask` | İnpaunting için isteğe bağlı maske (beyaz alanlar değiştirilecektir). Tam olarak bir referans görüntü gerektirir. | MASK | Hayır | Yok |

### gpt-image-1.5 Girdileri

Bu girdiler, `model` değeri `gpt-image-1.5` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `boyut` | Görüntü boyutu (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `arka_plan` | Görüntüyü arka planlı veya arka plansız döndürür (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `kalite` | Görüntü kalitesi; maliyeti ve üretim süresini etkiler (varsayılan: `"low"`). | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Görüntü düzenleme için isteğe bağlı referans görüntü(ler). En fazla 16 görüntü. Ayrıntılar için Referans Girdileri bölümüne bakın. | IMAGE | Hayır | 0 ile 16 arası |
| `model.mask` | İnpaunting için isteğe bağlı maske (beyaz alanlar değiştirilecektir). Tam olarak bir referans görüntü gerektirir. | MASK | Hayır | Yok |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model.images` | Büyütülebilir yuva: 1..N öğe bağlayın (örn. `image_1`...`image_16`); tüm modeller için en fazla 16 referans görüntü. | IMAGE | Hayır | 0 ile 16 arası |
| `model.mask` | İnpaunting için isteğe bağlı maske (beyaz alanlar değiştirilecektir). Tam olarak bir referans görüntü gerektirir. | MASK | Hayır | Yok |

**Parametre Kısıtlamaları ve Sınırlamaları:**

- `model.size` değeri "Custom" olduğunda (yalnızca `gpt-image-2.6-flare`, `gpt-image-2.6-sunburst`, `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst` ve `gpt-image-2` için), `model.custom_width` ve `model.custom_height` değerlerinin her ikisi de 16'nın katı olmalıdır, en uzun kenar 3840'ı aşmamalıdır, en-boy oranı 3:1'i aşmamalıdır ve toplam piksel sayısı 655.360 ile 8.294.400 arasında olmalıdır.
- `model.mask`, `model.images` içinde tam olarak bir referans görüntü gerektirir: görüntü olmadan kullanılamaz ve birden fazla görüntüyle kullanılamaz.
- `model.mask` kullanıldığında, yüksekliği ve genişliği referans görüntünün yükseklik ve genişliğiyle eşleşmelidir.
- `model.images` sağlandığında, düğüm görüntü düzenleme modunda çalışır; `model.images` olmadan, yalnızca istemden görüntü üretir.
- Referans görüntüler ve maske, API'ye gönderilmeden önce küçültülür.
- `"xhigh"` ve `"max"` kalite seviyeleri yalnızca `gpt-image-2.6-flare`, `gpt-image-2.6-sunburst`, `gpt-image-2.5-flare` ve `gpt-image-2.5-sunburst` için kullanılabilir.
- `model.complexity` yalnızca `gpt-image-2.6-flare` ve `gpt-image-2.6-sunburst` için kullanılabilir; diğer modeller sabit bir planlama derinliği kullanır.
- `seed` şu anda arka uçta uygulanmamıştır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Üretilen görüntü veya görüntüler. Döndürülen tüm görüntüler tek bir toplu işte birleştirilir; boyutları farklıysa, ilk görüntüyle eşleşecek şekilde yeniden boyutlandırılır. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `effc65978ac1cca52a8d8c85230784c23c9eb2afffd7f057aba9f9627e784a15`
