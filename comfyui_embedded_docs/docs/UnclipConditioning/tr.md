> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPConditioning/tr.md)

Bu düğüm, CLIP görüntü çıktılarını koşullandırma sürecine entegre etmek ve bu çıktıların etkisini belirtilen güç ve gürültü artırma parametrelerine göre ayarlamak için tasarlanmıştır. Koşullandırmayı görsel bağlamla zenginleştirerek üretim sürecini iyileştirir.

## Girişler

| Parametre              | Comfy dtype            | Açıklama |
|------------------------|------------------------|-------------|
| `conditioning`         | `CONDITIONING`         | CLIP görüntü çıktılarının ekleneceği temel koşullandırma verileri; daha sonraki değişiklikler için temel görevi görür. |
| `clip_vision_output`   | `CLIP_VISION_OUTPUT`   | Bir CLIP görüntü modelinden gelen, koşullandırmaya entegre edilen görsel bağlamı sağlayan çıktı. |
| `strength`             | `FLOAT`                | CLIP görüntü çıktısının koşullandırma üzerindeki etkisinin yoğunluğunu belirler. |
| `noise_augmentation`   | `FLOAT`                | CLIP görüntü çıktısına, koşullandırmaya entegre edilmeden önce uygulanacak gürültü artırma seviyesini belirtir. |

## Çıktılar

| Parametre             | Comfy dtype            | Açıklama |
|-----------------------|------------------------|-------------|
| `conditioning`         | `CONDITIONING`         | Artık uygulanmış güç ve gürültü artırma ile entegre CLIP görüntü çıktılarını içeren, zenginleştirilmiş koşullandırma verileri. |