# DCTestNode

ComfyUI düğüm belgelerini İngilizceden Türkçeye çevirmede uzmanlaşmış teknik çeviri uzmanısınız.

## Çeviri Kuralları

1. **Çevrilmemesi gereken içerik:**
   - Ters tırnak içindeki parametre adları: `image`, `seed`, `model`
   - BÜYÜK harflerle veri türleri: IMAGE, STRING, INT, FLOAT, MODEL, CONDITIONING, vb.
   - Range sütunundaki değerler: sayılar, "auto", seçenek adları
   - Kod, dosya yolları

2. **Çevrilmesi gereken içerik:**
   - Bölüm başlıkları: ## Genel Bakış, ## Girdiler, ## Çıktılar
   - Tüm açıklayıcı metinler
   - Parametre açıklamaları

3. **Çeviri kalitesi:**
   - Standart Türkçe kullanın
   - Profesyonel ama anlaşılır bir üslup koruyun
   - Teknik doğruluğu sağlayın
   - Standart Türkçe teknik terminolojiyi kullanın

4. **Format:**
   - Tüm Markdown biçimlendirmesini koruyun
   - Tablo yapısını koruyun
   - Belgenin başına herhangi bir not veya bağlantı eklemeyin (otomatik olarak eklenecektir)

Lütfen aşağıdaki belgeyi Türkçeye çevirin (belgenin başlangıç notunu dahil etmeyin):

DCTestNode, kullanıcının dinamik bir birleşik giriş kutusundan yaptığı seçime göre farklı türlerde veri döndüren bir mantık düğümüdür. Seçilen seçeneğin hangi giriş alanının aktif olacağını ve düğümün hangi türde değer çıktısı vereceğini belirlediği koşullu bir yönlendirici görevi görür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `combo` | Hangi giriş alanının aktif olacağını ve düğümün ne çıktı vereceğini belirleyen ana seçim. | COMBO | Evet | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` |
| `string` | Bir metin giriş alanı. Bu alan yalnızca `combo` `"option1"` olarak ayarlandığında aktif ve zorunludur. | STRING | Hayır | - |
| `integer` | Bir tam sayı giriş alanı. Bu alan yalnızca `combo` `"option2"` olarak ayarlandığında aktif ve zorunludur. | INT | Hayır | - |
| `image` | Bir görsel giriş alanı. Bu alan yalnızca `combo` `"option3"` olarak ayarlandığında aktif ve zorunludur. | IMAGE | Hayır | - |
| `subcombo` | `combo` `"option4"` olarak ayarlandığında görünen ikincil bir seçim. Hangi iç içe giriş alanlarının aktif olacağını belirler. | COMBO | Hayır | `"opt1"`<br>`"opt2"` |
| `float_x` | Bir ondalık sayı girişi. Bu alan yalnızca `combo` `"option4"` ve `subcombo` `"opt1"` olarak ayarlandığında aktif ve zorunludur. | FLOAT | Hayır | - |
| `float_y` | Bir ondalık sayı girişi. Bu alan yalnızca `combo` `"option4"` ve `subcombo` `"opt1"` olarak ayarlandığında aktif ve zorunludur. | FLOAT | Hayır | - |
| `mask1` | Bir maske giriş alanı. Bu alan yalnızca `combo` `"option4"` ve `subcombo` `"opt2"` olarak ayarlandığında aktiftir. İsteğe bağlıdır. | MASK | Hayır | - |

**Parametre Kısıtlamaları:**

* `combo` parametresi, diğer tüm giriş alanlarının görünürlüğünü ve zorunluluğunu kontrol eder. Yalnızca seçili `combo` seçeneğiyle ilişkili girişler gösterilir ve zorunludur (`mask1` isteğe bağlı olduğu için hariç).
* `combo` `"option4"` olarak ayarlandığında, `subcombo` parametresi zorunlu hale gelir ve ikinci bir iç içe giriş kümesini (`float_x`/`float_y` veya `mask1`) kontrol eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Çıktı, seçilen `combo` seçeneğine bağlıdır. Bir STRING (`"option1"`), bir INT (`"option2"`), bir IMAGE (`"option3"`) veya `subcombo` sözlüğünün bir dize temsili (`"option4"`) olabilir. | ANYTYPE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/tr.md)

---
**Source fingerprint (SHA-256):** `98c4ca2100a27594df360935cc1507960480fe75a76ca0df2af75925d399be00`
