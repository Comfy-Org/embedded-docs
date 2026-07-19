# Sadece Görüntü Kontrol Noktası Yükleyici (img2vid modeli)

Bu düğüm, `ComfyUI/models/checkpoints` klasöründe bulunan modelleri algılar ve ayrıca extra_model_paths.yaml dosyasında yapılandırılmış ek yollardaki modelleri de okur. Bazen, ilgili klasördeki model dosyalarını okuması için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

Bu düğüm, video oluşturma iş akışlarında özellikle görüntü tabanlı modeller için kontrol noktaları (checkpoint) yükleme konusunda uzmanlaşmıştır. Belirli bir kontrol noktasından gerekli bileşenleri verimli bir şekilde alır ve yapılandırır, modelin görüntüyle ilgili yönlerine odaklanır.

## Girişler

| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `ckpt_adı` | Yüklenecek kontrol noktasının adını belirtir. Önceden tanımlanmış bir listeden doğru kontrol noktası dosyasını tanımlamak ve almak için çok önemlidir. | COMBO[STRING] |

## Çıkışlar

| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Kontrol noktasından yüklenen, video oluşturma bağlamlarında görüntü işleme için yapılandırılmış ana modeli döndürür. | MODEL |
| `clip_vision` | Kontrol noktasından, görüntü anlama ve özellik çıkarma için uyarlanmış CLIP görüş bileşenini sağlar. | `CLIP_VISION` |
| `vae` | Görüntü işleme ve oluşturma görevleri için gerekli olan Varyasyonel Otomatik Kodlayıcı (VAE) bileşenini sunar. | VAE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointLoader/tr.md)
