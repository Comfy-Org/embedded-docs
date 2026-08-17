# Kayıp Grafiği Çiz

LossGraphNode, eğitim kaybı değerlerinin zaman içindeki görsel bir grafiğini oluşturur ve bunu bir önizleme görüntüsü olarak görüntüler. Eğitim süreçlerinden kayıp verilerini alır ve kaybın eğitim adımları boyunca nasıl değiştiğini gösteren bir çizgi grafiği üretir. Ortaya çıkan grafik, eksen etiketlerini ve minimum/maksimum kayıp değerlerini içerir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `loss` | Eğitim düğümünden gelen kayıp haritası. Grafiği çizmek için kullanılan kayıp değerlerinin bir listesini içeren bir `loss` anahtarı içermelidir. | LOSS_MAP | Evet | - |
| `filename_prefix` | Kaydedilen kayıp grafiği görüntüsü için önek. (varsayılan: "loss_graph") | STRING | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `ui.images` | Oluşturulan kayıp grafiği görüntüsü önizleme olarak görüntülenir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/tr.md)

---
**Source fingerprint (SHA-256):** `b1f0b72a03d4ce2d9461fc6e312bd1e847455f7dd5227667876a945494ea8cdb`
