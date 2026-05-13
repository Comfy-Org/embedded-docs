> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPCheckpointLoader/tr.md)

Bu düğüm, `ComfyUI/models/checkpoints` klasöründe bulunan modelleri tespit eder ve ayrıca extra_model_paths.yaml dosyasında yapılandırılan ek yollardaki modelleri de okur. Bazen, model dosyalarını ilgili klasörden okuması için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

unCLIPCheckpointLoader düğümü, özellikle unCLIP modelleri için uyarlanmış kontrol noktalarını yüklemek üzere tasarlanmıştır. Belirtilen bir kontrol noktasından modellerin, CLIP görüş modüllerinin ve VAE'lerin alınmasını ve başlatılmasını kolaylaştırarak, daha sonraki işlemler veya analizler için kurulum sürecini basitleştirir.

## Girişler

| Alan          | Comfy veri türü | Açıklama                                                                                          |
|---------------|-----------------|---------------------------------------------------------------------------------------------------|
| `ckpt_adı`   | `COMBO[STRING]` | Yüklenecek kontrol noktasının adını belirtir; önceden tanımlanmış bir dizinden doğru kontrol noktası dosyasını tanımlayıp alarak modellerin ve yapılandırmaların başlatılmasını belirler. |

## Çıkışlar

| Alan           | Comfy veri türü | Açıklama                                                              | Python veri türü      |
|----------------|-----------------|-----------------------------------------------------------------------|-----------------------|
| `model`        | `MODEL`         | Kontrol noktasından yüklenen ana modeli temsil eder.                   | `torch.nn.Module`     |
| `clip`         | `CLIP`          | Varsa, kontrol noktasından yüklenen CLIP modülünü temsil eder.        | `torch.nn.Module`     |
| `vae`          | `VAE`           | Varsa, kontrol noktasından yüklenen VAE modülünü temsil eder.         | `torch.nn.Module`     |
| `clip_vision`  | `CLIP_VISION`   | Varsa, kontrol noktasından yüklenen CLIP görüş modülünü temsil eder.  | `torch.nn.Module`     |