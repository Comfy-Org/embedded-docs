# unCLIPKontrolNoktasıYükleyici

Bu düğüm, `ComfyUI/models/checkpoints` klasöründe bulunan modelleri tespit eder ve ayrıca extra_model_paths.yaml dosyasında yapılandırılan ek yollardaki modelleri de okur. Bazen, model dosyalarını ilgili klasörden okuması için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

unCLIPCheckpointLoader düğümü, özellikle unCLIP modelleri için uyarlanmış kontrol noktalarını yüklemek üzere tasarlanmıştır. Belirtilen bir kontrol noktasından modellerin, CLIP görüş modüllerinin ve VAE'lerin alınmasını ve başlatılmasını kolaylaştırarak, daha sonraki işlemler veya analizler için kurulum sürecini basitleştirir.

## Girişler

| Alan | Açıklama | Comfy veri türü |
| --- | --- | --- |
| `ckpt_adı` | Yüklenecek kontrol noktasının adını belirtir; önceden tanımlanmış bir dizinden doğru kontrol noktası dosyasını tanımlayıp alarak modellerin ve yapılandırmaların başlatılmasını belirler. | `COMBO[STRING]` |

## Çıkışlar

| Alan | Açıklama | Comfy veri türü | Python veri türü |
| --- | --- | --- | --- |
| `model` | Kontrol noktasından yüklenen ana modeli temsil eder. | `MODEL` | `torch.nn.Module` |
| `clip` | Varsa, kontrol noktasından yüklenen CLIP modülünü temsil eder. | `CLIP` | `torch.nn.Module` |
| `vae` | Varsa, kontrol noktasından yüklenen VAE modülünü temsil eder. | `VAE` | `torch.nn.Module` |
| `clip_vision` | Varsa, kontrol noktasından yüklenen CLIP görüş modülünü temsil eder. | `CLIP_VISION` | `torch.nn.Module` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPCheckpointLoader/tr.md)
