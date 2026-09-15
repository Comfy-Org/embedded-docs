# PiD Koşullandırma

Bir CONDITIONING'e, PiD kod çözme veya ölçekleme için kullanılabilecek şekilde bir latent ve bir `degrade_sigma` değeri ekler. Bu, latentin işlenmeden önce ne kadar bozulacağını kontrol etmenizi sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `pozitif` | `latent` ve `degrade_sigma` değerlerinin ekleneceği koşullandırma verisi. | CONDITIONING | Evet | - |
| `latent` | Koşullandırmaya eklenecek latent (VAEEncode veya bir KSampler'dan). | LATENT | Evet | - |
| `latent_format` | Latentin biçimi. Flux1 (16 kanal) ve Flux2 (128 kanal) latentleri, "flux" altında kanal boyutundan otomatik algılanır. SD3 (16 kanal), SDXL (4 kanal) veya QwenImage (16 kanal) için manuel olarak seçin (varsayılan: "flux"). | COMBO | Evet | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | Uygulanacak bozulma miktarı. 0, temiz bir latent anlamına gelir. Bozulmuş latent çıktılarının gürültüsünü gidermek için bu değeri artırın (varsayılan: 0.0). | FLOAT | Evet | 0.0 ile 1.0 (adım: 0.01) |

Not: `latent_format` değeri `"flux"` olarak ayarlandığında, düğüm latent türünü kanal boyutundan otomatik algılar: 128 kanal Flux2 latent olarak, 16 kanal ise Flux1 latent olarak işlenir.

Not: Desteklenmeyen bir `latent_format` değeri hata verir, ancak mevcut tüm seçenekler düğüm tarafından işlenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `CONDITIONING` | `latent` ve `degrade_sigma` değeri eklenmiş orijinal koşullandırma verisi. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
