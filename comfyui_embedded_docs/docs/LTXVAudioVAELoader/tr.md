# LTXV Sesli VAE Yükleyici

LTXV Audio VAE Loader düğümü, önceden eğitilmiş bir Audio Variational Autoencoder (VAE) modelini bir kontrol noktası (checkpoint) dosyasından yükler. Belirtilen kontrol noktasını okur, ağırlıklarını ve meta verilerini yükler ve modeli ComfyUI içindeki ses üretimi veya işleme iş akışlarında kullanıma hazırlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `ckpt_name` | Yüklenecek Audio VAE kontrol noktası. Bu açılır liste, ComfyUI `checkpoints` dizininizde bulunan tüm dosyalarla doldurulur. | COMBO | Evet | `checkpoints` klasöründeki tüm dosyalar (dinamik olarak doldurulur).<br>*Örnek: `"audio_vae.safetensors"`* |

Not: Seçilen kontrol noktası dosyası bulunamazsa veya geçerli bir audio VAE içermiyorsa düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `Audio VAE` | Yüklenen Audio Variational Autoencoder modeli, diğer ses işleme düğümlerine bağlanmaya hazır. | VAE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/tr.md)

---
**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`
