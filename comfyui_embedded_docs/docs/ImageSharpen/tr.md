> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageSharpen/tr.md)

ImageSharpen düğümü, bir görüntünün kenarlarını ve detaylarını belirginleştirerek netliğini artırır. Görüntüye, yoğunluk ve yarıçap ayarlanabilen bir keskinleştirme filtresi uygular, böylece görüntünün daha tanımlanmış ve net görünmesini sağlar.

## Girdiler

| Alan          | Veri Türü | Açıklama                                                                                   |
|----------------|-------------|-----------------------------------------------------------------------------------------------|
| `görüntü`        | `IMAGE`     | Keskinleştirilecek giriş görüntüsü. Bu parametre, keskinleştirme etkisinin uygulanacağı temel görüntüyü belirlediği için çok önemlidir. |
| `keskinleştirme_yarıçapı`| `INT`       | Keskinleştirme etkisinin yarıçapını tanımlar. Daha büyük bir yarıçap, kenar etrafındaki daha fazla pikselin etkileneceği ve daha belirgin bir keskinleştirme etkisi oluşacağı anlamına gelir. |
| `sigma`        | `FLOAT`     | Keskinleştirme etkisinin yayılmasını kontrol eder. Daha yüksek bir sigma değeri, kenarlarda daha yumuşak bir geçişle sonuçlanırken, daha düşük bir sigma keskinleştirmeyi daha lokalize hale getirir. |
| `alfa`        | `FLOAT`     | Keskinleştirme etkisinin yoğunluğunu ayarlar. Daha yüksek alfa değerleri, daha güçlü bir keskinleştirme etkisiyle sonuçlanır. |

## Çıktılar

| Alan | Veri Türü | Açıklama                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `görüntü`| `IMAGE`     | Geliştirilmiş kenarlara ve detaylara sahip, daha fazla işleme veya görüntülemeye hazır, keskinleştirilmiş görüntü. |