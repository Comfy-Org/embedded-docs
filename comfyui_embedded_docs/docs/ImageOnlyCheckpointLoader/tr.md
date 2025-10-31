> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointLoader/tr.md)

Bu düğüm, `ComfyUI/models/checkpoints` klasöründe bulunan modelleri algılayacak ve ayrıca extra_model_paths.yaml dosyasında yapılandırılan ek yollardan modelleri okuyacaktır. Bazen, ilgili klasörden model dosyalarını okuyabilmesi için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

Bu düğüm, video oluşturma iş akışları içinde özellikle görüntü tabanlı modeller için kontrol noktalarını yüklemekte uzmanlaşmıştır. Belirli bir kontrol noktasından gerekli bileşenleri verimli bir şekilde alır ve modelin görüntüyle ilgili yönlerine odaklanarak yapılandırır.

## Girdiler

| Alan       | Veri Türü    | Açıklama                                                                       |
|------------|-------------|-----------------------------------------------------------------------------------|
| `ckpt_name`| COMBO[STRING] | Önceden tanımlanmış bir listeden doğru kontrol noktası dosyasını tanımlamak ve almak için kritik öneme sahip olan, yüklenecek kontrol noktasının adını belirtir. |

## Çıktılar

| Alan         | Veri Türü    | Açıklama                                                                                   |
|-----------|-------------|-----------------------------------------------------------------------------------------------|
| `model`   | MODEL     | Kontrol noktasından yüklenen, video oluşturma bağlamlarında görüntü işleme için yapılandırılmış ana modeli döndürür. |
| `clip_vision` | `CLIP_VISION` | Kontrol noktasından alınan, görüntü anlama ve özellik çıkarımı için uyarlanmış CLIP görüş bileşenini sağlar. |
| `vae`     | VAE       | Görüntü manipülasyonu ve oluşturma görevleri için gerekli olan Varyasyonel Otokodlayıcı (VAE) bileşenini sağlar. |