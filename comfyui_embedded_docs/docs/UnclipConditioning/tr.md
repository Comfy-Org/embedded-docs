Bu düğüm, CLIP görüntü çıktılarını koşullandırma sürecine entegre etmek ve bu çıktıların etkisini belirtilen güç ve gürültü artırma parametrelerine göre ayarlamak için tasarlanmıştır. Koşullandırmayı görsel bağlamla zenginleştirerek üretim sürecini iyileştirir.

## Girişler

| Parametre | Açıklama | Comfy dtype |
| --- | --- | --- |
| `koşullandırma` | CLIP görüntü çıktılarının ekleneceği temel koşullandırma verileri; daha sonraki değişiklikler için temel görevi görür. | `CONDITIONING` |
| `clip_görü_çıktısı` | Bir CLIP görüntü modelinden gelen, koşullandırmaya entegre edilen görsel bağlamı sağlayan çıktı. | `CLIP_VISION_OUTPUT` |
| `güç` | CLIP görüntü çıktısının koşullandırma üzerindeki etkisinin yoğunluğunu belirler. | `FLOAT` |
| `gürültü_artırımı` | CLIP görüntü çıktısına, koşullandırmaya entegre edilmeden önce uygulanacak gürültü artırma seviyesini belirtir. | `FLOAT` |

## Çıktılar

| Parametre | Açıklama | Comfy dtype |
| --- | --- | --- |
| `koşullandırma` | Artık uygulanmış güç ve gürültü artırma ile entegre CLIP görüntü çıktılarını içeren, zenginleştirilmiş koşullandırma verileri. | `CONDITIONING` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPConditioning/tr.md)
