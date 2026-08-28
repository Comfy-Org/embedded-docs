# LCM Büyütme Örnekleyici

SamplerLCMUpscale düğümü, Latent Tutarlılık Modeli (LCM) örneklemeyi görüntü yükseltme yetenekleriyle birleştiren özel bir örnekleme yöntemi sağlar. Örnekleme süreci sırasında görüntüyü çeşitli enterpolasyon yöntemleri kullanarak kademeli olarak yükseltir ve tek bir örnekleme geçişinde daha yüksek çözünürlüklü çıktıların üretilmesine olanak tanır. Çıktı, bir örnekleme düğümüne bağlanabilen yapılandırılmış bir örnekleyici nesnesidir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `ölçek_oranı` | Yükseltme sırasında uygulanacak toplam ölçekleme faktörü. 1.0 değeri orijinal çözünürlüğü korur (varsayılan: 1.0) | FLOAT | Evet | 0.1 - 20.0 |
| `ölçek_adımları` | Yükseltme süreci için kullanılacak adım sayısı. Örnekleme takvimine dayalı otomatik hesaplama için -1 kullanın (varsayılan: -1) | INT | Evet | -1 - 1000 |
| `büyütme_yöntemi` | Her yükseltme adımında görüntüyü yükseltmek için kullanılan enterpolasyon yöntemi (varsayılan: "bislerp") | COMBO | Evet | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

`scale_ratio` ve `scale_steps` gelişmiş parametrelerdir. Görüntü, yükseltme adımları boyunca orijinal boyutundan hedef `scale_ratio` değerine kademeli olarak yükseltilir. `scale_steps` -1 olduğunda, yükseltme adım sayısı örnekleme adım sayısının yaklaşık yarısı olacak şekilde otomatik hesaplanır ve minimum 2'dir; pozitif bir değer verildiğinde, düğüm bunu dahili olarak ayarlar ve toplam örnekleme adım sayısına göre sınırlar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | LCM örneklemesini kademeli yükseltme ile gerçekleştiren, örnekleme hattında kullanılmaya hazır, yapılandırılmış bir örnekleyici nesnesi | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/tr.md)

---
**Source fingerprint (SHA-256):** `5d6f6472fbb4d2c66a8a8b9d6dc34dcc52ac8272589fd6c29e4084d6cab3141b`
