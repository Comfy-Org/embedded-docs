KSamplerSelect düğümü, sağlanan örnekleyici adına göre belirli bir örnekleyici seçmek için tasarlanmıştır. Örnekleyici seçiminin karmaşıklığını soyutlayarak kullanıcıların görevleri için farklı örnekleme stratejileri arasında kolayca geçiş yapmasına olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `örnekleyici_adı` | Seçilecek örnekleyicinin adını belirtir. Bu parametre hangi örnekleme stratejisinin kullanılacağını belirleyerek genel örnekleme davranışını ve sonuçlarını etkiler. | COMBO[STRING] |

## Çıkışlar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Örnekleme görevlerinde kullanılmaya hazır, seçilen örnekleyici nesnesini döndürür. | `SAMPLER` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerSelect/tr.md)
