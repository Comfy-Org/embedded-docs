# KolayÖnbellek

EasyCache düğümü, örnekleme sürecinde önceden hesaplanmış adımları yeniden kullanarak performansı artırmak için modellere yerel bir önbellekleme sistemi uygular. Örnekleme zaman çizelgesinde önbelleğin kullanılmaya başlanacağı ve kullanımının durdurulacağı zamanlar için yapılandırılabilir eşiklerle bir modele EasyCache işlevselliği ekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | EasyCache'in ekleneceği model. | MODEL | Evet | - |
| `reuse_threshold` | Önbelleğe alınan adımların yeniden kullanılması için eşik (varsayılan: 0.2). | FLOAT | Evet | 0.0 - 3.0 |
| `start_percent` | EasyCache kullanımına başlanacak göreli örnekleme adımı (varsayılan: 0.15). | FLOAT | Evet | 0.0 - 1.0 |
| `end_percent` | EasyCache kullanımının sona ereceği göreli örnekleme adımı (varsayılan: 0.95). | FLOAT | Evet | 0.0 - 1.0 |
| `verbose` | Ayrıntılı bilgilerin günlüğe kaydedilip kaydedilmeyeceği (varsayılan: False). | BOOLEAN | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model` | EasyCache içeren model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/tr.md)

---
**Source fingerprint (SHA-256):** `3e10ac65f8df58ce8649fdf599e62bfb86f2d4166840bed5622c0aa2c419cd38`
