JsonExtractString düğümü, JSON verisi içeren bir metin dizesini okur ve belirli bir anahtarla ilişkili değeri çıkarır. Çıkarılan değeri bir dizeye dönüştürür. JSON geçersizse, anahtar bulunamazsa veya değer null ise, düğüm boş bir dize döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `json_string` | Ayrıştırılacak JSON verisini içeren metin. | STRING | Evet | Yok |
| `key` | JSON nesnesinden dize değerini çıkarmak istediğiniz belirli anahtar. | STRING | Evet | Yok |

**Not:** Düğüm yalnızca JSON nesnelerinden (sözlükler) değer çıkarır. Ayrıştırılan JSON bir nesne değilse veya belirtilen anahtar bu nesne içinde mevcut değilse, çıktı boş bir dize olacaktır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | JSON'dan belirtilen anahtar için çıkarılan dize değeri veya çıkarma başarısız olursa boş bir dize. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JsonExtractString/tr.md)

---
**Source fingerprint (SHA-256):** `f05e2d9fd4888870a844c85ac7543d6c38c1c56f2ef22a402fc93ee716743612`
