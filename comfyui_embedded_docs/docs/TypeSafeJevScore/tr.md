# TypeSafe Jev (Score)

The TypeSafe Jev (Score) düğümü, bağlanan metni, görselleri veya her ikisini birden 1 ile 10 arasında derecelendirir ve derecelendirmeyi bir eşik değeriyle karşılaştırır. Puan üzerinde işlem yapmak için `result` çıktısını bir If/Else Switch düğümüne bağlayın veya ham derecelendirmeyi kullanmak için `score` çıktısını okuyun. Bu bir API düğümüdür: Comfy'nin sunucularında çalışır ve kredili bir Comfy.org hesabı gerektirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak Jev modeli. Şu anda yalnızca bir model mevcuttur: `jev-1.14.0`. | COMBO | Evet | `"jev-1.14.0"` |
| `question` | 1 ile 10 arasında bir ölçekte neyin derecelendirileceği. Varsayılanda olduğu gibi 1 ve 10'un ne anlama geldiğini belirtin (varsayılan: `Rate the technical quality of the image from 1 (worst) to 10 (best).`). | STRING | Evet | 1 ile 1000 karakter arası |
| `threshold` | Puan en az bu değer olduğunda `result` true olur (varsayılan: 5.0). | FLOAT | Evet | 1.0 ile 10.0 arası (adım: 0.1) |
| `images` | Sorunun hakkında olduğu görseller. Toplamda en fazla 32 görsel; toplu girdi her görsel için bir kez sayılır. Her görselin uzun kenarı, toplam görsel sayısına göre sınırlandırılır: 4 görsele kadar 1568 px, 8 görsele kadar 1024 px, 16 görsele kadar 768 px ve 32 görsele kadar 512 px, böylece daha büyük bir toplu işlem her görseldeki ayrıntıyı azaltabilir. | AUTOGROW | Hayır | 0 ile 32 görsel arası |
| `text` | Sorunun hakkında olduğu metin, örneğin bir istem veya bir LLM yanıtı. | STRING | Hayır | 0 ile 3000 karakter arası |

**Notlar:**

- Metin veya en az bir görsel bağlayın; her ikisi de boş olduğunda düğüm bir hata verir.
- Puan 1 ile 10 arasında raporlanır ve en az `threshold` olduğunda `result` true olur.
- Faturalandırma token tabanlıdır; düğümdeki fiyat rozeti, 1M token başına yaklaşık ücreti gösterir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `result` | `score` en az `threshold` olduğunda true. | BOOLEAN |
| `score` | 1 (en kötü) ile 10 (en iyi) arasındaki puan. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevScore/tr.md)

---
**Source fingerprint (SHA-256):** `7e1970e903d2099ab3d7481a758c5291e87614b9eaf116d0ced6a1bcd36dc126`
