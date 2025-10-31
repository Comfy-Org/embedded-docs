> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAELoader/tr.md)

Bu düğüm, `ComfyUI/models/vae` klasöründe bulunan modelleri algılayacak ve ayrıca extra_model_paths.yaml dosyasında yapılandırılan ek yollardan modelleri okuyacaktır. Bazen, ilgili klasörden model dosyalarını okuyabilmesi için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

VAELoader düğümü, Varyasyonel Otokodlayıcı (VAE) modellerini yüklemek için tasarlanmış olup, hem standart hem de yaklaşık VAE'leri işlemeye özel olarak uyarlanmıştır. VAE'leri isme göre yüklemeyi destekler, 'taesd' ve 'taesdxl' modelleri için özel işleme içerir ve VAE'nin spesifik konfigürasyonuna bağlı olarak dinamik olarak uyum sağlar.

## Girdiler

| Alan       | Comfy Veri Türü   | Açıklama                                                                                   |
|------------|-------------------|-----------------------------------------------------------------------------------------------|
| `vae_name` | `COMBO[STRING]`    | Yüklenecek VAE'nin adını belirtir, hangi VAE modelinin getirileceğini ve yükleneceğini belirler; 'taesd' ve 'taesdxl' dahil olmak üzere bir dizi önceden tanımlanmış VAE adını destekler. |

## Çıktılar

| Alan  | Veri Türü | Açıklama                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `vae`  | `VAE`       | Kodlama veya kod çözme gibi ileri operasyonlar için hazır olarak yüklenen VAE modelini döndürür. Çıktı, yüklenen modelin durumunu içeren bir model nesnesidir. |