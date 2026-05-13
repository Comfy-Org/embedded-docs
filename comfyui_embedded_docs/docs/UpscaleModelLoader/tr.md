> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UpscaleModelLoader/tr.md)

Bu düğüm, `ComfyUI/models/upscale_models` klasöründe bulunan modelleri tespit eder ve ayrıca extra_model_paths.yaml dosyasında yapılandırılan ek yollardaki modelleri de okur. Bazen, ilgili klasördeki model dosyalarını okuyabilmesi için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

UpscaleModelLoader düğümü, belirtilen bir dizinden yükseltme modelleri yüklemek için tasarlanmıştır. Görüntü yükseltme görevleri için yükseltme modellerinin alınmasını ve hazırlanmasını kolaylaştırarak, modellerin değerlendirme için doğru şekilde yüklenmesini ve yapılandırılmasını sağlar.

## Girişler

| Alan           | Comfy veri türü    | Açıklama                                                                                     |
|----------------|--------------------|----------------------------------------------------------------------------------------------|
| `model_adı`   | `COMBO[STRING]`    | Yüklenecek yükseltme modelinin adını belirtir; yükseltme modelleri dizininden doğru model dosyasını tanımlar ve alır. |

## Çıkışlar

| Alan              | Comfy veri türü      | Açıklama                                                                        |
|-------------------|----------------------|---------------------------------------------------------------------------------|
| `upscale_model`   | `UPSCALE_MODEL`      | Yüklenmiş ve hazırlanmış yükseltme modelini döndürür; görüntü yükseltme görevlerinde kullanıma hazırdır. |