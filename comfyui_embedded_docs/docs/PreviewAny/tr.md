# Herhangi Bir Şeyi Önizle

PreviewAny, herhangi bir girdi değerini inceleyebilmeniz için okunabilir metne dönüştürür. Dizeler değişmeden geçer, sayılar ve boolean değerler düz metne dönüşür ve diğer veri türleri mümkün olduğunda JSON'a serileştirilir (serileştirme başarısız olursa düz dize biçimlerine geri döner). Elde edilen metin kullanıcı arayüzünde gösterilir ve daha fazla işleme için bir dize çıktısı olarak da döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `kaynak` | Önizleme gösterimi için herhangi bir girdi veri türünü kabul eder. Bir değer sağlanmazsa, önizleme 'None' gösterir. | ANY | Evet | Herhangi bir veri türü |

**Dönüştürme davranışı**

- STRING türündeki değerler sağlandığı şekilde aynen gösterilir.
- INT, FLOAT veya BOOLEAN türündeki değerler düz metne dönüştürülür.
- Diğer boş olmayan her değer, 4 boşluk girintisiyle JSON metnine dönüştürülür; bu dönüştürme başarısız olursa düğüm, değerin düz metin biçimine geri döner. Bu da başarısız olursa önizleme 'source exists, but could not be serialized.' mesajını gösterir.
- Hiçbir değer bağlı değilse veya değer boşsa, önizleme 'None' gösterir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `result` | Metin biçimine dönüştürülen girdi değeri. Aynı metin kullanıcı arayüzünde de gösterilir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/tr.md)

---
**Source fingerprint (SHA-256):** `66b5283b2d7d43e679c0bc6cdcad54c92539a986763333972e722b39c7963be8`
