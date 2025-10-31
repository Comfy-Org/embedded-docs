> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringContains/tr.md)

StringContains düğümü, belirli bir dizenin belirtilen bir alt dize içerip içermediğini kontrol eder. Bu kontrolü büyük/küçük harf duyarlı veya büyük/küçük harf duyarsız eşleme ile gerçekleştirebilir ve alt dizenin ana dize içinde bulunup bulunmadığını gösteren bir boolean sonuç döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Evet | - | İçinde arama yapılacak ana metin dizesi |
| `substring` | STRING | Evet | - | Ana dize içinde aranacak metin |
| `case_sensitive` | BOOLEAN | Hayır | - | Aramanın büyük/küçük harf duyarlı olup olmayacağını belirler (varsayılan: true) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `contains` | BOOLEAN | Alt dize dize içinde bulunursa true, aksi takdirde false döndürür |