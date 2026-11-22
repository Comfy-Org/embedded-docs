# TypeSafe Jev (Score)

TypeSafe Jev (Score) düğümü, bağlanan metni, görselleri veya her ikisini 1 ile 10 arasında derecelendirir ve derecelendirmeyi bir eşik değeriyle karşılaştırır. Puan üzerinde işlem yapmak için `result` çıktısını bir If/Else Switch düğümüne bağlayın veya ham derecelendirmeyi kullanmak için `score` çıktısını okuyun. Bu bir API düğümüdür ve Comfy.org hesabı ile API anahtarı gerektirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak Jev modeli. Şu anda yalnızca bir model mevcut: `jev-1.14.0`. | COMBO | Evet | `"jev-1.14.0"` |
| `question` | 1 ile 10 arasında bir ölçekte neyin derecelendirileceği. Varsayılan değerdeki gibi 1 ve 10'un ne anlama geldiğini belirtin (varsayılan: `Rate the technical quality of the image from 1 (worst) to 10 (best).`). | STRING | Evet | 1 ile 1000 karakter arası |
| `threshold` | Puan en az bu değer olduğunda `result` true olur (varsayılan: 5.0). | FLOAT | Evet | 1.0 ile 10.0 arası (adım: 0.1) |
| `images` | Sorunun ilişkin olduğu görseller. Toplamda en fazla 32 görsel; toplu bir girdi her görsel için bir kez sayılır ve 4'ten fazla görsel daha küçük bir boyutta gönderilir. | AUTOGROW | Hayır | 0 ile 32 görsel arası |
| `text` | Sorunun ilişkin olduğu metin; bir istem veya LLM yanıtı gibi. | STRING | Hayır | 0 ile 3000 karakter arası |

**Notlar:**

- Metin veya en az bir görsel bağlayın; her ikisi de boş olduğunda düğüm hata verir.
- Puan 1 ile 10 arasında bildirilir ve en az `threshold` olduğunda `result` true olur.
- Faturalandırma token tabanlıdır; düğümdeki fiyat rozeti 1 milyon token başına yaklaşık ücreti gösterir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `result` | `score` en az `threshold` olduğunda true. | BOOLEAN |
| `score` | 1 (en kötü) ile 10 (en iyi) arasındaki derecelendirme. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevScore/tr.md)

---
**Source fingerprint (SHA-256):** `7e1970e903d2099ab3d7481a758c5291e87614b9eaf116d0ced6a1bcd36dc126`
