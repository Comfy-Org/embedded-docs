# ByteDance Seedream 4.5 & 5.0

Bu düğüm, ByteDance Seedream modellerini (4.0, 4.5, 5.0 Lite ve 5.0 Pro) kullanarak görüntüler oluşturur veya düzenler. Bir metin isteminden yeni görüntüler üretir ve referans görüntülere ve tek cümlelik bir talimata dayanarak mevcut görüntüleri düzenleyebilir; 4K'ya kadar çözünürlükleri destekler.

## Girdiler

`model` seçici, hangi modele özgü girdilerin kullanılabilir olduğunu belirler. Aşağıdaki tablolar, ortak girdileri, her model için girdileri ve büyütülebilir referans-görüntü yuvalarını listeler.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Üretim için kullanılacak Seedream model sürümü. Her modelin farklı yetenekleri, sınırları ve fiyatlandırması vardır. | DYNAMIC_COMBO | Evet | `"seedream 5.0 pro"`<br>`"seedream 5.0 lite"`<br>`"seedream-4-5-251128"`<br>`"seedream-4-0-250828"` |
| `prompt` | Görüntü oluşturmak veya düzenlemek için metin istemi. | STRING | Evet | Herhangi bir metin (boş olmayan) |
| `seed` | Üretim için kullanılacak tohum (varsayılan: 0). | INT | Evet | 0 to 2147483647 |
| `watermark` | Görüntüye "AI generated" (Yapay zeka tarafından oluşturuldu) filigranı eklenip eklenmeyeceği (varsayılan: False). | BOOLEAN | Evet | True / False |
| `thinking` | Daha iyi uyum için modelin istem optimizasyonu muhakemesini ("thinking") etkinleştirin. Üretim süresini önemli ölçüde artırabilir — özellikle Seedream 5.0 Pro'da. Yalnızca metinden görüntüye üretimde devre dışı bırakılabilir (referans görüntüler sağlandığında değil). (varsayılan: True) | BOOLEAN | Hayır | True / False |

### seedream 5.0 pro Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Önerilen bir boyut seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Custom'ı seçin. | COMBO | Evet | Modele özgü ön ayarlar (Custom dahil) |
| `width` | Görüntü için özel genişlik. Değer yalnızca `size_preset` Custom olarak ayarlandığında çalışır (varsayılan: 2048). | INT | Evet | 1024 to 3136 (step 2) |
| `height` | Görüntü için özel yükseklik. Değer yalnızca `size_preset` Custom olarak ayarlandığında çalışır (varsayılan: 2048). | INT | Evet | 1024 to 2496 (step 2) |

### seedream 5.0 lite Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Önerilen bir boyut seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Custom'ı seçin. | COMBO | Evet | Modele özgü ön ayarlar (Custom dahil) |
| `width` | Görüntü için özel genişlik. Değer yalnızca `size_preset` Custom olarak ayarlandığında çalışır (varsayılan: 2048). | INT | Evet | 1024 to 6240 (step 2) |
| `height` | Görüntü için özel yükseklik. Değer yalnızca `size_preset` Custom olarak ayarlandığında çalışır (varsayılan: 2048). | INT | Evet | 1024 to 4992 (step 2) |
| `max_images` | Oluşturulacak maksimum görüntü sayısı. 1 ile tam olarak bir görüntü üretilir. >1 ile model, 1 ile max_images arasında ilişkili görüntüler üretir (örn. hikaye sahneleri, karakter varyasyonları). Toplam görüntü sayısı (girdi + oluşturulan) 15'i aşamaz. (varsayılan: 1) | INT | Evet | 1 to 14 |
| `fail_on_partial` | Etkinleştirilirse, istenen görüntülerden herhangi biri eksikse veya bir hata döndürürse yürütmeyi durdurur. (varsayılan: False) | BOOLEAN | Evet | True / False |

