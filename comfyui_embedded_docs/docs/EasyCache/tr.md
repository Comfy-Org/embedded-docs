> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/tr.md)

EasyCache düğümü, örnekleme işlemi sırasında önceden hesaplanmış adımları yeniden kullanarak performansı artırmak için modeller için yerel bir önbellek sistemi uygular. Örnekleme zaman çizelgesi boyunca önbelleği ne zaman kullanmaya başlayacağını ve ne zaman durduracağını yapılandırılabilir eşiklerle bir modele EasyCache işlevselliği ekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | EasyCache eklenek model. |
| `reuse_threshold` | FLOAT | Hayır | 0.0 - 3.0 | Önbelleğe alınmış adımların yeniden kullanım eşiği (varsayılan: 0.2). |
| `start_percent` | FLOAT | Hayır | 0.0 - 1.0 | EasyCache kullanımına başlamak için göreli örnekleme adımı (varsayılan: 0.15). |
| `end_percent` | FLOAT | Hayır | 0.0 - 1.0 | EasyCache kullanımını sonlandırmak için göreli örnekleme adımı (varsayılan: 0.95). |
| `verbose` | BOOLEAN | Hayır | - | Ayrıntılı bilgilerin günlüğe kaydedilip kaydedilmeyeceği (varsayılan: False). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | EasyCache işlevselliği eklenmiş model. |