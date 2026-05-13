> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedPNG/tr.md)

SaveAnimatedPNG düğümü, bir dizi kareden oluşan hareketli PNG görüntüleri oluşturmak ve kaydetmek için tasarlanmıştır. Tek tek görüntü karelerini tutarlı bir animasyon halinde birleştirerek, kare süresi, döngü ve meta veri ekleme gibi özelleştirmelere olanak tanır.

## Girişler

| Alan              | Veri Türü  | Açıklama                                                                           |
|-------------------|-------------|-------------------------------------------------------------------------------------|
| `görüntüler`          | `IMAGE`     | İşlenecek ve hareketli PNG olarak kaydedilecek görüntülerin listesi. Listedeki her görüntü, animasyonda bir kareyi temsil eder. |
| `dosyaadı_öneki` | `STRING`    | Çıktı dosyası için temel adı belirtir; oluşturulan hareketli PNG dosyaları için ön ek olarak kullanılır. |
| `fps`             | `FLOAT`     | Animasyonun saniyedeki kare sayısı (FPS) değeri; karelerin ne kadar hızlı görüntüleneceğini kontrol eder. |
| `sıkıştırma_seviyesi`  | `INT`       | Hareketli PNG dosyalarına uygulanan sıkıştırma seviyesi; dosya boyutunu ve görüntü netliğini etkiler. |

## Çıktılar

| Alan  | Veri Türü | Açıklama                                                                           |
|-------|-------------|-----------------------------------------------------------------------------------|
| `ui`  | Yok         | Oluşturulan hareketli PNG görüntülerini gösteren ve animasyonun tek kareli mi yoksa çok kareli mi olduğunu belirten bir kullanıcı arayüzü bileşeni sağlar. |