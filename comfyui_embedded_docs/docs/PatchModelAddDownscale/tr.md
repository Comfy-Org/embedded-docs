# Model Yaması Ekle Küçültme (Kohya Deep Shrink)

PatchModelAddDownscale (Kohya Deep Shrink), seçilen bir bloktaki ara özellikleri küçültüp ardından orijinal boyutlarına geri ölçekleyerek Kohya Deep Shrink tekniğini bir modele uygular. Küçültme yalnızca gürültü giderme (denoising) sürecinin seçilen bir bölümünde gerçekleşir; bu, işlem maliyetini azaltırken nihai sonucu orijinaline yakın tutabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Ölçek küçültme yamasının uygulanacağı model | MODEL | Evet | - |
| `blok_numarası` | Ölçek küçültmenin uygulanacağı belirli blok numarası (varsayılan: 3) | INT | Evet | 1-32 |
| `küçültme_faktörü` | Özelliklerin ölçek küçültme faktörü (varsayılan: 2.0) | FLOAT | Evet | 0.1-9.0 |
| `başlangıç_yüzdesi` | Gürültü giderme sürecinde ölçek küçültmenin başladığı başlangıç noktası (varsayılan: 0.0) | FLOAT | Evet | 0.0-1.0 |
| `bitiş_yüzdesi` | Gürültü giderme sürecinde ölçek küçültmenin durduğu bitiş noktası (varsayılan: 0.35) | FLOAT | Evet | 0.0-1.0 |
| `atlamadan_sonra_küçült` | Ölçek küçültmenin atlama bağlantılarından sonra uygulanıp uygulanmayacağı (varsayılan: True) | BOOLEAN | Evet | - |
| `küçültme_yöntemi` | Ölçek küçültme işlemleri için kullanılan interpolasyon yöntemi (varsayılan: "bicubic") | COMBO | Evet | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `büyütme_yöntemi` | Ölçek büyütme işlemleri için kullanılan interpolasyon yöntemi (varsayılan: "bicubic") | COMBO | Evet | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

Ölçek küçültme yaması yalnızca geçerli gürültü giderme adımı `start_percent` ve `end_percent` tarafından tanımlanan aralığa girdiğinde ve yalnızca `block_number` ile seçilen blokta uygulanır. `downscale_after_skip` etkinleştirildiğinde yama atlama bağlantısından sonra uygulanır; devre dışı bırakıldığında atlama bağlantısından önce uygulanır. Özellikler daha sonra orijinal boyutlarına geri ölçeklenir, ancak yalnızca geçerli özellik boyutu ölçek küçültmeden önce kaydedilen boyutla artık eşleşmediğinde.

`block_number`, `start_percent`, `end_percent` ve `downscale_after_skip` parametreleri düğüm arayüzünde gelişmiş seçenekler olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Ölçek küçültme yaması uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/tr.md)

---
**Source fingerprint (SHA-256):** `aa9434a521ab585b290a3bd8db804469bd3bb02103a0d830b6be6eb8e8c26a5e`
