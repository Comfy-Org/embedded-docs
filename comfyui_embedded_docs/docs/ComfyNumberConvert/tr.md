# Sayı Dönüştürme

Number Convert düğümü, çeşitli girdi veri türlerini sayısal değerlere dönüştürür. Tek bir girdi olarak tamsayı, kayan noktalı sayı, metin dizesi veya boolean değer kabul eder ve iki çıktı üretir: bir kayan noktalı sayı ve bir tamsayı. Bu, metin veya mantıksal değerleri, iş akışınızdaki diğer matematiksel veya işleme düğümleri tarafından kullanılabilecek bir biçime dönüştürmek için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `value` | Sayısal çıktılara dönüştürülecek değer. Bir tamsayı, kayan noktalı sayı, metin dizesi veya doğru/yanlış boolean kabul eder. | INT, FLOAT, STRING, BOOLEAN | Evet | N/A |

**Not:** Girdi bir dize olduğunda, boş olmamalı ve bir sayının geçerli bir temsilini içermelidir (örn. `"123"`, `"3.14"`). Düğüm, boş dizeler, sayı olarak ayrıştırılamayan metinler veya sonlu olmayan değerler (`"inf"` veya `"nan"` gibi) için hata üretir. Boolean girdiler için `true`, 1.0 (FLOAT) ve 1 (INT) değerine, `false` ise 0.0 (FLOAT) ve 0 (INT) değerine dönüştürülür. Kayan noktalı girdiler için tamsayı çıktısı, ondalık kısmın kesilmesiyle elde edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `FLOAT` | Girdi değerinin kayan noktalı sayıya dönüştürülmüş hali. | FLOAT |
| `INT` | Girdi değerinin tamsayıya dönüştürülmüş hali. Kayan noktalı girdilerde kesme işlemi uygulanır. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNumberConvert/tr.md)

---
**Source fingerprint (SHA-256):** `d6a774bf7c3ad9482b2275adc6ccc9e47c82b1f35f11c5a241b00efd29526f94`
