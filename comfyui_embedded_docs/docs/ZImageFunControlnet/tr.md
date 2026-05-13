> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/tr.md)

ZImageFunControlnet düğümü, görüntü oluşturma veya düzenleme sürecini etkilemek için özelleştirilmiş bir kontrol ağı uygular. Bir temel model, bir model yaması ve bir VAE kullanarak kontrol etkisinin gücünü ayarlamanıza olanak tanır. Bu düğüm, daha hedefli düzenlemeler için bir temel görüntü, bir rötuş görüntüsü ve bir maske ile çalışabilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | MODEL | Evet | - | Oluşturma sürecinde kullanılan temel model. |
| `model_patch` | MODEL_PATCH | Evet | - | Kontrol ağının yönlendirmesini uygulayan özelleştirilmiş bir yama modeli. |
| `vae` | VAE | Evet | - | Görüntüleri kodlamak ve kodunu çözmek için kullanılan Varyasyonel Otomatik Kodlayıcı. |
| `strength` | FLOAT | Evet | -10,0 ila 10,0 | Kontrol ağının etkisinin gücü. Pozitif değerler etkiyi uygularken, negatif değerler etkiyi tersine çevirebilir (varsayılan: 1,0). |
| `image` | IMAGE | Hayır | - | Oluşturma sürecini yönlendirmek için isteğe bağlı bir temel görüntü. |
| `inpaint_image` | IMAGE | Hayır | - | Bir maske tarafından tanımlanan alanları rötuşlamak için özel olarak kullanılan isteğe bağlı bir görüntü. |
| `mask` | MASK | Hayır | - | Bir görüntünün hangi alanlarının düzenlenmesi veya rötuşlanması gerektiğini tanımlayan isteğe bağlı bir maske. |

**Not:** `inpaint_image` parametresi tipik olarak rötuş için içeriği belirtmek amacıyla bir `mask` ile birlikte kullanılır. Düğümün davranışı, hangi isteğe bağlı girişlerin sağlandığına bağlı olarak değişebilir (örneğin, yönlendirme için `image` kullanmak veya rötuşlama için `image`, `mask` ve `inpaint_image` kullanmak).

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model` | MODEL | Kontrol ağı yaması uygulanmış, örnekleme hattında kullanıma hazır model. |
| `positive` | CONDITIONING | Kontrol ağı girişleri tarafından potansiyel olarak değiştirilmiş pozitif koşullandırma. |
| `negative` | CONDITIONING | Kontrol ağı girişleri tarafından potansiyel olarak değiştirilmiş negatif koşullandırma. |

---
**Source fingerprint (SHA-256):** `465f9eb0dd60af23e6cdc2031579e404b4fed021738e592ee6acbb6ee57e83a0`
