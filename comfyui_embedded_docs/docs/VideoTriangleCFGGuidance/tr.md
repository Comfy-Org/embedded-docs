> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/tr.md)

VideoTriangleCFGGuidance düğümü, video modellerine üçgen şeklinde bir sınıflandırıcısız kılavuzlama ölçeklendirme deseni uygular. Koşullandırma ölçeğini, minimum CFG değeri ile orijinal koşullandırma ölçeği arasında salınan bir üçgen dalga fonksiyonu kullanarak zaman içinde değiştirir. Bu, video oluşturma tutarlılığını ve kalitesini artırmaya yardımcı olabilecek dinamik bir kılavuzlama deseni oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Üçgen CFG kılavuzluğunun uygulanacağı video modeli |
| `min_cfg` | FLOAT | Evet | 0.0 - 100.0 | Üçgen desen için minimum CFG ölçek değeri (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Üçgen CFG kılavuzluğu uygulanmış modifiye edilmiş model |