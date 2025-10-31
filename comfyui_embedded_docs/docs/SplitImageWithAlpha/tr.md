> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageWithAlpha/tr.md)

SplitImageWithAlpha düğümü, bir görüntünün renk ve alfa bileşenlerini ayırmak için tasarlanmıştır. Bir girdi görüntü tensörünü işleyerek, RGB kanallarını renk bileşeni olarak ve alfa kanalını da şeffaflık bileşeni olarak çıkarır; bu farklı görüntü yönlerinin manipülasyonunu gerektiren işlemleri kolaylaştırır.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | 'image' parametresi, RGB ve alfa kanallarının ayrılacağı girdi görüntü tensörünü temsil eder. Bölme işlemi için kaynak veriyi sağladığından operasyon için çok önemlidir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | 'image' çıktısı, girdi görüntüsünün ayrılmış RGB kanallarını temsil eder ve şeffaflık bilgisi olmadan renk bileşenini sağlar. |
| `mask`    | `MASK`      | 'mask' çıktısı, girdi görüntüsünün ayrılmış alfa kanalını temsil eder ve şeffaflık bilgisini sağlar. |