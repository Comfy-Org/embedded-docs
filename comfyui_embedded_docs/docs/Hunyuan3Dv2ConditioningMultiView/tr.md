# Hunyuan3Dv2ÇokluGörünümKoşullandırma

Hunyuan3Dv2ConditioningMultiView düğümü, 3D video oluşturma için çoklu görünüm CLIP görsel yerleştirmelerini işler. İsteğe bağlı olarak ön, sol, arka ve sağ görünüm yerleştirmelerini alır ve bunları konumsal kodlama ile birleştirerek video modelleri için koşullandırma verileri oluşturur. Düğüm, birleştirilmiş yerleştirmelerden pozitif koşullandırma ve sıfır değerlerle negatif koşullandırma çıktısı verir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ön` | Ön görünüm için CLIP görsel çıktısı | CLIP_VISION_OUTPUT | Hayır | - |
| `sol` | Sol görünüm için CLIP görsel çıktısı | CLIP_VISION_OUTPUT | Hayır | - |
| `arka` | Arka görünüm için CLIP görsel çıktısı | CLIP_VISION_OUTPUT | Hayır | - |
| `sağ` | Sağ görünüm için CLIP görsel çıktısı | CLIP_VISION_OUTPUT | Hayır | - |

**Not:** Düğümün çalışması için en az bir görünüm girişi sağlanmalıdır. Düğüm, yalnızca geçerli CLIP görsel çıktı verisi içeren görünümleri işleyecektir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `negative` | Konumsal kodlama ile birleştirilmiş çoklu görünüm yerleştirmelerini içeren pozitif koşullandırma | CONDITIONING |
| `negative` | Karşılaştırmalı öğrenme için sıfır değerlerle negatif koşullandırma | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/tr.md)

---
**Source fingerprint (SHA-256):** `01998ae9ba7d2ae9a2f6a0b5aee4c03168f935fb9769317cd80d93a7a4b96f13`
