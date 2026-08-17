# ÖrneklemeYüzdesiToSigma

The SamplingPercentToSigma node, modelin örnekleme parametrelerini kullanarak bir örnekleme yüzdesi değerini karşılık gelen sigma değerine dönüştürür. 0.0 ile 1.0 arasında bir yüzde değeri alır ve bunu modelin gürültü çizelgesindeki uygun sigma değerine eşler; ayrıca hesaplanan sigmayı veya sınırlardaki gerçek maksimum/minimum sigma değerlerini döndürme seçenekleri sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Dönüştürme için kullanılan örnekleme parametrelerini içeren model | MODEL | Evet | - |
| `sampling_percent` | Sigmaya dönüştürülecek örnekleme yüzdesi (varsayılan: 0.0) | FLOAT | Evet | 0.0 to 1.0 (step: 0.0001) |
| `return_actual_sigma` | Aralık kontrollerinde kullanılan değer yerine gerçek sigma değerini döndürür. Bu yalnızca 0.0 ve 1.0 değerlerindeki sonuçları etkiler. (varsayılan: False) | BOOLEAN | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigma_value` | Girdi örnekleme yüzdesine karşılık gelen dönüştürülmüş sigma değeri | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/tr.md)

---
**Source fingerprint (SHA-256):** `30decf1d4804accbdf2a70eba1a773b41ef0e09cfb74f2a9388044dadf0a1ac1`
