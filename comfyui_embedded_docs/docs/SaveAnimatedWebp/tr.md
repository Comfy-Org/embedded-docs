> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedWEBP/tr.md)

Bu düğüm, bir dizi görüntüyü animasyonlu bir WEBP dosyası olarak kaydetmek için tasarlanmıştır. Tekil kareleri tutarlı bir animasyonda birleştirir, belirtilen meta verileri uygular ve çıktıyı kalite ve sıkıştırma ayarlarına göre optimize eder.

## Girdiler

| Alan              | Veri Türü   | Açıklama                                                                         |
|-------------------|-------------|-------------------------------------------------------------------------------------|
| `images`          | `IMAGE`     | Animasyonlu WEBP içinde kare olarak kaydedilecek görüntü listesi. Bu parametre, animasyonun görsel içeriğini tanımlamak için gereklidir. |
| `filename_prefix` | `STRING`    | Çıktı dosyası için, bir sayaç ve '.webp' uzantısı eklenmiş olacak şekilde temel adı belirtir. Bu parametre, kaydedilen dosyaları tanımlamak ve düzenlemek için çok önemlidir. |
| `fps`             | `FLOAT`     | Animasyonun saniye başına kare hızı, oynatma hızını etkiler. |
| `lossless`        | `BOOLEAN`   | Kayıpsız sıkıştırma kullanılıp kullanılmayacağını belirten bir boolean değer, dosya boyutunu ve animasyonun kalitesini etkiler. |
| `quality`         | `INT`       | 0 ile 100 arasında bir değer olup, sıkıştırma kalite seviyesini belirler; daha yüksek değerler daha iyi görüntü kalitesi ancak daha büyük dosya boyutları ile sonuçlanır. |
| `method`          | COMBO[STRING] | Kullanılacak sıkıştırma yöntemini belirtir; bu, kodlama hızını ve dosya boyutunu etkileyebilir. |

## Çıktılar

| Alan | Veri Türü | Açıklama                                                                       |
|-------|-------------|-----------------------------------------------------------------------------------|
| `ui`  | N/A         | Kaydedilen animasyonlu WEBP görüntülerini meta verileriyle birlikte gösteren bir UI bileşeni sağlar ve animasyonun etkin olup olmadığını belirtir. |