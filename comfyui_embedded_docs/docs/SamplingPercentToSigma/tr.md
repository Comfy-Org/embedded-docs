# ÖrneklemeYüzdesiToSigma

Bir örnekleme yüzdesini, seçili modelin örnekleme ayarlarını kullanarak eşleşen sigma değerine dönüştürür. 0.0 ile 1.0 arasındaki bir yüzdeyi modelin gürültü çizelgesine eşler ve isteğe bağlı olarak iki uç noktada modelin gerçek maksimum veya minimum sigma değerini döndürebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Dönüştürme için kullanılan örnekleme parametrelerini içeren model | MODEL | Evet | - |
| `örnekleme_yüzdesi` | Sigma değerine dönüştürülecek örnekleme yüzdesi (varsayılan: 0.0) | FLOAT | Evet | 0.0 ile 1.0 (step: 0.0001) |
| `gerçek_sigma_değerini_döndür` | Aralık kontrolleri için kullanılan değer yerine gerçek sigma değerini döndürür. Bu yalnızca 0.0 ve 1.0'daki sonuçları etkiler. (varsayılan: False) | BOOLEAN | Evet | - |

`return_actual_sigma` etkinleştirildiğinde, 0.0 değerinde bir `sampling_percent`, modelin maksimum sigma değerini (sigma_max) döndürür; 1.0 değerinde bir `sampling_percent` ise minimum sigma değerini (sigma_min) döndürür. Diğer tüm yüzdeler için sonuç, bu seçenek etkin olsun veya olmasın aynıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigma_value` | Girdi örnekleme yüzdesine karşılık gelen sigma değeri | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/tr.md)

---
**Source fingerprint (SHA-256):** `30decf1d4804accbdf2a70eba1a773b41ef0e09cfb74f2a9388044dadf0a1ac1`
