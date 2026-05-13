> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetLoader/tr.md)

Bu düğüm, `ComfyUI/models/controlnet` klasöründe bulunan modelleri tespit eder ve ayrıca extra_model_paths.yaml dosyasında yapılandırılmış ek yollardaki modelleri de okur. Bazen, ilgili klasördeki model dosyalarını okuyabilmesi için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

ControlNetLoader düğümü, belirtilen bir yoldan bir ControlNet modeli yüklemek için tasarlanmıştır. ControlNet modellerini başlatmada kritik bir rol oynar; bu modeller, oluşturulan içerik üzerinde kontrol mekanizmaları uygulamak veya kontrol sinyallerine dayalı olarak mevcut içeriği değiştirmek için gereklidir.

## Girişler

| Alan               | Comfy veri türü   | Açıklama                                                                                     |
|--------------------|-------------------|----------------------------------------------------------------------------------------------|
| `kontrol_ağı_adı` | `COMBO[STRING]`   | Yüklenecek ControlNet modelinin adını belirtir; model dosyasını önceden tanımlanmış bir dizin yapısı içinde bulmak için kullanılır. |

## Çıkışlar

| Alan           | Comfy veri türü   | Açıklama                                                                                     |
|----------------|-------------------|----------------------------------------------------------------------------------------------|
| `control_net`  | `CONTROL_NET`     | Yüklenen ControlNet modelini döndürür; içerik oluşturma süreçlerini kontrol etmek veya değiştirmek için kullanıma hazırdır. |