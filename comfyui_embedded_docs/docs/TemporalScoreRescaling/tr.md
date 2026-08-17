# TSR - Zamansal Skor Yeniden Ölçeklendirme

Bu düğüm, bir difüzyon modeline Temporal Score Rescaling (TSR) uygular. Gürültü giderme işlemi sırasında tahmin edilen gürültüyü veya skoru yeniden ölçeklendirerek modelin örnekleme davranışını değiştirir; bu, üretilen çıktının çeşitliliğini yönlendirebilir. Bu, CFG (Classifier-Free Guidance) sonrası bir işlev olarak uygulanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | TSR işleviyle yamalanacak difüzyon modeli. | MODEL | Yes | - |
| `tsr_k` | Yeniden ölçekleme gücünü kontrol eder. Düşük k değerleri daha ayrıntılı sonuçlar üretir; yüksek k değerleri görüntü üretiminde daha pürüzsüz sonuçlar üretir. k = 1 olarak ayarlamak yeniden ölçeklemeyi devre dışı bırakır. (varsayılan: 0.95) | FLOAT | No | 0.01 - 100.0 |
| `tsr_sigma` | Yeniden ölçeklemenin ne kadar erken etkisini göstereceğini kontrol eder. Daha büyük değerler daha erken etkisini gösterir. (varsayılan: 1.0) | FLOAT | No | 0.01 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `patched_model` | Örnekleme sürecine Temporal Score Rescaling işlevi uygulanmış girdi modeli. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/tr.md)

---
**Source fingerprint (SHA-256):** `4d4e3c64fb6e3a3fe4725ea944a361b46d871943a10e65d72d70e0e6d757dfca`
