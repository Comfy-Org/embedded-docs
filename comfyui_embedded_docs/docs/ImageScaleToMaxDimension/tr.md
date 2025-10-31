> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToMaxDimension/tr.md)

ImageScaleToMaxDimension düğümü, görüntüleri orijinal en-boy oranını koruyarak belirtilen maksimum boyuta sığacak şekilde yeniden boyutlandırır. Görüntünün dikey mi yatay mı olduğunu hesaplar, ardından daha büyük olan boyutu hedef boyutla eşleşecek şekilde ölçeklerken daha küçük olan boyutu da orantılı olarak ayarlar. Düğüm, farklı kalite ve performans gereksinimleri için birden fazla yukarı ölçekleme yöntemini destekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Ölçeklenecek girdi görüntüsü |
| `upscale_method` | STRING | Evet | "area"<br>"lanczos"<br>"bilinear"<br>"nearest-exact"<br>"bicubic" | Görüntüyü ölçeklemek için kullanılan enterpolasyon yöntemi |
| `largest_size` | INT | Evet | 0 - 16384 | Ölçeklenmiş görüntü için maksimum boyut (varsayılan: 512) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | En büyük boyutu belirtilen boyutla eşleşen ölçeklenmiş görüntü |