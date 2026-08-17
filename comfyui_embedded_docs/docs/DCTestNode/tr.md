# DCTestNode

DCTestNode, kullanıcının dinamik bir açılır kutudan seçimine göre farklı türde veriler döndüren bir mantık düğümüdür. Seçilen seçeneğin hangi girdi alanının aktif olduğunu ve düğümün ne tür bir değer çıktı olarak vereceğini belirlediği koşullu bir yönlendirici gibi çalışır.

## Girdiler

`combo` seçici her zaman görünürdür. Altında gösterilen girdi alanları, seçilen seçeneğe bağlıdır.

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `combo` | Hangi girdi alanının aktif olduğunu ve düğümün ne çıktı vereceğini belirleyen ana seçim. | DYNAMIC_COMBO | Evet | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` |

### option1 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `string` | Bir metin girdi alanı. Bu alan yalnızca `combo` `"option1"` olarak ayarlandığında aktif ve zorunludur. | STRING | Evet | - |

### option2 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `integer` | Bir tam sayı girdi alanı. Bu alan yalnızca `combo` `"option2"` olarak ayarlandığında aktif ve zorunludur. | INT | Evet | - |

### option3 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Bir görsel girdi alanı. Bu alan yalnızca `combo` `"option3"` olarak ayarlandığında aktif ve zorunludur. | IMAGE | Evet | - |

### option4 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `subcombo` | `combo` `"option4"` olarak ayarlandığında görünen ikincil bir seçim. Hangi iç içe girdi alanlarının aktif olduğunu belirler. | DYNAMIC_COMBO | Evet | `"opt1"`<br>`"opt2"` |

#### opt1 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `float_x` | Bir ondalık sayı girdi alanı. Bu alan yalnızca `combo` `"option4"` ve `subcombo` `"opt1"` olarak ayarlandığında aktif ve zorunludur. | FLOAT | Evet | - |
| `float_y` | Bir ondalık sayı girdi alanı. Bu alan yalnızca `combo` `"option4"` ve `subcombo` `"opt1"` olarak ayarlandığında aktif ve zorunludur. | FLOAT | Evet | - |

#### opt2 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `mask1` | Bir maske girdi alanı. Bu alan yalnızca `combo` `"option4"` ve `subcombo` `"opt2"` olarak ayarlandığında aktiftir. İsteğe bağlıdır. | MASK | Hayır | - |

**Parametre Kısıtlamaları:**

* `combo` parametresi, diğer tüm girdi alanlarının görünürlüğünü ve zorunluluğunu kontrol eder. Yalnızca seçili `combo` seçeneğiyle ilişkili girdiler gösterilir ve zorunludur (`mask1` hariç; bu alan isteğe bağlıdır).
* `combo` `"option4"` olarak ayarlandığında, `subcombo` parametresi aktif ve zorunlu hale gelir ve ikinci bir iç içe girdi kümesini kontrol eder: `"opt1"` `float_x` ve `float_y` alanlarını gösterir; `"opt2"` `mask1` alanını gösterir.
* `combo` beklenmeyen bir değere ayarlanırsa, düğüm bir ValueError hatası verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Çıktı, seçilen `combo` seçeneğine bağlıdır. Bir STRING (`"option1"`), bir INT (`"option2"`), bir IMAGE (`"option3"`) veya `subcombo` sözlüğünün bir dize temsili (`"option4"`) olabilir. | ANYTYPE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/tr.md)

---
**Source fingerprint (SHA-256):** `9dd616a427a56eddb78b48d6eea6f71419b7097d417afae5557132b333641e69`
