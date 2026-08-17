# Int

PrimitiveInt düğümü, iş akışınızda tam sayı değerleriyle çalışmanın basit bir yolunu sağlar. Bir tam sayı girdisi alır ve aynı değeri çıktı olarak verir; bu da onu düğümler arasında tam sayı parametreleri aktarmak veya diğer işlemler için belirli sayısal değerler ayarlamak açısından kullanışlı hale getirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `value` | Çıktı olarak verilecek tam sayı değeri (varsayılan: 0) | INT | Evet | -9223372036854775807 ile 9223372036854775807 |

Not: `value` parametresi sabit bir üretim sonrası kontrol davranışına ayarlanmıştır; bu nedenle değer, her üretimden sonra otomatik olarak değişmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Girdi olarak alınan tam sayı değeri değiştirilmeden iletilir | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveInt/tr.md)

---
**Source fingerprint (SHA-256):** `b928ec40c781043c1c8652de3aebedc755d9b63be9e2c773e3fb26ce4d594bba`
