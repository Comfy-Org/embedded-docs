# Sayı Dönüştürme

Number Convert düğümü, çeşitli girdi veri türlerini sayısal değerlere dönüştürür. Tamsayı, ondalık sayı, metin veya mantıksal değer türünde tek bir girdi kabul eder ve iki çıktı üretir: bir kayan noktalı sayı ve bir tamsayı. Bu, metin veya mantıksal değerleri, iş akışınızdaki diğer matematiksel veya işleme düğümleri tarafından kullanılabilecek bir biçime dönüştürmek için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `değer` | Sayısal çıktılara dönüştürülecek değer. Bir tamsayı, bir kayan noktalı sayı, bir metin dizesi veya doğru/yanlış mantıksal değer kabul eder. | INT, FLOAT, STRING, BOOLEAN | Evet | N/A |

**Not:** Girdi bir dize olduğunda boş olmamalı ve geçerli bir sayı gösterimi içermelidir (örn. `"123"`, `"3.14"`). Düğüm; boş dizeler, sayı olarak ayrıştırılamayan metinler veya sonlu olmayan değerler (örneğin `"inf"` veya `"nan"`) için hata verir. Mantıksal girdilerde `true`, 1.0 (FLOAT) ve 1 (INT) değerine dönüşür; `false` ise 0.0 (FLOAT) ve 0 (INT) değerine dönüşür. Ondalık sayı girdileri ve ondalık sayı içeren dizeler için tamsayı çıktısı, ondalık kısmın kesilmesiyle elde edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `FLOAT` | Kayan noktalı sayıya dönüştürülmüş girdi değeri. | FLOAT |
| `INT` | Tamsayıya dönüştürülmüş girdi değeri. Ondalık sayı girdileri ve ondalık dizeler için bu, bir kesme işlemi gerçekleştirir. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNumberConvert/tr.md)

---
**Source fingerprint (SHA-256):** `d6a774bf7c3ad9482b2275adc6ccc9e47c82b1f35f11c5a241b00efd29526f94`
