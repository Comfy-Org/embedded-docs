> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RescaleCFG/tr.md)

RescaleCFG düğümü, bir model çıktısının koşullu ve koşulsuz ölçeklerini belirtilen bir çarpan temelinde ayarlamak için tasarlanmıştır; bu sayede daha dengeli ve kontrollü bir üretim süreci hedeflenir. Model çıktısını yeniden ölçeklendirerek koşullu ve koşulsuz bileşenlerin etkisini değiştirir ve böylece modelin performansını veya çıktı kalitesini potansiyel olarak artırır.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `model`   | MODEL     | Model parametresi, ayarlanacak üretken modeli temsil eder. Düğüm, modelin çıktısına bir yeniden ölçeklendirme işlevi uyguladığından ve üretim sürecini doğrudan etkilediğinden kritik öneme sahiptir. |
| `çarpan` | `FLOAT` | Çarpan parametresi, model çıktısına uygulanan yeniden ölçeklendirmenin kapsamını kontrol eder. Orijinal ve yeniden ölçeklendirilmiş bileşenler arasındaki dengeyi belirleyerek nihai çıktının özelliklerini etkiler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `model`   | MODEL     | Koşullu ve koşulsuz ölçekleri ayarlanmış değiştirilmiş model. Bu modelin, uygulanan yeniden ölçeklendirme sayesinde potansiyel olarak gelişmiş özelliklere sahip çıktılar üretmesi beklenir. |