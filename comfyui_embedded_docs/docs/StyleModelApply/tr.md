> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StyleModelApply/tr.md)

Bu düğüm, bir stil modelini belirli bir koşullandırmaya uygulayarak, bir CLIP görüntü modelinin çıktısına dayalı olarak stilini geliştirir veya değiştirir. Stil modelinin koşullandırmasını mevcut koşullandırmaya entegre ederek, üretim sürecinde stillerin kusursuz bir şekilde harmanlanmasını sağlar.

## Girdiler

### Zorunlu

| Parametre            | Comfy dtype          | Açıklama |
|-----------------------|-----------------------|-------------|
| `conditioning`        | `CONDITIONING`       | Stil modelinin koşullandırmasının uygulanacağı orijinal koşullandırma verisi. Geliştirilecek veya değiştirilecek temel bağlamı veya stili tanımlamak için çok önemlidir. |
| `style_model`         | `STYLE_MODEL`        | CLIP görüntü modelinin çıktısına dayalı olarak yeni koşullandırma oluşturmak için kullanılan stil modeli. Uygulanacak yeni stili tanımlamada kilit rol oynar. |
| `clip_vision_output`  | `CLIP_VISION_OUTPUT` | Stil modeli tarafından yeni koşullandırma oluşturmak için kullanılan, bir CLIP görüntü modelinden gelen çıktı. Stil uygulaması için gerekli olan görsel bağlamı sağlar. |

## Çıktılar

| Parametre          | Comfy dtype           | Açıklama |
|----------------------|-----------------------|-------------|
| `conditioning`       | `CONDITIONING`        | Stil modelinin çıktısını içeren, geliştirilmiş veya değiştirilmiş koşullandırma. Daha fazla işleme veya üretim için hazır, nihai, stillendirilmiş koşullandırmayı temsil eder. |