> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetLoader/tr.md)

Bu düğüm, `ComfyUI/models/controlnet` klasöründe bulunan modelleri algılayacak ve ayrıca extra_model_paths.yaml dosyasında yapılandırılan ek yollardaki modelleri de okuyacaktır. Bazen, ilgili klasörden model dosyalarını okuyabilmesi için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

ControlNetLoader düğümü, belirtilen bir yoldan bir ControlNet modeli yüklemek için tasarlanmıştır. ControlNet modellerini başlatmada çok önemli bir rol oynar; bu modeller, üretilen içerik üzerinde kontrol mekanizmaları uygulamak veya mevcut içeriği kontrol sinyallerine dayanarak değiştirmek için gereklidir.

## Girdiler

| Alan             | Comfy dtype       | Açıklama                                                                       |
|-------------------|-------------------|---------------------------------------------------------------------------------|
| `control_net_name`| `COMBO[STRING]`    | Yüklenecek ControlNet modelinin adını belirtir, model dosyasını önceden tanımlanmış bir dizin yapısı içinde bulmak için kullanılır. |

## Çıktılar

| Alan          | Comfy dtype   | Açıklama                                                              |
|----------------|---------------|--------------------------------------------------------------------------|
| `control_net`  | `CONTROL_NET` | Yüklenen ControlNet modelini döndürür; içerik üretim süreçlerini kontrol etmek veya değiştirmek için kullanıma hazırdır. |