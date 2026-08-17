# PiD Koşullandırma

Bir CONDITIONING verisine bir latent görüntü ve bir bozulma sigma değeri ekler. Bu, PiD (Pixel-in-Detail) kod çözme veya yükseltme için kullanılır ve işlemden önce latentin ne kadar bozulacağını kontrol etmenizi sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `positive` | Latent ve bozulma sigma değerinin ekleneceği conditioning verisi. | CONDITIONING | Evet | - |
| `latent` | Conditioning'e eklenecek latent görüntü (VAEEncode veya bir KSampler'dan). | LATENT | Evet | - |
| `latent_format` | Latentin formatı. Flux1 (16 kanallı) ve Flux2 (128 kanallı) latentler, "flux" altındaki kanal boyutundan otomatik olarak algılanır. SD3 (16 kanallı), SDXL (4 kanallı) veya QwenImage (16 kanallı) için manuel olarak seçin (varsayılan: "flux"). | COMBO | Evet | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | 0 = temiz latent. Bozulmuş latent çıktılarını gidermek için artırın (varsayılan: 0.0). | FLOAT | Evet | 0.0 ila 1.0 (adım: 0.01) |

Not: `latent_format` "flux" olduğunda, düğüm latentin Flux1 (16 kanal) mı yoksa Flux2 (128 kanal) mı olduğunu kanal boyutuna göre otomatik olarak algılar. İşlenen latent 5 boyutluysa, yalnızca son boyut boyunca ilk dilim kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `CONDITIONING` | Orijinal conditioning verisi, üzerine latent ve bozulma sigma değerleri eklenmiş halde. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
