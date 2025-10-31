> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RescaleCFG/tr.md)

RescaleCFG düğümü, bir modelin çıktısındaki koşullandırma ve koşulsuzlandırma ölçeklerini belirli bir çarpan kullanarak ayarlamak için tasarlanmıştır ve böylece daha dengeli ve kontrollü bir üretim süreci hedefler. Modelin çıktısını yeniden ölçeklendirerek, koşullu ve koşulsuz bileşenlerin etkisini değiştirir ve bu sayede modelin performansını veya çıktı kalitesini potansiyel olarak iyileştirir.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `model`   | MODEL     | Model parametresi, ayarlanacak olan üretim modelini temsil eder. Düğümün model çıktısına bir yeniden ölçeklendirme işlevi uygulaması nedeniyle kritik öneme sahiptir ve bu doğrudan üretim sürecini etkiler. |
| `multiplier` | `FLOAT` | Multiplier parametresi, model çıktısına uygulanan yeniden ölçeklendirme miktarını kontrol eder. Orijinal ve yeniden ölçeklendirilmiş bileşenler arasındaki dengeyi belirleyerek, nihai çıktının özelliklerini etkiler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `model`   | MODEL     | Koşullandırma ve koşulsuzlandırma ölçekleri ayarlanmış, değiştirilmiş model. Uygulanan yeniden ölçeklendirme nedeniyle, bu modelin potansiyel olarak gelişmiş özelliklere sahip çıktılar üretmesi beklenir. |