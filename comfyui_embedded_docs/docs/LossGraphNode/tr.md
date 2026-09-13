# Kayıp Grafiği Çiz

LossGraphNode, eğitim kaybı değerlerinin eğitim adımlarına göre çizgi grafiğini oluşturur ve bunu bir önizleme görüntüsü olarak gösterir. Bir eğitim düğümünden kayıp değerlerini okur, bunları etiketli eksenler ve minimum/maksimum kayıp değerleriyle bir grafik üzerinde çizer ve grafiği kullanıcı arayüzünde görüntü önizlemesi olarak döndürür. Bu düğüm deneysel olarak işaretlenmiştir ve bir çıktı düğümüdür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `kayıp` | Eğitim düğümünden gelen kayıp haritası. Sayısal kayıp değerlerinden oluşan bir liste içeren bir `loss` anahtarı içermelidir. | LOSS_MAP | Evet | - |
| `dosya_adı_ön_eki` | Kaydedilen kayıp grafiği görüntüsü için önek. (varsayılan: "loss_graph") | STRING | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `ui.images` | Önizleme olarak görüntülenen oluşturulmuş kayıp grafiği görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/tr.md)

---
**Source fingerprint (SHA-256):** `b1f0b72a03d4ce2d9461fc6e312bd1e847455f7dd5227667876a945494ea8cdb`
