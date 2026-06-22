# FluxRehberliğiDevreDışıBırak

Bu düğüm, Flux ve benzeri modeller için rehberlik gömme işlevini tamamen devre dışı bırakır. Giriş olarak koşullandırma verilerini alır ve rehberlik bileşenini `None` olarak ayarlayarak kaldırır, böylece üretim süreci için rehberlik tabanlı koşullandırmayı etkili bir şekilde kapatır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `koşullandırma` | Rehberliğin kaldırılacağı ve işlenecek koşullandırma verileri | CONDITIONING | Evet | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `koşullandırma` | Rehberlik devre dışı bırakılmış şekilde değiştirilmiş koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/tr.md)

---
**Source fingerprint (SHA-256):** `37e544460d5e50542cebb451997c0320f16d822cc5695cb34825d2038866a455`
