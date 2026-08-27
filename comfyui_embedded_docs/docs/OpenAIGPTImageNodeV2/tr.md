# OpenAI GPT Görüntü 2

Bu düğüm, OpenAI'nin GPT Image API'sini kullanarak görseller üretir. Birden fazla modeli (`gpt-image-2`, `gpt-image-1.5` ve `gpt-image-1`) destekler, düzenleme için referans görseller sağlamanıza olanak tanır ve bir görselin hangi bölümlerinin değiştirileceğini belirtmek için bir maske kullanabilir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak OpenAI GPT Image modeli. Bir model seçmek, o modele özgü ek parametreleri ortaya çıkarır. | DYNAMIC_COMBO | Evet | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `istem` | GPT Image için metin istemi (varsayılan: `""`). | STRING | Evet | N/A |
| `n` | Kaç adet görsel üretileceği (varsayılan: `1`). | INT | Evet | 1 ile 8 |
| `tohum` | Tekrar üretilebilirlik için tohum (seed) değeri (varsayılan: `0`). Henüz arka uçta uygulanmadı. | INT | Evet | 0 ile 2147483647 |

### gpt-image-2 Girdileri

Bu girdiler, `model` `gpt-image-2` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `boyut` | Görsel boyutu. Özel genişlik ve yüksekliği kullanmak için "Custom" seçin (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `özel_genişlik` | Yalnızca `model.size` "Custom" olduğunda kullanılır. 16'nın katı olmalıdır (varsayılan: `1024`). | INT | Hayır | 1024 ile 3840 |
| `özel_yükseklik` | Yalnızca `model.size` "Custom" olduğunda kullanılır. 16'nın katı olmalıdır (varsayılan: `1024`). | INT | Hayır | 1024 ile 3840 |
| `arka_plan` | Görseli arka planlı veya arka plansız döndürür (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"opaque"` |
| `kalite` | Görsel kalitesi, maliyeti ve üretim süresini etkiler (varsayılan: `"low"`). | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Görsel düzenleme için isteğe bağlı referans görsel(ler)i. En fazla 16 görsel. Ayrıntılar için Referans Girdileri'ne bakın. | IMAGE | Hayır | 0 ile 16 |
| `model.mask` | Inpainting için isteğe bağlı maske (beyaz alanlar değiştirilecektir). Tam olarak bir referans görsel gerektirir. | MASK | Hayır | N/A |

### gpt-image-1.5 ve gpt-image-1 Girdileri

Bu girdiler, `model` `gpt-image-1.5` veya `gpt-image-1` olarak ayarlandığında görünür. Her iki model de aynı parametre kümesini paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `boyut` | Görsel boyutu (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `arka_plan` | Görseli arka planlı veya arka plansız döndürür (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `kalite` | Görsel kalitesi, maliyeti ve üretim süresini etkiler (varsayılan: `"low"`). | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Görsel düzenleme için isteğe bağlı referans görsel(ler)i. En fazla 16 görsel. Ayrıntılar için Referans Girdileri'ne bakın. | IMAGE | Hayır | 0 ile 16 |
| `model.mask` | Inpainting için isteğe bağlı maske (beyaz alanlar değiştirilecektir). Tam olarak bir referans görsel gerektirir. | MASK | Hayır | N/A |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model.images` | Genişletilebilir yuva: 1..N öğe bağlayın (örn. `image_1`...`image_16`); tüm modeller için en fazla 16 referans görsel. | IMAGE | Hayır | 1 ile 16 |
| `model.mask` | Inpainting için isteğe bağlı maske (beyaz alanlar değiştirilecektir). Tam olarak bir referans görsel gerektirir. | MASK | Hayır | N/A |

**Parametre Kısıtlamaları ve Sınırlamalar:**

- `model.size` "Custom" olduğunda (yalnızca gpt-image-2), `model.custom_width` ve `model.custom_height` değerlerinin her ikisi de 16'nın katı olmalı, en uzun kenar 3840'ı aşmamalı, en-boy oranı 3:1'i aşmamalı ve toplam piksel sayısı 655.360 ile 8.294.400 arasında olmalıdır.
- `model.mask`, `model.images` içinde tam olarak bir referans görsel gerektirir: görsel olmadan kullanılamaz ve birden fazla görselle kullanılamaz.
- `model.mask` kullanıldığında, boyutları referans görselin boyutlarıyla eşleşmelidir.
- `model.images` sağlandığında, düğüm görsel düzenleme modunda çalışır; `model.images` olmadan, görselleri yalnızca prompt'tan üretir.
- Referans görseller API'ye gönderilmeden önce küçültülür.
- `seed` şu anda arka uçta uygulanmamıştır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Üretilen görsel veya görseller. Döndürülen tüm görseller tek bir batch halinde istiflenir; boyutları farklıysa, ilk görsele uyacak şekilde yeniden boyutlandırılır. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `fb3491f949151fbd3f5825ec9f9ae124019767d083f56966ef34af278aef50c0`
