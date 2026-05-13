> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/tr.md)

Hunyuan3Dv2ConditioningMultiView düğümü, 3D video oluşturma için çoklu görünüm CLIP görsel yerleştirmelerini işler. İsteğe bağlı olarak ön, sol, arka ve sağ görünüm yerleştirmelerini alır ve bunları konumsal kodlama ile birleştirerek video modelleri için koşullandırma verileri oluşturur. Düğüm, birleştirilmiş yerleştirmelerden pozitif koşullandırma ve sıfır değerlerle negatif koşullandırma çıktısı verir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `front` | CLIP_VISION_OUTPUT | Hayır | - | Ön görünüm için CLIP görsel çıktısı |
| `left` | CLIP_VISION_OUTPUT | Hayır | - | Sol görünüm için CLIP görsel çıktısı |
| `back` | CLIP_VISION_OUTPUT | Hayır | - | Arka görünüm için CLIP görsel çıktısı |
| `right` | CLIP_VISION_OUTPUT | Hayır | - | Sağ görünüm için CLIP görsel çıktısı |

**Not:** Düğümün çalışması için en az bir görünüm girişi sağlanmalıdır. Düğüm, yalnızca geçerli CLIP görsel çıktı verisi içeren görünümleri işleyecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `positive` | CONDITIONING | Konumsal kodlama ile birleştirilmiş çoklu görünüm yerleştirmelerini içeren pozitif koşullandırma |
| `negative` | CONDITIONING | Karşılaştırmalı öğrenme için sıfır değerlerle negatif koşullandırma |

---
**Source fingerprint (SHA-256):** `01998ae9ba7d2ae9a2f6a0b5aee4c03168f935fb9769317cd80d93a7a4b96f13`
