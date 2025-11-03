> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPConditioning/tr.md)

Bu düğüm, CLIP görüntü işleme çıktılarını koşullandırma sürecine entegre etmek ve bu çıktıların etkisini belirtilen güç ve gürültü artırımı parametrelerine göre ayarlamak için tasarlanmıştır. Koşullandırmayı görsel bağlamla zenginleştirerek üretim sürecini geliştirir.

## Girdiler

| Parametre             | Comfy Veri Türü       | Açıklama |
|-----------------------|-----------------------|-------------|
| `koşullandırma`         | `CONDITIONING`        | CLIP görüntü işleme çıktılarının ekleneceği temel koşullandırma verisi; daha fazla değişiklik için temel oluşturur. |
| `clip_görü_çıktısı`   | `CLIP_VISION_OUTPUT`  | Koşullandırmaya entegre edilen görsel bağlamı sağlayan, bir CLIP görüntü modelinden alınan çıktı. |
| `güç`             | `FLOAT`               | CLIP görüntü işleme çıktısının koşullandırma üzerindeki etki yoğunluğunu belirler. |
| `gürültü_artırımı`   | `FLOAT`               | CLIP görüntü işleme çıktısını koşullandırmaya entegre etmeden önce uygulanacak gürültü artırımı seviyesini belirtir. |

## Çıktılar

| Parametre            | Comfy Veri Türü       | Açıklama |
|----------------------|-----------------------|-------------|
| `koşullandırma`        | `CONDITIONING`        | Uygulanmış güç ve gürültü artırımı ile entegre edilmiş CLIP görüntü işleme çıktılarını içeren, zenginleştirilmiş koşullandırma verisi. |