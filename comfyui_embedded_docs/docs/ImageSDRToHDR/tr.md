# Convert SDR to HDR

**Convert SDR to HDR** düğümü, standart dinamik aralıklı sRGB görüntülerini Rec.2020 HLG HDR'ye genişletir. Görüntünün mevcut görünümünü korur ve parlaklığını daha geniş bir aralığa eşler; bu nedenle sonucun HDR renk uzayı seçilerek kaydedilmesi gerekir. Alfa değişmeden korunur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | HDR'ye genişletilecek sRGB'deki SDR görüntü(ler). | IMAGE | Evet | - |
| `algorithm` | HDR genişletme algoritması. Bir algoritma seçildiğinde parametrelerini (`target_luminance`) gösterir. | DYNAMIC_COMBO | Evet | `"lottes"` |

### lottes Girdileri

Bu parametreler `algorithm` değeri `"lottes"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `target_luminance` | Nit cinsinden tepe beyaz hedefi. 0, kalibre edilmiş görüntülemeyi korur. Koyu görüntüler bu tepe değerine normalleştirilmez. (varsayılan: 650.0) | FLOAT | Evet | 0.0 ila 10000.0 (adım 1.0) |

Gruptaki her görüntü ayrı ayrı dönüştürülür: sRGB kodlaması doğrusal ışığa ters çevrilir, parlaklık kalibre edilmiş monotonik log-kazanç eğrisiyle harmanlanmış Lottes tarzı rasyonel bir eğriyle genişletilir ve sonuç Rec.2020 HLG olarak yeniden kodlanır. Çıktı HDR olduğundan, kaydetme düğümü `HDR` renk uzayını kullanmalıdır; sRGB olarak kaydetmek parlaklığı yanlış işler.

HLG, 1000 nit referans ekran varsayar; bu nedenle 1000'in altındaki `target_luminance` değerleri bu referansı korur ve `0` değeri kalibre edilmiş görüntülemeyi değiştirmeden bırakır. Tek kanallı görüntüler dönüştürmeden önce üç kanala genişletilir ve alfa kanalı değişmeden kopyalanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Rec.2020 HLG HDR görüntü(ler). | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageSDRToHDR/tr.md)

---
**Source fingerprint (SHA-256):** `51eb0beac3d48345a30ba66d80d95873384cf5155fc06c33353b6d1dc029658a`
