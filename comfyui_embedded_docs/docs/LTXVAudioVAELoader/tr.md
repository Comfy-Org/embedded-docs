> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/tr.md)

LTXV Audio VAE Yükleyici düğümü, önceden eğitilmiş bir Ses Varyasyonel Otomatik Kodlayıcı (VAE) modelini bir kontrol noktası dosyasından yükler. Belirtilen kontrol noktasını okur, ağırlıklarını ve meta verilerini yükler ve modeli ComfyUI içindeki ses üretimi veya işleme iş akışlarında kullanılmak üzere hazırlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `ckpt_name` | STRING | Evet | `checkpoints` klasöründeki tüm dosyalar.<br>*Örnek: `"audio_vae.safetensors"`* | Yüklenecek Ses VAE kontrol noktası. Bu, ComfyUI `checkpoints` dizininizde bulunan tüm dosyalarla doldurulmuş bir açılır listedir. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `Audio VAE` | VAE | Yüklenen Ses Varyasyonel Otomatik Kodlayıcı modeli, diğer ses işleme düğümlerine bağlanmaya hazır. |
