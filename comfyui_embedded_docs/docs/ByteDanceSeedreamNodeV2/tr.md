# ByteDance Seedream 4.5 & 5.0

Bu düğüm, ByteDance'in Seedream modellerini (4.0, 4.5, 5.0 Lite ve 5.0 Pro sürümleri) kullanarak görsel üretir veya düzenler. 4K çözünürlüğe kadar birleşik metinden görüntüye üretim ve tek cümlelik hassas görüntü düzenleme sunar. Bu, Seedream düğümünün eski (V2) sürümüdür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Üretim için kullanılacak Seedream model sürümü. Her modelin farklı yetenekleri ve fiyatlandırması vardır. | DYNAMIC_COMBO | Evet | `"seedream 5.0 pro"`<br>`"seedream 5.0 lite"`<br>`"seedream-4-5-251128"`<br>`"seedream-4-0-250828"` |
| `istem` | Görsel oluşturmak veya düzenlemek için metin istemi (varsayılan: boş dize). | STRING | Evet | N/A |
| `tohum` | Üretim için kullanılacak tohum (varsayılan: 0). | INT | Evet | 0 ile 2147483647 |
| `filigran` | Görsele "AI generated" filigranı eklenip eklenmeyeceği (varsayılan: False). | BOOLEAN | Evet | True / False |
| `düşünme` | İstemlere daha iyi uyum sağlamak için modelin istem optimizasyonu akıl yürütmesini ('thinking') etkinleştirir. Üretim süresini önemli ölçüde artırabilir; özellikle Seedream 5.0 Pro'da. Yalnızca metinden görüntüye üretimde devre dışı bırakılabilir (referans görseller sağlandığında değil) (varsayılan: True). | BOOLEAN | Hayır | True / False |

### `seedream 5.0 pro` Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Önerilen bir boyut seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Custom seçeneğini belirleyin. | COMBO | Evet | Modele özel birden çok hazır boyut mevcuttur; `Custom` dahildir |
| `width` | Görsel için özel genişlik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında çalışır (varsayılan: 2048). | INT | Evet | 1024 ile 3136 (adım 2) |
| `height` | Görsel için özel yükseklik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında çalışır (varsayılan: 2048). | INT | Evet | 1024 ile 2496 (adım 2) |

### `seedream 5.0 lite` Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Önerilen bir boyut seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Custom seçeneğini belirleyin. | COMBO | Evet | Modele özel birden çok hazır boyut mevcuttur; `Custom` dahildir |
| `width` | Görsel için özel genişlik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında çalışır (varsayılan: 2048). | INT | Evet | 1024 ile 6240 (adım 2) |
| `height` | Görsel için özel yükseklik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında çalışır (varsayılan: 2048). | INT | Evet | 1024 ile 4992 (adım 2) |
| `max_images` | Üretilecek maksimum görsel sayısı. 1 olduğunda tam olarak bir görsel üretilir. >1 olduğunda model, 1 ile max_images arasında ilişkili görsel üretir (ör. hikaye sahneleri, karakter varyasyonları). Toplam görsel sayısı (girdi + üretilen) 15'i aşamaz. (varsayılan: 1) | INT | Evet | 1 ile 14 |
| `fail_on_partial` | Etkinleştirilirse, istenen görsellerden herhangi biri eksikse veya bir hata dönerse yürütmeyi durdurur. (varsayılan: False) | BOOLEAN | Evet | True / False |

### `seedream-4-5-251128` Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Önerilen bir boyut seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Custom seçeneğini belirleyin. | COMBO | Evet | Modele özel birden çok hazır boyut mevcuttur; `Custom` dahildir |
| `width` | Görsel için özel genişlik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında çalışır (varsayılan: 2048). | INT | Evet | 1024 ile 6240 (adım 2) |
| `height` | Görsel için özel yükseklik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında çalışır (varsayılan: 2048). | INT | Evet | 1024 ile 4992 (adım 2) |
| `max_images` | Üretilecek maksimum görsel sayısı. 1 olduğunda tam olarak bir görsel üretilir. >1 olduğunda model, 1 ile max_images arasında ilişkili görsel üretir (ör. hikaye sahneleri, karakter varyasyonları). Toplam görsel sayısı (girdi + üretilen) 15'i aşamaz. (varsayılan: 1) | INT | Evet | 1 ile 10 |
| `fail_on_partial` | Etkinleştirilirse, istenen görsellerden herhangi biri eksikse veya bir hata dönerse yürütmeyi durdurur. (varsayılan: False) | BOOLEAN | Evet | True / False |

### `seedream-4-0-250828` Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Önerilen bir boyut seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Custom seçeneğini belirleyin. | COMBO | Evet | Modele özel birden çok hazır boyut mevcuttur; `Custom` dahildir |
| `width` | Görsel için özel genişlik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında çalışır (varsayılan: 2048). | INT | Evet | 1024 ile 6240 (adım 2) |
| `height` | Görsel için özel yükseklik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında çalışır (varsayılan: 2048). | INT | Evet | 1024 ile 4992 (adım 2) |
| `max_images` | Üretilecek maksimum görsel sayısı. 1 olduğunda tam olarak bir görsel üretilir. >1 olduğunda model, 1 ile max_images arasında ilişkili görsel üretir (ör. hikaye sahneleri, karakter varyasyonları). Toplam görsel sayısı (girdi + üretilen) 15'i aşamaz. (varsayılan: 1) | INT | Evet | 1 ile 10 |
| `fail_on_partial` | Etkinleştirilirse, istenen görsellerden herhangi biri eksikse veya bir hata dönerse yürütmeyi durdurur. (varsayılan: False) | BOOLEAN | Evet | True / False |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Genişletilebilir yuva: 1..N öğe bağlayın (örn. `image_1`, `image_2`, ...); sayı sınırı seçilen modele bağlıdır (model bölümlerine bakın). Görüntüden görüntüye veya çoklu referanslı üretim için isteğe bağlı referans görsel(ler)i. Referans görsel olmadığında düğüm metinden görüntüye modunda çalışır. | IMAGE | Hayır | 0 ile 10 görsel (`seedream 5.0 pro`, `seedream-4-5-251128`, `seedream-4-0-250828`)<br>0 ile 14 görsel (`seedream 5.0 lite`) |

### Kısıtlamalara İlişkin Notlar

- `width` ve `height` yalnızca `size_preset` `Custom` olarak ayarlandığında etkili olur.
- Referans görsellerin ve üretilen görsellerin toplam sayısı 15'i aşamaz.
- `thinking` yalnızca metinden görüntüye üretimde devre dışı bırakılabilir; referans görseller sağlandığında devre dışı bırakılamaz.
- Seedream 5.0 Pro toplu üretimi desteklemez: her zaman tek bir görsel üretir, bu nedenle `max_images` ve `fail_on_partial` bu model için kullanılamaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Üretilen veya düzenlenen görsel, bir tensör olarak. Birden fazla görsel istenirse, bunlar tek bir toplu iş (batch) halinde birleştirilir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `f1a84171d94c602ec5417e43857ddf511ab1e54caa089b1928f740d3a38423f8`
