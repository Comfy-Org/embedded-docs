# ZImageFunControlnet

ZImageFunControlnet düğümü, görüntü oluşturma veya düzenleme sürecini etkilemek için özel bir kontrol ağı uygular. Temel bir model, model yaması ve VAE kullanarak kontrol etkisinin gücünü ayarlamanıza olanak tanır. Bu düğüm, daha hedefli düzenlemeler için temel görüntü, rötuşlama görüntüsü ve maske ile çalışabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Oluşturma sürecinde kullanılan temel model. | MODEL | Evet | - |
| `model_patch` | Kontrol ağının yönlendirmesini uygulayan özel bir yama modeli. | MODEL_PATCH | Evet | - |
| `vae` | Görüntüleri kodlamak ve kodunu çözmek için kullanılan Varyasyonel Otomatik Kodlayıcı. | VAE | Evet | - |
| `strength` | Kontrol ağının etkisinin gücü. Pozitif değerler efekti uygular, negatif değerler ise tersine çevirebilir (varsayılan: 1.0). | FLOAT | Evet | -10.0 to 10.0 |
| `image` | Oluşturma sürecini yönlendirmek için isteğe bağlı temel görüntü. | IMAGE | Hayır | - |
| `inpaint_image` | Bir maske tarafından tanımlanan alanları rötuşlamak için özel olarak kullanılan isteğe bağlı görüntü. | IMAGE | Hayır | - |
| `mask` | Bir görüntünün hangi alanlarının düzenleneceğini veya rötuşlanacağını tanımlayan isteğe bağlı maske. | MASK | Hayır | - |

**Not:** `inpaint_image` parametresi genellikle rötuşlama içeriğini belirtmek için bir `mask` ile birlikte kullanılır. Düğümün davranışı, hangi isteğe bağlı girdilerin sağlandığına bağlı olarak değişebilir (ör. yönlendirme için `image` kullanmak veya rötuşlama için `image`, `mask` ve `inpaint_image` kullanmak).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Kontrol ağı yaması uygulanmış, örnekleme hattında kullanıma hazır model. | MODEL |
| `positive` | Kontrol ağı girdileri tarafından potansiyel olarak değiştirilmiş pozitif koşullandırma. | CONDITIONING |
| `negative` | Kontrol ağı girdileri tarafından potansiyel olarak değiştirilmiş negatif koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/tr.md)

---
**Source fingerprint (SHA-256):** `e1946190a06c52dd951078d9cb753962081957cb6c38accdea26eb4129a51793`
