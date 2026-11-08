# OpenAI GPT Image 2.6

## Genel Bakış

OpenAI GPT Image 2.6, OpenAI'nin GPT Image modellerini kullanarak bir istemden görüntüler oluşturur ve referans görüntüleri bağladığınızda bunları düzenler. Düğüm dört model sunar: `gpt-image-2.6-flare`, `gpt-image-2.6-sunburst`, `gpt-image-2.5-flare` ve `gpt-image-2.5-sunburst`. İlk referans görüntüsünün üzerine açıklamalar çizin ve modele tam olarak nerede düzenleme yapılacağını göstermek için bunları bir işaretleme çifti olarak bağlayın.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak GPT Image modeli. Bir model seçildiğinde o modelin parametreleri görünür. | DYNAMIC_COMBO | Evet | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"`<br>`"gpt-image-2.5-flare"`<br>`"gpt-image-2.5-sunburst"` |

### gpt-image-2.6-flare ve gpt-image-2.6-sunburst Girdileri

Bu girdiler `model` değeri `gpt-image-2.6-flare` veya `gpt-image-2.6-sunburst` olarak ayarlandığında görünür. Her iki model de aynı parametreleri paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model.prompt` | Ne oluşturulacağı veya yapılacak düzenleme. (varsayılan: `""`) | STRING | Evet | N/A |
| `model.size` | Görüntü boyutu. Özel genişlik ve yüksekliği kullanmak için "Custom" seçeneğini seçin. (varsayılan: `"auto"`) | COMBO | Evet | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Yalnızca `model.size` "Custom" olduğunda kullanılır. 16'nın katı olmalıdır. (varsayılan: `1024`) | INT | Hayır | 480 ile 3840 arası (adım 16) |
| `model.custom_height` | Yalnızca `model.size` "Custom" olduğunda kullanılır. 16'nın katı olmalıdır. (varsayılan: `1024`) | INT | Hayır | 480 ile 3840 arası (adım 16) |
| `model.background` | Görüntüyü arka planlı veya arka plansız döndürür. (varsayılan: `"auto"`) | COMBO | Evet | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Görüntü kalitesi. Daha yüksek seviyeler daha maliyetlidir ve daha uzun sürer. (varsayılan: `"low"`) | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.complexity` | Modelin görüntüyü oluşturmadan önce ne kadar planladığı. (varsayılan: `"high"`) | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Düzenleme için isteğe bağlı referans görüntüleri. En fazla 16. | AUTOGROW | Hayır | 0 ile 16 arası |
| `model.markup` | İlk referans görüntüsü üzerine çizilen ve nerede düzenleme yapılacağını gösteren açıklamalar. O görüntünün boyutuyla eşleşmeli ve `model.markup_alpha` ile birlikte bağlanmalıdır. | IMAGE | Hayır | N/A |
| `model.markup_alpha` | Beyaz, `model.markup` içindeki açıklamaları işaretler. Painter düğümünün MASK çıktısı doğrudan uygundur; bir Load Image maskesi için önce Invert Mask gerekir. | MASK | Hayır | N/A |
| `model.seed` | Düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: `42`) | INT | Evet | 0 ile 2147483647 arası |

### gpt-image-2.5-flare ve gpt-image-2.5-sunburst Girdileri

Bu girdiler `model` değeri `gpt-image-2.5-flare` veya `gpt-image-2.5-sunburst` olarak ayarlandığında görünür. `model.complexity` sunulmadığı dışında 2.6 modelleriyle aynıdır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model.prompt` | Ne oluşturulacağı veya yapılacak düzenleme. (varsayılan: `""`) | STRING | Evet | N/A |
| `model.size` | Görüntü boyutu. Özel genişlik ve yüksekliği kullanmak için "Custom" seçeneğini seçin. (varsayılan: `"auto"`) | COMBO | Evet | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Yalnızca `model.size` "Custom" olduğunda kullanılır. 16'nın katı olmalıdır. (varsayılan: `1024`) | INT | Hayır | 480 ile 3840 arası (adım 16) |
| `model.custom_height` | Yalnızca `model.size` "Custom" olduğunda kullanılır. 16'nın katı olmalıdır. (varsayılan: `1024`) | INT | Hayır | 480 ile 3840 arası (adım 16) |
| `model.background` | Görüntüyü arka planlı veya arka plansız döndürür. (varsayılan: `"auto"`) | COMBO | Evet | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Görüntü kalitesi. Daha yüksek seviyeler daha maliyetlidir ve daha uzun sürer. (varsayılan: `"low"`) | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.images` | Düzenleme için isteğe bağlı referans görüntüleri. En fazla 16. | AUTOGROW | Hayır | 0 ile 16 arası |
| `model.markup` | İlk referans görüntüsü üzerine çizilen ve nerede düzenleme yapılacağını gösteren açıklamalar. O görüntünün boyutuyla eşleşmeli ve `model.markup_alpha` ile birlikte bağlanmalıdır. | IMAGE | Hayır | N/A |
| `model.markup_alpha` | Beyaz, `model.markup` içindeki açıklamaları işaretler. Painter düğümünün MASK çıktısı doğrudan uygundur; bir Load Image maskesi için önce Invert Mask gerekir. | MASK | Hayır | N/A |
| `model.seed` | Düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: `42`) | INT | Evet | 0 ile 2147483647 arası |

**Parametre Kısıtlamaları ve Sınırlamaları:**

- `model.size` "Custom" olarak ayarlandığında, `model.custom_width` ve `model.custom_height` değerlerinin ikisi de 16'nın katı olmalıdır; en uzun kenar 3840'ı aşmamalıdır, en-boy oranı 3:1'i aşmamalıdır ve toplam piksel sayısı 655.360 ile 8.294.400 arasında olmalıdır.
- `model.markup` ve `model.markup_alpha` birlikte bağlanmalıdır. İşaretleme en az bir referans görüntüsü gerektirir ve genişliği ile yüksekliği ilk referans görüntüsüyle eşleşmelidir.
- `model.images` olmadan düğüm, yalnızca istemden görüntüler oluşturur; referans görüntülerle ise bunları düzenler ve birleştirir.
- Referans görüntüleri API'ye gönderilmeden önce küçültülür.
- `model.complexity` yalnızca `gpt-image-2.6-flare` ve `gpt-image-2.6-sunburst` modellerinde bulunur; 2.5 modelleri sabit bir planlama derinliği kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Oluşturulan görüntü veya görüntüler. Döndürülen tüm görüntüler tek bir toplu işte istiflenir; boyutları farklıysa ilk görüntüyle eşleşecek şekilde yeniden boyutlandırılır. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV3/tr.md)

---
**Source fingerprint (SHA-256):** `33f5d91af56c215cc7f7c704f9b123fe1c35bf287012072b818b76b551c04667`
