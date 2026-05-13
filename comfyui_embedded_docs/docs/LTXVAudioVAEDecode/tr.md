> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEDecode/tr.md)

LTXV Ses VAE Kod Çözücü düğümü, bir sesin gizli uzay temsilini tekrar ses dalga formuna dönüştürür. Bu kod çözme işlemini gerçekleştirmek için özel bir Ses VAE modeli kullanır ve belirli bir örnekleme hızında ses çıktısı üretir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `samples` | LATENT | Evet | Yok | Kod çözülecek gizli uzay temsili. |
| `audio_vae` | VAE | Evet | Yok | Gizli uzay temsilini kod çözmek için kullanılan Ses VAE modeli. |

**Not:** Sağlanan gizli uzay temsili iç içe geçmişse (birden fazla gizli uzay içeriyorsa), düğüm kod çözme için otomatik olarak dizideki son gizli uzayı kullanacaktır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `Audio` | AUDIO | Kod çözülmüş ses dalga formu ve ilişkili örnekleme hızı. Dalga formu, giriş gizli uzay temsiliyle aynı cihaza taşınmış bir tensördür ve örnekleme hızı Ses VAE modeli tarafından belirlenir. |

---
**Source fingerprint (SHA-256):** `e9df1da8ca0424cfc7ce97951e65154df845d98c3b73f76725fa657d851a3a07`
