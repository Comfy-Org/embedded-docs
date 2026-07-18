SaveAnimatedPNG düğümü, bir dizi kareden oluşan hareketli PNG görüntüleri oluşturmak ve kaydetmek için tasarlanmıştır. Tek tek görüntü karelerini tutarlı bir animasyon halinde birleştirerek, kare süresi, döngü ve meta veri ekleme gibi özelleştirmelere olanak tanır.

## Girişler

| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntüler` | İşlenecek ve hareketli PNG olarak kaydedilecek görüntülerin listesi. Listedeki her görüntü, animasyonda bir kareyi temsil eder. | `IMAGE` |
| `dosyaadı_öneki` | Çıktı dosyası için temel adı belirtir; oluşturulan hareketli PNG dosyaları için ön ek olarak kullanılır. | `STRING` |
| `fps` | Animasyonun saniyedeki kare sayısı (FPS) değeri; karelerin ne kadar hızlı görüntüleneceğini kontrol eder. | `FLOAT` |
| `sıkıştırma_seviyesi` | Hareketli PNG dosyalarına uygulanan sıkıştırma seviyesi; dosya boyutunu ve görüntü netliğini etkiler. | `INT` |

## Çıktılar

| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Oluşturulan hareketli PNG görüntülerini gösteren ve animasyonun tek kareli mi yoksa çok kareli mi olduğunu belirten bir kullanıcı arayüzü bileşeni sağlar. | Yok |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedPNG/tr.md)
