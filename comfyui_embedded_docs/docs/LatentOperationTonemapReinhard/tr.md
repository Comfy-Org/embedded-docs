# GizliİşlemTonEşlemeReinhard

LatentOperationTonemapReinhard düğümü, latent vektörlere Reinhard ton eşleme uygular. Bu teknik, latent vektörleri normalize eder ve büyüklüklerini ortalama ve standart sapmaya dayalı istatistiksel bir yaklaşımla ayarlar; yoğunluk, bir çarpan parametresiyle kontrol edilir. Bu düğüm şu anda deneysel olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `çarpan` | Ton eşleme efektinin yoğunluğunu kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 100.0 (step 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `operation` | Latent vektörlere uygulanabilen bir ton eşleme işlemi döndürür | LATENT_OPERATION |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/tr.md)

---
**Source fingerprint (SHA-256):** `19d58c288967ab27eb1e84e60bc35a6d6c8b4e643168de689132396ae0ee3cbe`
