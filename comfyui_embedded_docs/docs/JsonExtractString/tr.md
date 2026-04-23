> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JsonExtractString/tr.md)

JsonExtractString düğümü, JSON verisi içeren bir metin dizesini okur ve belirli bir anahtarla ilişkili değeri çıkarır. Çıkarılan değeri bir dizeye dönüştürür. JSON geçersizse, anahtar bulunamazsa veya değer null ise, düğüm boş bir dize döndürür.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `json_string` | STRING | Evet | Yok | Ayrıştırılacak JSON verisini içeren metin. |
| `key` | STRING | Evet | Yok | JSON nesnesinden dize değerini çıkarmak istediğiniz belirli anahtar. |

**Not:** Düğüm yalnızca JSON nesnelerinden (sözlükler) değer çıkarır. Ayrıştırılan JSON bir nesne değilse veya belirtilen anahtar bu nesne içinde mevcut değilse, çıktı boş bir dize olacaktır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | STRING | Belirtilen anahtar için JSON'dan çıkarılan dize değeri veya çıkarma başarısız olursa boş dize. |