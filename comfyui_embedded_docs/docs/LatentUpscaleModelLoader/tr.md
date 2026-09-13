# Latent Büyütme Modelini Yükle

LatentUpscaleModelLoader düğümü, ComfyUI'nin `latent_upscale_models` klasöründe saklanan bir dosyadan latent temsilleri büyütme konusunda uzmanlaşmış bir model yükler. Model mimarisini dosya içeriğinden otomatik olarak algılar (Hunyuan Video 720p, Hunyuan Video 1080p veya bir Latent Upsampler) ve eşleşen dahili modeli yapılandırır; böylece sonuç diğer düğümler tarafından kullanılmaya hazır olur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model_name` | Yüklenecek latent büyütme modeli dosyasının adı. Kullanılabilir seçenekler ComfyUI'nin `latent_upscale_models` dizininde bulunan dosyalara göre dinamik olarak doldurulur. | COMBO | Evet | `latent_upscale_models` klasöründeki tüm dosyalar |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Yüklenen latent büyütme modeli, yapılandırılmış ve kullanıma hazır. Algılanan dosya içeriğine bağlı olarak bu, 720p Hunyuan Video büyütücüsü, 1080p Hunyuan Video büyütücüsü veya sarmalanmış bir Latent Upsampler modelidir. | LATENT_UPSCALE_MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/tr.md)

---
**Source fingerprint (SHA-256):** `7e23214b1b1fc11be84910a5a209c7990a5199120cb0e6b6c61302a442dcf153`
