# LCM Büyütme Örnekleyici

SamplerLCMUpscale düğümü, Gizli Tutarlılık Modeli (LCM) örneklemesini görüntü büyütme yetenekleriyle birleştiren özel bir örnekleme yöntemi sunar. Çeşitli enterpolasyon yöntemleri kullanarak örnekleme işlemi sırasında görüntüleri büyütmenize olanak tanır; bu da görüntü kalitesini korurken daha yüksek çözünürlüklü çıktılar üretmek için kullanışlıdır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ölçek_oranı` | Büyütme sırasında uygulanacak ölçekleme faktörü (varsayılan: 1.0) | FLOAT | Hayır | 0.1 - 20.0 |
| `ölçek_adımları` | Büyütme işlemi için kullanılacak adım sayısı. Otomatik hesaplama için -1 kullanın (varsayılan: -1) | INT | Hayır | -1 - 1000 |
| `büyütme_yöntemi` | Görüntüyü büyütmek için kullanılan enterpolasyon yöntemi | COMBO | Evet | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Örnekleme hattında kullanılabilecek yapılandırılmış bir örnekleyici nesnesi döndürür | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/tr.md)

---
**Source fingerprint (SHA-256):** `fe0d4c8676454a9e8ecf4bb4e149c9b5e22083322447749116d624984d75e73c`
