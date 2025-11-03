> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringConcatenate/tr.md)

StringConcatenate düğümü, iki metin dizisini belirtilen bir ayırıcı ile birleştirerek tek bir metin haline getirir. İki giriş dizisi ve bir ayırıcı karakter veya dizi alır, ardından iki girişin arasına ayırıcı yerleştirilmiş şekilde tek bir dizi çıktı olarak verir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `string_a` | STRING | Evet | - | Birleştirilecek ilk metin dizisi |
| `string_b` | STRING | Evet | - | Birleştirilecek ikinci metin dizisi |
| `delimiter` | STRING | Hayır | - | İki giriş dizisi arasına eklenecek karakter veya dizi (varsayılan: boş dizi) |

## Çıkışlar

| Çıkış Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `output` | STRING | string_a ve string_b arasına ayırıcı yerleştirilmiş şekilde birleştirilmiş dizi |