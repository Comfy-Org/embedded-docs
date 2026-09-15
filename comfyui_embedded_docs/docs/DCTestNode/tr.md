# DCTestNode

DCTestNode, kullanıcının dinamik bir açılır kutu seçimine göre farklı veri türleri döndüren bir mantık düğümüdür. Seçilen seçeneğin hangi giriş alanının etkin olduğunu ve düğümün hangi tür değeri çıkaracağını belirlediği koşullu bir yönlendirici olarak çalışır. Düğüm, ComfyUI'de bir çıktı düğümü olarak işaretlenmiştir.

## Girdiler

Düğüm dinamik bir combo seçici kullanır: `combo` parametresi her zaman görünürdür ve diğer giriş alanları yalnızca karşılık gelen seçenek seçildiğinde görünür.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `combo` | Hangi giriş alanının etkin olacağını ve düğümün ne çıkaracağını belirleyen ana seçim. | DYNAMIC_COMBO | Evet | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` |

### option1 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `string` | Bir metin giriş alanı. Bu alan yalnızca `combo` `"option1"` olarak ayarlandığında etkindir ve gereklidir. | STRING | Evet | - |

### option2 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `integer` | Bir tam sayı giriş alanı. Bu alan yalnızca `combo` `"option2"` olarak ayarlandığında etkindir ve gereklidir. | INT | Evet | - |

### option3 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Bir görüntü giriş alanı. Bu alan yalnızca `combo` `"option3"` olarak ayarlandığında etkindir ve gereklidir. | IMAGE | Evet | - |

### option4 Girdileri

`combo` `"option4"` olarak ayarlandığında, düğüm iç içe bir giriş alanları kümesini kontrol eden ikinci bir dinamik combo seçici (`subcombo`) gösterir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `subcombo` | `combo` `"option4"` olarak ayarlandığında görünen ikincil dinamik combo seçimi. Hangi iç içe giriş alanlarının etkin olacağını belirler. | DYNAMIC_COMBO | Evet | `"opt1"`<br>`"opt2"` |
| `float_x` | Bir ondalık sayı girişi. Bu alan yalnızca `combo` `"option4"` ve `subcombo` `"opt1"` olarak ayarlandığında etkindir ve gereklidir. | FLOAT | Evet | - |
| `float_y` | Bir ondalık sayı girişi. Bu alan yalnızca `combo` `"option4"` ve `subcombo` `"opt1"` olarak ayarlandığında etkindir ve gereklidir. | FLOAT | Evet | - |
| `mask1` | Bir maske giriş alanı. Bu alan yalnızca `combo` `"option4"` ve `subcombo` `"opt2"` olarak ayarlandığında etkindir. İsteğe bağlıdır. | MASK | Hayır | - |

**Parametre Kısıtlamaları:**

* `combo` parametresi diğer tüm giriş alanlarının görünürlüğünü ve gerekliliğini kontrol eder. Yalnızca seçilen `combo` seçeneğiyle ilişkili girişler gösterilir ve gereklidir (`mask1` isteğe bağlı olduğu için hariç).
* `combo` `"option4"` olarak ayarlandığında, `subcombo` parametresi gerekli hale gelir ve ikinci bir iç içe giriş kümesini (`float_x`/`float_y` veya `mask1`) kontrol eder.
* Eğer `combo` listelenen dört seçenekten biri olmayan bir değer alırsa, düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Çıktı, seçilen `combo` seçeneğine bağlıdır. Bir STRING (`"option1"`), bir INT (`"option2"`), bir IMAGE (`"option3"`) veya `subcombo` değerinin bir dize temsili (`"option4"`) olabilir. | ANYTYPE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/tr.md)

---
**Source fingerprint (SHA-256):** `9dd616a427a56eddb78b48d6eea6f71419b7097d417afae5557132b333641e69`
