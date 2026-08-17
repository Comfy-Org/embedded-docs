# LTXV Sesli VAE Kodla

LTXV Audio VAE Encode düğümü, bir ses girdisi alır ve belirtilen bir Audio VAE modelini kullanarak bunu daha küçük, gizli (latent) bir temsile sıkıştırır. Bu işlem, ham ses verisini boru hattındaki diğer düğümlerin anlayıp işleyebileceği bir biçime dönüştürdüğü için, gizli uzay iş akışında ses üretmek veya işlemek açısından önemlidir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `audio` | Kodlanacak ses. | AUDIO | Evet | - |
| `audio_vae` | Kodlama için kullanılacak Audio VAE modeli. | VAE | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `Audio Latent` | Girdi sesin sıkıştırılmış gizli temsili. Çıktı; gizli örnekleri, VAE modelinin örnekleme hızını ve bir tür tanımlayıcısını içerir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEEncode/tr.md)

---
**Source fingerprint (SHA-256):** `68f70e0f8048cd9ba723f52eefc93cc33564eb3e68c0cb9b677964dc99aecb97`
