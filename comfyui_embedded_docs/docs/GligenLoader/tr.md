> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLIGENLoader/tr.md)

Bu düğüm, `ComfyUI/models/gligen` klasöründe bulunan modelleri tespit edecek ve ayrıca extra_model_paths.yaml dosyasında yapılandırılan ek model yollarından da modelleri okuyacaktır. Bazen, ComfyUI arayüzünün ilgili klasörden model dosyalarını okuyabilmesi için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

`GLIGENLoader` düğümü, özel üretim modelleri olan GLIGEN modellerini yüklemek için tasarlanmıştır. Bu modellerin belirtilen yollardan alınmasını ve başlatılmasını kolaylaştırarak, onları daha sonraki üretim görevleri için hazır hale getirir.

## Girdiler

| Alan        | Comfy Veri Türü   | Açıklama                                                                           |
|-------------|-------------------|-----------------------------------------------------------------------------------|
| `gligen_adı`| `COMBO[STRING]`    | Yüklenecek GLIGEN modelinin adı. Hangi model dosyasının alınacağını ve yükleneceğini belirtir, GLIGEN modelinin başlatılması için çok önemlidir. |

## Çıktılar

| Alan     | Veri Türü | Açıklama                                                              |
|----------|-----------|-----------------------------------------------------------------------|
| `gligen` | `GLIGEN`  | Yüklenen GLIGEN modeli, üretim görevlerinde kullanılmaya hazır, belirtilen yoldan yüklenen tamamen başlatılmış modeli temsil eder. |