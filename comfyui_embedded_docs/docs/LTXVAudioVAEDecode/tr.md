# LTXV Sesli VAE Çöz

LTXV Ses VAE Kod Çözücü düğümü, bir sesin gizli uzay temsilini tekrar ses dalga formuna dönüştürür. Bu kod çözme işlemini gerçekleştirmek için özel bir Ses VAE modeli kullanır ve belirli bir örnekleme hızında ses çıktısı üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `samples` | Kod çözülecek gizli uzay temsili. | LATENT | Evet | Yok |
| `audio_vae` | Gizli uzay temsilini kod çözmek için kullanılan Ses VAE modeli. | VAE | Evet | Yok |

**Not:** Sağlanan gizli uzay temsili iç içe geçmişse (birden fazla gizli uzay içeriyorsa), düğüm kod çözme için otomatik olarak dizideki son gizli uzayı kullanacaktır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `Ses` | Kod çözülmüş ses dalga formu ve ilişkili örnekleme hızı. Dalga formu, giriş gizli uzay temsiliyle aynı cihaza taşınmış bir tensördür ve örnekleme hızı Ses VAE modeli tarafından belirlenir. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEDecode/tr.md)

---
**Source fingerprint (SHA-256):** `e9df1da8ca0424cfc7ce97951e65154df845d98c3b73f76725fa657d851a3a07`
