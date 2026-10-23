# Bria Product Holding

Bu düğüm, Bria ile bir ürünü bir kişinin ellerine yerleştirir. Kişinin kimliği, duruşu ve arka planı korunurken sahne yaklaşık 1 megapikselde yeniden oluşturulur, bu nedenle sonuç giriş fotoğrafıyla piksel hizalı değildir. Tüm ürün görselleri, bir ürünü farklı açılardan veya aşamalardan tanımlar.

## Girdiler

`moderation` seçicisi `"true"` olarak ayarlandığında ek bir moderasyon seçeneği gösterir.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `person_image` | Ürünü tutan kişinin fotoğrafı. Görsel yüklenmeden önce alfa kanalı kaldırılır. | IMAGE | Evet | - |
| `product_images` | Bir ürünün 1 ila 3 görseli: ürünün kendisi, ambalajı, başka bir açısı veya tamamlayıcı bir öğe. Toplu giriş, görsel başına bir kez sayılır ve saydam alanlar beyaz olarak işlenir. | AUTOGROW | Evet | 1 ila 3 görsel |
| `instruction` | Bria'nın yerleşik talimatına eklenen isteğe bağlı ek yönlendirme, örneğin hangi elin kullanılacağı veya etiketin hangi yöne bakacağı. Varsayılan: `""` (boş dize). | STRING | Evet | - |
| `aspect_ratio` | `"auto"` kişi fotoğrafının çerçevelenmesini yaklaşık 1 megapikselde tutar. Sabit bir oran 0,6 ila 1 megapiksel arasında döndürür, örneğin `"3:4"` için 768x1024. Varsayılan: `"auto"`. | COMBO | Evet | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"` |
| `seed` | Bria'ya istek ile gönderilen tohum. Varsayılan: 42. | INT | Evet | 1 ila 2147483647 |
| `moderation` | Moderasyon ayarları. `"true"` olarak ayarlandığında, aşağıdaki moderasyon işareti kullanılabilir hale gelir. | DYNAMIC_COMBO | Evet | `"false"`<br>`"true"` |

### Moderasyon `"true"` Girdileri

Bu parametre yalnızca `moderation` `"true"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `visual_output_moderation` | Oluşturulan görselde içerik moderasyonunu etkinleştirir. Varsayılan: `False`. | BOOLEAN | Hayır | True / False |

**Kısıtlamalar:**

* `product_images` en fazla 3 görsel kabul eder, giriş toplu olduğunda görsel başına sayılır.
* Ürün görsellerindeki saydam pikseller yüklenmeden önce beyaz üzerine birleştirilir.
* `person_image` öğesinin alfa kanalı yüklenmeden önce kaldırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Ürünün kişinin ellerine yerleştirildiği düzenlenmiş fotoğraf. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaProductHolding/tr.md)

---
**Source fingerprint (SHA-256):** `91a4a4dde0e9d7fe2480130da87edf1f8ed9d4ae0c86f8a8d030c36987dcdb8e`
