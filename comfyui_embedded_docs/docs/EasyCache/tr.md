# KolayÖnbellek

EasyCache düğümü, bir difüzyon modeline, her adımı yeniden hesaplamak yerine önceden hesaplanan adımların sonuçlarını yeniden kullanarak örneklemeyi hızlandıran yerleşik bir önbellekleme sistemi ekler. Yalnızca örnekleme sürecinin yapılandırılabilir bir başlangıç ve bitiş noktası arasında etkinleşir ve tahmini çıktı değişimi kullanıcı tanımlı bir eşiğin altında kaldığında adımları atlar. Bu, ileri düzey hata ayıklama kullanımına yönelik deneysel bir düğümdür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | EasyCache'in ekleneceği model. | MODEL | Evet | - |
| `reuse_threshold` | Önbelleğe alınmış adımların yeniden kullanılması için eşik (varsayılan: 0.2). | FLOAT | Evet | 0.0 - 3.0 |
| `start_percent` | EasyCache kullanımının başlayacağı göreli örnekleme adımı (varsayılan: 0.15). | FLOAT | Evet | 0.0 - 1.0 |
| `end_percent` | EasyCache kullanımının sona ereceği göreli örnekleme adımı (varsayılan: 0.95). | FLOAT | Evet | 0.0 - 1.0 |
| `verbose` | Ayrıntılı bilgilerin günlüğe kaydedilip kaydedilmeyeceği (varsayılan: False). | BOOLEAN | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | EasyCache işlevselliği eklenmiş model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/tr.md)

---
**Source fingerprint (SHA-256):** `3e10ac65f8df58ce8649fdf599e62bfb86f2d4166840bed5622c0aa2c419cd38`
