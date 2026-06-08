Bu düğüm, `ComfyUI/models/style_models` klasöründe bulunan modelleri algılar ve ayrıca extra_model_paths.yaml dosyasında yapılandırılan ek yollardan modelleri okur. Bazen, ilgili klasördeki model dosyalarını okuması için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

StyleModelLoader düğümü, belirtilen bir yoldan stil modeli yüklemek için tasarlanmıştır. Görüntülere belirli sanatsal stiller uygulamak için kullanılabilecek stil modellerini alıp başlatmaya odaklanır, böylece yüklenen stil modeline dayalı olarak görsel çıktıların özelleştirilmesini sağlar.

## Girişler

| Parametre Adı | Açıklama | Comfy dtype | Python dtype |
| --- | --- | --- | --- |
| `stil_modeli_adı` | Yüklenecek stil modelinin adını belirtir. Bu ad, model dosyasını önceden tanımlanmış bir dizin yapısı içinde bulmak için kullanılır ve kullanıcı girişine veya uygulama ihtiyaçlarına göre farklı stil modellerinin dinamik olarak yüklenmesine olanak tanır. | COMBO[STRING] | `str` |

## Çıktılar

| Parametre Adı | Açıklama | Comfy dtype | Python dtype |
| --- | --- | --- | --- |
| `style_model` | Yüklenen stil modelini döndürür ve görüntülere stiller uygulamak için kullanıma hazırdır. Bu, farklı sanatsal stiller uygulayarak görsel çıktıların dinamik olarak özelleştirilmesini sağlar. | `STYLE_MODEL` | `StyleModel` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StyleModelLoader/tr.md)
