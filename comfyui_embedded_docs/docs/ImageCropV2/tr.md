> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropV2/tr.md)

Image Crop düğümü, bir giriş görüntüsünden dikdörtgen bir bölüm çıkarır. Tutulacak bölgeyi, sol üst köşe koordinatlarını ve genişlik ile yüksekliğini belirterek tanımlarsınız. Düğüm daha sonra orijinal görüntünün kırpılan kısmını döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | Yok | Kırpılacak giriş görüntüsü. |
| `crop_region` | BOUNDINGBOX | Evet | Yok | Görüntüden çıkarılacak dikdörtgen alanı tanımlar. `x` (yatay başlangıç), `y` (dikey başlangıç), `width` (genişlik) ve `height` (yükseklik) ile belirtilir. Tanımlanan bölge görüntünün sınırlarının ötesine uzanıyorsa, görüntü boyutlarına sığacak şekilde otomatik olarak ayarlanır. |

**Bölge Kısıtlamaları Notu:** Kırpma bölgesi, giriş görüntüsünün sınırları içinde kalacak şekilde otomatik olarak kısıtlanır. Belirtilen `x` veya `y` koordinatı görüntünün genişliğinden veya yüksekliğinden büyükse, maksimum geçerli konuma ayarlanacaktır. Ortaya çıkan kırpma genişliği ve yüksekliği, bölgenin görüntü kenarlarını aşmaması için ayarlanır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Orijinal giriş görüntüsünün kırpılmış bölümü. |
