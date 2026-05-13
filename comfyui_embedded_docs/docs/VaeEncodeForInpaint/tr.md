> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeForInpaint/tr.md)

Bu düğüm, görüntüleri iç boyama (inpainting) görevlerine uygun bir gizli temsile (latent representation) kodlamak için tasarlanmış olup, VAE modeli tarafından optimum kodlama için giriş görüntüsünü ve maskesini ayarlamak üzere ek ön işleme adımlarını içerir.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `pixels`  | `IMAGE`     | Kodlanacak giriş görüntüsü. Bu görüntü, kodlamadan önce VAE modelinin beklenen giriş boyutlarına uyacak şekilde ön işleme ve yeniden boyutlandırmaya tabi tutulur. |
| `vae`     | VAE       | Görüntüyü gizli temsiline (latent representation) kodlamak için kullanılan VAE modeli. Dönüşüm sürecinde kritik bir rol oynar ve çıktı gizli uzayının (latent space) kalitesini ve özelliklerini belirler. |
| `mask`    | `MASK`      | Giriş görüntüsünün iç boyanacak bölgelerini belirten bir maske. Kodlamadan önce görüntüyü değiştirmek için kullanılır ve VAE'nin ilgili alanlara odaklanmasını sağlar. |
| `grow_mask_by` | `INT` | Gizli uzayda (latent space) kesintisiz geçişler sağlamak için iç boyama maskesinin ne kadar genişletileceğini belirtir. Daha büyük bir değer, iç boyamadan etkilenen alanı artırır. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Çıktı, görüntünün kodlanmış gizli temsilini (latent representation) ve bir gürültü maskesini (noise mask) içerir; her ikisi de sonraki iç boyama görevleri için kritik öneme sahiptir. |