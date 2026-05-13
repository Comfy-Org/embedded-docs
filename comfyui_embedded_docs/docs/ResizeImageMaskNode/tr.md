> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImageMaskNode/tr.md)

Görüntü/Maske Yeniden Boyutlandırma düğümü, bir giriş görüntüsünün veya maskesinin boyutlarını değiştirmek için birden fazla yöntem sunar. Bir çarpanla ölçekleyebilir, belirli boyutlar ayarlayabilir, başka bir girişin boyutuna uydurabilir veya piksel sayısına göre ayarlama yapabilir; kalite için çeşitli enterpolasyon yöntemleri kullanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `input` | IMAGE veya MASK | Evet | Yok | Yeniden boyutlandırılacak görüntü veya maske. |
| `resize_type` | COMBO | Evet | `SCALE_BY`<br>`SCALE_DIMENSIONS`<br>`SCALE_LONGER_DIMENSION`<br>`SCALE_SHORTER_DIMENSION`<br>`SCALE_WIDTH`<br>`SCALE_HEIGHT`<br>`SCALE_TOTAL_PIXELS`<br>`MATCH_SIZE` | Yeni boyutu belirlemek için kullanılan yöntem. Gerekli parametreler seçilen türe göre değişir. |
| `multiplier` | FLOAT | Hayır | 0,01 ila 8,0 | Ölçekleme faktörü. `resize_type` `SCALE_BY` olduğunda gereklidir (varsayılan: 1,00). |
| `width` | INT | Hayır | 0 ila 8192 | Piksel cinsinden hedef genişlik. `resize_type` `SCALE_DIMENSIONS` veya `SCALE_WIDTH` olduğunda gereklidir (varsayılan: 512). |
| `height` | INT | Hayır | 0 ila 8192 | Piksel cinsinden hedef yükseklik. `resize_type` `SCALE_DIMENSIONS` veya `SCALE_HEIGHT` olduğunda gereklidir (varsayılan: 512). |
| `crop` | COMBO | Hayır | `"disabled"`<br>`"center"` | Boyutlar en-boy oranıyla eşleşmediğinde uygulanacak kırpma yöntemi. Yalnızca `resize_type` `SCALE_DIMENSIONS` veya `MATCH_SIZE` olduğunda kullanılabilir (varsayılan: "center"). |
| `longer_size` | INT | Hayır | 0 ila 8192 | Görüntünün uzun kenarı için hedef boyut. `resize_type` `SCALE_LONGER_DIMENSION` olduğunda gereklidir (varsayılan: 512). |
| `shorter_size` | INT | Hayır | 0 ila 8192 | Görüntünün kısa kenarı için hedef boyut. `resize_type` `SCALE_SHORTER_DIMENSION` olduğunda gereklidir (varsayılan: 512). |
| `megapixels` | FLOAT | Hayır | 0,01 ila 16,0 | Hedef toplam megapiksel sayısı. `resize_type` `SCALE_TOTAL_PIXELS` olduğunda gereklidir (varsayılan: 1,0). |
| `match` | IMAGE veya MASK | Hayır | Yok | Girişin boyutlarının eşleştirileceği görüntü veya maske. `resize_type` `MATCH_SIZE` olduğunda gereklidir. |
| `scale_method` | COMBO | Evet | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"lanczos"` | Ölçekleme için kullanılan enterpolasyon algoritması (varsayılan: "area"). |

**Not:** `crop` parametresi yalnızca `resize_type` `SCALE_DIMENSIONS` veya `MATCH_SIZE` olarak ayarlandığında kullanılabilir ve geçerlidir. `SCALE_WIDTH` veya `SCALE_HEIGHT` kullanılırken, diğer boyut, orijinal en-boy oranını korumak için otomatik olarak ölçeklenir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `resized` | IMAGE veya MASK | Girişin veri türüyle eşleşen, yeniden boyutlandırılmış görüntü veya maske. |

---
**Source fingerprint (SHA-256):** `9ac0b153608ac971bb11d9d12ebd1f0f4d6e926604e8727a1bc3a311d95fbc03`
