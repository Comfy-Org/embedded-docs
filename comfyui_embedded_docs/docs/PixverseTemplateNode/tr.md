> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTemplateNode/tr.md)

PixVerse Template düğümü, PixVerse video oluşturma için mevcut şablonlardan seçim yapmanıza olanak tanır. Seçtiğiniz şablon adını, PixVerse API'sinin video oluşturma için gerektirdiği karşılık gelen şablon kimliğine dönüştürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `template` | STRING | Evet | Birden fazla seçenek mevcut | PixVerse video oluşturma için kullanılacak şablon. Mevcut seçenekler, PixVerse sistemindeki önceden tanımlanmış şablonlara karşılık gelir. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `pixverse_template` | INT | Seçilen şablon adına karşılık gelen şablon kimliği; video oluşturma için diğer PixVerse düğümleri tarafından kullanılabilir. |