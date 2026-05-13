> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/tr.md)

PreviewAny düğümü, herhangi bir girdi veri türünün önizlemesini metin biçiminde görüntüler. Girdi olarak herhangi bir veri türünü kabul eder ve okunabilir bir dize temsiline dönüştürerek görüntülenmesini sağlar. Düğüm, dizeler, sayılar, boolean değerler ve karmaşık nesneler dahil olmak üzere farklı veri türlerini JSON biçimine serileştirmeye çalışarak otomatik olarak işler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `source` | ANY | Evet | Herhangi bir veri türü | Önizleme görüntülemesi için herhangi bir girdi veri türünü kabul eder |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `UI Metin Görüntüleme` | STRING | Girdi verilerini metin biçimine dönüştürerek kullanıcı arayüzünde görüntüler. Ayrıca metni daha sonraki işlemler için bir dize çıktısı olarak döndürür. |

---
**Source fingerprint (SHA-256):** `6011c39a31ef9a6786a1dff6e135edcf35def2f715b49301dd49a6467f859271`
