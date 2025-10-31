> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/tr.md)

ImageOnlyCheckpointSave düğümü, bir model, CLIP görüntü kodlayıcı ve VAE içeren bir kontrol noktası dosyasını kaydeder. Belirtilen dosya adı önekiyle bir safetensors dosyası oluşturur ve çıktı dizininde saklar. Bu düğüm özellikle görüntüyle ilgili model bileşenlerini tek bir kontrol noktası dosyasında birlikte kaydetmek için tasarlanmıştır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Kontrol noktasına kaydedilecek model |
| `clip_görü` | CLIP_VISION | Evet | - | Kontrol noktasına kaydedilecek CLIP görüntü kodlayıcı |
| `vae` | VAE | Evet | - | Kontrol noktasına kaydedilecek VAE (Değişimli Otokodlayıcı) |
| `dosyaadı_öneki` | STRING | Evet | - | Çıktı dosya adı için önek (varsayılan: "checkpoints/ComfyUI") |
| `prompt` | PROMPT | Hayır | - | İş akışı istem verileri için gizli parametre |
| `extra_pnginfo` | EXTRA_PNGINFO | Hayır | - | Ek PNG üst verileri için gizli parametre |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| - | - | Bu düğüm herhangi bir çıktı döndürmez |