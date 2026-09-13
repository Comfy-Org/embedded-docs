# GizliİşlemUygulaCFG

The LatentApplyOperationCFG düğümü, bir modelin örnekleme sürecinin sınıflandırıcıdan bağımsız yönlendirme (CFG) adımında latent bir işlem uygular. CFG'den önce üretilen koşullandırma çıktılarını yakalar, bağlı işlemi latent değerlere uygular ve bu değiştirilmiş örnekleme davranışına sahip modeli döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | CFG işleminin uygulanacağı model | MODEL | Evet | - |
| `işlem` | CFG örnekleme sürecinde uygulanacak latent işlemi | LATENT_OPERATION | Evet | - |

Not: Bu düğüm deneysel olarak işaretlenmiştir. İşlem, CFG örnekleme sürecinde modelin koşullandırma çıktılarına uygulanır. İki koşullandırma çıktısı mevcut olduğunda, işlem birinci ve ikinci çıktı arasındaki farka uygulanır ve ikinci çıktı sonuca geri eklenir. Yalnızca bir koşullandırma çıktısı mevcut olduğunda, işlem doğrudan ona uygulanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Örnekleme sürecine CFG işlemi uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/tr.md)

---
**Source fingerprint (SHA-256):** `e383684a785878bfa4004c2fac78ae562d8e035fdfe081f8e4ebbb2c50161987`
