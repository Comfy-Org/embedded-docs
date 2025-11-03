> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffControlNetLoader/tr.md)

Bu düğüm, `ComfyUI/models/controlnet` klasöründe bulunan modelleri tespit edecek ve ayrıca extra_model_paths.yaml dosyasında yapılandırılan ek yollardaki modelleri de okuyacaktır. Bazen, ilgili klasörden model dosyalarını okuyabilmesi için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

DiffControlNetLoader düğümü, diferansiyel kontrol ağlarını yüklemek için tasarlanmıştır. Bunlar, kontrol ağı özelliklerine dayanarak başka bir modelin davranışını değiştirebilen özelleştirilmiş modellerdir. Bu düğüm, diferansiyel kontrol ağları uygulayarak model davranışlarının dinamik olarak ayarlanmasına olanak tanır ve özelleştirilmiş model çıktılarının oluşturulmasını kolaylaştırır.

## Girdiler

| Alan               | Comfy Veri Türü | Açıklama                                                                                 |
|---------------------|-------------------|---------------------------------------------------------------------------------------------|
| `model`             | `MODEL`           | Diferansiyel kontrol ağının uygulanacağı ve modelin davranışının özelleştirilmesine izin verecek temel model. |
| `kontrol_ağı_adı`  | `COMBO[STRING]`    | Temel modelin davranışını değiştirmek için yüklenecek ve uygulanacak spesifik diferansiyel kontrol ağını tanımlar. |

## Çıktılar

| Alan          | Comfy Veri Türü   | Açıklama                                                                   |
|----------------|---------------|-------------------------------------------------------------------------------|
| `control_net`  | `CONTROL_NET` | Yüklenmiş olan ve bir temel modele davranış değişikliği için uygulanmaya hazır bir diferansiyel kontrol ağı. |