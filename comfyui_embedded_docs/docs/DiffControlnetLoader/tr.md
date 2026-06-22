# ControlNet Modelini Yükle (fark)

Bu düğüm, `ComfyUI/models/controlnet` klasöründe bulunan modelleri tespit eder ve ayrıca extra_model_paths.yaml dosyasında yapılandırılan ek yollardaki modelleri de okur. Bazen, ilgili klasördeki model dosyalarını okuyabilmesi için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

DiffControlNetLoader düğümü, diferansiyel kontrol ağlarını yüklemek için tasarlanmıştır. Bu ağlar, kontrol ağı özelliklerine dayalı olarak başka bir modelin davranışını değiştirebilen özel modellerdir. Bu düğüm, diferansiyel kontrol ağları uygulayarak model davranışlarının dinamik olarak ayarlanmasına olanak tanır ve özelleştirilmiş model çıktılarının oluşturulmasını kolaylaştırır.

## Girişler

| Alan | Açıklama | Comfy dtype |
| --- | --- | --- |
| `model` | Diferansiyel kontrol ağının uygulanacağı temel model. Modelin davranışının özelleştirilmesine olanak tanır. | `MODEL` |
| `kontrol_ağı_adı` | Yüklenecek ve temel modele uygulanarak davranışını değiştirecek belirli diferansiyel kontrol ağını tanımlar. | `COMBO[STRING]` |

## Çıkışlar

| Alan | Açıklama | Comfy dtype |
| --- | --- | --- |
| `control_net` | Yüklenmiş ve davranış değişikliği için bir temel modele uygulanmaya hazır bir diferansiyel kontrol ağı. | `CONTROL_NET` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffControlNetLoader/tr.md)
