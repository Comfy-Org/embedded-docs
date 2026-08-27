# Reve Görsel Düzenle

Reve Image Edit düğümü, doğal dil metin talimatına dayalı olarak mevcut bir görüntüyü düzenler. Giriş görüntüsünü ve talimatınızı Reve API'sine gönderir; API, istenen düzenlemelerin uygulandığı yeni bir görüntü döndürür.

## Girdiler

`model` seçici, hangi modele özgü girdilerin gösterileceğini belirler. `upscale` seçici, büyütme faktörü girdisinin kullanılabilir olup olmadığını kontrol eder.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görsel` | Düzenlenecek görüntü. | IMAGE | Evet | - |
| `düzenleme_talimatı` | Görüntünün nasıl düzenleneceğine dair metin açıklaması. En fazla 2560 karakter. | STRING | Evet | - |
| `model` | Düzenleme için kullanılacak model sürümü. | DYNAMIC_COMBO | Evet | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` |
| `upscale` | Üretilen görüntüyü büyütür. Ek maliyete neden olabilir. (varsayılan: "disabled") | DYNAMIC_COMBO | Hayır | `"disabled"`<br>`"enabled"` |
| `remove_background` | Üretilen görüntüden arka planı kaldırır. Ek maliyete neden olabilir. (varsayılan: False) | BOOLEAN | Hayır | `true`<br>`false` |
| `seed` | Tohum (seed), düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar, tohum değeri ne olursa olsun deterministik değildir. (varsayılan: 0) | INT | Hayır | 0 ila 2147483647 |

### Model Girdileri (`reve-edit@20250915` ve `reve-edit-fast@20251030` tarafından paylaşılan)

Her iki model sürümü de aynı modele özgü girdileri sunar.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `en_boy_oranı` | Çıktı görüntüsünün en-boy oranı. "auto" olarak ayarlandığında, en-boy oranı otomatik olarak belirlenir. | COMBO | Hayır | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_zamanı_ölçekleme` | Gelişmiş seçenek. Daha yüksek değerler daha iyi görüntüler üretir ancak daha fazla kredi harcar. (varsayılan: 1) | INT | Hayır | 1 ila 5 |

### Büyütme Girdileri (`upscale` "enabled" olarak ayarlandığında)

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `upscale.upscale_factor` | Büyütme faktörü (2x, 3x veya 4x). (varsayılan: 2) | INT | Hayır | 2 ila 4 |

**Not:**

- `upscale.upscale_factor` yalnızca `upscale` "enabled" olarak ayarlandığında geçerlidir. Büyütme ve arka plan kaldırma birlikte veya bağımsız olarak etkinleştirilebilir.
- `edit_instruction` boş olmamalı ve 2560 karakteri aşmamalıdır.
- `model.aspect_ratio` "auto" olarak ayarlandığında, API'ye sabit bir en-boy oranı gönderilmez ve en-boy oranı otomatik olarak seçilir.
- `model.test_time_scaling` yalnızca değeri 1'den büyük olduğunda API'ye gönderilir; varsayılan değer olan 1, API'nin varsayılan davranışını korur.
- Sonuçlar, tohum değeri ne olursa olsun deterministik değildir; tohum yalnızca düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder.
- Bu düğüm kullanımdan kaldırılmış olarak işaretlenmiştir.
- USD cinsinden yaklaşık maliyet (düğümün fiyat rozetine göre): `reve-edit-fast@20251030` için `$0.01001`; büyütme olmadan `reve-edit@20250915` için `$0.0572`; 2x büyütme ile `$0.0686`, 3x büyütme ile `$0.0819` ve 4x büyütme ile `$0.0991`.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Talimata dayalı olarak üretilen düzenlenmiş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/tr.md)

---
**Source fingerprint (SHA-256):** `4001f3ab4cc4e705c235f578e90e497bb30d22110ef69b16fb072a91a65d15df`
