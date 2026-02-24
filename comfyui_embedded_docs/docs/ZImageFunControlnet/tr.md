> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/tr.md)

ZImageFunControlnet düğümü, görüntü oluşturma veya düzenleme sürecini etkilemek için özelleştirilmiş bir kontrol ağı uygular. Bir temel model, bir model yaması ve bir VAE kullanarak kontrol etkisinin gücünü ayarlamanıza olanak tanır. Bu düğüm, daha hedefli düzenlemeler için bir temel görüntü, bir boyama görüntüsü ve bir maske ile çalışabilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Oluşturma süreci için kullanılan temel model. |
| `model_patch` | MODEL_PATCH | Evet | - | Kontrol ağının rehberliğini uygulayan özelleştirilmiş bir yama modeli. |
| `vae` | VAE | Evet | - | Görüntüleri kodlamak ve kodunu çözmek için kullanılan Varyasyonel Otokodlayıcı. |
| `strength` | FLOAT | Evet | -10.0 ile 10.0 | Kontrol ağının etki gücü. Pozitif değerler efekti uygular, negatif değerler ise tersine çevirebilir (varsayılan: 1.0). |
| `image` | IMAGE | Hayır | - | Oluşturma sürecini yönlendirmek için isteğe bağlı bir temel görüntü. |
| `inpaint_image` | IMAGE | Hayır | - | Bir maske ile tanımlanan alanları boyamak için özel olarak kullanılan isteğe bağlı bir görüntü. |
| `mask` | MASK | Hayır | - | Bir görüntünün hangi alanlarının düzenleneceğini veya boyanacağını tanımlayan isteğe bağlı bir maske. |

**Not:** `inpaint_image` parametresi genellikle, boyama için içeriği belirtmek üzere bir `mask` ile birlikte kullanılır. Düğümün davranışı, hangi isteğe bağlı girdilerin sağlandığına bağlı olarak değişebilir (örneğin, rehberlik için `image` kullanmak veya boyama için `image`, `mask` ve `inpaint_image` kullanmak).

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Kontrol ağı yaması uygulanmış, örnekleme işlem hattında kullanıma hazır model. |
| `positive` | CONDITIONING | Kontrol ağı girdileri tarafından potansiyel olarak değiştirilmiş pozitif koşullandırma. |
| `negative` | CONDITIONING | Kontrol ağı girdileri tarafından potansiyel olarak değiştirilmiş negatif koşullandırma. |
