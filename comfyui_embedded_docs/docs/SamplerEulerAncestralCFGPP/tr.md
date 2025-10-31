> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/tr.md)

SamplerEulerAncestralCFGPP düğümü, Euler Ata yöntemini sınıflandırıcısız kılavuzluk ile kullanarak görüntü oluşturmak için özelleştirilmiş bir örnekleyici oluşturur. Bu örnekleyici, ata örnekleme tekniklerini kılavuzluk koşullandırmasıyla birleştirerek, tutarlılığı korurken çeşitli görüntü varyasyonları üretir. Gürültü ve adım boyutu ayarlamalarını kontrol eden parametreler aracılığıyla örnekleme sürecinin ince ayar yapılmasına olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | Evet | 0.0 - 1.0 | Örnekleme sırasındaki adım boyutunu kontrol eder, daha yüksek değerler daha agresif güncellemelere yol açar (varsayılan: 1.0) |
| `s_noise` | FLOAT | Evet | 0.0 - 10.0 | Örnekleme sürecinde eklenen gürültü miktarını ayarlar (varsayılan: 1.0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Görüntü oluşturma işlem hattında kullanılabilecek yapılandırılmış bir örnekleyici nesnesi döndürür |