# Latent Büyütme Modelini Yükle

LatentUpscaleModelLoader düğümü, gizli (latent) temsilleri yükseltmek için tasarlanmış özel bir model yükler. Sistemin belirlenmiş klasöründen bir model dosyası okur ve türünü (720p, 1080p veya diğer) otomatik olarak algılayarak doğru dahili model mimarisini başlatır ve yapılandırır. Yüklenen model daha sonra diğer düğümler tarafından gizli alan süper çözünürlük görevleri için kullanılmaya hazır hale gelir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model_name` | Yüklenecek gizli yükseltme modeli dosyasının adı. Kullanılabilir seçenekler, ComfyUI'nizin `latent_upscale_models` dizininde bulunan dosyalardan dinamik olarak doldurulur. | STRING | Evet | `latent_upscale_models` klasöründeki tüm dosyalar |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Yapılandırılmış ve kullanıma hazır, yüklenmiş gizli yükseltme modeli. | LATENT_UPSCALE_MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/tr.md)

---
**Source fingerprint (SHA-256):** `bd97f3ec1422aaabbd60779aa4112be44791daddc6307de53ae0e4219a90ab0e`
