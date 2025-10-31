> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/tr.md)

PerturbedAttentionGuidance düğümü, üretim kalitesini artırmak için bir difüzyon modeline bozulmuş dikkat kılavuzluğu uygular. Modelin öz-dikkat mekanizmasını örnekleme sırasında, değer projeksiyonlarına odaklanan basitleştirilmiş bir versiyonuyla değiştirir. Bu teknik, koşullu gürültü giderme sürecini ayarlayarak üretilen görüntülerin tutarlılığını ve kalitesini artırmaya yardımcı olur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Bozulmuş dikkat kılavuzluğu uygulanacak difüzyon modeli |
| `ölçek` | FLOAT | Hayır | 0.0 - 100.0 | Bozulmuş dikkat kılavuzluğu etkisinin gücü (varsayılan: 3.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Bozulmuş dikkat kılavuzluğu uygulanmış modifiye edilmiş model |