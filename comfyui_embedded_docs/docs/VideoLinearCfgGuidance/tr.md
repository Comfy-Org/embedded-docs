VideoLinearCFGGuidance düğümü, bir video modeline doğrusal koşullandırma yönlendirme ölçeği uygulayarak, belirtilen bir aralıkta koşullandırılmış ve koşullandırılmamış bileşenlerin etkisini ayarlar. Bu, üretim süreci üzerinde dinamik kontrol sağlayarak, model çıktısının istenen koşullandırma seviyesine göre ince ayar yapılmasına olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Model parametresi, doğrusal CFG yönlendirmesinin uygulanacağı video modelini temsil eder. Yönlendirme ölçeği ile değiştirilecek temel modeli tanımlamak için kritik öneme sahiptir. | MODEL |
| `min_cfg` | min_cfg parametresi, uygulanacak minimum koşullandırma yönlendirme ölçeğini belirtir ve doğrusal ölçek ayarlaması için başlangıç noktası görevi görür. Yönlendirme ölçeğinin alt sınırını belirlemede kilit rol oynar ve model çıktısını etkiler. | `FLOAT` |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Çıktı, doğrusal CFG yönlendirme ölçeğinin uygulandığı, giriş modelinin değiştirilmiş bir sürümüdür. Bu ayarlanmış model, belirtilen yönlendirme ölçeğine bağlı olarak, değişen derecelerde koşullandırma ile çıktılar üretebilir. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoLinearCFGGuidance/tr.md)
