# Tembel Önbellek

## Genel Bakış

LazyCache, EasyCache'in daha da kolay bir uygulama sağlayan ev yapımı bir sürümüdür. ComfyUI'deki herhangi bir modelle çalışır ve örnekleme sırasında hesaplamayı azaltmak için önbellekleme işlevi ekler. Genel olarak EasyCache'ten daha kötü performans gösterse de, bazı nadir durumlarda daha etkili olabilir ve evrensel uyumluluk sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | LazyCache'in ekleneceği model. | MODEL | Evet | - |
| `yeniden kullanım eşiği` | Önbelleğe alınmış adımların yeniden kullanım eşiği (varsayılan: 0.2). | FLOAT | Hayır | 0.0 - 3.0 |
| `başlangıç_yüzdesi` | LazyCache kullanımının başlayacağı göreceli örnekleme adımı (varsayılan: 0.15). | FLOAT | Hayır | 0.0 - 1.0 |
| `bitiş_yüzdesi` | LazyCache kullanımının sona ereceği göreceli örnekleme adımı (varsayılan: 0.95). | FLOAT | Hayır | 0.0 - 1.0 |
| `ayrıntılı` | Ayrıntılı bilgilerin günlüğe kaydedilip kaydedilmeyeceği (varsayılan: False). | BOOLEAN | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | LazyCache işlevi eklenmiş model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/tr.md)

---
**Source fingerprint (SHA-256):** `72a5e85b7cf517e88583fc1b75d3ab4a5d40fe8604d50c34f555e677d2ea9e51`
