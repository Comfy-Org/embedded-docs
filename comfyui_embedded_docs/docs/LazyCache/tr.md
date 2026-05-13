> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/tr.md)

## Genel Bakış

LazyCache, EasyCache'in daha da kolay bir uygulama sağlayan ev yapımı bir sürümüdür. ComfyUI'deki herhangi bir modelle çalışır ve örnekleme sırasında hesaplamayı azaltmak için önbellekleme işlevi ekler. Genel olarak EasyCache'ten daha kötü performans gösterse de, bazı nadir durumlarda daha etkili olabilir ve evrensel uyumluluk sunar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | LazyCache'in ekleneceği model. |
| `reuse_threshold` | FLOAT | Hayır | 0.0 - 3.0 | Önbelleğe alınmış adımların yeniden kullanım eşiği (varsayılan: 0.2). |
| `start_percent` | FLOAT | Hayır | 0.0 - 1.0 | LazyCache kullanımının başlayacağı göreceli örnekleme adımı (varsayılan: 0.15). |
| `end_percent` | FLOAT | Hayır | 0.0 - 1.0 | LazyCache kullanımının sona ereceği göreceli örnekleme adımı (varsayılan: 0.95). |
| `verbose` | BOOLEAN | Hayır | - | Ayrıntılı bilgilerin günlüğe kaydedilip kaydedilmeyeceği (varsayılan: False). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | LazyCache işlevi eklenmiş model. |

---
**Source fingerprint (SHA-256):** `72a5e85b7cf517e88583fc1b75d3ab4a5d40fe8604d50c34f555e677d2ea9e51`
