# FluxRehberliğiDevreDışıBırak

Bu düğüm, Flux ve Flux benzeri modellerde guidance embed'ini tamamen devre dışı bırakır. Girdi olarak conditioning verisini alır ve guidance değerini None olarak ayarlar; böylece üretim süreci için guidance tabanlı conditioning'i etkili bir şekilde kapatır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `conditioning` | İşlenecek ve guidance'ın kaldırılacağı conditioning verisi | CONDITIONING | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `conditioning` | Guidance devre dışı bırakılmış, değiştirilmiş conditioning verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/tr.md)

---
**Source fingerprint (SHA-256):** `da3286194f9f5e7e49dd7047d6b0a0c97bb2570eaa9281abbd3992a743302fbf`
