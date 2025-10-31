> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedPNG/tr.md)

SaveAnimatedPNG düğümü, bir dizi kareden animasyonlu PNG görselleri oluşturmak ve kaydetmek için tasarlanmıştır. Tekil görüntü karelerini uyumlu bir animasyona dönüştürme işlemini gerçekleştirir ve kare süresi, döngü ve meta veri ekleme özelliklerinin özelleştirilmesine olanak tanır.

## Girdiler

| Alan              | Veri Türü | Açıklama                                                                         |
|-------------------|-----------|----------------------------------------------------------------------------------|
| `görüntüler`          | `IMAGE`   | İşlenecek ve animasyonlu PNG olarak kaydedilecek bir görüntü listesi. Listedeki her bir görüntü, animasyonda bir kareyi temsil eder. |
| `dosyaadı_öneki` | `STRING`  | Çıktı dosyası için temel adı belirtir; bu, oluşturulan animasyonlu PNG dosyaları için bir önek olarak kullanılacaktır. |
| `fps`             | `FLOAT`   | Animasyonun saniye başına kare hızı; karelerin ne kadar hızlı görüntüleneceğini kontrol eder. |
| `sıkıştırma_seviyesi`  | `INT`     | Animasyonlu PNG dosyalarına uygulanan sıkıştırma seviyesi; dosya boyutunu ve görüntü netliğini etkiler. |

## Çıktılar

| Alan | Veri Türü | Açıklama                                                                       |
|------|-----------|--------------------------------------------------------------------------------|
| `ui` | N/A       | Oluşturulan animasyonlu PNG görsellerini gösteren ve animasyonun tek kareli mi yoksa çok kareli mi olduğunu belirten bir kullanıcı arayüzü bileşeni sağlar. |