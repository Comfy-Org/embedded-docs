# PiD Koşullandırma

Bir latent görüntüyü ve bir degrade sigma değerini bir CONDITIONING verisine ekler. Bu, PiD (Pixel-in-Detail) kod çözme veya yükseltme için kullanılır ve latentin işlenmeden önce ne kadar bozulacağını kontrol etmenizi sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `pozitif` | Latent ve degrade sigma'nın ekleneceği conditioning verisi. | CONDITIONING | Evet | - |
| `latent` | Conditioning'e eklenecek latent (VAEEncode veya bir KSampler'dan). | LATENT | Evet | - |
| `latent_format` | Latent'in formatı. Flux1 (16-kanal) ve Flux2 (128-kanal) latentleri, "flux" altında kanal boyutundan otomatik algılanır. SD3 (16-kanal), SDXL (4-kanal) veya QwenImage (16-kanal) için manuel seçim yapın (varsayılan: "flux"). | COMBO | Evet | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | Uygulanacak bozulma miktarı. 0, temiz bir latent anlamına gelir. Bozuk latent çıktılarını gidermek için bu değeri artırın (varsayılan: 0.0). | FLOAT | Evet | 0.0 ile 1.0 (adım: 0.01) |

Not: `latent_format` "flux" olarak ayarlandığında, düğüm latent türünü kanal boyutundan otomatik olarak algılar: 128 kanal Flux2 latentleri olarak, 16 kanal ise Flux1 latentleri olarak işlenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `CONDITIONING` | Latent ve degrade sigma değerleri eklenmiş orijinal conditioning verisi. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
