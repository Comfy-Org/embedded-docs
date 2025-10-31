> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/tr.md)

ModelSamplingLTXV düğümü, bir modele belirteç sayısına dayalı gelişmiş örnekleme parametreleri uygular. Girdi gizli değişkenindeki belirteç sayısına bağlı olarak, temel ve maksimum kaydırma değerleri arasında doğrusal bir enterpolasyon kullanarak bir kaydırma değeri hesaplar. Düğüm daha sonra özelleştirilmiş bir model örnekleme yapılandırması oluşturur ve bunu girdi modeline uygular.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Örnekleme parametrelerinin uygulanacağı girdi modeli |
| `max_shift` | FLOAT | Hayır | 0.0 - 100.0 | Hesaplamada kullanılan maksimum kaydırma değeri (varsayılan: 2.05) |
| `base_shift` | FLOAT | Hayır | 0.0 - 100.0 | Hesaplamada kullanılan temel kaydırma değeri (varsayılan: 0.95) |
| `latent` | LATENT | Hayır | - | Kaydırma hesaplaması için belirteç sayısını belirlemek üzere kullanılan isteğe bağlı gizli değişken girdisi |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Uygulanan örnekleme parametreleriyle değiştirilmiş model |