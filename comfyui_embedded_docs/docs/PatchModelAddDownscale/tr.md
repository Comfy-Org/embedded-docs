> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/tr.md)

PatchModelAddDownscale düğümü, Kohya Deep Shrink işlevselliğini bir modeldeki belirli bloklara küçültme ve büyütme işlemleri uygulayarak gerçekleştirir. İşlem sırasında ara özelliklerin çözünürlüğünü düşürür ve ardından bunları orijinal boyutuna geri getirir, bu da kaliteyi korurken performansı iyileştirebilir. Düğüm, modelin yürütülmesi sırasında bu ölçeklendirme işlemlerinin ne zaman ve nasıl gerçekleşeceği üzerinde hassas kontrol sağlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Küçültme yaması uygulanacak model |
| `block_number` | INT | Hayır | 1-32 | Küçültmenin uygulanacağı belirli blok numarası (varsayılan: 3) |
| `downscale_factor` | FLOAT | Hayır | 0.1-9.0 | Özelliklerin küçültüleceği faktör (varsayılan: 2.0) |
| `start_percent` | FLOAT | Hayır | 0.0-1.0 | Küçültmenin başladığı gürültü giderme işlemi başlangıç noktası (varsayılan: 0.0) |
| `end_percent` | FLOAT | Hayır | 0.0-1.0 | Küçültmenin durduğu gürültü giderme işlemi bitiş noktası (varsayılan: 0.35) |
| `downscale_after_skip` | BOOLEAN | Hayır | - | Atlama bağlantılarından sonra küçültme uygulanıp uygulanmayacağı (varsayılan: True) |
| `downscale_method` | COMBO | Hayır | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | Küçültme işlemleri için kullanılan enterpolasyon yöntemi |
| `upscale_method` | COMBO | Hayır | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | Büyütme işlemleri için kullanılan enterpolasyon yöntemi |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Küçültme yaması uygulanmış değiştirilmiş model |