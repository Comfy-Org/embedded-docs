# DCTestNode

DCTestNode, kullanıcının dinamik bir birleşik giriş kutusundan yaptığı seçime göre farklı türde veriler döndüren bir mantık düğümüdür. Seçilen seçenek, hangi girdi alanının etkin olacağını ve düğümün hangi türde değer çıktı olarak vereceğini belirleyen koşullu bir yönlendirici gibi çalışır.

## Girdiler

Düğüm, dinamik bir birleşik giriş seçici kullanır: `combo` parametresi her zaman görünür ve diğer girdi alanları yalnızca ilgili seçenek seçildiğinde görünür.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `combo` | Hangi girdi alanının etkin olacağını ve düğümün ne çıktı vereceğini belirleyen ana seçim. | DYNAMIC_COMBO | Evet | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` |

### option1 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `string` | Metin girdi alanı. Bu alan yalnızca `combo` `"option1"` olarak ayarlandığında etkindir ve zorunludur. | STRING | Evet | - |

### option2 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `integer` | Tam sayı girdi alanı. Bu alan yalnızca `combo` `"option2"` olarak ayarlandığında etkindir ve zorunludur. | INT | Evet | - |

### option3 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Görüntü girdi alanı. Bu alan yalnızca `combo` `"option3"` olarak ayarlandığında etkindir ve zorunludur. | IMAGE | Evet | - |

### option4 Girdileri

`combo` `"option4"` olarak ayarlandığında düğüm, iç içe bir dizi girdi alanını kontrol eden ikinci bir dinamik birleşik giriş seçici (`subcombo`) gösterir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `subcombo` | `combo` `"option4"` olarak ayarlandığında görünen ikincil dinamik birleşik giriş seçimidir. Hangi iç içe girdi alanlarının etkin olacağını belirler. | DYNAMIC_COMBO | Evet | `"opt1"`<br>`"opt2"` |
| `float_x` | Ondalık sayı girdisi. Bu alan yalnızca `combo` `"option4"` ve `subcombo` `"opt1"` olarak ayarlandığında etkindir ve zorunludur. | FLOAT | Evet | - |
| `float_y` | Ondalık sayı girdisi. Bu alan yalnızca `combo` `"option4"` ve `subcombo` `"opt1"` olarak ayarlandığında etkindir ve zorunludur. | FLOAT | Evet | - |
| `mask1` | Maske girdi alanı. Bu alan yalnızca `combo` `"option4"` ve `subcombo` `"opt2"` olarak ayarlandığında etkindir. İsteğe bağlıdır. | MASK | Hayır | - |

**Parametre Kısıtlamaları:**

* `combo` parametresi, diğer tüm girdi alanlarının görünürlüğünü ve gerekliliğini kontrol eder. Yalnızca seçili `combo` seçeneğiyle ilişkili girdiler gösterilir ve zorunludur (`mask1` isteğe bağlıdır).
* `combo` `"option4"` olarak ayarlandığında `subcombo` parametresi zorunlu hale gelir ve ikinci bir iç içe girdi kümesini (`float_x`/`float_y` veya `mask1`) kontrol eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Çıktı, seçili `combo` seçeneğine bağlıdır. Bir STRING (`"option1"`), bir INT (`"option2"`), bir IMAGE (`"option3"`) veya `subcombo` sözlüğünün bir dize gösterimi (`"option4"`) olabilir. | ANYTYPE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/tr.md)

---
**Source fingerprint (SHA-256):** `9dd616a427a56eddb78b48d6eea6f71419b7097d417afae5557132b333641e69`
