# TSR - Zamansal Skor Yeniden Ölçeklendirme

Bu düğüm, bir difüzyon modeline Temporal Score Rescaling (TSR) uygular. Gürültü giderme işlemi sırasında tahmin edilen gürültüyü veya skoru yeniden ölçeklendirerek modelin örnekleme davranışını değiştirir; bu da üretilen çıktının çeşitliliğini yönlendirebilir. Bu işlev, CFG (Classifier-Free Guidance) sonrası bir işlev olarak uygulanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | TSR işleviyle yamalanacak difüzyon modeli. | MODEL | Evet | - |
| `tsr_k` | Yeniden ölçekleme gücünü kontrol eder. Düşük k değeri görüntü üretiminde daha detaylı sonuçlar üretir; yüksek k değeri daha pürüzsüz sonuçlar üretir. k = 1 olarak ayarlanması yeniden ölçeklemeyi devre dışı bırakır. (varsayılan: 0.95) | FLOAT | Evet | 0.01 - 100.0 |
| `tsr_sigma` | Yeniden ölçeklemenin ne kadar erken etkili olacağını kontrol eder. Daha büyük değerler daha erken etkili olur. (varsayılan: 1.0) | FLOAT | Evet | 0.01 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `yama_uygulanmış_model` | Örnekleme sürecine Temporal Score Rescaling işlevi uygulanmış olan girdi modeli. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/tr.md)

---
**Source fingerprint (SHA-256):** `4d4e3c64fb6e3a3fe4725ea944a361b46d871943a10e65d72d70e0e6d757dfca`
