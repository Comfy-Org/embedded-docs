# ZImageFunControlnet

ZImageFunControlnet, görüntü oluşturma veya düzenleme sürecini etkilemek için özel bir kontrol ağı uygular. Kontrol etkisinin gücünü ayarlamanıza olanak tanıyan bir taban model, bir yama modeli ve bir VAE kullanır. Bu düğüm, daha hedefli düzenlemeler için bir taban görüntü, bir inpainting görüntüsü ve bir maske ile çalışabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Oluşturma sürecinde kullanılan taban model. | MODEL | Evet | - |
| `model_patch` | Kontrol ağının yönlendirmesini uygulayan özel bir yama modeli. | MODEL_PATCH | Evet | - |
| `vae` | Görüntüleri kodlamak ve kodunu çözmek için kullanılan Varyasyonel Otomatik Kodlayıcı (VAE). | VAE | Evet | - |
| `güç` | Kontrol ağının etkisinin gücü. Pozitif değerler etkiyi uygular, negatif değerler ise etkiyi tersine çevirebilir (varsayılan: 1.0). | FLOAT | Evet | -10.0 ile 10.0 |
| `görsel` | Oluşturma sürecine yön vermek için kullanılan isteğe bağlı taban görüntü. | IMAGE | Hayır | - |
| `boyanacak_görsel` | Bir maske ile tanımlanan alanlara inpainting uygulamak için özel olarak kullanılan isteğe bağlı görüntü. | IMAGE | Hayır | - |
| `mask` | Bir görüntünün hangi alanlarının düzenleneceğini veya inpainting uygulanacağını tanımlayan isteğe bağlı maske. | MASK | Hayır | - |

**Not:** `inpaint_image` parametresi, inpainting için içeriği belirtmek amacıyla tipik olarak bir `mask` ile birlikte kullanılır. Düğümün davranışı, hangi isteğe bağlı girdilerin sağlandığına bağlı olarak değişebilir (örn. yönlendirme için `image` kullanımı veya inpainting için `image`, `mask` ve `inpaint_image` kullanımı).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Kontrol ağı yaması uygulanmış, örnekleme hattında kullanıma hazır model. | MODEL |
| `positive` | Kontrol ağı girdileri tarafından değiştirilmiş olabilen pozitif koşullandırma. | CONDITIONING |
| `negative` | Kontrol ağı girdileri tarafından değiştirilmiş olabilen negatif koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/tr.md)

---
**Source fingerprint (SHA-256):** `e1946190a06c52dd951078d9cb753962081957cb6c38accdea26eb4129a51793`
