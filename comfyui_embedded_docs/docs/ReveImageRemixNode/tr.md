# Reve Görsel Remix

Reve Image Remix düğümü, yeni bir görüntü oluşturmak için Reve API'sini kullanır. Bir veya daha fazla referans görüntüyü bir metin istemiyle birleştirerek sağlanan açıklamaya dayalı yeni, remikslenmiş bir görüntü oluşturur.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Remiks için kullanılacak model sürümü. | DYNAMIC_COMBO | Evet | `"reve-remix@20250915"`<br>`"reve-remix-fast@20251030"` |
| `prompt` | İstenen görüntünün metin açıklaması. Belirli görüntülere dizinle başvurmak için XML img etiketleri içerebilir, örn. `<img>0</img>`, `<img>1</img>`, vb. (varsayılan: boş) | STRING | Evet | 1 ila 2560 karakter |
| `upscale` | Üretilen görüntüyü büyütür. Ek maliyet ekleyebilir. (varsayılan: "disabled") | DYNAMIC_COMBO | Hayır | `"disabled"`<br>`"enabled"` |
| `remove_background` | Üretilen görüntüden arka planı kaldırır. Ek maliyet ekleyebilir. (varsayılan: false) | BOOLEAN | Hayır | `true`<br>`false` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Hayır | 0 ila 2147483647 |

### Model Girdileri (reve-remix@20250915 ve reve-remix-fast@20251030 tarafından paylaşılır)

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Çıktı görüntüsünün en-boy oranı. (varsayılan: "auto") | COMBO | Evet | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Daha yüksek değerler daha iyi görüntüler üretir ancak daha fazla kredi harcar. (varsayılan: 1) | INT | Hayır | 1 ila 5 |

### Büyütme Girdileri (`upscale` "enabled" Olarak Ayarlandığında Görünür)

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `upscale_factor` | Büyütme faktörü (2x, 3x veya 4x). (varsayılan: 2) | INT | Hayır | 2 ila 4 |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `referans_görseller` | Genişletilebilir yuva: remiks için görsel temel olarak kullanmak üzere 1 ila 6 görüntü bağlayın (`image_1` ile `image_6`). En az bir referans görüntü gereklidir. | IMAGE | Evet | 1 ila 6 görüntü |

**Not:** İstem (prompt) 1 ile 2560 karakter arasında olmalıdır. `aspect_ratio` "auto" olarak ayarlandığında, hizmet çıktı görüntüsünün en-boy oranını belirler. `test_time_scaling` değeri 1 olduğunda standart işleme uygulanır; daha yüksek değerler görüntü kalitesini artırır ancak daha fazla kredi tüketir. `upscale_factor` widget'ı yalnızca `upscale` "enabled" olarak ayarlandığında görünür. Remiks sonuçları seed değerinden bağımsız olarak deterministik değildir. Bu düğüm kullanımdan kaldırılmıştır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Reve remiks süreci tarafından üretilen yeni görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/tr.md)

---
**Source fingerprint (SHA-256):** `9cf0c6653aa620179ed5d888a455fe248a240b0db04687eade6652730eb5f003`
