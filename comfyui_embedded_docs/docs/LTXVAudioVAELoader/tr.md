# LTXV Sesli VAE Yükleyici

LTXV Audio VAE Loader düğümü, önceden eğitilmiş bir Audio Variational Autoencoder (VAE) modelini bir checkpoint dosyasından yükler. Belirtilen checkpoint'i okur, Audio VAE ve vocoder ağırlıklarını korur ve modeli ComfyUI içindeki ses üretimi veya işleme iş akışlarında kullanıma hazırlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ckpt_name` | Yüklenecek Audio VAE checkpoint'i. Bu, ComfyUI `checkpoints` dizininizde bulunan tüm dosyalarla doldurulan bir açılır listedir. | COMBO | Evet | `checkpoints` klasöründeki tüm dosyalar. Liste çalışma zamanında oluşturulur. |

Seçilen dosya geçerli bir LTXV audio VAE checkpoint'i olmalıdır. Düğüm, dosyadan yalnızca Audio VAE ve vocoder ağırlıklarını tutar ve yüklenen model geçerli bir VAE değilse hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `Audio VAE` | Yüklenen Audio Variational Autoencoder modeli; diğer ses işleme düğümlerine bağlanmaya hazırdır. | VAE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/tr.md)

---
**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`
