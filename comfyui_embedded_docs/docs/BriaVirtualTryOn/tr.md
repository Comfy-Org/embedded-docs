# Bria Virtual Try-On

Bu düğüm, Bria ile bir kişiyi giysiler veya aksesuarlarla giydirir. Kişinin kimliği, duruşu ve arka planı korunurken sahne yaklaşık 1 megapikselde yeniden oluşturulur, bu nedenle sonuç giriş fotoğrafıyla piksel hizalı değildir. Her giysi görüntüsü, kişinin halihazırda giydiği eşleşen öğenin yerini alır.

## Girdiler

`moderation` seçicisi `"true"` olarak ayarlandığında ek bir moderasyon seçeneği ortaya çıkarır.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `person_image` | Giysileri deneyen kişinin fotoğrafı. Görüntü yüklenmeden önce alfa kanalı kaldırılır. | IMAGE | Evet | - |
| `garment_images` | Birlikte giyilen 1 ila 3 giysi veya aksesuar; her biri kişinin giydiği eşleşen öğenin yerini alır. Toplu girdi, görüntü başına bir kez sayılır ve saydam alanlar beyaz olarak işlenir. | AUTOGROW | Evet | 1 ile 3 arası görüntü |
| `instruction` | Bria'nın yerleşik talimatına eklenen isteğe bağlı ek yönlendirme, örneğin hangi giysinin üstüne katmanlanacağı. Varsayılan: `""` (boş dize). | STRING | Evet | - |
| `aspect_ratio` | `"auto"` kişi fotoğrafının çerçevelemesini yaklaşık 1 megapikselde tutar. Sabit bir oran 0,6 ila 1 megapiksel döndürür, örneğin `"3:4"` için 768x1024. Varsayılan: `"auto"`. | COMBO | Evet | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"` |
| `seed` | İstekle birlikte Bria'ya gönderilen tohum. Varsayılan: 42. | INT | Evet | 1 ile 2147483647 arası |
| `moderation` | Moderasyon ayarları. `"true"` olarak ayarlandığında, aşağıdaki moderasyon işareti kullanılabilir hale gelir. | DYNAMIC_COMBO | Evet | `"false"`<br>`"true"` |

### Moderation "true" Girdileri

Bu parametre yalnızca `moderation` `"true"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `visual_output_moderation` | Oluşturulan görüntüde içerik moderasyonunu etkinleştirir. Varsayılan: `False`. | BOOLEAN | Hayır | True / False |

**Kısıtlamalar:**

* `garment_images` en fazla 3 görüntü kabul eder, girdi toplu olduğunda görüntü başına sayılır.
* Giysi görüntülerindeki saydam pikseller yüklemeden önce beyaz üzerine birleştirilir.
* `person_image` görüntüsünün alfa kanalı yüklemeden önce kaldırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Kişinin sağlanan giysileri giydiği düzenlenmiş fotoğraf. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVirtualTryOn/tr.md)

---
**Source fingerprint (SHA-256):** `32f89c8685d8624bdef2c17ba5ba916b030d1dc88718b83c79aadb9a5fa378de`
