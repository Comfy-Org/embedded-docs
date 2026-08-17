# CFGNorm

CFGNorm, difüzyon modellerindeki sınıflandırıcısız rehberlik (CFG) sürecine bir normalizasyon tekniği uygular. Koşullu ve koşulsuz çıktıların normlarını karşılaştırarak gürültü giderme tahmininin ölçeğini ayarlar ve etkiyi kontrol etmek için bir güç çarpanı uygular. Bu, rehberlik ölçeklemesinde aşırı değerleri önleyerek üretim sürecini dengelemeye yardımcı olur. `pre_cfg` etkinleştirildiğinde, yeniden ölçekleme bunun yerine örnekleyicinin CFG birleştirmesinden önce birleştirilmiş gürültüye uygulanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | CFG normalizasyonunun uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `strength` | CFG ölçeklemesine uygulanan normalizasyon etkisinin yoğunluğunu kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 100.0 (adım 0.01) |
| `pre_cfg` | True ise, birleştirilmiş gürültüyü örnekleyicinin CFG birleştirmesinden ÖNCE yeniden ölçeklendirir (sınırlama olmadan; yükseltebilir). Lens gibi modeller tarafından kullanılan norm ölçekli CFG ile eşleşir. Varsayılan False, orijinal CFG sonrası x0-uzayı yalnızca zayıflatma davranışını korur. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |

Not: Varsayılan CFG sonrası modda, yeniden ölçekleme faktörü 0.0 ile 1.0 arasında sınırlandırılır, bu nedenle tahmin ölçeğini yalnızca zayıflatabilir (azaltabilir). `pre_cfg` etkinleştirildiğinde herhangi bir sınırlama uygulanmaz, bu nedenle birleştirilmiş gürültü yükseltilebilir. Bu modda, 1.0 dışındaki bir `strength` değeri sonucu standart doğrusal CFG'ye geri karıştırır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `patched_model` | Örnekleme sürecine CFG normalizasyonu uygulanmış değiştirilmiş modeli döndürür | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/tr.md)

---
**Source fingerprint (SHA-256):** `427dda498ebda2642489aa2591f063355a77b1e064e0dc7fa8570ed8200c2734`
