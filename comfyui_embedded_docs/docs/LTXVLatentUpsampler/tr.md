# LTXVLatentUpsampler

LTXVLatentUpsampler düğümü, bir video latent temsilinin uzamsal çözünürlüğünü iki katına çıkarır. Latent verisini işlemek için özel bir büyütme modeli kullanır; bu veri önce normalizasyondan çıkarılır ve ardından sağlanan VAE'nin kanal istatistikleri kullanılarak yeniden normalize edilir. Bu düğüm, latent uzayı içindeki video iş akışları için tasarlanmıştır.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `samples` | Büyütülecek videonun girdi latent temsili. | LATENT | Evet |  |
| `upscale_model` | Latent verisi üzerinde 2x büyütme gerçekleştirmek için kullanılan yüklenmiş model. | LATENT_UPSCALE_MODEL | Evet |  |
| `vae` | Büyütmeden önce girdi latentlerini normalizasyondan çıkarmak ve sonrasında çıktı latentlerini normalize etmek için kullanılan VAE modeli. | VAE | Evet |  |

Not: Bu düğüm ComfyUI'de deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `LATENT` | Girdiye kıyasla uzamsal boyutları iki katına çıkarılmış latent temsili. Çıktı latent, girdiyle aynı batch boyutuna, kanal sayısına ve zamansal uzunluğa sahiptir. Girdide varsa `noise_mask` çıktıdan kaldırılır. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/tr.md)

---
**Source fingerprint (SHA-256):** `7d7f0b733cb3758e9ec985cac30134d719b130b5b86c35bfdd14576a5b4575db`
