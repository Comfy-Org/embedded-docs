> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAdd/tr.md)

CLIPAdd düğümü, iki CLIP modelini anahtar yamalarını birleştirerek birleştirir. İlk CLIP modelinin bir kopyasını oluşturur ve ardından konum kimlikleri ve logit ölçek parametreleri hariç tutularak ikinci modelden gelen anahtar yamaların çoğunu ekler. Bu, ilk modelin yapısını korurken farklı CLIP modellerinden özellikleri harmanlamanıza olanak tanır.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `clip1` | CLIP | Gerekli | - | - | Birleştirme için temel olarak kullanılacak birincil CLIP modeli |
| `clip2` | CLIP | Gerekli | - | - | Eklenmek üzere ek yamalar sağlayan ikincil CLIP modeli |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Her iki girdi modelinden gelen özellikleri birleştirilmiş bir CLIP modeli döndürür |