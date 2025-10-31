> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/tr.md)

BetaSamplingScheduler düğümü, beta zamanlama algoritmasını kullanarak örnekleme işlemi için bir gürültü seviyeleri (sigmas) dizisi oluşturur. Görüntü oluşturma sırasındaki gürültü giderme işlemini kontrol eden özelleştirilmiş bir gürültü zamanlaması oluşturmak için bir model ve yapılandırma parametrelerini alır. Bu zamanlayıcı, alfa ve beta parametreleri aracılığıyla gürültü azaltma yörüngesinin ince ayarına olanak tanır.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | Gerekli | - | - | Model örnekleme nesnesini sağlayan, örnekleme için kullanılan model |
| `steps` | INT | Gerekli | 20 | 1-10000 | Sigmaların oluşturulacağı örnekleme adım sayısı |
| `alpha` | FLOAT | Gerekli | 0.6 | 0.0-50.0 | Beta zamanlayıcı için alfa parametresi, zamanlama eğrisini kontrol eder |
| `beta` | FLOAT | Gerekli | 0.6 | 0.0-50.0 | Beta zamanlayıcı için beta parametresi, zamanlama eğrisini kontrol eder |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `SIGMAS` | SIGMAS | Örnekleme işlemi için kullanılan bir gürültü seviyeleri (sigmas) dizisi |