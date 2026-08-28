# LTXV Sesli VAE Yükleyici

LTXV Audio VAE Loader düğümü, bir kontrol noktası (checkpoint) dosyasından önceden eğitilmiş bir Ses Varyasyonel Otomatik Kodlayıcı (VAE) modeli yükler. Belirtilen kontrol noktasını okur, ağırlıklarını ve meta verilerini yükler ve modeli ComfyUI içindeki ses üretimi veya işleme iş akışlarında kullanıma hazır hale getirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ckpt_name` | Yüklenecek Ses VAE kontrol noktası. ComfyUI `checkpoints` dizininde bulunan tüm dosyalarla doldurulan açılır listedir. | COMBO | Evet | `checkpoints` klasöründeki tüm dosyalar. Liste çalışma zamanında oluşturulur. |

Seçilen dosya geçerli bir LTXV ses VAE kontrol noktası olmalıdır. Düğüm, dosyadan yalnızca ses VAE ve vocoder ağırlıklarını alır; yüklenen model geçerli bir VAE değilse hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| Audio VAE | Yüklenen Ses Varyasyonel Otomatik Kodlayıcı modeli; diğer ses işleme düğümlerine bağlanmaya hazırdır. | VAE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/tr.md)

---
**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`
