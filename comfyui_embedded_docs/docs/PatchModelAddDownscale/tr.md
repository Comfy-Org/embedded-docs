> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/tr.md)

PatchModelAddDownscale düğümü, bir modeldeki belirli bloklara küçültme ve büyütme işlemleri uygulayarak Kohya Deep Shrink işlevselliğini gerçekleştirir. İşleme sırasında ara özelliklerin çözünürlüğünü azaltır ve ardından orijinal boyutlarına geri yükler; bu da kaliteyi korurken performansı artırabilir. Düğüm, bu ölçekleme işlemlerinin modelin yürütülmesi sırasında ne zaman ve nasıl gerçekleşeceği üzerinde hassas kontrol sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Küçültme yamasının uygulanacağı model |
| `blok_numarası` | INT | Hayır | 1-32 | Küçültmenin uygulanacağı belirli blok numarası (varsayılan: 3) |
| `küçültme_faktörü` | FLOAT | Hayır | 0.1-9.0 | Özelliklerin küçültüleceği faktör (varsayılan: 2.0) |
| `başlangıç_yüzdesi` | FLOAT | Hayır | 0.0-1.0 | Gürültü giderme işleminde küçültmenin başladığı başlangıç noktası (varsayılan: 0.0) |
| `bitiş_yüzdesi` | FLOAT | Hayır | 0.0-1.0 | Gürültü giderme işleminde küçültmenin durduğu bitiş noktası (varsayılan: 0.35) |
| `atlamadan_sonra_küçült` | BOOLEAN | Hayır | - | Atlama bağlantılarından sonra küçültme uygulanıp uygulanmayacağı (varsayılan: True) |
| `küçültme_yöntemi` | COMBO | Hayır | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | Küçültme işlemleri için kullanılan enterpolasyon yöntemi |
| `büyütme_yöntemi` | COMBO | Hayır | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | Büyütme işlemleri için kullanılan enterpolasyon yöntemi |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Küçültme yaması uygulanmış değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `93ece77ad2dce3c1cdd554583ae1f2e6be51a43ab072d408869dddbcc7798c40`
