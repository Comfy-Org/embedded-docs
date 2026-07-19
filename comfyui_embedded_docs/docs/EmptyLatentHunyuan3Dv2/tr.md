# BoşGizliHunyuan3Dv2

EmptyLatentHunyuan3Dv2 düğümü, Hunyuan3Dv2 3B oluşturma modelleri için özel olarak biçimlendirilmiş boş gizil tensörler oluşturur. Hunyuan3Dv2 mimarisi tarafından gereken doğru boyut ve yapıya sahip boş gizil uzaylar üreterek, 3B oluşturma iş akışlarına sıfırdan başlamanızı sağlar. Düğüm, sonraki 3B oluşturma süreçleri için temel görevi gören, sıfırlarla doldurulmuş gizil tensörler üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `çözünürlük` | Gizil uzay için çözünürlük boyutu (varsayılan: 3072) | INT | Evet | 1 - 8192 |
| `toplu_boyut` | Gruptaki gizil görüntü sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Hunyuan3Dv2 3B oluşturma için biçimlendirilmiş boş örnekler içeren bir gizil tensör döndürür | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/tr.md)

---
**Source fingerprint (SHA-256):** `f912b226bcec4e2edd52250682d0583ab378b5502173f8e027e0e8fbff1db08f`
