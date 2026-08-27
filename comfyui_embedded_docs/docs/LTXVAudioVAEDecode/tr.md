# LTXV Sesli VAE Çöz

LTXV Audio VAE Decode düğümü, sesin latent temsilini tekrar bir ses dalga formuna dönüştürür. Bu kod çözme işlemini gerçekleştirmek için özel bir Audio VAE modeli kullanır ve ilişkili örnekleme hızıyla birlikte bir ses çıktısı üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `samples` | Kod çözülecek latent. | LATENT | Evet | N/A |
| `audio_vae` | Latenti kod çözmek için kullanılan Audio VAE modeli. | VAE | Evet | N/A |

**Not:** Sağlanan latent iç içe geçmişse (birden fazla latent içeriyorsa), düğüm kod çözme için otomatik olarak sıradaki son latenti kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `Ses` | Kod çözülmüş ses dalga formu ve ilişkili örnekleme hızı. Dalga formu, girdi latentiyle aynı cihaza yerleştirilir ve örnekleme hızı Audio VAE modeli tarafından belirlenir. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEDecode/tr.md)

---
**Source fingerprint (SHA-256):** `fc94f3cb78ede86ada374444d613411cc9bb5849e5cdb8a24074babee50719b1`
