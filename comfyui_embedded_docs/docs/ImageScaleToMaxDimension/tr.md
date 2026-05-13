> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToMaxDimension/tr.md)

ImageScaleToMaxDimension düğümü, görüntüleri orijinal en-boy oranını koruyarak belirtilen maksimum boyuta sığacak şekilde yeniden boyutlandırır. Görüntünün dikey mi yoksa yatay mı olduğunu hesaplar, ardından büyük boyutu hedef boyuta ölçeklerken küçük boyutu orantılı olarak ayarlar. Düğüm, farklı kalite ve performans gereksinimleri için birden fazla büyütme yöntemini destekler.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `image` | IMAGE | Evet | - | Ölçeklenecek giriş görüntüsü |
| `upscale_method` | STRING | Evet | "area"<br>"lanczos"<br>"bilinear"<br>"nearest-exact"<br>"bilinear"<br>"bicubic" | Görüntüyü ölçeklemek için kullanılan enterpolasyon yöntemi (varsayılan: "area") |
| `largest_size` | INT | Evet | 0 ile 16384 | Ölçeklenen görüntü için maksimum boyut (varsayılan: 512) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `image` | IMAGE | En büyük boyutu belirtilen boyutla eşleşen ölçeklenmiş görüntü |

---
**Source fingerprint (SHA-256):** `be113c1a98ab9d884b2c728b790c41fb236857d59af567e43e2be0ef0362cc5e`
