# Kling 4.0 Long Image

Kling 4.0 ile tek bir uzun görüntü oluşturun: tam bir web sayfası tasarımı veya bir e-ticaret ürün detay sayfası. İstediğiniz düzene uyan `skill` değerini seçin; düğüm, o düzenin girdilerini gösterir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `beceri` | Oluşturulacak düzen. `"webpage"` isteğe bağlı bir stil görüntüsü ve konu etrafında tam bir sayfa tasarlar; `"ecommerce"` ürün fotoğraflarından bir ürün detay sayfası oluşturur. | DYNAMIC_COMBO | Evet | `"webpage"`<br>`"ecommerce"` |

### `webpage` Girdileri

Bu girdiler `skill` değeri `"webpage"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `style_image` | Görsel stil ve düzen için isteğe bağlı referans. Buna `@Image1` olarak başvurun. | IMAGE | Hayır | Tek görüntü |
| `subject_image` | Sayfayı etrafında tasarlamak ve korumak için isteğe bağlı konu. Buna `@Image2` olarak başvurun. | IMAGE | Hayır | Tek görüntü |
| `prompt` | Sayfanın isteğe bağlı açıklaması. Stil görüntüsüne `@Image1` ve konu görüntüsüne `@Image2` olarak başvurun ve sayfa metninin dilini belirtin, örneğin "Görünen tüm metin yalnızca İngilizce olmalıdır." Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin |
| `resolution` | Çıktı görüntüsünün çözünürlüğü. Varsayılan: `"1K"`. | COMBO | Evet | `"1K"`<br>`"2K"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak belirleyici değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

### `ecommerce` Girdileri

Bu girdiler `skill` değeri `"ecommerce"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `product_images` | Ürün fotoğrafları için büyütülebilir yuvalar (`image_1` ... `image_3`). İstemde bunlara `@Image1`, `@Image2`, `@Image3` olarak başvurun. | AUTOGROW | Evet | 1 ile 3 görsel arası |
| `prompt` | Sayfanın isteğe bağlı açıklaması. Ürün görüntülerine `@Image1`, `@Image2`, `@Image3` olarak başvurun. Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin |
| `length` | Oluşturulan sayfanın uzunluğu. Varsayılan: `"medium"`. | COMBO | Evet | `"short"`<br>`"medium"`<br>`"long"` |
| `resolution` | Çıktı görüntüsünün çözünürlüğü. Varsayılan: `"1K"`. | COMBO | Evet | `"1K"`<br>`"2K"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak belirleyici değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

**Kısıtlamalar ve davranış:**

* `ecommerce` modunda en fazla 3 ürün görüntüsü bağlanabilir.
* Her görüntü en az 300x300 piksel olmalı ve en-boy oranı 2:5 ile 5:2 arasında olmalıdır.
* `webpage` modunda, `@Image1` veya `@Image2` içeren bir istem, ilgili görüntü bağlı değilse hata verir.
* Bir çağrının fiyatı; beceriye, çözünürlüğe ve `ecommerce` için sayfa uzunluğuna bağlıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Görev tamamlandığında Kling'den indirilen oluşturulmuş uzun görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4LongImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `f1e687bcc8334229c60b318118120b85ddd580d1b62f343164f9803b98a1f987`
