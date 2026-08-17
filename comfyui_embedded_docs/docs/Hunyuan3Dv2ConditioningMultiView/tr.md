# Hunyuan3Dv2ÇokluGörünümKoşullandırma

Hunyuan3Dv2ConditioningMultiView düğümü, 3D video üretimi için çok görünümlü CLIP görüş yerleştirmelerini işler. Ön, sol, arka ve sağ görünüm yerleştirmelerini isteğe bağlı olarak alır ve bunları tek bir conditioning dizisinde birleştirmeden önce sağlanan her görünüme konumsal kodlama ekler. Düğüm, birleştirilmiş yerleştirmelerden hem pozitif conditioning hem de sıfır değerli negatif conditioning çıktısı üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `front` | Ön görünüm için CLIP görüş çıktısı | CLIP_VISION_OUTPUT | Hayır | - |
| `left` | Sol görünüm için CLIP görüş çıktısı | CLIP_VISION_OUTPUT | Hayır | - |
| `back` | Arka görünüm için CLIP görüş çıktısı | CLIP_VISION_OUTPUT | Hayır | - |
| `right` | Sağ görünüm için CLIP görüş çıktısı | CLIP_VISION_OUTPUT | Hayır | - |

**Not:** Düğümün çalışması için en az bir görünüm girdisi sağlanmalıdır. Düğüm yalnızca geçerli CLIP görüş çıktı verisi içeren görünümleri işler. Sağlanan her görünüm, görünüm konumuna (ön, sol, arka, sağ) göre bir konumsal kodlama alır ve kodlanmış görünümler aynı sırayla birleştirilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Konumsal kodlama ile birleştirilmiş çok görünümlü yerleştirmeleri içeren pozitif conditioning | CONDITIONING |
| `negative` | Pozitif conditioning ile aynı şekle sahip sıfır değerleri içeren negatif conditioning | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/tr.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
