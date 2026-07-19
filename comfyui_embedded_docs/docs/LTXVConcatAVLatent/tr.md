# LTXVConcatAVLatent

LTXVConcatAVLatent düğümü, bir video gizli temsilini ve bir ses gizli temsilini tek bir birleştirilmiş gizli çıktıda birleştirir. Her iki girdiden gelen `samples` tensörlerini ve varsa `noise_mask` tensörlerini birleştirerek bunları bir video oluşturma hattında daha ileri işleme hazırlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `video_latent` | Video verisinin gizli temsili. | LATENT | Evet |  |
| `audio_latent` | Ses verisinin gizli temsili. | LATENT | Evet |  |

**Not:** `video_latent` ve `audio_latent` girdilerinden gelen `samples` tensörleri birleştirilir. Herhangi bir girdi bir `noise_mask` içeriyorsa bu kullanılır; eğer biri eksikse, onun için birlerden oluşan bir maske (karşılık gelen `samples` ile aynı şekle sahip) oluşturulur. Ortaya çıkan maskeler daha sonra da birleştirilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Video ve ses girdilerinden birleştirilmiş `samples` ve varsa birleştirilmiş `noise_mask` içeren tek bir gizli sözlük. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/tr.md)

---
**Source fingerprint (SHA-256):** `322d6870f110fb1ef8b472cb49649cc9fff7865f4c7a83fbfd536f1fdfd694f8`
