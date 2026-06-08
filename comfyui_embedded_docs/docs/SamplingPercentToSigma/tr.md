## Genel Bakış SamplingPercentToSigma düğümü, modelin örnekleme parametrelerini kullanarak bir örnekleme yüzde değerini karşılık gelen sigma değerine dönüştürür. 0.0 ile 1.0 arasında bir yüzde değeri alır ve bunu modelin gürültü planındaki uygun sigma değerine eşler; sınırlarda hesaplanan sigma veya gerçek maksimum/minimum sigma değerlerini döndürme seçenekleri sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Dönüşüm için kullanılan örnekleme parametrelerini içeren model | MODEL | Evet | - |
| `örnekleme_yüzdesi` | Sigma'ya dönüştürülecek örnekleme yüzdesi (varsayılan: 0.0) | FLOAT | Evet | 0.0 ile 1.0 |
| `gerçek_sigma_değerini_döndür` | Aralık kontrolleri için kullanılan değer yerine gerçek sigma değerini döndürür. Bu yalnızca 0.0 ve 1.0'daki sonuçları etkiler. (varsayılan: False) | BOOLEAN | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigma_value` | Giriş örnekleme yüzdesine karşılık gelen dönüştürülmüş sigma değeri | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/tr.md)

---
**Source fingerprint (SHA-256):** `88ecea0528dfeff75248a8dfee8381e1f73d1a2d9ee3e7f8e37fef0f2b2499ec`
