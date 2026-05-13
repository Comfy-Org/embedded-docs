> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropV2/tr.md)

Görüntü Kırp düğümü, bir giriş görüntüsünden dikdörtgen bir bölüm çıkarır. Korunacak bölgeyi, sol üst köşe koordinatlarını, genişliğini ve yüksekliğini belirterek tanımlarsınız. Düğüm daha sonra orijinal görüntünün kırpılmış kısmını döndürür.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `görüntü` | IMAGE | Evet | Yok | Kırpılacak giriş görüntüsü. |
| `kırpma_bölgesi` | BOUNDINGBOX | Evet | Yok | Görüntüden çıkarılacak dikdörtgen alanı tanımlar. `x` (yatay başlangıç), `y` (dikey başlangıç), `width` (genişlik) ve `height` (yükseklik) ile belirtilir. Tanımlanan bölge görüntünün sınırlarının dışına taşarsa, otomatik olarak görüntü boyutlarına sığacak şekilde ayarlanır. |

**Bölge Kısıtlamaları Hakkında Not:** Kırpma bölgesi, giriş görüntüsünün sınırları içinde kalacak şekilde otomatik olarak kısıtlanır. Belirtilen `x` veya `y` koordinatı görüntünün genişliğinden veya yüksekliğinden büyükse, izin verilen maksimum konuma ayarlanır. Ortaya çıkan kırpma genişliği ve yüksekliği, bölgenin görüntünün kenarlarını aşmaması için ayarlanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `görüntü` | IMAGE | Orijinal giriş görüntüsünün kırpılmış bölümü. |

---
**Source fingerprint (SHA-256):** `9d3543aa8396ae2ab0353accc3c89ae6be6495f6fdcefbb5439fa865a5d3059f`
