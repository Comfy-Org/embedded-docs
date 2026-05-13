> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAELoader/tr.md)

Bu düğüm, `ComfyUI/models/vae` klasöründe bulunan modelleri algılar ve ayrıca extra_model_paths.yaml dosyasında yapılandırılan ek yollardaki modelleri de okur. Bazen, ilgili klasördeki model dosyalarını okuyabilmesi için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

VAELoader düğümü, Varyasyonel Otomatik Kodlayıcı (VAE) modellerini yüklemek için tasarlanmıştır ve hem standart hem de yaklaşık VAE'leri işlemek üzere özelleştirilmiştir. VAE'leri ada göre yüklemeyi destekler; 'taesd' ve 'taesdxl' modelleri için özel işleme dahil olmak üzere, VAE'nin belirli yapılandırmasına göre dinamik olarak ayarlama yapar.

## Girişler

| Alan | Comfy veri türü | Açıklama |
|---------|-------------------|-----------------------------------------------------------------------------------------------|
| `vae_name` | `COMBO[STRING]` | Yüklenecek VAE'nin adını belirtir; hangi VAE modelinin getirilip yükleneceğini belirler ve 'taesd' ile 'taesdxl' dahil olmak üzere önceden tanımlanmış bir dizi VAE adını destekler. |

## Çıkışlar

| Alan | Veri Türü | Açıklama |
|-------|-------------|--------------------------------------------------------------------------|
| `vae` | `VAE` | Kodlama veya kod çözme gibi daha ileri işlemler için hazır, yüklenmiş VAE modelini döndürür. Çıktı, yüklenen modelin durumunu kapsayan bir model nesnesidir. |