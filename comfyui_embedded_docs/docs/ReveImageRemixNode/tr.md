# Reve Görsel Remix

Reve Image Remix düğümü, yeni bir görüntü oluşturmak için Reve API'sini kullanır. Bir veya daha fazla referans görüntüsünü bir metin istemiyle birleştirerek sağlanan açıklamaya dayalı yeni, remikslenmiş bir görüntü oluşturur. İki model sürümü mevcuttur ve yükseltme veya arka plan kaldırma gibi isteğe bağlı son işlemler uygulanabilir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Remiksleme için kullanılacak model sürümü. Bir model seçmek, en-boy oranı ve test zamanı ölçekleme ayarlarını gösterir. | DYNAMIC_COMBO | Evet | `reve-remix@20250915`<br>`reve-remix-fast@20251030` |
| `prompt` | İstenen görüntünün metin açıklaması. Belirli görüntülere dizine göre başvurmak için XML img etiketleri içerebilir, örn. `<img>0</img>`, `<img>1</img>`, vb. (varsayılan: boş) | STRING | Evet | 1 ila 2560 karakter |
| `upscale` | Oluşturulan görüntüyü yükseltir. Ek maliyet ekleyebilir. "enabled" olarak ayarlandığında, bir `upscale_factor` ayarı gösterilir. (varsayılan: "disabled") | DYNAMIC_COMBO | Hayır | `"disabled"`<br>`"enabled"` |
| `remove_background` | Oluşturulan görüntüden arka planı kaldırır. Ek maliyet ekleyebilir. (varsayılan: false) | BOOLEAN | Hayır | `true`<br>`false` |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Hayır | 0 ila 2147483647 |

### Model Sürümü Girdileri (`reve-remix@20250915` ve `reve-remix-fast@20251030` tarafından paylaşılır)

Her iki model sürümü de aynı ayarları sunar.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Çıktı görüntüsünün en-boy oranı. "auto" olarak ayarlandığında, API en-boy oranına otomatik olarak karar verir. | COMBO | Hayır | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Daha yüksek değerler daha iyi görüntüler üretir ancak daha fazla kredi harcar. (varsayılan: 1; yalnızca 1'den büyük değerler uygulanır) | INT | Hayır | 1 ila 5 (adım 1) |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Genişletilebilir yuva: remiks için temel olarak kullanılacak 1 ila 6 referans görüntüsü bağlayın (yuvalar `image_1`, `image_2`, vb. olarak adlandırılır). En az bir referans görüntüsü gereklidir. | IMAGE | Evet | 1 ila 6 görüntü |

**Not:** İstem 1 ila 2560 karakter arasında olmalıdır. `upscale` "enabled" olarak ayarlandığında, iç içe `upscale_factor` ayarı 2, 3 veya 4 değerini kabul eder (varsayılan: 2) ve ek maliyet ekleyebilir. Arka planı kaldırmak da ek maliyet ekleyebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Reve remiks süreci tarafından oluşturulan yeni görüntü. | IMAGE |

Not: Bu düğüm kullanımdan kaldırılmış olarak işaretlenmiştir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/tr.md)

---
**Source fingerprint (SHA-256):** `9cf0c6653aa620179ed5d888a455fe248a240b0db04687eade6652730eb5f003`
