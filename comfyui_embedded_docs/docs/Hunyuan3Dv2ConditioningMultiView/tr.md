# Hunyuan3Dv2ÇokluGörünümKoşullandırma

Hunyuan3Dv2ConditioningMultiView düğümü, dört görünüme kadar (ön, sol, arka ve sağ) CLIP görüş çıktılarını tek bir çok görünümlü koşullandırmada birleştirir. Sağlanan her görünümün CLIP görüş yerleştirmesine konumsal kodlama eklenir ve ortaya çıkan yerleştirmeler birleştirilir. Düğüm, birleştirilmiş yerleştirmelere dayalı pozitif bir koşullandırma ve aynı şekle sahip sıfırlarla doldurulmuş negatif bir koşullandırma çıkarır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `ön` | Ön görünüm için CLIP görüş çıktısı. İsteğe bağlı görünüm girdisi. | CLIP_VISION_OUTPUT | Hayır | - |
| `sol` | Sol görünüm için CLIP görüş çıktısı. İsteğe bağlı görünüm girdisi. | CLIP_VISION_OUTPUT | Hayır | - |
| `arka` | Arka görünüm için CLIP görüş çıktısı. İsteğe bağlı görünüm girdisi. | CLIP_VISION_OUTPUT | Hayır | - |
| `sağ` | Sağ görünüm için CLIP görüş çıktısı. İsteğe bağlı görünüm girdisi. | CLIP_VISION_OUTPUT | Hayır | - |

**Not:** Düğümün çalışması için en az bir görünüm girdisi sağlanmalıdır. Düğüm yalnızca geçerli CLIP görüş çıktı verisi içeren görünümleri işler ve bağlı olmayan görünümleri atlar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Konumsal kodlama ile birleştirilmiş çok görünümlü yerleştirmeleri içeren pozitif koşullandırma. | CONDITIONING |
| `negative` | Pozitif koşullandırma şekliyle eşleşen sıfır değerlere sahip negatif koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/tr.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
