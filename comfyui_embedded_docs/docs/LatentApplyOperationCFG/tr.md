# GizliİşlemUygulaCFG

LatentApplyOperationCFG düğümü, bir modeldeki koşullandırma yönlendirme sürecini değiştirmek için bir latent işlem uygular. Sınıflandırıcısız yönlendirme (CFG) örnekleme süreci sırasında koşullandırma çıktılarını yakalayarak çalışır ve belirtilen işlemi, üretimde kullanılmadan önce latent gösterimlere uygular. Örnekleyici iki koşullandırma çıktısı ürettiğinde, işlem bunlar arasındaki farka uygulanır ve ardından ikinci çıktı sonuca geri eklenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | CFG işleminin uygulanacağı model | MODEL | Evet | - |
| `işlem` | CFG örnekleme sürecinde uygulanacak latent işlem | LATENT_OPERATION | Evet | - |

Not: Bu düğüm deneysel olarak işaretlenmiştir. İşlem, CFG örnekleme süreci sırasında modelin koşullandırma çıktılarına uygulanır. İki koşullandırma çıktısı mevcut olduğunda, işlem birinci ve ikinci çıktı arasındaki farka uygulanır ve ikinci çıktı geri eklenir. Yalnızca bir koşullandırma çıktısı mevcut olduğunda, işlem doğrudan bu çıktıya uygulanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Örnekleme sürecine CFG işlemi uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/tr.md)

---
**Source fingerprint (SHA-256):** `e383684a785878bfa4004c2fac78ae562d8e035fdfe081f8e4ebbb2c50161987`
