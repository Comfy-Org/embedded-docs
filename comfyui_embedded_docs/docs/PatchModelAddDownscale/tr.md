# Model Yaması Ekle Küçültme (Kohya Deep Shrink)

PatchModelAddDownscale (Kohya Deep Shrink), bir modeldeki belirli bloklara küçültme ve büyütme işlemleri uygulayarak Kohya Deep Shrink tekniğini uygular. İşleme sırasında ara özelliklerin çözünürlüğünü düşürür ve ardından bunları orijinal boyutlarına geri getirir; bu da kaliteyi korurken performansı artırabilir. Düğüm, bu ölçekleme işlemlerinin modelin çalıştırılması sırasında ne zaman ve nasıl gerçekleşeceği üzerinde hassas kontrol sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Küçültme yamasının uygulanacağı model | MODEL | Evet | - |
| `blok_numarası` | Küçültmenin uygulanacağı belirli blok numarası (varsayılan: 3) | INT | Evet | 1-32 |
| `küçültme_faktörü` | Özelliklerin küçültüleceği faktör (varsayılan: 2.0) | FLOAT | Evet | 0.1-9.0 |
| `başlangıç_yüzdesi` | Küçültmenin başladığı gürültü giderme sürecindeki başlangıç noktası (varsayılan: 0.0) | FLOAT | Evet | 0.0-1.0 |
| `bitiş_yüzdesi` | Küçültmenin durduğu gürültü giderme sürecindeki bitiş noktası (varsayılan: 0.35) | FLOAT | Evet | 0.0-1.0 |
| `atlamadan_sonra_küçült` | Atlamalı bağlantılardan sonra küçültme uygulanıp uygulanmayacağı (varsayılan: True) | BOOLEAN | Evet | - |
| `küçültme_yöntemi` | Küçültme işlemleri için kullanılan enterpolasyon yöntemi | COMBO | Evet | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `büyütme_yöntemi` | Büyütme işlemleri için kullanılan enterpolasyon yöntemi | COMBO | Evet | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

Küçültme yaması, yalnızca geçerli gürültü giderme adımı `start_percent` ve `end_percent` tarafından tanımlanan aralık içinde olduğunda ve yalnızca `block_number` tarafından seçilen blokta uygulanır. `downscale_after_skip` etkinleştirildiğinde, yama atlamalı bağlantıdan sonra uygulanır; devre dışı bırakıldığında, atlamalı bağlantıdan önce uygulanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Küçültme yaması uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/tr.md)

---
**Source fingerprint (SHA-256):** `aa9434a521ab585b290a3bd8db804469bd3bb02103a0d830b6be6eb8e8c26a5e`
