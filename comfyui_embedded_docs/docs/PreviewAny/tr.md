# Herhangi Bir Şeyi Önizle

PreviewAny, herhangi bir girdi değerini inceleyebilmeniz için okunabilir metne dönüştürür. Dizeler değişmeden geçer, sayılar ve boolean değerler düz metin haline gelir ve diğer veri türleri mümkün olduğunda JSON olarak serileştirilir (serileştirme başarısız olursa düz dize biçimine geri dönülür). Ortaya çıkan metin kullanıcı arayüzünde gösterilir ve ayrıca daha sonraki işlemler için bir dize çıktısı olarak döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `kaynak` | Önizleme görüntüsü için herhangi bir girdi veri türünü kabul eder. Bir değer sağlanmazsa, önizleme 'None' gösterir. | ANY | Evet | Herhangi bir veri türü |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `result` | Girdi değerinin metin biçimine dönüştürülmüş hali. Aynı metin kullanıcı arayüzünde de görüntülenir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/tr.md)

---
**Source fingerprint (SHA-256):** `9572eac396aa27a83148a940e4bf37a9ec4e4a47e9526db8bb983611f9237536`
