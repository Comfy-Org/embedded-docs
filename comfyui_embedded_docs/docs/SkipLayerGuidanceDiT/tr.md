> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiT/tr.md)

Detaylı yapıya doğru rehberliği, atlanmış katmanlara sahip başka bir CFG negatif seti kullanarak geliştirir. SkipLayerGuidance'ın bu genel versiyonu, her DiT modelinde kullanılabilir ve Perturbed Attention Guidance'dan ilham almıştır. Orijinal deneysel uygulama SD3 için oluşturulmuştur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Atlanmış katman rehberliğinin uygulanacağı model |
| `double_layers` | STRING | Evet | - | Çift bloklar için atlanacak virgülle ayrılmış katman numaraları (varsayılan: "7, 8, 9") |
| `single_layers` | STRING | Evet | - | Tek bloklar için atlanacak virgülle ayrılmış katman numaraları (varsayılan: "7, 8, 9") |
| `scale` | FLOAT | Evet | 0.0 - 10.0 | Rehberlik ölçek faktörü (varsayılan: 3.0) |
| `start_percent` | FLOAT | Evet | 0.0 - 1.0 | Rehberlik uygulaması için başlangıç yüzdesi (varsayılan: 0.01) |
| `end_percent` | FLOAT | Evet | 0.0 - 1.0 | Rehberlik uygulaması için bitiş yüzdesi (varsayılan: 0.15) |
| `rescaling_scale` | FLOAT | Evet | 0.0 - 10.0 | Yeniden ölçeklendirme ölçek faktörü (varsayılan: 0.0) |

**Not:** Hem `double_layers` hem de `single_layers` boşsa (hiç katman numarası içermiyorsa), düğüm herhangi bir rehberlik uygulamadan orijinal modeli döndürür.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Atlanmış katman rehberliği uygulanmış modifiye edilmiş model |