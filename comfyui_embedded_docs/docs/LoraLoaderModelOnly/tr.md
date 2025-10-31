> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderModelOnly/tr.md)

Bu düğüm, `ComfyUI/models/loras` klasöründe bulunan modelleri tespit edecek ve ayrıca extra_model_paths.yaml dosyasında yapılandırılan ek yollardan modelleri okuyacaktır. Bazen, ilgili klasörden model dosyalarını okuyabilmesi için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

Bu düğüm, bir CLIP modeli gerektirmeden bir LoRA modeli yüklemekte uzmanlaşmış olup, LoRA parametrelerine dayalı olarak belirli bir modeli geliştirmeye veya değiştirmeye odaklanır. Modelin davranışı üzerinde hassas ayarlı kontrol sağlayarak, LoRA parametreleri aracılığıyla modelin gücünün dinamik olarak ayarlanmasına olanak tanır.

## Girdiler

| Alan             | Comfy Veri Türü | Açıklama                                                                                   |
|-------------------|-------------------|-----------------------------------------------------------------------------------------------|
| `model`           | `MODEL`           | LoRA ayarlarının uygulanacağı, değişiklikler için temel model.                   |
| `lora_adı`       | `COMBO[STRING]`   | Modele uygulanacak ayarları belirten, yüklenecek LoRA dosyasının adı.      |
| `model_gücü`  | `FLOAT`           | LoRA ayarlarının yoğunluğunu belirler; daha yüksek değerler daha güçlü değişiklikleri ifade eder. |

## Çıktılar

| Alan   | Veri Türü | Açıklama                                                              |
|---------|-------------|--------------------------------------------------------------------------|
| `model` | `MODEL`     | Model davranışındaki veya yeteneklerindeki değişiklikleri yansıtan, LoRA ayarları uygulanmış değiştirilmiş model. |