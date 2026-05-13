> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/tr.md)

LTXV Ses VAE Yükleyici düğümü, bir kontrol noktası dosyasından önceden eğitilmiş bir Ses Değişkenli Otomatik Kodlayıcı (VAE) modeli yükler. Belirtilen kontrol noktasını okur, ağırlıklarını ve meta verilerini yükler ve modeli ComfyUI içinde ses oluşturma veya işleme iş akışlarında kullanıma hazır hale getirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `ckpt_name` | STRING | Evet | `checkpoints` klasöründeki tüm dosyalar.<br>*Örnek: `"audio_vae.safetensors"`* | Yüklenecek Ses VAE kontrol noktası. Bu, ComfyUI `checkpoints` dizininizde bulunan tüm dosyalarla doldurulmuş bir açılır listedir. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `Audio VAE` | VAE | Yüklenen Ses Değişkenli Otomatik Kodlayıcı modeli, diğer ses işleme düğümlerine bağlanmaya hazırdır. |

---
**Source fingerprint (SHA-256):** `44e79f694eed796a83f3ac25c56946baaa12b016568bd8824eb179bf79e50588`
