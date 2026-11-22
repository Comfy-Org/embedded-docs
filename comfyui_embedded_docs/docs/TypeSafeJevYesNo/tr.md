# TypeSafe Jev (Yes/No)

TypeSafe Jev (Evet/Hayır) düğümü, bağlanan metin, görseller veya her ikisi hakkında bir evet veya hayır sorusu sorar ve yanıtı boolean olarak döndürür. İş akışını yönlendirmek için `result` çıktısını bir If/Else Switch düğümüne bağlayın veya modelin ne kadar emin olduğuna göre işlem yapmak için `probability` değerini okuyun. Bu bir API düğümüdür: Comfy'nin sunucularında çalışır ve krediye sahip bir Comfy.org hesabı gerektirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak Jev modeli. Şu anda yalnızca bir model mevcuttur: `jev-1.14.0`. | COMBO | Evet | `"jev-1.14.0"` |
| `question` | Bağlanan metin ve görsellerin yanıtlayacağı evet veya hayır sorusu. Soruyu, üzerinde işlem yapacağınız durum evet olacak şekilde sorun; birden fazla görsel yuvası varsa adlarını kullanın, örneğin `Does image_2 show the same person as image_1?` (varsayılan: `Is there a person in the image?`). | STRING | Evet | 1 ile 1000 karakter arası |
| `threshold` | Evet olasılığı en az bu değer olduğunda yanıt evet olur (varsayılan: 0.5). | FLOAT | Evet | 0.01 ile 0.99 arası (adım: 0.01) |
| `images` | Sorunun hakkında olduğu görseller. Toplamda 32 görsele kadar; toplu bir girdi her görsel için bir kez sayılır. Her görselin uzun kenarı toplam görsel sayısına göre sınırlandırılır: 4 görsele kadar 1568 px, 8'e kadar 1024 px, 16'ya kadar 768 px ve 32'ye kadar 512 px; bu nedenle daha büyük bir toplu işlem her görselde daha az ayrıntı anlamına gelir. | AUTOGROW | Hayır | 0 ile 32 görsel arası |
| `text` | Sorunun hakkında olduğu metin; örneğin bir istem veya bir LLM yanıtı. | STRING | Hayır | 0 ile 3000 karakter arası |

**Notlar:**

- Metin veya en az bir görsel bağlayın; her ikisi de boş olduğunda düğüm hata verir.
- `result`, `probability` en az `threshold` olduğunda true olur ve `answer` aynı sonucu `yes` veya `no` olarak döndürür.
- Faturalandırma token tabanlıdır; düğümdeki fiyat rozeti 1M token başına yaklaşık ücreti gösterir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `result` | Yanıtın boolean olarak değeri: evet olasılığı en az `threshold` olduğunda true. | BOOLEAN |
| `answer` | Yanıt, metin olarak `yes` veya `no`. | STRING |
| `probability` | Evet olasılığı; 0 (kesinlikle hayır) ile 1 (kesinlikle evet) arasında. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevYesNo/tr.md)

---
**Source fingerprint (SHA-256):** `e8c7de5558c61e7c9058b28104a72d8d8961165983d02d63a5c9078c40855385`
