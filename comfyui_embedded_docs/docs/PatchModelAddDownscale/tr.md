> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/tr.md)

PatchModelAddDownscale düğümü, Kohya Deep Shrink işlevselliğini bir modeldeki belirli bloklara küçültme ve büyütme işlemleri uygulayarak gerçekleştirir. İşlem sırasında ara özelliklerin çözünürlüğünü düşürür ve ardından bunları orijinal boyutuna geri getirir, bu da kaliteyi korurken performansı iyileştirebilir. Düğüm, modelin yürütülmesi sırasında bu ölçeklendirme işlemlerinin ne zaman ve nasıl gerçekleşeceği üzerinde hassas kontrol sağlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Küçültme yaması uygulanacak model |
| `blok_numarası` | INT | Hayır | 1-32 | Küçültmenin uygulanacağı belirli blok numarası (varsayılan: 3) |
| `küçültme_faktörü` | FLOAT | Hayır | 0.1-9.0 | Özelliklerin küçültüleceği faktör (varsayılan: 2.0) |
| `başlangıç_yüzdesi` | FLOAT | Hayır | 0.0-1.0 | Küçültmenin başladığı gürültü giderme işlemi başlangıç noktası (varsayılan: 0.0) |
| `bitiş_yüzdesi` | FLOAT | Hayır | 0.0-1.0 | Küçültmenin durduğu gürültü giderme işlemi bitiş noktası (varsayılan: 0.35) |
| `atlamadan_sonra_küçült` | BOOLEAN | Hayır | - | Atlama bağlantılarından sonra küçültme uygulanıp uygulanmayacağı (varsayılan: True) |
| `küçültme_yöntemi` | COMBO | Hayır | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | Küçültme işlemleri için kullanılan enterpolasyon yöntemi |
| `büyütme_yöntemi` | COMBO | Hayır | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | Büyütme işlemleri için kullanılan enterpolasyon yöntemi |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Küçültme yaması uygulanmış değiştirilmiş model |