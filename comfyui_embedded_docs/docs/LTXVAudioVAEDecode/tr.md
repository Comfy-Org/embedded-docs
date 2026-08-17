# LTXV Sesli VAE Çöz

LTXV Audio VAE Decode düğümü, bir ses latent temsilini tekrar ses dalga formuna dönüştürür. Bu kod çözme işlemini gerçekleştirmek için özel bir Audio VAE modeli kullanır ve belirli bir örnekleme hızına sahip bir ses çıktısı üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `samples` | Kod çözülecek latent. | LATENT | Evet | N/A |
| `audio_vae` | Latent'i kod çözmek için kullanılan Audio VAE modeli. | VAE | Evet | N/A |

**Not:** Sağlanan latent iç içe geçmişse (birden fazla latent içeriyorsa), düğüm otomatik olarak dizideki son latent'i kod çözme için kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `Audio` | Kod çözülmüş ses dalga formu ve ilişkili örnekleme hızı. Dalga formu, girdi latent'i ile aynı cihaza taşınmış bir tensördür ve örnekleme hızı Audio VAE modeli tarafından belirlenir. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEDecode/tr.md)

---
**Source fingerprint (SHA-256):** `fc94f3cb78ede86ada374444d613411cc9bb5849e5cdb8a24074babee50719b1`
