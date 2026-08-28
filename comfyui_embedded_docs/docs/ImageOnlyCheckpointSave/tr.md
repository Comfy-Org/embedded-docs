# SadeceGörüntüKontrolNoktasıKaydet

ImageOnlyCheckpointSave düğümü, bir model, CLIP görsel kodlayıcısı ve VAE içeren bir kontrol noktası (checkpoint) dosyası kaydeder. Belirtilen dosya adı önekine sahip bir safetensors dosyası oluşturur ve bunu çıktı dizinine kaydeder. Bu düğüm, görüntüyle ilgili model bileşenlerini tek bir kontrol noktası dosyasında birlikte kaydetmek için özel olarak tasarlanmıştır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kontrol noktasına kaydedilecek model | MODEL | Evet | - |
| `clip_görü` | Kontrol noktasına kaydedilecek CLIP görsel kodlayıcısı | CLIP_VISION | Evet | - |
| `vae` | Kontrol noktasına kaydedilecek VAE (Varyasyonel Otomatik Kodlayıcı) | VAE | Evet | - |
| `dosyaadı_öneki` | Çıktı dosya adı için önek (varsayılan: "checkpoints/ComfyUI") | STRING | Evet | - |
| `prompt` | İş akışı prompt verileri için gizli parametre | PROMPT | Hayır | - |
| `extra_pnginfo` | Ek PNG meta verileri | EXTRA_PNGINFO | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| - | Bu düğüm herhangi bir çıktı döndürmez | - |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/tr.md)

---
**Source fingerprint (SHA-256):** `8ff4b3a78d8da523eaa5f784f847e954ba73b4d6037e748dcce592b447fcdee9`
