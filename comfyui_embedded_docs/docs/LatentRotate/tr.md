LatentRotate düğümü, görüntülerin gizli uzay temsillerini belirtilen açılarla döndürmek için tasarlanmıştır. Döndürme efektleri elde etmek için gizli uzayı manipüle etmenin karmaşıklığını soyutlayarak, kullanıcıların üretken bir modelin gizli uzayında görüntüleri kolayca dönüştürmesine olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `örnekler` | 'samples' parametresi, döndürülecek görüntülerin gizli uzay temsillerini temsil eder. Döndürme işleminin başlangıç noktasını belirlemek için kritik öneme sahiptir. | `LATENT` |
| `döndürme` | 'rotation' parametresi, gizli görüntülerin hangi açıyla döndürülmesi gerektiğini belirtir. Ortaya çıkan görüntülerin yönünü doğrudan etkiler. | COMBO[STRING] |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Çıktı, girdi gizli uzay temsillerinin belirtilen açıyla döndürülmüş değiştirilmiş bir sürümüdür. | `LATENT` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentRotate/tr.md)