### seedream-4-5-251128 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Önerilen bir boyut seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Custom'ı seçin. | COMBO | Evet | Modele özgü ön ayarlar (Custom dahil) |
| `width` | Görüntü için özel genişlik. Değer yalnızca `size_preset` Custom olarak ayarlandığında çalışır (varsayılan: 2048). | INT | Evet | 1024 to 6240 (step 2) |
| `height` | Görüntü için özel yükseklik. Değer yalnızca `size_preset` Custom olarak ayarlandığında çalışır (varsayılan: 2048). | INT | Evet | 1024 to 4992 (step 2) |
| `max_images` | Oluşturulacak maksimum görüntü sayısı. 1 ile tam olarak bir görüntü üretilir. >1 ile model, 1 ile max_images arasında ilişkili görüntüler üretir (örn. hikaye sahneleri, karakter varyasyonları). Toplam görüntü sayısı (girdi + oluşturulan) 15'i aşamaz. (varsayılan: 1) | INT | Evet | 1 to 10 |
| `fail_on_partial` | Etkinleştirilirse, istenen görüntülerden herhangi biri eksikse veya bir hata döndürürse yürütmeyi durdurur. (varsayılan: False) | BOOLEAN | Evet | True / False |

### seedream-4-0-250828 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Önerilen bir boyut seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Custom'ı seçin. | COMBO | Evet | Modele özgü ön ayarlar (Custom dahil) |
| `width` | Görüntü için özel genişlik. Değer yalnızca `size_preset` Custom olarak ayarlandığında çalışır (varsayılan: 2048). | INT | Evet | 1024 to 6240 (step 2) |
| `height` | Görüntü için özel yükseklik. Değer yalnızca `size_preset` Custom olarak ayarlandığında çalışır (varsayılan: 2048). | INT | Evet | 1024 to 4992 (step 2) |
| `max_images` | Oluşturulacak maksimum görüntü sayısı. 1 ile tam olarak bir görüntü üretilir. >1 ile model, 1 ile max_images arasında ilişkili görüntüler üretir (örn. hikaye sahneleri, karakter varyasyonları). Toplam görüntü sayısı (girdi + oluşturulan) 15'i aşamaz. (varsayılan: 1) | INT | Evet | 1 to 10 |
| `fail_on_partial` | Etkinleştirilirse, istenen görüntülerden herhangi biri eksikse veya bir hata döndürürse yürütmeyi durdurur. (varsayılan: False) | BOOLEAN | Evet | True / False |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Görüntüden görüntüye veya çoklu referans üretimi için isteğe bağlı referans görüntü(ler)i. Büyütülebilir yuva: 1..N öğe bağlayın (`image_1`, `image_2`, ..., `image_N`); maksimum sayı seçilen modele bağlıdır (seedream 5.0 pro, seedream-4-5-251128 ve seedream-4-0-250828 için 10; seedream 5.0 lite için 14). | IMAGE | Hayır | 0 to 10<br>0 to 14 (seedream 5.0 lite) |

### Notlar

- Özel `width` ve `height` değerleri yalnızca `size_preset` Custom olarak ayarlandığında etkili olur.
- Çözünürlük sınırları (genişlik × yüksekliğe göre):
  - seedream 5.0 pro: minimum 0.92 MP, maksimum 4.19 MP.
  - seedream 5.0 lite ve seedream-4-5-251128: minimum 3.68 MP.
  - seedream-4-0-250828: minimum 0.92 MP.
  - seedream 5.0 lite, seedream-4-5-251128 ve seedream-4-0-250828: maksimum 16.78 MP.
- Referans görüntülerin en-boy oranı 1:3 ile 3:1 arasında olmalıdır.
- `max_images` 1'den büyük olduğunda (seedream 5.0 lite, seedream-4-5-251128 ve seedream-4-0-250828'de kullanılabilir), toplam görüntü sayısı (referans görüntüler artı oluşturulan görüntüler) 15'i aşamaz.
- `thinking` yalnızca metinden görüntüye üretimde devre dışı bırakılabilir; referans görüntüler sağlandığında etkinleştirilmiş olmalıdır.
- seedream 5.0 pro her zaman tek bir görüntü üretir ve `max_images` veya `fail_on_partial` girdilerini göstermez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Oluşturulan veya düzenlenen görüntü. `max_images` ile birden fazla görüntü istendiyse, bunlar tek bir toplu iş halinde birleştirilmiş olarak döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `b57e0d85a586aaeb7cf02ceaaddcd2d36cdac20f5251cba48de602a979420f1c`
