> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiTSimple/tr.md)

Gürültü giderme işlemi sırasında yalnızca koşulsuz geçişi değiştiren SkipLayerGuidanceDiT düğümünün basitleştirilmiş versiyonu. Bu düğüm, belirtilen zamanlama ve katman parametrelerine dayanarak koşulsuz geçiş sırasında belirli katmanları seçici bir şekilde atlayarak DiT (Diffusion Transformer) modellerindeki belirli transformer katmanlarına skip layer guidance uygular.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Skip layer guidance uygulanacak model |
| `double_layers` | STRING | Evet | - | Atlanacak çift blok katman indekslerinin virgülle ayrılmış listesi (varsayılan: "7, 8, 9") |
| `single_layers` | STRING | Evet | - | Atlanacak tek blok katman indekslerinin virgülle ayrılmış listesi (varsayılan: "7, 8, 9") |
| `start_percent` | FLOAT | Evet | 0.0 - 1.0 | Skip layer guidance'ın başladığı gürültü giderme işleminin başlangıç yüzdesi (varsayılan: 0.0) |
| `end_percent` | FLOAT | Evet | 0.0 - 1.0 | Skip layer guidance'ın durduğu gürültü giderme işleminin bitiş yüzdesi (varsayılan: 1.0) |

**Not:** Skip layer guidance yalnızca hem `double_layers` hem de `single_layers` geçerli katman indeksleri içerdiğinde uygulanır. Eğer her ikisi de boşsa, düğüm orijinal modeli değiştirilmeden döndürür.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Belirtilen katmanlara skip layer guidance uygulanmış değiştirilmiş model |