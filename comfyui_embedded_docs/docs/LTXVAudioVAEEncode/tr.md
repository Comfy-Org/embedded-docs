> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEEncode/tr.md)

LTXV Audio VAE Encode düğümü, bir ses girişi alır ve belirtilen bir Audio VAE modeli kullanarak onu daha küçük, gizli bir temsile sıkıştırır. Bu işlem, ham ses verilerini, işlem hattındaki diğer düğümlerin anlayabileceği ve işleyebileceği bir formata dönüştürdüğü için, gizli uzay iş akışı içinde ses oluşturmak veya manipüle etmek için gereklidir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Evet | - | Kodlanacak ses. |
| `audio_vae` | VAE | Evet | - | Kodlama için kullanılacak Audio VAE modeli. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `Audio Latent` | LATENT | Giriş sesinin sıkıştırılmış gizli temsili. Çıktı, gizli örnekleri, VAE modelinin örnekleme hızını ve bir tür tanımlayıcısını içerir. |
