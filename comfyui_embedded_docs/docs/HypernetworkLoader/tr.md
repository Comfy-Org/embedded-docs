> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HypernetworkLoader/tr.md)

Bu düğüm, `ComfyUI/models/hypernetworks` klasöründe bulunan modelleri algılayacak ve ayrıca extra_model_paths.yaml dosyasında yapılandırılan ek yol(lar)dan da modelleri okuyacaktır. Bazen, ilgili klasörden model dosyalarını okuyabilmesi için **ComfyUI arayüzünü yenilemeniz** gerekebilir.

HypernetworkLoader düğümü, bir hiper ağ uygulayarak belirli bir modelin yeteneklerini geliştirmek veya değiştirmek için tasarlanmıştır. Belirtilen bir hiper ağı yükler ve model üzerinde, güç parametresine bağlı olarak modelin davranışını veya performansını potansiyel olarak değiştirecek şekilde uygular. Bu süreç, modelin mimarisi veya parametreleri üzerinde dinamik ayarlamalara izin vererek daha esnek ve uyarlanabilir yapay zeka sistemlerinin önünü açar.

## Girdiler

| Alan                 | Comfy Veri Türü   | Açıklama                                                                                  |
|-----------------------|-------------------|----------------------------------------------------------------------------------------------|
| `model`               | `MODEL`           | Hiper ağın uygulanacağı, geliştirilecek veya değiştirilecek mimariyi belirleyen temel model. |
| `hypernetwork_name`  | `COMBO[STRING]`   | Modele yüklenecek ve uygulanacak, modelin değiştirilmiş davranışını veya performansını etkileyen hiper ağın adı. |
| `strength`            | `FLOAT`           | Hiper ağın model üzerindeki etkisinin yoğunluğunu ayarlayan, değişikliklerin ince ayarına olanak tanıyan bir skaler değer. |

## Çıktılar

| Alan   | Veri Türü | Açıklama                                                              |
|---------|-------------|--------------------------------------------------------------------------|
| `model` | `MODEL`     | Hiper ağ uygulandıktan sonra, hiper ağın orijinal model üzerindeki etkisini sergileyen değiştirilmiş model. |