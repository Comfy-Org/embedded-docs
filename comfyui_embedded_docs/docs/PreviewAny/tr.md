# Herhangi Bir Şeyi Önizle

PreviewAny düğümü herhangi bir girdi değerini kabul eder ve arayüzde okunabilir metin olarak görüntüler. Bir iş akışının herhangi bir noktasında değerleri incelemek ve hata ayıklamak için tasarlanmıştır: dizeler olduğu gibi gösterilir, sayılar ve boole değerleri metne dönüştürülür, diğer nesneler JSON biçiminde biçimlendirilir. Dönüştürülen metin, diğer düğümler tarafından kullanılabilmesi için bir dize çıktısı olarak da iletilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `source` | Metin olarak önizlenecek değer. Herhangi bir veri türünü kabul eder. Dizeler değiştirilmeden geçirilir; sayılar ve boole değerleri metne dönüştürülür; diğer değerler girintili JSON olarak serileştirilir. JSON serileştirme başarısız olursa, değerin düz dize gösterimi kullanılır; bu da başarısız olursa, "kaynak mevcut ancak serileştirilemedi." metni görüntülenir. | ANY | Evet | Herhangi bir veri türü |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `UI Text Display` | Girdi verilerinin metne dönüştürülmüş halini kullanıcı arayüzünde gösterir. Aynı metin, diğer düğümler tarafından daha fazla işlenmek üzere bir dize çıktısı olarak da döndürülür. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/tr.md)

---
**Source fingerprint (SHA-256):** `9572eac396aa27a83148a940e4bf37a9ec4e4a47e9526db8bb983611f9237536`
