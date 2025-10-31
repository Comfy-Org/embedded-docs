> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeForInpaint/tr.md)

Bu düğüm, görüntüleri, giriş görüntüsünü ve maskeyi VAE modeli tarafından optimal kodlama için ayarlamak üzere ek ön işleme adımları içeren, inpaintleme görevleri için uygun bir latent temsile kodlamak üzere tasarlanmıştır.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `pixels`  | `IMAGE`     | Kodlanacak giriş görüntüsü. Bu görüntü, kodlamadan önce VAE modelinin beklenen giriş boyutlarına uyacak şekilde ön işleme ve yeniden boyutlandırmaya tabi tutulur. |
| `vae`     | VAE       | Görüntüyü latent temsiline kodlamak için kullanılan VAE modeli. Dönüşüm sürecinde çok önemli bir rol oynar ve çıktı latent uzayının kalitesini ve özelliklerini belirler. |
| `mask`    | `MASK`      | Giriş görüntüsünün inpaintlenecek bölgelerini gösteren bir maske. Kodlamadan önce görüntüyü değiştirmek için kullanılır ve VAE'nin ilgili alanlara odaklanmasını sağlar. |
| `grow_mask_by` | `INT` | Latent uzayda kesintisiz geçişler sağlamak için inpaintleme maskesinin ne kadar genişletileceğini belirtir. Daha büyük bir değer, inpaintlemeden etkilenen alanı artırır. |

## Çıktılar

| Parametre | Veri Türu | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Çıktı, görüntünün kodlanmış latent temsilini ve sonraki inpaintleme görevleri için çok önemli olan bir gürültü maskesini içerir. |