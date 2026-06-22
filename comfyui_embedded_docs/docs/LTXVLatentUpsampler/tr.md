# LTXVLatentUpsampler

LTXVLatentUpsampler düğümü, bir video gizli temsilinin uzamsal çözünürlüğünü iki katına çıkarır. Gizli verileri işlemek için özel bir yükseltme modeli kullanır; bu veriler önce normalleştirmeden çıkarılır, ardından sağlanan VAE'nin kanal istatistikleri kullanılarak yeniden normalleştirilir. Bu düğüm, gizli uzaydaki video iş akışları için tasarlanmıştır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `örnekler` | Yükseltilecek videonun giriş gizli temsili. | LATENT | Evet |  |
| `büyütme_modeli` | Gizli veriler üzerinde 2 kat yükseltme işlemini gerçekleştirmek için kullanılan yüklenmiş model. | LATENT_UPSCALE_MODEL | Evet |  |
| `vae` | Yükseltmeden önce giriş gizli verilerini normalleştirmeden çıkarmak ve sonrasında çıkış gizli verilerini normalleştirmek için kullanılan VAE modeli. | VAE | Evet |  |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Uzamsal boyutları girişe kıyasla iki katına çıkarılmış, yükseltilmiş gizli temsil. Çıkış gizli verisi, girişle aynı grup boyutuna, kanal sayısına ve zamansal uzunluğa sahiptir. Varsa girişteki `noise_mask`, çıkıştan kaldırılır. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/tr.md)

---
**Source fingerprint (SHA-256):** `b2c726d3a3e4881eee7e1d3bae8c478adf01cd87a9652be882579f4e26c1536f`
