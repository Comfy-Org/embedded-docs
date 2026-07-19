# KolayÖnbellek

EasyCache düğümü, örnekleme işlemi sırasında önceden hesaplanmış adımları yeniden kullanarak performansı artırmak için modeller için yerel bir önbellekleme sistemi uygular. Örnekleme zaman çizelgesinde önbelleğin ne zaman kullanılmaya başlanacağı ve ne zaman durdurulacağı için yapılandırılabilir eşik değerleriyle bir modele EasyCache işlevselliği ekler.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | EasyCache eklenecek model. | MODEL | Evet | - |
| `yeniden_kullanım_eşiği` | Önbelleğe alınmış adımların yeniden kullanımı için eşik değeri (varsayılan: 0.2). | FLOAT | Hayır | 0.0 - 3.0 |
| `başlangıç_yüzdesi` | EasyCache kullanımının başlayacağı göreceli örnekleme adımı (varsayılan: 0.15). | FLOAT | Hayır | 0.0 - 1.0 |
| `bitiş_yüzdesi` | EasyCache kullanımının sona ereceği göreceli örnekleme adımı (varsayılan: 0.95). | FLOAT | Hayır | 0.0 - 1.0 |
| `ayrıntılı` | Ayrıntılı bilgilerin günlüğe kaydedilip kaydedilmeyeceği (varsayılan: False). | BOOLEAN | Hayır | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | EasyCache işlevselliği eklenmiş model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/tr.md)

---
**Source fingerprint (SHA-256):** `e9d9bf5ecae8034b562f1a27acf528d1f3241d7d28621beba149d3e9bd66a247`
