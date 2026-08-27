# ÖrneklemeYüzdesiToSigma

SamplingPercentToSigma düğümü, bir örnekleme yüzdesi değerini modelin örnekleme parametrelerini kullanarak karşılık gelen sigma değerine dönüştürür. 0.0 ile 1.0 arasında bir yüzde değeri alır ve bunu modelin gürültü çizelgesindeki uygun sigma değerine eşler; sınırlarda hesaplanan sigmayı veya gerçek maksimum/minimum sigma değerlerini döndürme seçenekleri sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Dönüşüm için kullanılan örnekleme parametrelerini içeren model | MODEL | Evet | - |
| `örnekleme_yüzdesi` | Sigma değerine dönüştürülecek örnekleme yüzdesi (varsayılan: 0.0) | FLOAT | Evet | 0.0 ile 1.0 (step: 0.0001) |
| `gerçek_sigma_değerini_döndür` | Aralık kontrolleri için kullanılan değer yerine gerçek sigma değerini döndürür. Bu yalnızca 0.0 ve 1.0 değerlerindeki sonuçları etkiler. (varsayılan: False) | BOOLEAN | Evet | - |

`return_actual_sigma` etkinleştirildiğinde, `sampling_percent` değeri 0.0 olan bir girdi modelin maksimum sigma değerini (sigma_max), 1.0 olan bir girdi ise minimum sigma değerini (sigma_min) döndürür. Diğer tüm yüzdelerde sonuç, seçeneğin etkin olup olmamasına bakılmaksızın aynıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigma_değeri` | Girdi örnekleme yüzdesine karşılık gelen dönüştürülmüş sigma değeri | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/tr.md)

---
**Source fingerprint (SHA-256):** `30decf1d4804accbdf2a70eba1a773b41ef0e09cfb74f2a9388044dadf0a1ac1`
