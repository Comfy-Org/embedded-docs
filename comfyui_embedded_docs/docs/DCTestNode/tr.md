> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/tr.md)

DCTestNode, kullanıcının dinamik bir birleşik giriş kutusundan yaptığı seçime bağlı olarak farklı veri türleri döndüren bir mantık düğümüdür. Seçilen seçeneğin hangi giriş alanının etkin olacağını ve düğümün ne tür bir değer çıktılayacağını belirlediği bir koşullu yönlendirici gibi çalışır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `combo` | COMBO | Evet | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` | Hangi giriş alanının etkin olacağını ve düğümün ne çıktılayacağını belirleyen ana seçim. |
| `string` | STRING | Hayır | - | Bir metin giriş alanı. Bu alan yalnızca `combo` `"option1"` olarak ayarlandığında etkin ve zorunludur. |
| `integer` | INT | Hayır | - | Bir tam sayı giriş alanı. Bu alan yalnızca `combo` `"option2"` olarak ayarlandığında etkin ve zorunludur. |
| `image` | IMAGE | Hayır | - | Bir görüntü giriş alanı. Bu alan yalnızca `combo` `"option3"` olarak ayarlandığında etkin ve zorunludur. |
| `subcombo` | COMBO | Hayır | `"opt1"`<br>`"opt2"` | `combo` `"option4"` olarak ayarlandığında görünen ikincil bir seçim. Hangi iç içe giriş alanlarının etkin olacağını belirler. |
| `float_x` | FLOAT | Hayır | - | Bir ondalık sayı girişi. Bu alan yalnızca `combo` `"option4"` ve `subcombo` `"opt1"` olarak ayarlandığında etkin ve zorunludur. |
| `float_y` | FLOAT | Hayır | - | Bir ondalık sayı girişi. Bu alan yalnızca `combo` `"option4"` ve `subcombo` `"opt1"` olarak ayarlandığında etkin ve zorunludur. |
| `mask1` | MASK | Hayır | - | Bir maske giriş alanı. Bu alan yalnızca `combo` `"option4"` ve `subcombo` `"opt2"` olarak ayarlandığında etkindir. İsteğe bağlıdır. |

**Parametre Kısıtlamaları:**

* `combo` parametresi, diğer tüm giriş alanlarının görünürlüğünü ve zorunluluğunu kontrol eder. Yalnızca seçilen `combo` seçeneğiyle ilişkili girişler gösterilecek ve zorunlu olacaktır (`mask1` hariç, bu isteğe bağlıdır).
* `combo` `"option4"` olarak ayarlandığında, `subcombo` parametresi zorunlu hale gelir ve ikinci bir iç içe giriş kümesini (`float_x`/`float_y` veya `mask1`) kontrol eder.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | ANYTYPE | Çıktı, seçilen `combo` seçeneğine bağlıdır. Bir STRING (`"option1"`), bir INT (`"option2"`), bir IMAGE (`"option3"`) veya `subcombo` sözlüğünün bir dize temsili (`"option4"`) olabilir. |
