> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/tr.md)

Hunyuan3Dv2ConditioningMultiView düğümü, 3D video üretimi için çok görüntülü CLIP görüntü yerleştirmelerini işler. İsteğe bağlı ön, sol, arka ve sağ görüntü yerleştirmelerini alır ve bunları video modelleri için koşullandırma verisi oluşturmak üzere konumsal kodlama ile birleştirir. Düğüm, birleştirilmiş yerleştirmelerden elde edilen pozitif koşullandırma ve sıfır değerlerle negatif koşullandırma olmak üzere her ikisini de çıktı olarak verir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `front` | CLIP_VISION_OUTPUT | Hayır | - | Ön görüntü için CLIP görüntü çıktısı |
| `left` | CLIP_VISION_OUTPUT | Hayır | - | Sol görüntü için CLIP görüntü çıktısı |
| `back` | CLIP_VISION_OUTPUT | Hayır | - | Arka görüntü için CLIP görüntü çıktısı |
| `right` | CLIP_VISION_OUTPUT | Hayır | - | Sağ görüntü için CLIP görüntü çıktısı |

**Not:** Düğümün çalışması için en az bir görüntü girdisi sağlanmalıdır. Düğüm yalnızca geçerli CLIP görüntü çıktı verisi içeren görüntüleri işleyecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Konumsal kodlama ile birleştirilmiş çok görüntülü yerleştirmeleri içeren pozitif koşullandırma |
| `negative` | CONDITIONING | Karşılaştırmalı öğrenme için sıfır değerlerle negatif koşullandırma |