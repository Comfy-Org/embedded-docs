ImageSharpen düğümü, bir görüntünün kenarlarını ve detaylarını vurgulayarak netliğini artırır. Görüntüye, yoğunluğu ve yarıçapı ayarlanabilen bir keskinleştirme filtresi uygulayarak görüntünün daha belirgin ve net görünmesini sağlar.

## Girişler

| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Keskinleştirilecek giriş görüntüsü. Bu parametre, keskinleştirme efektinin uygulanacağı temel görüntüyü belirlediği için kritik öneme sahiptir. | `IMAGE` |
| `keskinleştirme_yarıçapı` | Keskinleştirme efektinin yarıçapını tanımlar. Daha büyük bir yarıçap, kenar çevresinde daha fazla pikselin etkileneceği anlamına gelir ve bu da daha belirgin bir keskinleştirme efekti sağlar. | `INT` |
| `sigma` | Keskinleştirme efektinin yayılımını kontrol eder. Daha yüksek bir sigma değeri, kenarlarda daha yumuşak bir geçiş sağlarken, daha düşük bir sigma keskinleştirmeyi daha yerel hale getirir. | `FLOAT` |
| `alfa` | Keskinleştirme efektinin yoğunluğunu ayarlar. Daha yüksek alfa değerleri, daha güçlü bir keskinleştirme efekti sağlar. | `FLOAT` |

## Çıktılar

| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Kenarları ve detayları vurgulanmış, daha ileri işleme veya görüntüleme için hazır, keskinleştirilmiş görüntü. | `IMAGE` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageSharpen/tr.md)
