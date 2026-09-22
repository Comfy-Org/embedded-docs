# JSON'dan Dize Çıkar

JsonExtractString düğümü, bir metin dizesini tarayarak ilk geçerli JSON nesnesini bulur ve belirli bir anahtarla ilişkili değeri dizeye dönüştürerek çıkarır. JSON nesnesinin öncesindeki veya sonrasındaki tüm metin yok sayılır; böylece düğüm Markdown kod bloklarında ve JSON'u ek metinle saran model yanıtlarında da çalışır. Geçerli bir JSON nesnesi bulunamazsa, anahtar bulunamazsa veya değer null ise düğüm boş bir dize döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `json_string` | JSON nesnesini aramak için kullanılacak metin. Bu alan çok satırlı girişi destekler ve çevresinde düz metin veya Markdown kod çitleri bulunabilir. | STRING | Evet | N/A |
| `key` | JSON nesnesinden değerini çıkarmak istediğiniz belirli anahtar. Bu alan yalnızca tek satırlı girişi destekler. | STRING | Evet | N/A |

**Not:** Düğüm, değerleri yalnızca JSON nesnelerinden (sözlüklerden) çıkarır. Girdideki her `{` işaretini sırayla dener ve geçerli bir JSON nesnesi üreten ilk konumdan itibaren çözümler; böylece baştaki veya sondaki metin atlanır. Hiçbir JSON nesnesi çözümlenemezse veya belirtilen anahtar bunun içinde yoksa çıktı boş bir dizedir. Anahtarla ilişkili değer `null` ise düğüm yine boş bir dize döndürür. Dize olmayan değerler, dize gösterimleri olarak döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Belirtilen anahtar için JSON'dan çıkarılan dize değeri veya çıkarma başarısız olursa boş bir dize. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JsonExtractString/tr.md)

---
**Source fingerprint (SHA-256):** `ca697fd3bd2d4de764372470ad1102b345d9d60f6df1c151fa0573e85fab2382`
