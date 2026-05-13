> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/tr.md)

ImageOnlyCheckpointSave düğümü, bir model, CLIP görüntü kodlayıcı ve VAE içeren bir kontrol noktası dosyası kaydeder. Belirtilen dosya adı önekiyle bir safetensors dosyası oluşturur ve bunu çıktı dizinine kaydeder. Bu düğüm, özellikle görüntüyle ilgili model bileşenlerini tek bir kontrol noktası dosyasında birlikte kaydetmek için tasarlanmıştır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `model` | MODEL | Evet | - | Kontrol noktasına kaydedilecek model |
| `clip_vision` | CLIP_VISION | Evet | - | Kontrol noktasına kaydedilecek CLIP görüntü kodlayıcı |
| `vae` | VAE | Evet | - | Kontrol noktasına kaydedilecek VAE (Değişimsel Otomatik Kodlayıcı) |
| `filename_prefix` | STRING | Evet | - | Çıktı dosyası adı öneki (varsayılan: "checkpoints/ComfyUI") |
| `prompt` | PROMPT | Hayır | - | İş akışı istem verileri için gizli parametre |
| `extra_pnginfo` | EXTRA_PNGINFO | Hayır | - | Ek PNG meta verileri için gizli parametre |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| - | - | Bu düğüm herhangi bir çıktı döndürmez |

---
**Source fingerprint (SHA-256):** `d2a26933f0e2fcccf3c57f50038fb40ef5b23d00ccdd2e1d215b3cb78203b9fd`
