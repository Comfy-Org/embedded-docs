# TypeSafe Jev (Choice)

TypeSafe Jev (Choice) düğümü, bağlanan metin, görüntü veya her ikisi için kendi seçeneklerinizden birini seçer. `choice` çıktısını, girdileri seçenek adlarını taşıyan bir Branch düğümüne bağlayın veya seçilen seçeneğin konumuna göre geçiş yapmak için `option_index` kullanın. Bu bir API düğümüdür ve Comfy.org hesabı ile API anahtarı gerektirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak Jev modeli. Şu anda yalnızca bir model mevcuttur: `jev-1.14.0`. | COMBO | Evet | `"jev-1.14.0"` |
| `question` | Seçeneklerin yanıtladığı soru. Birden fazla görüntü yuvası olduğunda, adlarını kullanın; örneğin `Which season is shown in image_1?` (varsayılan: `What style is the image?`). | STRING | Evet | 1 ile 1000 karakter arası |
| `options` | Aralarından seçim yapılacak seçenekler, her satırda bir tane. Bunlardan hiçbirine uymayan girdiler için `other` gibi bir seçenek ekleyin (varsayılan: `photo`, `illustration`, `3d render`, `anime`, `sketch` ve `other`, her satırda bir tane). | STRING | Evet | 2 ile 50 seçenek arası, her biri en fazla 40 karakter |
| `images` | Sorunun hakkında olduğu görüntüler. Toplamda en fazla 32 görüntü; toplu bir girdi her görüntü için bir kez sayılır ve 4'ten fazla görüntü daha küçük bir boyutta gönderilir. | AUTOGROW | Hayır | 0 ile 32 görüntü arası |
| `text` | Sorunun hakkında olduğu metin; istem veya LLM yanıtı gibi. | STRING | Hayır | 0 ile 3000 karakter arası |

**Notlar:**

- Metni veya en az bir görüntüyü bağlayın; her ikisi de boş olduğunda düğüm hata verir.
- 2'den az veya 50'den fazla seçenek verildiğinde, bir seçenek 40 karakterden uzun olduğunda veya iki seçenek yalnızca harf büyüklüğü/küçüklüğü bakımından farklı olduğunda düğüm hata verir.
- `option_index` 0'dan başlar; bu nedenle listedeki ilk seçeneğin indeksi 0'dır.
- Faturalandırma jeton tabanlıdır; düğümdeki fiyat rozeti 1 milyon jeton başına yaklaşık ücreti gösterir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `choice` | Seçilen seçenek, `options` içinde göründüğü şekilde tam olarak yazılır. | STRING |
| `option_index` | Seçilen seçeneğin seçenekler listesindeki konumu, 0'dan başlar. | INT |
| `confidence` | Jev'in ne kadar emin olduğu, 0 (net bir kazanan yok) ile 1 (kesin) arasında. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevChoice/tr.md)

---
**Source fingerprint (SHA-256):** `b1cd36d600f5c07935c455d9e926e6c0a53f172fcc1a6f602c8d4dc70eeffabe`
