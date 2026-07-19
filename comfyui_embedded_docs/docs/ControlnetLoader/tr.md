# ControlNet Modelini Yükle

Bu düğüm, `ComfyUI/models/controlnet` klasöründe bulunan modelleri tespit eder ve ayrıca extra_model_paths.yaml dosyasında yapılandırılmış ek yollardaki modelleri de okur. Bazen, ilgili klasördeki model dosyalarını okuyabilmesi için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

ControlNetLoader düğümü, belirtilen bir yoldan bir ControlNet modeli yüklemek için tasarlanmıştır. ControlNet modellerini başlatmada kritik bir rol oynar; bu modeller, oluşturulan içerik üzerinde kontrol mekanizmaları uygulamak veya kontrol sinyallerine dayalı olarak mevcut içeriği değiştirmek için gereklidir.

## Girişler

| Alan | Açıklama | Comfy veri türü |
| --- | --- | --- |
| `kontrol_ağı_adı` | Yüklenecek ControlNet modelinin adını belirtir; model dosyasını önceden tanımlanmış bir dizin yapısı içinde bulmak için kullanılır. | `COMBO[STRING]` |

## Çıkışlar

| Alan | Açıklama | Comfy veri türü |
| --- | --- | --- |
| `control_net` | Yüklenen ControlNet modelini döndürür; içerik oluşturma süreçlerini kontrol etmek veya değiştirmek için kullanıma hazırdır. | `CONTROL_NET` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetLoader/tr.md)
