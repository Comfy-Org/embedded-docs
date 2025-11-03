> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/tr.md)

LazyCache, daha kolay bir uygulama sağlayan EasyCache'in ev yapımı bir versiyonudur. ComfyUI'deki herhangi bir modelle çalışır ve örnekleme sırasında hesaplamayı azaltmak için önbellekleme işlevselliği ekler. Genellikle EasyCache'ten daha düşük performans gösterse de, bazı nadir durumlarda daha etkili olabilir ve evrensel uyumluluk sunar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | LazyCache eklemek için kullanılacak model. |
| `reuse_threshold` | FLOAT | Hayır | 0.0 - 3.0 | Önbelleğe alınmış adımların yeniden kullanılması için eşik değeri (varsayılan: 0.2). |
| `start_percent` | FLOAT | Hayır | 0.0 - 1.0 | LazyCache kullanımına başlamak için göreli örnekleme adımı (varsayılan: 0.15). |
| `end_percent` | FLOAT | Hayır | 0.0 - 1.0 | LazyCache kullanımını sonlandırmak için göreli örnekleme adımı (varsayılan: 0.95). |
| `verbose` | BOOLEAN | Hayır | - | Ayrıntılı bilgilerin günlüğe kaydedilip kaydedilmeyeceği (varsayılan: False). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | LazyCache işlevselliği eklenmiş model. |