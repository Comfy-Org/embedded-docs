# LTXVLatentUpsampler

LTXVLatentUpsampler düğümü, bir video latent temsilinin uzamsal çözünürlüğünü iki katına çıkarır. Latent verilerini işlemek için özel bir upscale modeli kullanır; veriler önce denormalize edilir, ardından sağlanan VAE'nin kanal istatistikleri kullanılarak yeniden normalize edilir. Bu düğüm, latent uzaydaki video iş akışları için tasarlanmıştır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `samples` | Ölçek büyütülecek videonun girdi latent temsili. | LATENT | Evet |  |
| `upscale_model` | Latent verileri üzerinde 2 kat ölçek büyütme gerçekleştirmek için kullanılan yüklenmiş model. | LATENT_UPSCALE_MODEL | Evet |  |
| `vae` | Ölçek büyütmeden önce girdi latentlerini denormalize etmek ve ardından çıktı latentlerini normalize etmek için kullanılan VAE modeli. | VAE | Evet |  |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Girdiye kıyasla uzamsal boyutları iki katına çıkarılmış, ölçek büyütülmüş latent temsil. Çıktı latentleri; girdiyle aynı batch boyutuna, kanal sayısına ve zamansal uzunluğa sahiptir ve girdi latentleriyle aynı veri türüne geri dönüştürülür. Girdideki `noise_mask` (varsa) çıktıdan kaldırılır. | LATENT |

Not: Bu düğüm deneysel olarak işaretlenmiştir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/tr.md)

---
**Source fingerprint (SHA-256):** `7d7f0b733cb3758e9ec985cac30134d719b130b5b86c35bfdd14576a5b4575db`
