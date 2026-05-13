> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/tr.md)

EasyCache düğümü, örnekleme işlemi sırasında önceden hesaplanmış adımları yeniden kullanarak performansı artırmak için modeller için yerel bir önbellekleme sistemi uygular. Örnekleme zaman çizelgesinde önbelleğin ne zaman kullanılmaya başlanacağı ve ne zaman durdurulacağı için yapılandırılabilir eşik değerleriyle bir modele EasyCache işlevselliği ekler.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | EasyCache eklenecek model. |
| `yeniden_kullanım_eşiği` | FLOAT | Hayır | 0.0 - 3.0 | Önbelleğe alınmış adımların yeniden kullanımı için eşik değeri (varsayılan: 0.2). |
| `başlangıç_yüzdesi` | FLOAT | Hayır | 0.0 - 1.0 | EasyCache kullanımının başlayacağı göreceli örnekleme adımı (varsayılan: 0.15). |
| `bitiş_yüzdesi` | FLOAT | Hayır | 0.0 - 1.0 | EasyCache kullanımının sona ereceği göreceli örnekleme adımı (varsayılan: 0.95). |
| `ayrıntılı` | BOOLEAN | Hayır | - | Ayrıntılı bilgilerin günlüğe kaydedilip kaydedilmeyeceği (varsayılan: False). |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | EasyCache işlevselliği eklenmiş model. |

---
**Source fingerprint (SHA-256):** `e9d9bf5ecae8034b562f1a27acf528d1f3241d7d28621beba149d3e9bd66a247`
