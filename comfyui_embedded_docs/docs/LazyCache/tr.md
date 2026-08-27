# Tembel Önbellek

LazyCache, EasyCache'in daha da kolay bir uygulama sunan özel yapım bir sürümüdür. ComfyUI'deki herhangi bir modelle çalışır ve örnekleme sırasında hesaplamayı azaltmak için önbelleğe alma işlevi ekler. Genel olarak EasyCache'ten daha kötü performans gösterse de, bazı nadir durumlarda daha etkili olabilir ve evrensel uyumluluk sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | LazyCache'in ekleneceği model. | MODEL | Evet | - |
| `yeniden kullanım eşiği` | Önbelleğe alınmış adımların yeniden kullanılması için eşik (varsayılan: 0.2). | FLOAT | Hayır | 0.0 - 3.0 |
| `başlangıç_yüzdesi` | LazyCache kullanımına başlanacak göreli örnekleme adımı (varsayılan: 0.15). | FLOAT | Hayır | 0.0 - 1.0 |
| `bitiş_yüzdesi` | LazyCache kullanımının sonlandırılacağı göreli örnekleme adımı (varsayılan: 0.95). | FLOAT | Hayır | 0.0 - 1.0 |
| `ayrıntılı` | Ayrıntılı bilgilerin günlüğe kaydedilip kaydedilmeyeceği (varsayılan: False). | BOOLEAN | Hayır | - |

Not: `reuse_threshold`, `start_percent`, `end_percent` ve `verbose` isteğe bağlı gelişmiş seçeneklerdir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | LazyCache işlevi eklenmiş model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/tr.md)

---
**Source fingerprint (SHA-256):** `78f9c13473567e068fc2be35b2f8f5aa459d43d3f13300a6ea858af98d3e2a44`
