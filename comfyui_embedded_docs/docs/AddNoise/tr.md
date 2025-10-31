> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/tr.md)

# AddNoise

Bu düğüm, belirli gürültü parametreleri ve sigma değerleri kullanarak bir gizli görüntüye kontrollü gürültü ekler. Girdiyi, verilen sigma aralığı için uygun olan gürültü ölçeklendirmesini uygulamak üzere modelin örnekleme sistemi aracılığıyla işler.

## Nasıl Çalışır

Düğüm, bir gizli görüntü alır ve sağlanan gürültü üreteci ve sigma değerlerine dayanarak ona gürültü uygular. İlk olarak herhangi bir sigma sağlanıp sağlanmadığını kontrol eder - eğer yoksa, orijinal gizli görüntüyü değiştirilmeden döndürür. Düğüm daha sonra gizli görüntüyü işlemek ve ölçeklendirilmiş gürültü uygulamak için modelin örnekleme sistemini kullanır. Gürültü ölçeklendirmesi, birden fazla sigma sağlandığında ilk ve son sigma değerleri arasındaki farkla veya yalnızca bir sigma mevcut olduğunda tek bir sigma değeriyle belirlenir. Boş gizli görüntüler (yalnızca sıfırlar içeren) işleme sırasında kaydırılmaz. Son çıktı, uygulanan gürültüye sahip yeni bir gizli temsildir ve kararlılık için herhangi bir NaN veya sonsuz değer sıfıra dönüştürülür.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | Gerekli | - | - | Örnekleme parametrelerini ve işleme fonksiyonlarını içeren model |
| `noise` | NOISE | Gerekli | - | - | Temel gürültü desenini üreten gürültü üreteci |
| `sigmas` | SIGMAS | Gerekli | - | - | Gürültü ölçeklendirme yoğunluğunu kontrol eden sigma değerleri |
| `latent_image` | LATENT | Gerekli | - | - | Gürültünün ekleneceği girdi gizli temsili |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Eklenen gürültü ile değiştirilmiş gizli temsil |