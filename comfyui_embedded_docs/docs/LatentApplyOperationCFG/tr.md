# GizliİşlemUygulaCFG

**LatentApplyOperationCFG** düğümü, bir modeldeki koşullandırma yönlendirme sürecini değiştirmek için bir latent işlem uygular. Sınıflandırıcısız yönlendirme (CFG) örnekleme süreci sırasında koşullandırma çıktılarını keserek ve belirtilen işlemi, üretim için kullanılmadan önce latent temsillere uygulayarak çalışır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | CFG işleminin uygulanacağı model | MODEL | Evet | - |
| `işlem` | CFG örnekleme süreci sırasında uygulanacak latent işlem | LATENT_OPERATION | Evet | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Örnekleme sürecine CFG işlemi uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/tr.md)

---
**Source fingerprint (SHA-256):** `9fbcc9183abf89bb93e55263bb655e931549360c05a561f7dacae8723db62e52`
