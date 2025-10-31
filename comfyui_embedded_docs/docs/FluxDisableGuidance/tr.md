> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/tr.md)

Bu düğüm, Flux ve benzeri modeller için kılavuz gömme işlevini tamamen devre dışı bırakır. Girdi olarak koşullandırma verisini alır ve kılavuz bileşenini None olarak ayarlayarak kaldırır, böylece üretim süreci için kılavuz tabanlı koşullandırmayı etkin bir şekilde kapatır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | Evet | - | İşlenecek ve kılavuzdan arındırılacak koşullandırma verisi |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Kılavuzu devre dışı bırakılmış şekilde değiştirilmiş koşullandırma verisi |