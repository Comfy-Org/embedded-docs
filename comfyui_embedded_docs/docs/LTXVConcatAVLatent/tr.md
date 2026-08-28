# AV Latent Birleştir

Bu düğüm, bir video latent'ini ve bir ses latent'ini, LTXV veya MiniMax H3 gibi AV modelleri için hazır, tek bir birleşik ses-video (AV) latent'inde birleştirir. Video girdisi zaten bir AV latent'i ise, video akışı korunur ve yalnızca ses akışı, sağlanan ses latent'iyle değiştirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `video_latent` | Video verisinin latent gösterimi. Zaten hem video hem de ses akışı içerdiğinde, düğüm video akışını korur ve `audio_latent` içindeki sesi bununla değiştirir. | LATENT | Evet |  |
| `audio_latent` | Ses verisinin latent gösterimi. Uzunluğu video akışına uyacak şekilde ayarlanır: daha uzun ses kırpılır, daha kısa ses sıfırlarla doldurulur. | LATENT | Evet |  |

**Not:** Her iki girdinin örnekleri, iç içe bir tensörde video ve ses akışı çifti olarak birleştirilir. Girdilerden herhangi biri bir `noise_mask` içeriyorsa, çıktı birleşik bir tane içerir; eksik bir maske, örneklerinin şekline uyan bir tüm-birler maskesiyle değiştirilir. Daha kısa ses eklendiğinde, eklenen bölge maskesiz bırakılır, böylece model onu üretebilir. Ses latent'i video latent'ine sığdırılamazsa, örneğin iki latent birden fazla boyutta farklılık gösteriyorsa veya batch veya kanal boyutlarında farklılık gösteriyorsa, düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Video ve ses örneklerini iki akış olarak bir araya getiren ve en az bir girdi sağladığında birleşik bir `noise_mask` içeren bir latent. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/tr.md)

---
**Source fingerprint (SHA-256):** `0231f9db2ce73132d8555fbb33f295b68aa68a0c1c54e4a0c5d2e1f67b5611cb`
