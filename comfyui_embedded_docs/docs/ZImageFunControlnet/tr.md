# ZImageFunControlnet

ZImageFunControlnet, görüntü oluşturma veya düzenleme sürecine rehberlik edebilmesi için temel modele bir kontrol ağı yaması uygular. Bir modeli, bir model yamasını ve bir VAE'yi birleştirir ve kontrol etkisinin sonucu ne kadar güçlü etkileyeceğini denetlemenizi sağlar. İsteğe bağlı görüntü, iç boyama görüntüsü ve maske girdileri daha hedefli düzenlemelere olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Üretim süreci için kullanılan temel model. | MODEL | Evet | - |
| `model_patch` | Kontrol ağının rehberliğini uygulayan özelleşmiş yama modeli. | MODEL_PATCH | Evet | - |
| `vae` | Görüntüleri kodlamak ve kodunu çözmek için kullanılan Varyasyonel Otokodlayıcı (VAE). | VAE | Evet | - |
| `strength` | Kontrol ağının etkisinin gücü. Pozitif değerler etkiyi uygular, negatif değerler ise onu tersine çevirebilir (varsayılan: 1.0). | FLOAT | Evet | -10.0 ile 10.0 arası (adım 0.01) |
| `image` | Üretim sürecine rehberlik etmek için isteğe bağlı temel görüntü. | IMAGE | Hayır | - |
| `inpaint_image` | Bir maske tarafından tanımlanan alanların iç boyaması için özel olarak kullanılan isteğe bağlı görüntü. | IMAGE | Hayır | - |
| `mask` | Bir görüntünün hangi alanlarının düzenleneceğini veya iç boyanacağını tanımlayan isteğe bağlı maske. | MASK | Hayır | - |

**Not:** `inpaint_image` parametresi tipik olarak iç boyama için içeriği belirtmek üzere bir `mask` ile birlikte kullanılır. Düğümün davranışı, hangi isteğe bağlı girdilerin sağlandığına bağlı olarak değişebilir (örn. rehberlik için `image` kullanılması veya iç boyama için `image`, `mask` ve `inpaint_image` kullanılması).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Kontrol ağı yaması uygulanmış model; örnekleme hattında kullanıma hazır. | MODEL |
| `positive` | Kontrol ağı girdileri tarafından potansiyel olarak değiştirilmiş pozitif koşullandırma. | CONDITIONING |
| `negative` | Kontrol ağı girdileri tarafından potansiyel olarak değiştirilmiş negatif koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/tr.md)

---
**Source fingerprint (SHA-256):** `e1946190a06c52dd951078d9cb753962081957cb6c38accdea26eb4129a51793`
