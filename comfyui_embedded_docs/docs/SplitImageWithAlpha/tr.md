SplitImageWithAlpha düğümü, bir görüntünün renk ve alfa bileşenlerini ayırmak için tasarlanmıştır. Giriş görüntü tensorunu işleyerek RGB kanallarını renk bileşeni, alfa kanalını ise saydamlık bileşeni olarak çıkarır; böylece bu farklı görüntü özelliklerinin manipülasyonunu gerektiren işlemleri kolaylaştırır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | 'image' parametresi, RGB ve alfa kanallarının ayrılacağı giriş görüntü tensorunu temsil eder. Ayırma işlemi için kaynak veriyi sağladığından işlem açısından kritik öneme sahiptir. | `IMAGE` |

## Çıkışlar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | 'image' çıkışı, giriş görüntüsünün ayrılmış RGB kanallarını temsil eder ve saydamlık bilgisi olmadan renk bileşenini sağlar. | `IMAGE` |
| `mask` | 'mask' çıkışı, giriş görüntüsünün ayrılmış alfa kanalını temsil eder ve saydamlık bilgisini sağlar. | `MASK` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageWithAlpha/tr.md)
