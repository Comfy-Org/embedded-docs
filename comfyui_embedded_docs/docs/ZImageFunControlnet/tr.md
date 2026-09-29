# ZImageFunControlnet

ZImageFunControlnet, görüntü oluşturma veya düzenleme sürecine rehberlik edebilmesi için temel modele bir kontrol ağı yaması uygular. Bir modeli, bir model yamasını ve bir VAE'yi birleştirir ve kontrol etkisinin sonucu ne kadar güçlü etkileyeceğini denetlemenize olanak tanır. İsteğe bağlı görüntü, inpainting görüntüsü ve maske girdileri daha hedefli düzenlemelere izin verir. Düğüm, Z-Image ControlNet yamalarıyla ve Load Model Patch düğümü aracılığıyla yüklenen Qwen Image 2.1 Fun ControlNet yamalarıyla çalışır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Oluşturma süreci için kullanılan temel model. | MODEL | Evet | - |
| `model_patch` | Kontrol ağının rehberliğini uygulayan özelleşmiş yama modeli. | MODEL_PATCH | Evet | - |
| `vae` | Görüntüleri kodlamak ve kodunu çözmek için kullanılan VAE (Değişimsel Otomatik Kodlayıcı). | VAE | Evet | - |
| `güç` | Kontrol ağının etkisinin gücü. Pozitif değerler etkiyi uygular, negatif değerler ise tersine çevirebilir (varsayılan: 1.0). | FLOAT | Evet | -10.0 ila 10.0 (adım 0.01) |
| `görsel` | Oluşturma sürecine rehberlik etmek için isteğe bağlı temel görüntü. | IMAGE | Hayır | - |
| `boyanacak_görsel` | Bir maske tarafından tanımlanan alanlarda inpainting için özel olarak kullanılan isteğe bağlı görüntü. | IMAGE | Hayır | - |
| `mask` | Bir görüntünün hangi alanlarının düzenleneceğini veya inpainting yapılacağını tanımlayan isteğe bağlı maske. | MASK | Hayır | - |
| `start_percent` | Gürültü giderme sürecinde, toplam örnekleme adımlarının bir kesri olarak, kontrol ağının etkili olmaya başladığı nokta (varsayılan: 0.0). | FLOAT | Hayır | 0.0 ila 1.0 (adım 0.001) |
| `end_percent` | Gürültü giderme sürecinde kontrol ağının etkili olmayı bıraktığı nokta (varsayılan: 1.0). | FLOAT | Hayır | 0.0 ila 1.0 (adım 0.001) |

**Not:** `inpaint_image` parametresi tipik olarak, inpainting yapılacak içeriği belirtmek için bir `mask` ile birlikte kullanılır. Düğümün davranışı, hangi isteğe bağlı girdilerin sağlandığına bağlı olarak değişebilir (örn. rehberlik için `image` kullanmak veya inpainting için `image`, `mask` ve `inpaint_image` kullanmak). `start_percent` ve `end_percent` değerleri kontrol ağını gürültü giderme sürecinin bir penceresiyle sınırlar; bu pencerenin dışında model, yama olmadan örneklenir. `strength` 0 ise veya `image`, `inpaint_image` ve `mask` öğelerinden hiçbiri bağlı değilse, düğüm temel modeli değiştirmeden döndürür. Z-Image Control yamaları için sağlanan maske kullanılmadan önce ters çevrilir (1.0 - mask); Qwen Image 2.1 Fun ControlNet yaması ise maskeyi verildiği gibi kullanır. Bu düğüm deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Kontrol ağı yaması uygulanmış, örnekleme hattında kullanıma hazır model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/tr.md)

---
**Source fingerprint (SHA-256):** `9673b8b6e091713bcc93fe5fd1cfed12e6941571d1017e10ac94c19e1afd4ca1`
