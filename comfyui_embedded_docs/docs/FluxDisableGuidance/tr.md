# FluxRehberliğiDevreDışıBırak

Bu düğüm, Flux ve Flux benzeri modellerde guidance embed bileşenini tamamen devre dışı bırakır. Girdi olarak conditioning verisi alır ve guidance bileşenini None olarak ayarlayarak kaldırır; böylece üretim sürecinde guidance tabanlı conditioning'i etkili bir şekilde kapatır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `koşullandırma` | Üzerinde işlem yapılacak ve guidance bileşeni kaldırılacak conditioning verisi | CONDITIONING | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `conditioning` | Guidance devre dışı bırakılmış, değiştirilmiş conditioning verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/tr.md)

---
**Source fingerprint (SHA-256):** `da3286194f9f5e7e49dd7047d6b0a0c97bb2570eaa9281abbd3992a743302fbf`
