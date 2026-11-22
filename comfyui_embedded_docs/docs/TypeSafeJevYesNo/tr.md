# TypeSafe Jev (Yes/No)

TypeSafe Jev (Yes/No) düğümü, bağlanan metin, görseller veya her ikisi hakkında evet/hayır sorusu sorar ve yanıtı boolean olarak döndürür. İş akışını yönlendirmek için `result` çıktısını bir If/Else Switch düğümüne bağlayın veya modelin ne kadar emin olduğuna göre işlem yapmak için `probability` değerini okuyun. Bu bir API düğümüdür ve Comfy.org hesabı ile API anahtarı gerektirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak Jev modeli. Şu anda yalnızca bir model mevcut: `jev-1.14.0`. | COMBO | Evet | `"jev-1.14.0"` |
| `question` | Bağlanan metnin ve görsellerin yanıtlayacağı evet/hayır sorusu. Soruyu, evet yanıtının üzerine işlem yapacağınız durum olacak şekilde sorun; birden fazla görsel yuvası olduğunda adlarını kullanın, örneğin `image_2, image_1 ile aynı kişiyi mi gösteriyor?` (varsayılan: `Is there a person in the image?`). | STRING | Evet | 1 ile 1000 karakter arası |
| `threshold` | Evet olasılığı en az bu değer olduğunda yanıt evet olur (varsayılan: 0.5). | FLOAT | Evet | 0.01 ile 0.99 arası (adım: 0.01) |
| `images` | Sorunun hakkında olduğu görseller. Toplamda en fazla 32 görsel; toplu bir girdi her görsel için bir kez sayılır ve 4'ten fazla görsel daha küçük boyutta gönderilir. | AUTOGROW | Hayır | 0 ile 32 görsel arası |
| `text` | Sorunun hakkında olduğu metin; bir istem veya bir LLM yanıtı gibi. | STRING | Hayır | 0 ile 3000 karakter arası |

**Notlar:**

- Metin veya en az bir görsel bağlayın; her ikisi de boş olduğunda düğüm hata verir.
- `probability` en az `threshold` olduğunda `result` true olur ve `answer` aynı hükmü `yes` veya `no` olarak döndürür.
- Faturalandırma token tabanlıdır; düğümdeki fiyat rozeti, 1M token başına yaklaşık ücreti gösterir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `result` | Yanıt bir boolean olarak: evet olasılığı en az `threshold` olduğunda true. | BOOLEAN |
| `answer` | Yanıt `yes` veya `no` metni olarak. | STRING |
| `probability` | Evet olasılığı, 0 (kesinlikle hayır) ile 1 (kesinlikle evet) arasında. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevYesNo/tr.md)

---
**Source fingerprint (SHA-256):** `e8c7de5558c61e7c9058b28104a72d8d8961165983d02d63a5c9078c40855385`
