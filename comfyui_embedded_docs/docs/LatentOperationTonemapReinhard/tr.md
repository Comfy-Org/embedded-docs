# GizliİşlemTonEşlemeReinhard

Bu düğüm, latent vektörlere Reinhard ton eşlemesi uygulayan bir latent işlemi oluşturur. Her latent vektörü normalleştirir, genel büyüklük dağılımını (ortalama ve standart sapma) ölçer ve ardından Reinhard eğrisini kullanarak aşırı büyüklükleri sıkıştırır; genel güç, bir çarpan ile kontrol edilir. Düğüm deneysel olarak işaretlenmiştir (ayrıca "hdr latent" olarak aranabilir).

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `çarpan` | Ton eşleme etkisinin yoğunluğunu kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 (adım 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `operation` | Latent vektörlere uygulanabilen bir ton eşleme işlemi döndürür | LATENT_OPERATION |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/tr.md)

---
**Source fingerprint (SHA-256):** `19d58c288967ab27eb1e84e60bc35a6d6c8b4e643168de689132396ae0ee3cbe`
