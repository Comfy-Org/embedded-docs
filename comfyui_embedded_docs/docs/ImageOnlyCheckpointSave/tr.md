# SadeceGörüntüKontrolNoktasıKaydet

ImageOnlyCheckpointSave düğümü, bir model, CLIP görüntü kodlayıcı ve VAE içeren bir kontrol noktası dosyası kaydeder. Belirtilen dosya adı önekiyle bir safetensors dosyası oluşturur ve bunu çıktı dizinine kaydeder. Bu düğüm, özellikle görüntüyle ilgili model bileşenlerini tek bir kontrol noktası dosyasında birlikte kaydetmek için tasarlanmıştır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kontrol noktasına kaydedilecek model | MODEL | Evet | - |
| `clip_görü` | Kontrol noktasına kaydedilecek CLIP görüntü kodlayıcı | CLIP_VISION | Evet | - |
| `vae` | Kontrol noktasına kaydedilecek VAE (Değişimsel Otomatik Kodlayıcı) | VAE | Evet | - |
| `dosyaadı_öneki` | Çıktı dosyası adı öneki (varsayılan: "checkpoints/ComfyUI") | STRING | Evet | - |
| `prompt` | İş akışı istem verileri için gizli parametre | PROMPT | Hayır | - |
| `extra_pnginfo` | Ek PNG meta verileri için gizli parametre | EXTRA_PNGINFO | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| - | Bu düğüm herhangi bir çıktı döndürmez | - |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/tr.md)

---
**Source fingerprint (SHA-256):** `d2a26933f0e2fcccf3c57f50038fb40ef5b23d00ccdd2e1d215b3cb78203b9fd`
