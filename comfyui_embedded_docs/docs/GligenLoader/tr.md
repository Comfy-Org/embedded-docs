Bu düğüm, `ComfyUI/models/gligen` klasöründe bulunan modelleri tespit eder ve ayrıca extra_model_paths.yaml dosyasında yapılandırılmış ek yollardaki modelleri de okur. Bazen, ilgili klasördeki model dosyalarını okuması için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

`GLIGENLoader` düğümü, özel üretken modeller olan GLIGEN modellerini yüklemek için tasarlanmıştır. Belirtilen yollardan bu modelleri alma ve başlatma sürecini kolaylaştırarak, onları daha sonraki üretken görevler için hazır hale getirir.

## Girişler

| Alan | Açıklama | Comfy veri türü |
| --- | --- | --- |
| `gligen_adı` | Yüklenecek GLIGEN modelinin adı; hangi model dosyasının alınıp yükleneceğini belirtir. GLIGEN modelinin başlatılması için kritik öneme sahiptir. | `COMBO[STRING]` |

## Çıkışlar

| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `gligen` | Yüklenen GLIGEN modeli. Üretken görevlerde kullanıma hazırdır ve belirtilen yoldan yüklenen, tamamen başlatılmış modeli temsil eder. | `GLIGEN` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLIGENLoader/tr.md)
