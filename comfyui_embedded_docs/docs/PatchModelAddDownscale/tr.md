# Model Yaması Ekle Küçültme (Kohya Deep Shrink)

PatchModelAddDownscale düğümü, modeldeki belirli bloklara küçültme ve büyütme işlemleri uygulayarak Kohya Deep Shrink işlevini gerçekleştirir. İşlem sırasında ara özelliklerin çözünürlüğünü azaltır ve ardından bunları orijinal boyutlarına geri yükler; bu sayede kalite korunurken performans iyileştirilebilir. Düğüm, bu ölçekleme işlemlerinin modelin yürütülmesi sırasında ne zaman ve nasıl gerçekleşeceği üzerinde hassas kontrol sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Küçültme yamasının uygulanacağı model | MODEL | Evet | - |
| `block_number` | Küçültmenin uygulanacağı belirli blok numarası (varsayılan: 3) | INT | Hayır | 1-32 |
| `downscale_factor` | Özelliklerin küçültüleceği faktör (varsayılan: 2.0) | FLOAT | Hayır | 0.1-9.0 |
| `start_percent` | Küçültmenin başladığı gürültü giderme sürecindeki başlangıç noktası (varsayılan: 0.0) | FLOAT | Hayır | 0.0-1.0 |
| `end_percent` | Küçültmenin durduğu gürültü giderme sürecindeki bitiş noktası (varsayılan: 0.35) | FLOAT | Hayır | 0.0-1.0 |
| `downscale_after_skip` | Atlamalı bağlantılardan sonra küçültme uygulanıp uygulanmayacağı (varsayılan: True) | BOOLEAN | Hayır | - |
| `downscale_method` | Küçültme işlemleri için kullanılan interpolasyon yöntemi | COMBO | Hayır | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `upscale_method` | Büyütme işlemleri için kullanılan interpolasyon yöntemi | COMBO | Hayır | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Küçültme yaması uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/tr.md)

---
**Source fingerprint (SHA-256):** `aa9434a521ab585b290a3bd8db804469bd3bb02103a0d830b6be6eb8e8c26a5e`
