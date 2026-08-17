# SadeceGörüntüKontrolNoktasıKaydet

The ImageOnlyCheckpointSave node, bir model, CLIP görüntü kodlayıcısı ve VAE içeren bir kontrol noktası (checkpoint) dosyası kaydeder. Belirtilen dosya adı önekiyle bir safetensors dosyası oluşturur ve bunu çıktı dizininde saklar. Bu düğüm, görüntüyle ilgili model bileşenlerini tek bir kontrol noktası dosyasında birlikte kaydetmek için özel olarak tasarlanmıştır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kontrol noktasında kaydedilecek model | MODEL | Evet | - |
| `clip_vision` | Kontrol noktasında kaydedilecek CLIP görüntü kodlayıcı | CLIP_VISION | Evet | - |
| `vae` | Kontrol noktasında kaydedilecek VAE (Değişken Otomatik Kodlayıcı) | VAE | Evet | - |
| `filename_prefix` | Çıktı dosya adı için önek (varsayılan: "checkpoints/ComfyUI") | STRING | Evet | - |
| `prompt` | İş akışı prompt verileri için gizli parametre | PROMPT | Hayır | - |
| `extra_pnginfo` | Ek PNG meta verileri için gizli parametre | EXTRA_PNGINFO | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| - | Bu düğüm herhangi bir çıktı döndürmez | - |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/tr.md)

---
**Source fingerprint (SHA-256):** `8ff4b3a78d8da523eaa5f784f847e954ba73b4d6037e748dcce592b447fcdee9`
