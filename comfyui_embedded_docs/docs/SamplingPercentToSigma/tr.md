> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/tr.md)

SamplingPercentToSigma düğümü, bir örnekleme yüzdesi değerini modelin örnekleme parametrelerini kullanarak karşılık gelen bir sigma değerine dönüştürür. 0.0 ile 1.0 arasında bir yüzde değeri alır ve bunu modelin gürültü zamanlamasındaki uygun sigma değerine eşler; sınırlarda hesaplanan sigma değerini veya gerçek maksimum/minimum sigma değerlerini döndürme seçenekleri mevcuttur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Dönüşüm için kullanılan örnekleme parametrelerini içeren model |
| `sampling_percent` | FLOAT | Evet | 0.0 - 1.0 | Sigma'ya dönüştürülecek örnekleme yüzdesi (varsayılan: 0.0) |
| `return_actual_sigma` | BOOLEAN | Evet | - | Aralık kontrolleri için kullanılan değer yerine gerçek sigma değerini döndürür. Bu yalnızca 0.0 ve 1.0 değerlerindeki sonuçları etkiler. (varsayılan: False) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sigma_value` | FLOAT | Giriş örnekleme yüzdesine karşılık gelen dönüştürülmüş sigma değeri |