> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConvertStringToComboNode/tr.md)

Convert String to Combo düğümü, bir metin dizisini girdi olarak alır ve onu bir Combo veri türüne dönüştürür. Bu, bir metin değerini, Combo girdisi gerektiren diğer düğümler için bir seçim olarak kullanmanıza olanak tanır. Dize değerini değiştirmeden aktarır, ancak veri türünü değiştirir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Evet | Yok | Combo türüne dönüştürülecek metin dizisi. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | COMBO | Girdi dizisi, artık Combo veri türü olarak biçimlendirilmiş şekilde. |
