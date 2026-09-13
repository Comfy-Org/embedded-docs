# Tembel Önbellek

LazyCache, örnekleme sırasında önbellekleme ekleyerek hesaplamayı azaltan deneysel, gayriresmî bir EasyCache sürümüdür. ComfyUI'daki modellerle evrensel uyumluluk için tasarlanmıştır; ancak genellikle EasyCache'ten daha kötü performans gösterir ve yalnızca nadir durumlarda daha iyi çalışabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | LazyCache'in ekleneceği model. | MODEL | Evet | - |
| `reuse_threshold` | Önbelleğe alınmış adımların yeniden kullanılması için eşik. Varsayılan: 0.2. | FLOAT | Evet | 0.0 - 3.0 (adım: 0.01) |
| `start_percent` | LazyCache kullanımının başlatılacağı göreli örnekleme adımı. Varsayılan: 0.15. | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `end_percent` | LazyCache kullanımının sonlandırılacağı göreli örnekleme adımı. Varsayılan: 0.95. | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `verbose` | Ayrıntılı bilgilerin günlüğe kaydedilip kaydedilmeyeceği. Varsayılan: False. | BOOLEAN | Evet | - |

Not: `reuse_threshold`, `start_percent`, `end_percent` ve `verbose` gelişmiş girdiler olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | LazyCache işlevselliği eklenmiş model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/tr.md)

---
**Source fingerprint (SHA-256):** `78f9c13473567e068fc2be35b2f8f5aa459d43d3f13300a6ea858af98d3e2a44`
