# Görüntüyü Maksimum Boyuta Ölçekle

ImageScaleToMaxDimension düğümü, görüntüleri orijinal en-boy oranını koruyarak belirtilen maksimum boyuta sığacak şekilde yeniden boyutlandırır. Görüntünün dikey mi yoksa yatay mı olduğunu hesaplar, ardından büyük boyutu hedef boyuta ölçeklerken küçük boyutu orantılı olarak ayarlar. Düğüm, farklı kalite ve performans gereksinimleri için birden fazla büyütme yöntemini destekler.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Ölçeklenecek giriş görüntüsü | IMAGE | Evet | - |
| `ölçeklendirme yöntemi` | Görüntüyü ölçeklemek için kullanılan enterpolasyon yöntemi (varsayılan: "area") | STRING | Evet | "area"<br>"lanczos"<br>"bilinear"<br>"nearest-exact"<br>"bilinear"<br>"bicubic" |
| `en büyük boyut` | Ölçeklenen görüntü için maksimum boyut (varsayılan: 512) | INT | Evet | 0 ile 16384 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | En büyük boyutu belirtilen boyutla eşleşen ölçeklenmiş görüntü | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToMaxDimension/tr.md)

---
**Source fingerprint (SHA-256):** `be113c1a98ab9d884b2c728b790c41fb236857d59af567e43e2be0ef0362cc5e`
