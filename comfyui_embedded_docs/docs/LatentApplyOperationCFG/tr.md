# GizliİşlemUygulaCFG

LatentApplyOperationCFG düğümü, bir modeldeki koşullandırma yönlendirme sürecini değiştirmek için bir latent işlem uygular. Sınıflandırıcısız yönlendirme (CFG) örnekleme süreci sırasında koşullandırma çıktılarını yakalayarak ve belirtilen işlemi, üretim için kullanılmadan önce latent temsillere uygulayarak çalışır.

Model iki koşullandırma çıktısı ürettiğinde (örneğin, pozitif ve negatif koşullandırma), işlem bunlar arasındaki farka uygulanır ve ardından ikinci koşullandırma geri eklenir. Yalnızca bir koşullandırma çıktısı olduğunda, işlem doğrudan ona uygulanır. Bu düğüm deneysel olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | CFG işleminin uygulanacağı model | MODEL | Evet | - |
| `operation` | CFG örnekleme süreci sırasında uygulanacak latent işlem | LATENT_OPERATION | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Örnekleme sürecine CFG işlemi uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/tr.md)

---
**Source fingerprint (SHA-256):** `e383684a785878bfa4004c2fac78ae562d8e035fdfe081f8e4ebbb2c50161987`
