> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/tr.md)

**SamplerLMS** düğümü, difüzyon modellerinde kullanılmak üzere bir En Küçük Ortalama Kareler (LMS) örnekleyici oluşturur. Örnekleme sürecinde kullanılabilecek bir örnekleyici nesnesi oluşturur ve LMS algoritmasının sayısal kararlılık ve doğruluk için sırasını kontrol etmenize olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `sıra` | INT | Evet | 1 - 100 | LMS örnekleyici algoritması için sıra parametresi; sayısal yöntemin doğruluğunu ve kararlılığını kontrol eder (varsayılan: 4) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Örnekleme işlem hattında kullanılabilecek yapılandırılmış bir LMS örnekleyici nesnesi |