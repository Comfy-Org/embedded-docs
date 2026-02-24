> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/tr.md)

LatentUpscaleModelLoader düğümü, gizli (latent) temsilleri büyütmek için tasarlanmış özel bir model yükler. Sistemin belirlenmiş klasöründen bir model dosyasını okur ve doğru dahili model mimarisini örneklemek ve yapılandırmak için türünü (720p, 1080p veya diğer) otomatik olarak algılar. Yüklenen model daha sonra, gizli uzay süper çözünürlük görevleri için diğer düğümler tarafından kullanılmaya hazır hale gelir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_name` | STRING | Evet | *`latent_upscale_models` klasöründeki tüm dosyalar* | Yüklenecek gizli büyütme model dosyasının adı. Mevcut seçenekler, ComfyUI'nizin `latent_upscale_models` dizininde bulunan dosyalardan dinamik olarak doldurulur. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | LATENT_UPSCALE_MODEL | Yüklenen, yapılandırılan ve kullanıma hazır hale getirilen gizli büyütme modeli. |
