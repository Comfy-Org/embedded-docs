> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringContains/tr.md)

StringContains düğümü, belirtilen bir dizenin belirli bir alt dizeyi içerip içermediğini kontrol eder. Bu kontrolü büyük/küçük harf duyarlı veya duyarsız eşleştirme ile gerçekleştirebilir ve alt dizenin ana dize içinde bulunup bulunmadığını belirten bir boolean sonucu döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Evet | - | İçinde arama yapılacak ana metin dizesi |
| `substring` | STRING | Evet | - | Ana dize içinde aranacak metin |
| `case_sensitive` | BOOLEAN | Hayır | - | Aramanın büyük/küçük harf duyarlı olup olmayacağını belirler (varsayılan: true) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `contains` | BOOLEAN | Alt dize dizede bulunursa true, aksi halde false döndürür |

---
**Source fingerprint (SHA-256):** `ef7329ca8586e0f894306d93835490edb948a346db1e0cb011e4da5a6fe44202`
