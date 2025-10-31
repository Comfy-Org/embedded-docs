> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringReplace/tr.md)

StringReplace düğümü, giriş dizeleri üzerinde metin değiştirme işlemleri gerçekleştirir. Giriş metni içinde belirli bir alt dizeyi arar ve tüm bulunan örneklerini farklı bir alt dizeyle değiştirir. Bu düğüm, tüm değiştirmelerin uygulandığı değiştirilmiş diziyi döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Evet | - | Değiştirme işlemlerinin yapılacağı giriş metin dizesi |
| `find` | STRING | Evet | - | Giriş metni içinde aranacak alt dize |
| `replace` | STRING | Evet | - | Bulunan tüm örneklerin yerine geçecek değiştirme metni |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | STRING | Bulunan metnin tüm örneklerinin değiştirme metniyle değiştirildiği değiştirilmiş dize |