# MoGe Modelini Yükle

Bir MoGe (Monoküler Geometri) modelini bir dosyadan yükler ve geometri tahmini görevlerinde kullanıma hazırlar. Düğüm, seçilen model dosyasını `geometry_estimation` klasöründen okur ve MoGe modelini depolanmış ağırlıklarıyla başlatır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model_name` | Yüklenecek MoGe model dosyasının adı. ComfyUI kurulumunuzun `geometry_estimation` klasöründe bulunan model dosyaları arasından seçin. | COMBO | Evet | `geometry_estimation` klasöründeki kullanılabilir model dosyalarının listesi |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MOGE_MODEL` | Yüklenen MoGe model örneği; geometri tahmini iş akışlarında kullanıma hazırdır. | MOGE_MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMoGeModel/tr.md)

---
**Source fingerprint (SHA-256):** `b5b55f94d3762852d5a1480c0b00d15da4e534adbeb544bf7c47da012e5a6353`
