# MoGe Modelini Yükle

Bir dosyadan MoGe (Monocular Geometry) modeli yükler ve geometri tahmini görevlerinde kullanıma hazırlar. Bu düğüm, `geometry_estimation` klasöründen bir model dosyası okur ve MoGe modelini eğitilmiş ağırlıklarıyla başlatır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model_name` | Yüklenecek MoGe model dosyasının adı. ComfyUI kurulumunuzdaki mevcut model dosyalarından seçin. | COMBO | Evet | `geometry_estimation` klasöründeki mevcut model dosyalarının listesi |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MOGE_MODEL` | Geometri tahmini iş akışlarında kullanıma hazır, yüklenmiş MoGe model örneği. | MOGE_MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMoGeModel/tr.md)

---
**Source fingerprint (SHA-256):** `b5b55f94d3762852d5a1480c0b00d15da4e534adbeb544bf7c47da012e5a6353`
