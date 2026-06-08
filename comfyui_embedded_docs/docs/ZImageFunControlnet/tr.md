ZImageFunControlnet düğümü, görüntü oluşturma veya düzenleme sürecini etkilemek için özelleştirilmiş bir kontrol ağı uygular. Bir temel model, bir model yaması ve bir VAE kullanarak kontrol etkisinin gücünü ayarlamanıza olanak tanır. Bu düğüm, daha hedefli düzenlemeler için bir temel görüntü, bir rötuş görüntüsü ve bir maske ile çalışabilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Oluşturma sürecinde kullanılan temel model. | MODEL | Evet | - |
| `model_patch` | Kontrol ağının yönlendirmesini uygulayan özelleştirilmiş bir yama modeli. | MODEL_PATCH | Evet | - |
| `vae` | Görüntüleri kodlamak ve kodunu çözmek için kullanılan Varyasyonel Otomatik Kodlayıcı. | VAE | Evet | - |
| `güç` | Kontrol ağının etkisinin gücü. Pozitif değerler etkiyi uygularken, negatif değerler etkiyi tersine çevirebilir (varsayılan: 1,0). | FLOAT | Evet | -10,0 ila 10,0 |
| `görsel` | Oluşturma sürecini yönlendirmek için isteğe bağlı bir temel görüntü. | IMAGE | Hayır | - |
| `boyanacak_görsel` | Bir maske tarafından tanımlanan alanları rötuşlamak için özel olarak kullanılan isteğe bağlı bir görüntü. | IMAGE | Hayır | - |
| `mask` | Bir görüntünün hangi alanlarının düzenlenmesi veya rötuşlanması gerektiğini tanımlayan isteğe bağlı bir maske. | MASK | Hayır | - |

**Not:** `inpaint_image` parametresi tipik olarak rötuş için içeriği belirtmek amacıyla bir `mask` ile birlikte kullanılır. Düğümün davranışı, hangi isteğe bağlı girişlerin sağlandığına bağlı olarak değişebilir (örneğin, yönlendirme için `image` kullanmak veya rötuşlama için `image`, `mask` ve `inpaint_image` kullanmak).

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Kontrol ağı yaması uygulanmış, örnekleme hattında kullanıma hazır model. | MODEL |
| `positive` | Kontrol ağı girişleri tarafından potansiyel olarak değiştirilmiş pozitif koşullandırma. | CONDITIONING |
| `negative` | Kontrol ağı girişleri tarafından potansiyel olarak değiştirilmiş negatif koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/tr.md)

---
**Source fingerprint (SHA-256):** `465f9eb0dd60af23e6cdc2031579e404b4fed021738e592ee6acbb6ee57e83a0`
