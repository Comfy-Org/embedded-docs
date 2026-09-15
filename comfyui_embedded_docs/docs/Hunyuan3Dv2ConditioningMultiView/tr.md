# Hunyuan3Dv2ÇokluGörünümKoşullandırma

Hunyuan3Dv2ConditioningMultiView düğümü, en fazla dört görünümden (ön, sol, arka ve sağ) gelen CLIP vision çıktılarını tek bir çok görünümlü koşullandırmada birleştirir. Sağlanan her görünümün CLIP vision gömme vektörüne bir konumsal kodlama eklenir ve elde edilen gömme vektörleri birleştirilir. Düğüm, birleştirilmiş gömme vektörlerine dayanan bir pozitif koşullandırma ve aynı şekle sahip sıfırlarla doldurulmuş bir negatif koşullandırma verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `ön` | Ön görünüm için CLIP vision çıktısı. İsteğe bağlı görünüm girdisi. | CLIP_VISION_OUTPUT | Hayır | - |
| `sol` | Sol görünüm için CLIP vision çıktısı. İsteğe bağlı görünüm girdisi. | CLIP_VISION_OUTPUT | Hayır | - |
| `arka` | Arka görünüm için CLIP vision çıktısı. İsteğe bağlı görünüm girdisi. | CLIP_VISION_OUTPUT | Hayır | - |
| `sağ` | Sağ görünüm için CLIP vision çıktısı. İsteğe bağlı görünüm girdisi. | CLIP_VISION_OUTPUT | Hayır | - |

**Not:** Düğümün çalışması için en az bir görünüm girdisi sağlanmalıdır. Düğüm yalnızca geçerli CLIP vision çıktı verisi içeren görünümleri işler ve bağlı olmayan görünümleri atlar. Her görünüm, yuvasına (ön, sol, arka, sağ) göre sabit bir konumsal kodlama alır ve sağlanan tüm görünümlerden işlenen gömme vektörleri dizi boyutu boyunca birleştirilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Konumsal kodlamalı birleştirilmiş çok görünümlü gömme vektörlerini içeren pozitif koşullandırma. | CONDITIONING |
| `negative` | Pozitif koşullandırmanın şekliyle eşleşen sıfır değerlerine sahip negatif koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/tr.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
