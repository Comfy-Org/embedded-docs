> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringReplace/tr.md)

StringReplace düğümü, girdi dizeleri üzerinde metin değiştirme işlemleri gerçekleştirir. Girdi metni içinde belirtilen bir alt dizeyi arar ve tüm bulunan örnekleri farklı bir alt dizeyle değiştirir. Bu düğüm, tüm değiştirmeler uygulanmış şekilde değiştirilmiş dizeyi döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Evet | - | Değiştirme işlemlerinin yapılacağı girdi metin dizesi |
| `find` | STRING | Evet | - | Girdi metni içinde aranacak alt dize |
| `replace` | STRING | Evet | - | Bulunan tüm örneklerin yerine geçecek değiştirme metni |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | STRING | Bulunan metnin tüm örneklerinin değiştirme metniyle değiştirildiği değiştirilmiş dize |

---
**Source fingerprint (SHA-256):** `72159dba72261efe9df283c1ea3f789651eade923efdaeb108bacc1d0da663f8`
