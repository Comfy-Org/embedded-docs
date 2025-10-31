> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPCheckpointLoader/tr.md)

Bu düğüm, `ComfyUI/models/checkpoints` klasöründe bulunan modelleri algılayacak ve ayrıca extra_model_paths.yaml dosyasında yapılandırılan ek yollardan modelleri okuyacaktır. Bazen, ilgili klasörden model dosyalarını okuyabilmesi için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

unCLIPCheckpointLoader düğümü, özellikle unCLIP modelleri için uyarlanmış kontrol noktalarını yüklemek üzere tasarlanmıştır. Belirtilen bir kontrol noktasından modellerin, CLIP görü modüllerinin ve VAE'lerin alınmasını ve başlatılmasını kolaylaştırarak, ilerideki işlemler veya analizler için kurulum sürecini basitleştirir.

## Girdiler

| Alan       | Comfy dtype      | Açıklama                                                                       |
|------------|------------------|---------------------------------------------------------------------------------|
| `ckpt_adı`| `COMBO[STRING]`  | Yüklenecek kontrol noktasının adını belirtir, önceden tanımlanmış bir dizinden doğru kontrol noktası dosyasını tanımlar ve alır, modellerin ve yapılandırmaların başlatılmasını belirler. |

## Çıktılar

| Alan         | Comfy dtype   | Açıklama                                                              | Python dtype         |
|--------------|---------------|-----------------------------------------------------------------------|---------------------|
| `model`      | `MODEL`       | Kontrol noktasından yüklenen birincil modeli temsil eder.               | `torch.nn.Module`   |
| `clip`       | `CLIP`        | Kontrol noktasından yüklenen CLIP modülünü temsil eder (mevcutsa).     | `torch.nn.Module`   |
| `vae`        | `VAE`         | Kontrol noktasından yüklenen VAE modülünü temsil eder (mevcutsa).       | `torch.nn.Module`   |
| `clip_vision`| `CLIP_VISION` | Kontrol noktasından yüklenen CLIP görü modülünü temsil eder (mevcutsa). | `torch.nn.Module`   |