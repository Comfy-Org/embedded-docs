# CFGNorm

CFGNorm, difüzyon modellerinde sınıflandırıcısız yönlendirmenin (CFG) nasıl uygulandığını, koşullu tahminin boyutunu (norm) yönlendirilmiş tahminle karşılaştırarak ve sonucu yeniden ölçeklendirerek ayarlar. Bir `strength` değeri, ayarın ne kadarının uygulanacağını kontrol eder. Varsayılan olarak ölçekleme yalnızca yönlendirme çıktısını zayıflatır; `pre_cfg` etkinleştirildiğinde ise örnekleyicinin CFG birleştirmesinden önce birleştirilmiş gürültüyü sınırlama olmadan yeniden ölçeklendirir, bu da sonucu güçlendirebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | CFG normalizasyonunun uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `güç` | CFG ölçeklemesine uygulanan normalizasyon etkisinin yoğunluğunu kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 100.0 arası (adım 0.01) |
| `pre_cfg` | True ise, örnekleyicinin CFG birleştirmesinden ÖNCE birleştirilmiş gürültüyü sınırlama olmadan yeniden ölçeklendirir (güçlendirebilir). Lens gibi modeller tarafından kullanılan normla ölçeklenmiş CFG ile eşleşir. Varsayılan false, özgün CFG sonrası x0-uzayındaki yalnızca zayıflatma davranışını korur. (varsayılan: False) | BOOLEAN | Hayır | true / false |

Not: Bu düğüm deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `patched_model` | Örnekleme sürecine CFG normalizasyonu uygulanmış değiştirilmiş modeli döndürür | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/tr.md)

---
**Source fingerprint (SHA-256):** `427dda498ebda2642489aa2591f063355a77b1e064e0dc7fa8570ed8200c2734`
