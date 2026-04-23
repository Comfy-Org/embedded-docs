> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNumberConvert/tr.md)

Sayı Dönüştür düğümü, çeşitli girdi veri türlerini sayısal değerlere dönüştürür. Tam sayı, ondalıklı sayı, metin veya mantıksal değer türlerinde tek bir girdi kabul eder ve iki çıktı üretir: bir ondalıklı sayı ve bir tam sayı. Bu, metin veya mantıksal değerleri, iş akışınızdaki diğer matematiksel veya işlem düğümleri tarafından kullanılabilecek bir biçime dönüştürmek için kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `value` | INT, FLOAT, STRING, BOOLEAN | Evet | Yok | Sayısal çıktılara dönüştürülecek değer. Bir tam sayı, ondalıklı sayı, metin dizisi veya doğru/yanlış mantıksal değer kabul eder. |

**Not:** Girdi bir metin dizisi olduğunda, boş olmamalı ve geçerli bir sayı temsili içermelidir (ör. `"123"`, `"3.14"`). Düğüm, boş diziler, sayı olarak ayrıştırılamayan metinler veya sonlu olmayan değerler (`"inf"` veya `"nan"` gibi) için hata verecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `FLOAT` | FLOAT | Girdi değerinin ondalıklı sayıya dönüştürülmüş hali. |
| `INT` | INT | Girdi değerinin tam sayıya dönüştürülmüş hali. Ondalıklı sayı girdilerinde, bu işlem kesme (truncation) yapar. |