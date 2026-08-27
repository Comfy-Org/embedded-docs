# Sayı Dönüştürme

Number Convert düğümü, çeşitli girdi veri türlerini sayısal değerlere dönüştürür. Tek bir girdi olarak tamsayı, ondalıklı sayı, metin veya mantıksal (boolean) değer kabul eder ve iki çıktı üretir: bir ondalıklı sayı ve bir tamsayı. Bu, metin veya mantıksal değerleri, iş akışınızdaki diğer matematiksel veya işleme düğümleri tarafından kullanılabilecek bir biçime dönüştürmek için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `değer` | Sayısal çıktılara dönüştürülecek değer. Bir tamsayı, ondalıklı sayı, metin dizesi veya doğru/yanlış (true/false) mantıksal değer kabul eder. | INT, FLOAT, STRING, BOOLEAN | Evet | N/A |

**Not:** Girdi bir metin olduğunda, boş olmamalı ve geçerli bir sayı temsili içermelidir (örn. `"123"`, `"3.14"`). Düğüm; boş metinler, sayı olarak ayrıştırılamayan metinler veya sonlu olmayan değerler (örn. `"inf"` veya `"nan"`) için hata verecektir. Mantıksal girdilerde `true`, 1.0 (FLOAT) ve 1 (INT) değerine dönüşürken, `false`, 0.0 (FLOAT) ve 0 (INT) değerine dönüşür. Ondalıklı sayı girdileri ve ondalık sayı içeren metinler için tamsayı çıktısı, ondalık kısmın atılmasıyla elde edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `FLOAT` | Ondalıklı sayıya dönüştürülmüş girdi değeri. | FLOAT |
| `INT` | Tamsayıya dönüştürülmüş girdi değeri. Ondalıklı sayı girdilerinde bu, kesme işlemi gerçekleştirir. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNumberConvert/tr.md)

---
**Source fingerprint (SHA-256):** `d6a774bf7c3ad9482b2275adc6ccc9e47c82b1f35f11c5a241b00efd29526f94`
