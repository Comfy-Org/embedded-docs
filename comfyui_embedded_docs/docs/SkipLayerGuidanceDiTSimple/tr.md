> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiTSimple/tr.md)

SkipLayerGuidanceDiT düğümünün, gürültü giderme işlemi sırasında yalnızca koşulsuz geçişi değiştiren basit sürümü. Bu düğüm, belirtilen zamanlama ve katman parametrelerine göre koşulsuz geçiş sırasında belirli katmanları seçmeli olarak atlayarak DiT (Difüzyon Transformer) modellerindeki belirli transformer katmanlarına atlama katmanı yönlendirmesi uygular.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-----------|
| `model` | MODEL | Evet | - | Atlama katmanı yönlendirmesinin uygulanacağı model |
| `double_layers` | STRING | Hayır | - | Atlanacak çift blok katman indekslerinin virgülle ayrılmış listesi (varsayılan: "7, 8, 9") |
| `single_layers` | STRING | Hayır | - | Atlanacak tek blok katman indekslerinin virgülle ayrılmış listesi (varsayılan: "7, 8, 9") |
| `start_percent` | FLOAT | Hayır | 0.0 - 1.0 | Atlama katmanı yönlendirmesinin başladığı gürültü giderme işleminin başlangıç yüzdesi (varsayılan: 0.0) |
| `end_percent` | FLOAT | Hayır | 0.0 - 1.0 | Atlama katmanı yönlendirmesinin durduğu gürültü giderme işleminin bitiş yüzdesi (varsayılan: 1.0) |

**Not:** Atlama katmanı yönlendirmesi yalnızca hem `double_layers` hem de `single_layers` geçerli katman indeksleri içerdiğinde uygulanır. Her ikisi de boşsa, düğüm orijinal modeli değiştirmeden döndürür. Atlama katmanı yönlendirmesi yalnızca mevcut gürültü giderme adımının sigma değeri `start_percent` ile `end_percent` arasında olduğunda (dahili olarak sigma değerlerine dönüştürülür) etkindir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model` | MODEL | Belirtilen katmanlara atlama katmanı yönlendirmesi uygulanmış değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `6795a67a63d9aa8b2adea3d96e49272d88c21d0642bb507e175a2fcf3a125f98`
