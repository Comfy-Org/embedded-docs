# FluxRehberliğiDevreDışıBırak

Bu düğüm, Flux ve Flux benzeri modeller için guidance embed işlevini tamamen devre dışı bırakır. Koşullandırma verisini girdi olarak alır, guidance bileşenini None olarak ayarlayarak kaldırır ve değiştirilmiş koşullandırma verisini döndürür; böylece üretim sürecinde guidance tabanlı koşullandırmayı etkili bir şekilde kapatır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `conditioning` | Guidance'ın kaldırılması için işlenecek koşullandırma verisi | CONDITIONING | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `conditioning` | Guidance devre dışı bırakılmış değiştirilmiş koşullandırma verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/tr.md)

---
**Source fingerprint (SHA-256):** `da3286194f9f5e7e49dd7047d6b0a0c97bb2570eaa9281abbd3992a743302fbf`
