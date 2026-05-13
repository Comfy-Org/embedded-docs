> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderModelOnly/tr.md)

Bu düğüm, `ComfyUI/models/loras` klasöründe bulunan modelleri tespit eder ve ayrıca extra_model_paths.yaml dosyasında yapılandırılan ek yollardaki modelleri de okur. Bazen, ilgili klasördeki model dosyalarını okuması için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

Bu düğüm, bir CLIP modeli gerektirmeden bir LoRA modeli yükleme konusunda uzmanlaşmıştır ve LoRA parametrelerine dayalı olarak belirli bir modeli geliştirmeye veya değiştirmeye odaklanır. LoRA parametreleri aracılığıyla modelin gücünün dinamik olarak ayarlanmasına olanak tanıyarak, model davranışı üzerinde ince ayarlı kontrol sağlar.

## Girişler

| Alan               | Comfy Veri Türü   | Açıklama                                                                                   |
|-------------------|-------------------|-----------------------------------------------------------------------------------------------|
| `model`           | `MODEL`           | Değişiklikler için temel model; LoRA ayarlamaları bu modele uygulanacaktır.                   |
| `lora_name`       | `COMBO[STRING]`   | Yüklenecek LoRA dosyasının adı; modele uygulanacak ayarlamaları belirtir.      |
| `strength_model`  | `FLOAT`           | LoRA ayarlamalarının yoğunluğunu belirler; daha yüksek değerler daha güçlü değişiklikleri ifade eder. |

## Çıkışlar

| Alan   | Veri Türü | Açıklama                                                              |
|---------|-------------|--------------------------------------------------------------------------|
| `model` | `MODEL`     | LoRA ayarlamaları uygulanmış, model davranışında veya yeteneklerinde değişiklikleri yansıtan değiştirilmiş model. |