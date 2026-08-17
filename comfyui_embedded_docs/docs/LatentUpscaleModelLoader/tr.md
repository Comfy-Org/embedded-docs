# Latent Büyütme Modelini Yükle

LatentUpscaleModelLoader düğümü, latent temsilleri büyütmek için tasarlanmış özel bir modeli yükler. Sistemin belirlenmiş klasöründen bir model dosyası okur ve doğru dahili model mimarisini oluşturup yapılandırmak için türünü (720p, 1080p veya diğer) otomatik olarak algılar. Yüklenen model daha sonra latent uzay süper çözünürlük görevleri için diğer düğümler tarafından kullanılmaya hazırdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model_name` | Yüklenecek latent büyütme modeli dosyasının adı. Kullanılabilir seçenekler, ComfyUI'nizin `latent_upscale_models` dizininde bulunan dosyalardan dinamik olarak doldurulur. | COMBO | Evet | `latent_upscale_models` klasöründeki tüm dosyalar |

Not: Düğüm, model mimarisini dosya içeriğinden otomatik olarak algılar. 720p HunyuanVideo süper çözünürlük katmanları içeren modeller 720p model olarak yüklenir, 1080p tarzı yukarı örnekleme katmanlarına sahip modeller 1080p model olarak yüklenir ve diğer katman yapılarına sahip modeller LatentUpsampler model olarak yüklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Yüklenen latent büyütme modeli, yapılandırılmış ve kullanıma hazır. | LATENT_UPSCALE_MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/tr.md)

---
**Source fingerprint (SHA-256):** `7e23214b1b1fc11be84910a5a209c7990a5199120cb0e6b6c61302a442dcf153`
