# Kayıp Grafiği Çiz

LossGraphNode, eğitim kayıp değerlerinin zaman içindeki görsel grafiğini oluşturur ve bunu bir önizleme görüntüsü olarak görüntüler. Eğitim süreçlerinden gelen kayıp verilerini alır ve kaybın eğitim adımları boyunca nasıl değiştiğini gösteren bir çizgi grafiği oluşturur. Ortaya çıkan grafik, eksen etiketlerini ve minimum/maksimum kayıp değerlerini içerir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `kayıp` | Eğitim düğümünden gelen kayıp haritası. | LOSS_MAP | Evet | - |
| `dosya_adı_ön_eki` | Kaydedilen kayıp grafiği görüntüsü için ön ek. (varsayılan: "loss_graph") | STRING | Evet | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `ui.images` | Önizleme olarak görüntülenen oluşturulan kayıp grafiği görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/tr.md)

---
**Source fingerprint (SHA-256):** `9b1c844cb4babafc61102ee7bfd1039c325c6665abff1721d92a6da7d18029f9`
