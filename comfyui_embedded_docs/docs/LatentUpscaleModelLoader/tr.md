# Latent Büyütme Modelini Yükle

LatentUpscaleModelLoader düğümü, ComfyUI'nin `latent_upscale_models` klasöründe saklanan bir dosyadan latent temsilleri yükseltme konusunda uzmanlaşmış bir model yükler. Model türünü (720p, 1080p veya başka bir latent yükseltici) dosya içeriğinden otomatik olarak algılar ve eşleşen dahili mimariyi yapılandırarak yüklenen modeli diğer düğümler tarafından kullanıma hazır hale getirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model_name` | Yüklenecek latent yükseltme modeli dosyasının adı. Kullanılabilir seçenekler, ComfyUI'nin `latent_upscale_models` dizininde bulunan dosyalardan dinamik olarak doldurulur. | COMBO | Evet | `latent_upscale_models` klasöründeki tüm dosyalar |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Yüklenen latent yükseltme modeli, kullanıma hazır şekilde yapılandırılmıştır. | LATENT_UPSCALE_MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/tr.md)

---
**Source fingerprint (SHA-256):** `7e23214b1b1fc11be84910a5a209c7990a5199120cb0e6b6c61302a442dcf153`
