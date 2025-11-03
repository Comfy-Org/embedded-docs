> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringTrim/tr.md)

StringTrim düğümü, bir metin dizesinin başından, sonundan veya her iki tarafından boşluk karakterlerini kaldırır. Dizenin sol tarafından, sağ tarafından veya her iki tarafından kırpma yapmayı seçebilirsiniz. Bu, istenmeyen boşlukları, sekmeleri veya satırsonu karakterlerini kaldırarak metin girişlerini temizlemek için kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Evet | - | İşlenecek metin dizesi. Çok satırlı girişi destekler. |
| `mode` | COMBO | Evet | "Both"<br>"Left"<br>"Right" | Dizenin hangi taraf(lar)ından kırpma yapılacağını belirtir. "Both" her iki uçtaki boşlukları kaldırır, "Left" sadece başından kaldırır, "Right" sadece sonundan kaldırır. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | STRING | Seçilen moda göre boşlukları kaldırılmış kırpılmış metin dizesi. |