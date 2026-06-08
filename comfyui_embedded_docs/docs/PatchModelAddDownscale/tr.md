PatchModelAddDownscale düğümü, bir modeldeki belirli bloklara küçültme ve büyütme işlemleri uygulayarak Kohya Deep Shrink işlevselliğini gerçekleştirir. İşleme sırasında ara özelliklerin çözünürlüğünü azaltır ve ardından orijinal boyutlarına geri yükler; bu da kaliteyi korurken performansı artırabilir. Düğüm, bu ölçekleme işlemlerinin modelin yürütülmesi sırasında ne zaman ve nasıl gerçekleşeceği üzerinde hassas kontrol sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Küçültme yamasının uygulanacağı model | MODEL | Evet | - |
| `blok_numarası` | Küçültmenin uygulanacağı belirli blok numarası (varsayılan: 3) | INT | Hayır | 1-32 |
| `küçültme_faktörü` | Özelliklerin küçültüleceği faktör (varsayılan: 2.0) | FLOAT | Hayır | 0.1-9.0 |
| `başlangıç_yüzdesi` | Gürültü giderme işleminde küçültmenin başladığı başlangıç noktası (varsayılan: 0.0) | FLOAT | Hayır | 0.0-1.0 |
| `bitiş_yüzdesi` | Gürültü giderme işleminde küçültmenin durduğu bitiş noktası (varsayılan: 0.35) | FLOAT | Hayır | 0.0-1.0 |
| `atlamadan_sonra_küçült` | Atlama bağlantılarından sonra küçültme uygulanıp uygulanmayacağı (varsayılan: True) | BOOLEAN | Hayır | - |
| `küçültme_yöntemi` | Küçültme işlemleri için kullanılan enterpolasyon yöntemi | COMBO | Hayır | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `büyütme_yöntemi` | Büyütme işlemleri için kullanılan enterpolasyon yöntemi | COMBO | Hayır | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Küçültme yaması uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/tr.md)

---
**Source fingerprint (SHA-256):** `93ece77ad2dce3c1cdd554583ae1f2e6be51a43ab072d408869dddbcc7798c40`
