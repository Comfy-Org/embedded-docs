# AV Latent Birleştir

LTXVConcatAVLatent düğümü, bir video latentini ve bir ses latentini, LTXV veya MiniMax H3 gibi görsel-işitsel modellerde kullanılmak üzere tek bir birleşik latentte birleştirir. Her iki girdiden `samples` değerlerini bir araya getirir ve eğer girdilerden herhangi biri bir `noise_mask` içeriyorsa, bu maskeler de bir araya getirilir. Video latenti zaten bir AV latenti ise, düğüm video akışını korur ve ses akışını sağlanan ses latenti ile değiştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `video_latent` | Video verilerinin latent gösterimi. | LATENT | Evet |  |
| `audio_latent` | Video latenti ile birleştirilecek ses verilerinin latent gösterimi. | LATENT | Evet |  |

**Ses uzunluğu hakkında not:** `video_latent` zaten bir AV latenti olduğunda, `audio_latent` gömülü ses akışıyla tüm boyutlarda aynı olmalıdır; tek boyut hariç. Düğüm, sesi bu boyut boyunca mevcut akış uzunluğuna uyacak şekilde kırpar veya sıfırla doldurur. Doldurulmuş kuyruk masksız bırakılır, böylece model onu üretebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Birleştirilmiş video ve ses `samples` değerlerini içeren bir latent. Girdilerden herhangi biri bir `noise_mask` sağlarsa, çıktı ayrıca birleştirilmiş bir `noise_mask` içerir; eksik bir maske, birler ile değiştirilir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/tr.md)

---
**Source fingerprint (SHA-256):** `0231f9db2ce73132d8555fbb33f295b68aa68a0c1c54e4a0c5d2e1f67b5611cb`
