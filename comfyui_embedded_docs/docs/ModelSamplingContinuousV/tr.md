> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/tr.md)

ModelSamplingContinuousV düğümü, bir modelin örnekleme davranışını sürekli V-tahmini örnekleme parametreleri uygulayarak değiştirir. Girdi modelinin bir klonunu oluşturur ve gelişmiş örnekleme kontrolü için özel sigma aralığı ayarlarıyla yapılandırır. Bu, kullanıcıların belirli minimum ve maksimum sigma değerleriyle örnekleme sürecini hassas şekilde ayarlamasına olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Sürekli V-tahmini örnekleme ile değiştirilecek girdi modeli |
| `örnekleme` | STRING | Evet | "v_prediction" | Uygulanacak örnekleme yöntemi (şu anda yalnızca V-tahmini desteklenmektedir) |
| `sigma_maks` | FLOAT | Evet | 0.0 - 1000.0 | Örnekleme için maksimum sigma değeri (varsayılan: 500.0) |
| `sigma_min` | FLOAT | Evet | 0.0 - 1000.0 | Örnekleme için minimum sigma değeri (varsayılan: 0.03) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Sürekli V-tahmini örnekleme uygulanmış değiştirilmiş model |