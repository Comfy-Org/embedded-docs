# LTXVLatentUpsampler

LTXVLatentUpsampler düğümü, bir video gizli temsilinin uzamsal çözünürlüğünü iki katına çıkarır. Gizli verileri işlemek için özel bir yükseltme modeli kullanır; bu veriler, sağlanan VAE'nin kanal istatistikleri kullanılarak önce normalizasyondan geçirilir ve ardından yeniden normalize edilir. Bu düğüm, gizli uzaydaki video iş akışları için tasarlanmıştır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `örnekler` | Yükseltilecek videonun girdi gizli temsili. | LATENT | Evet |  |
| `büyütme_modeli` | Gizli veriler üzerinde 2 kat yükseltme işlemini gerçekleştirmek için kullanılan yüklenmiş model. | LATENT_UPSCALE_MODEL | Evet |  |
| `vae` | Yükseltmeden önce girdi gizli değişkenlerinin normalizasyonunu kaldırmak ve yükseltme sonrasında çıktı gizli değişkenlerini normalize etmek için kullanılan VAE modeli. | VAE | Evet |  |

Not: Bu düğüm ComfyUI'de deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Uzamsal boyutları girdiye kıyasla iki katına çıkarılmış, yükseltilmiş gizli temsil. Çıktı gizli değişkeni, girdiyle aynı parti boyutuna, kanal sayısına ve zamansal uzunluğa sahiptir. Girdide bulunan `noise_mask` (varsa) çıktıdan kaldırılır. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/tr.md)

---
**Source fingerprint (SHA-256):** `7d7f0b733cb3758e9ec985cac30134d719b130b5b86c35bfdd14576a5b4575db`
