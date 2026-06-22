# Sayı Dönüştürme

## Genel Bakış

Sayı Dönüştür düğümü, çeşitli giriş veri türlerini sayısal değerlere dönüştürür. Tam sayı, ondalıklı sayı, metin veya mantıksal değer türünde tek bir giriş kabul eder ve iki çıktı üretir: bir ondalıklı sayı ve bir tam sayı. Bu, metin veya mantıksal değerleri, iş akışınızdaki diğer matematiksel veya işleme düğümleri tarafından kullanılabilecek bir formata dönüştürmek için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `değer` | Sayısal çıktılara dönüştürülecek değer. Tam sayı, ondalıklı sayı, metin dizisi veya doğru/yanlış mantıksal değer kabul eder. | INT, FLOAT, STRING, BOOLEAN | Evet | Yok |

**Not:** Giriş bir metin dizisi olduğunda, boş olmamalı ve geçerli bir sayı temsili içermelidir (örneğin, `"123"`, `"3.14"`). Düğüm, boş diziler, sayı olarak ayrıştırılamayan metinler veya sonlu olmayan değerler (örneğin, `"inf"` veya `"nan"`) için hata verecektir. Mantıksal girişlerde, `true` değeri 1.0 (FLOAT) ve 1 (INT)'e dönüşürken, `false` değeri 0.0 (FLOAT) ve 0 (INT)'a dönüşür. Ondalıklı sayı girişlerinde, tam sayı çıktısı ondalık kısmın kesilmesiyle elde edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `FLOAT` | Giriş değerinin ondalıklı sayıya dönüştürülmüş hali. | FLOAT |
| `INT` | Giriş değerinin tam sayıya dönüştürülmüş hali. Ondalıklı sayı girişlerinde, ondalık kısmı keser. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNumberConvert/tr.md)

---
**Source fingerprint (SHA-256):** `961fbea05b22c68f768f9ecaae2ee455b1913afe4a65d8c0e6b6497b1e24ce72`
