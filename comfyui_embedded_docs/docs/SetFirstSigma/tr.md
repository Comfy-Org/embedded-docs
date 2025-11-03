> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/tr.md)

SetFirstSigma düğümü, bir sigma değerleri dizisini, dizideki ilk sigma değerini özel bir değerle değiştirerek düzenler. Mevcut bir sigma dizisini ve yeni bir sigma değerini girdi olarak alır, ardından yalnızca ilk elemanın değiştirildiği ve diğer tüm sigma değerlerinin değişmeden kaldığı yeni bir sigma dizisi döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `sigmalar` | SIGMAS | Evet | - | Değiştirilecek sigma değerlerinin girdi dizisi |
| `sigma` | FLOAT | Evet | 0.0 - 20000.0 | Dizideki ilk eleman olarak ayarlanacak yeni sigma değeri (varsayılan: 136.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sigmalar` | SIGMAS | İlk elemanı özel sigma değeri ile değiştirilmiş olan düzenlenmiş sigma dizisi |