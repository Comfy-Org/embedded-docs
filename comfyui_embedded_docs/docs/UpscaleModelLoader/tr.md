> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UpscaleModelLoader/tr.md)

Bu düğüm, `ComfyUI/models/upscale_models` klasöründe bulunan modelleri algılayacak ve ayrıca extra_model_paths.yaml dosyasında yapılandırılan ek yollardan modelleri okuyacaktır. Bazen, ComfyUI arayüzünün ilgili klasörden model dosyalarını okuyabilmesi için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

UpscaleModelLoader düğümü, belirli bir dizinden yükseltme modellerini yüklemek için tasarlanmıştır. Görüntü yükseltme görevleri için yükseltme modellerinin alınmasını ve hazırlanmasını kolaylaştırarak modellerin değerlendirme için doğru şekilde yüklendiğinden ve yapılandırıldığından emin olur.

## Girdiler

| Alan          | Comfy Veri Türü    | Açıklama                                                                       |
|----------------|-------------------|---------------------------------------------------------------------------------|
| `model_name`   | `COMBO[STRING]`    | Yüklenecek yükseltme modelinin adını belirtir; yükseltme modelleri dizininden doğru model dosyasını tanımlar ve alır. |

## Çıktılar

| Alan            | Comfy Veri Türü     | Açıklama                                                              |
|-------------------|---------------------|--------------------------------------------------------------------------|
| `upscale_model`  | `UPSCALE_MODEL`     | Görüntü yükseltme görevlerinde kullanıma hazır, yüklenmiş ve hazırlanmış yükseltme modelini döndürür. |