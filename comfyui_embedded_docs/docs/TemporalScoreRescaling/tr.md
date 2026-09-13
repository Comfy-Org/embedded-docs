# TSR - Zamansal Skor Yeniden Ölçeklendirme

Bu düğüm, bir difüzyon modeline Zamansal Skor Yeniden Ölçeklendirme (Temporal Score Rescaling, TSR) uygular. Modeli, örnekleme sırasında tahmin edilen skoru veya gürültüyü yeniden ölçeklendirerek üretilen sonuçların çeşitliliğini yönlendirecek şekilde yamalar. Bu, CFG (Classifier-Free Guidance) sonrası bir işlev olarak uygulanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | TSR işleviyle yamalanacak difüzyon modeli. | MODEL | Evet | - |
| `tsr_k` | Yeniden ölçeklendirme gücünü kontrol eder. Daha düşük k daha ayrıntılı sonuçlar üretir; daha yüksek k görüntü üretiminde daha pürüzsüz sonuçlar üretir. k = 1 olarak ayarlanması yeniden ölçeklendirmeyi devre dışı bırakır. (varsayılan: 0.95) | FLOAT | Evet | 0.01 - 100.0 |
| `tsr_sigma` | Yeniden ölçeklendirmenin ne kadar erken etkili olacağını kontrol eder. Daha büyük değerler daha erken etkili olur. (varsayılan: 1.0) | FLOAT | Evet | 0.01 - 100.0 |

Not: Yeniden ölçeklendirme, `tsr_k` 1 olarak ayarlandığında, sigma değeri 0 olduğunda veya sinyal-gürültü oranı 0 olduğunda atlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `patched_model` | Örnekleme sürecine Zamansal Skor Yeniden Ölçeklendirme işlevi uygulanmış olarak yamalanan girdi modeli. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/tr.md)

---
**Source fingerprint (SHA-256):** `4d4e3c64fb6e3a3fe4725ea944a361b46d871943a10e65d72d70e0e6d757dfca`
