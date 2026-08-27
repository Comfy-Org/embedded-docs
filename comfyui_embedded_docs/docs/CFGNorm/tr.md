# CFGNorm

CFGNorm, difüzyon modellerinde sınıflandırıcısız rehberlik (CFG) sürecine bir normalizasyon tekniği uygular. Koşullu ve koşulsuz çıktıların normlarını karşılaştırarak gürültü giderme tahmininin ölçeğini ayarlar ve etkiyi kontrol etmek için bir güç çarpanı uygular. Varsayılan olarak normalizasyon yalnızca rehberlik çıktısını zayıflatır, ancak `pre_cfg` etkinleştirilmesi, örnekleyicinin CFG birleştirmesinden önce birleştirilmiş gürültüyü sıkıştırma olmadan yeniden ölçeklendirir ve bu da yükseltebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | CFG normalizasyonunun uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `güç` | CFG ölçeklendirmesine uygulanan normalizasyon etkisinin yoğunluğunu kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 100.0 arası |
| `pre_cfg` | true ise, birleştirilmiş gürültüyü örnekleyicinin CFG birleştirmesinden ÖNCE sıkıştırma olmadan yeniden ölçeklendirir (yükseltebilir). Lens gibi modeller tarafından kullanılan norm ölçekli CFG ile eşleşir. Varsayılan false, orijinal post-CFG x0-uzayı yalnızca zayıflatma davranışını korur. (varsayılan: False) | BOOLEAN | Hayır | true / false |

Not: Bu düğüm deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `yama uygulanmış model` | CFG normalizasyonu örnekleme sürecine uygulanmış değiştirilmiş modeli döndürür | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/tr.md)

---
**Source fingerprint (SHA-256):** `427dda498ebda2642489aa2591f063355a77b1e064e0dc7fa8570ed8200c2734`
