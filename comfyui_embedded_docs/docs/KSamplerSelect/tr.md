> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerSelect/tr.md)

KSamplerSelect düğümü, belirtilen örnekleyici adına dayalı olarak belirli bir örnekleyiciyi seçmek için tasarlanmıştır. Örnekleyici seçiminin karmaşıklığını soyutlayarak, kullanıcıların görevleri için farklı örnekleme stratejileri arasında kolayca geçiş yapmasına olanak tanır.

## Girdiler

| Parametre         | Veri Tipi      | Açıklama                                                                                      |
|-------------------|----------------|------------------------------------------------------------------------------------------------|
| `sampler_name`    | COMBO[STRING] | Seçilecek örnekleyicinin adını belirtir. Bu parametre, genel örnekleme davranışını ve sonuçlarını etkileyen hangi örnekleme stratejisinin kullanılacağını belirler. |

## Çıktılar

| Parametre   | Veri Tipi   | Açıklama                                                                 |
|-------------|-------------|-----------------------------------------------------------------------------|
| `sampler`   | `SAMPLER`   | Seçilen örnekleyici nesnesini döndürür, örnekleme görevlerinde kullanılmaya hazırdır. |