> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StyleModelApply/tr.md)

Bu düğüm, bir CLIP görme modelinin çıktısına dayanarak belirli bir koşullandırmaya (conditioning) bir stil modeli uygular, stilini geliştirir veya değiştirir. Stil modelinin koşullandırmasını mevcut koşullandırmaya entegre ederek, üretim sürecinde stillerin sorunsuz bir şekilde harmanlanmasını sağlar.

## Girişler

### Zorunlu

| Parametre            | Comfy veri türü      | Açıklama |
|-----------------------|-----------------------|-------------|
| `koşullandırma`        | `CONDITIONING`       | Stil modelinin koşullandırmasının uygulanacağı orijinal koşullandırma verisi. Geliştirilecek veya değiştirilecek temel bağlamı veya stili tanımlamak için çok önemlidir. |
| `stil_modeli`         | `STYLE_MODEL`        | CLIP görme modelinin çıktısına dayanarak yeni koşullandırma oluşturmak için kullanılan stil modeli. Uygulanacak yeni stili tanımlamada anahtar rol oynar. |
| `clip_görü_çıktısı`  | `CLIP_VISION_OUTPUT` | Stil modelinin yeni koşullandırma oluşturmak için kullandığı bir CLIP görme modelinin çıktısı. Stil uygulaması için gerekli görsel bağlamı sağlar. |

## Çıktılar

| Parametre            | Comfy veri türü      | Açıklama |
|----------------------|-----------------------|-------------|
| `koşullandırma`       | `CONDITIONING`        | Stil modelinin çıktısını içeren, geliştirilmiş veya değiştirilmiş koşullandırma. Daha sonraki işlemlere veya üretime hazır, son halini almış, stillendirilmiş koşullandırmayı temsil eder. |