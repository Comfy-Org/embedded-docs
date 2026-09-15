# LCM Büyütme Örnekleyici

Bu düğüm, Latent Consistency Model (LCM) örneklemesini aşamalı görüntü büyütme ile birleştiren özelleştirilmiş bir örnekleme yöntemi sunar. Örnekleme sırasında görüntü, seçilen bir interpolasyon yöntemi kullanılarak hedef ölçek oranına doğru adım adım büyütülür; bu da tek bir örnekleme geçişinde daha yüksek çözünürlüklü sonuçlar elde edilmesini sağlar. Düğüm, bir örnekleme düğümüne bağlanabilen yapılandırılmış bir örnekleyici nesnesi verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `ölçek_oranı` | Büyütme sırasında uygulanacak toplam ölçekleme faktörü. 1.0 değeri orijinal çözünürlüğü korur (varsayılan: 1.0) | FLOAT | Evet | 0.1 - 20.0 |
| `ölçek_adımları` | Büyütme işlemi için kullanılacak adım sayısı. Örnekleme çizelgesine göre otomatik hesaplama için -1 kullanın (varsayılan: -1) | INT | Evet | -1 - 1000 |
| `büyütme_yöntemi` | Her büyütme adımında görüntüyü büyütmek için kullanılan interpolasyon yöntemi (varsayılan: "bislerp") | COMBO | Evet | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

`scale_ratio` ve `scale_steps` gelişmiş parametrelerdir. Görüntü, büyütme adımları boyunca orijinal boyutundan hedef `scale_ratio` değerine kademeli olarak büyütülür. `scale_steps` -1 olduğunda, büyütme adımlarının sayısı otomatik olarak örnekleme adımlarının sayısının yaklaşık yarısı kadar hesaplanır ve en az 2 olur; pozitif bir değer verildiğinde ise düğüm bunu dahili olarak ayarlar ve toplam örnekleme adımı sayısına göre sınırlar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Aşamalı büyütme ile LCM örneklemesi gerçekleştiren ve örnekleme hattında kullanılmaya hazır, yapılandırılmış bir örnekleyici nesnesi | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/tr.md)

---
**Source fingerprint (SHA-256):** `5d6f6472fbb4d2c66a8a8b9d6dc34dcc52ac8272589fd6c29e4084d6cab3141b`
