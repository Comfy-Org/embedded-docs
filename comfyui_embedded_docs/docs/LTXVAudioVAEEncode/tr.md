> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEEncode/tr.md)

LTXV Ses VAE Kodlama düğümü, bir ses girişini alır ve belirtilen bir Ses VAE modeli kullanarak daha küçük bir gizli (latent) temsile sıkıştırır. Bu işlem, ham ses verilerini işlem hattındaki diğer düğümlerin anlayıp işleyebileceği bir formata dönüştürdüğü için, gizli alan iş akışında ses oluşturma veya manipüle etme için gereklidir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Evet | - | Kodlanacak ses. |
| `audio_vae` | VAE | Evet | - | Kodlama için kullanılacak Ses VAE modeli. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `Ses Gizli (Audio Latent)` | LATENT | Giriş sesinin sıkıştırılmış gizli temsili. Çıktı, gizli örnekleri, VAE modelinin örnekleme hızını ve bir tür tanımlayıcısını içerir. |

---
**Source fingerprint (SHA-256):** `fc10d8bbdca5150b7c87adb52960b8690397c3d003c89f9ec6a8410c541a347f`
