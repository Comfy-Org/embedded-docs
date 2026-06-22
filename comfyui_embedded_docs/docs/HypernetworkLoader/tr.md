# HiperAğYükleyici

Bu düğüm, `ComfyUI/models/hypernetworks` klasöründe bulunan modelleri tespit eder ve ayrıca extra_model_paths.yaml dosyasında yapılandırılan ek yollardaki modelleri de okur. Bazen, model dosyalarını ilgili klasörden okuması için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

HypernetworkLoader düğümü, bir hiper ağ uygulayarak belirli bir modelin yeteneklerini geliştirmek veya değiştirmek için tasarlanmıştır. Belirtilen bir hiper ağı yükler ve bunu modele uygulayarak, güç parametresine bağlı olarak modelin davranışını veya performansını potansiyel olarak değiştirir. Bu süreç, modelin mimarisinde veya parametrelerinde dinamik ayarlamalara olanak tanıyarak daha esnek ve uyarlanabilir yapay zeka sistemleri sağlar.

## Girişler

| Alan | Açıklama | Comfy veri türü |
| --- | --- | --- |
| `model` | Hiper ağın uygulanacağı temel model olup, geliştirilecek veya değiştirilecek mimariyi belirler. | `MODEL` |
| `hiperağ_adı` | Modele yüklenecek ve uygulanacak hiper ağın adı olup, modelin değiştirilmiş davranışını veya performansını etkiler. | `COMBO[STRING]` |
| `güç` | Hiper ağın model üzerindeki etkisinin yoğunluğunu ayarlayan bir skaler olup, değişikliklerin ince ayarını sağlar. | `FLOAT` |

## Çıkışlar

| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Hiper ağ uygulandıktan sonraki değiştirilmiş model olup, hiper ağın orijinal model üzerindeki etkisini sergiler. | `MODEL` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HypernetworkLoader/tr.md)
