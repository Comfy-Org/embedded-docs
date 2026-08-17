# LCM Büyütme Örnekleyici

SamplerLCMUpscale düğümü, Latent Consistency Model (LCM) örneklemeyi görüntü yükseltme yetenekleriyle birleştiren özel bir örnekleme yöntemi sağlar. Örnekleme süreci sırasında çeşitli enterpolasyon yöntemleri kullanarak görüntüleri yükseltmenize olanak tanır; bu da görüntü kalitesini korurken daha yüksek çözünürlüklü çıktılar üretmek için kullanışlıdır. Yükseltme, hedef `scale_ratio` değerine ulaşılana kadar örnekleme adımları boyunca kademeli olarak uygulanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `scale_ratio` | Yükseltme sırasında uygulanacak ölçek faktörü (varsayılan: 1.0) | FLOAT | Hayır | 0.1 - 20.0 |
| `scale_steps` | Yükseltme işlemi için kullanılacak adım sayısı. Otomatik hesaplama için -1 kullanın (varsayılan: -1) | INT | Hayır | -1 - 1000 |
| `upscale_method` | Görüntüyü yükseltmek için kullanılan enterpolasyon yöntemi (varsayılan: bislerp) | COMBO | Evet | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

Not: `scale_steps` pozitif bir değere ayarlandığında, etkin yükseltme adım sayısı, örnekleyicinin toplam örnekleme adım sayısıyla sınırlıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Örnekleme hattında kullanılabilen yapılandırılmış bir örnekleyici nesnesi döndürür | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/tr.md)

---
**Source fingerprint (SHA-256):** `5d6f6472fbb4d2c66a8a8b9d6dc34dcc52ac8272589fd6c29e4084d6cab3141b`
