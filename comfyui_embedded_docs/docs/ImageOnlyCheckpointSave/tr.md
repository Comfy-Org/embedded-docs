# SadeceGörüntüKontrolNoktasıKaydet

Bu düğüm, bir modeli CLIP görüntü kodlayıcısı ve VAE'siyle birlikte paketleyen bir checkpoint dosyası kaydeder. Dosya, verilen dosya adı öneki kullanılarak çıktı dizinine safetensors biçiminde yazılır; böylece bir modelin görüntüyle ilgili bileşenleri tek bir checkpoint olarak depolanabilir.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Checkpoint'e kaydedilecek model | MODEL | Evet | - |
| `clip_görü` | Checkpoint'e kaydedilecek CLIP görüntü kodlayıcısı | CLIP_VISION | Evet | - |
| `vae` | Checkpoint'e kaydedilecek VAE (Varyasyonel Otomatik Kodlayıcı) | VAE | Evet | - |
| `dosyaadı_öneki` | Çıktı dosya adı için önek (varsayılan: "checkpoints/ComfyUI") | STRING | Evet | - |
| `prompt` | İş akışı istem verisini alan gizli parametre | PROMPT | Hayır | - |
| `extra_pnginfo` | Ek PNG meta verisini alan gizli parametre | EXTRA_PNGINFO | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| - | Bu düğüm herhangi bir çıktı döndürmez | - |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/tr.md)

---
**Source fingerprint (SHA-256):** `8ff4b3a78d8da523eaa5f784f847e954ba73b4d6037e748dcce592b447fcdee9`
