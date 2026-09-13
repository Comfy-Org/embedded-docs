# ByteDance Seedream 4.5 & 5.0

ByteDance Seedream 4.5 ve 5.0, ByteDance Seedream 4.0, 4.5 ve 5.0 modellerini kullanarak 4K çözünürlüğe kadar metin isteminden görüntü üretir (metinden görüntüye) veya isteğe bağlı referans görüntülerle yönlendirilen görüntüleri üretir/düzenler. Düğüm, istemi ve varsa referans görüntüleri ByteDance API'sine gönderir, üretim görevinin tamamlanmasını bekler ve ortaya çıkan görüntü tensörünü veya tensörlerini döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Görüntü oluşturmak veya düzenlemek için metin istemi. Boşluklar kırpıldıktan sonra boş olmamalıdır. | STRING | Evet | Çok satırlı metin |
| `model` | Kullanılacak Seedream modelini seçer. Her model aşağıda kendi alt parametre ve sınırlarını sunar. | DYNAMIC_COMBO | Evet | "seedream 5.0 pro"<br>"seedream 5.0 lite"<br>"seedream-4-5-251128"<br>"seedream-4-0-250828" |

### Seedream 5.0 Pro Girdileri (seedream 5.0 pro)

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Önerilen bir boyut seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Custom'ı seçin. Varsayılan: bu model için ilk önerilen ön ayar. | COMBO | Hayır | Modele özgü önerilen boyut ön ayarları<br>"Custom" |
| `width` | Görüntü için özel genişlik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında geçerlidir. Varsayılan: 2048. | INT | Hayır | 1024 - 3136 (adım 2) |
| `height` | Görüntü için özel yükseklik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında geçerlidir. Varsayılan: 2048. | INT | Hayır | 1024 - 2496 (adım 2) |
| `prompt_optimization` | Referans görüntüler sağlandığında istem optimizasyon modu: 'standard' daha yüksek kalite, 'fast' daha kısa üretim süresi verir. Varsayılan: "standard". | COMBO | Hayır | "standard"<br>"fast" |
| `seed` | Üretim için kullanılacak tohum. Varsayılan: 42. | INT | Hayır | 0 - 2147483647 |
| `watermark` | Görüntüye "AI generated" filigranı eklenip eklenmeyeceği. Varsayılan: false. | BOOLEAN | Hayır | true / false |
| `thinking` | Daha iyi uyum için modelin istem optimizasyonu akıl yürütmesini ('thinking') etkinleştirir. Üretim süresini önemli ölçüde artırabilir — özellikle Seedream 5.0 Pro'da. Yalnızca metinden görüntüye için devre dışı bırakılabilir (referans görüntüler sağlandığında değil). Varsayılan: true. | BOOLEAN | Hayır | true / false |

### Seedream 5.0 Lite Girdileri (seedream 5.0 lite)

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Önerilen bir boyut seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Custom'ı seçin. Varsayılan: bu model için ilk önerilen ön ayar. | COMBO | Hayır | Modele özgü önerilen boyut ön ayarları<br>"Custom" |
| `width` | Görüntü için özel genişlik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında geçerlidir. Varsayılan: 2048. | INT | Hayır | 1024 - 6240 (adım 2) |
| `height` | Görüntü için özel yükseklik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında geçerlidir. Varsayılan: 2048. | INT | Hayır | 1024 - 4992 (adım 2) |
| `max_images` | Üretilecek maksimum görüntü sayısı. 1 ile tam olarak bir görüntü üretilir. >1 ile model, 1 ile max_images arasında ilişkili görüntü üretir (örn. hikaye sahneleri, karakter varyasyonları). Toplam görüntü (girdi + üretilen) 15'i aşamaz. Varsayılan: 1. | INT | Hayır | 1 - 14 |
| `fail_on_partial` | Etkinleştirilirse, istenen görüntülerden herhangi biri eksikse veya bir hata döndürülürse yürütmeyi durdurur. Varsayılan: false. | BOOLEAN | Hayır | true / false |
| `seed` | Üretim için kullanılacak tohum. Varsayılan: 42. | INT | Hayır | 0 - 2147483647 |
| `watermark` | Görüntüye "AI generated" filigranı eklenip eklenmeyeceği. Varsayılan: false. | BOOLEAN | Hayır | true / false |
| `thinking` | Daha iyi uyum için modelin istem optimizasyonu akıl yürütmesini ('thinking') etkinleştirir. Üretim süresini önemli ölçüde artırabilir — özellikle Seedream 5.0 Pro'da. Yalnızca metinden görüntüye için devre dışı bırakılabilir (referans görüntüler sağlandığında değil). Varsayılan: true. | BOOLEAN | Hayır | true / false |

### Seedream 4.5 Girdileri (seedream-4-5-251128)

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Önerilen bir boyut seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Custom'ı seçin. Varsayılan: bu model için ilk önerilen ön ayar. | COMBO | Hayır | Modele özgü önerilen boyut ön ayarları<br>"Custom" |
| `width` | Görüntü için özel genişlik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında geçerlidir. Varsayılan: 2048. | INT | Hayır | 1024 - 6240 (adım 2) |
| `height` | Görüntü için özel yükseklik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında geçerlidir. Varsayılan: 2048. | INT | Hayır | 1024 - 4992 (adım 2) |
| `max_images` | Üretilecek maksimum görüntü sayısı. 1 ile tam olarak bir görüntü üretilir. >1 ile model, 1 ile max_images arasında ilişkili görüntü üretir (örn. hikaye sahneleri, karakter varyasyonları). Toplam görüntü (girdi + üretilen) 15'i aşamaz. Varsayılan: 1. | INT | Hayır | 1 - 10 |
| `fail_on_partial` | Etkinleştirilirse, istenen görüntülerden herhangi biri eksikse veya bir hata döndürülürse yürütmeyi durdurur. Varsayılan: false. | BOOLEAN | Hayır | true / false |
| `seed` | Üretim için kullanılacak tohum. Varsayılan: 42. | INT | Hayır | 0 - 2147483647 |
| `watermark` | Görüntüye "AI generated" filigranı eklenip eklenmeyeceği. Varsayılan: false. | BOOLEAN | Hayır | true / false |
| `thinking` | Daha iyi uyum için modelin istem optimizasyonu akıl yürütmesini ('thinking') etkinleştirir. Üretim süresini önemli ölçüde artırabilir — özellikle Seedream 5.0 Pro'da. Yalnızca metinden görüntüye için devre dışı bırakılabilir (referans görüntüler sağlandığında değil). Varsayılan: true. | BOOLEAN | Hayır | true / false |

### Seedream 4.0 Girdileri (seedream-4-0-250828)

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Önerilen bir boyut seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Custom'ı seçin. Varsayılan: bu model için ilk önerilen ön ayar. | COMBO | Hayır | Modele özgü önerilen boyut ön ayarları<br>"Custom" |
| `width` | Görüntü için özel genişlik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında geçerlidir. Varsayılan: 2048. | INT | Hayır | 1024 - 6240 (adım 2) |
| `height` | Görüntü için özel yükseklik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında geçerlidir. Varsayılan: 2048. | INT | Hayır | 1024 - 4992 (adım 2) |
| `max_images` | Üretilecek maksimum görüntü sayısı. 1 ile tam olarak bir görüntü üretilir. >1 ile model, 1 ile max_images arasında ilişkili görüntü üretir (örn. hikaye sahneleri, karakter varyasyonları). Toplam görüntü (girdi + üretilen) 15'i aşamaz. Varsayılan: 1. | INT | Hayır | 1 - 10 |
| `fail_on_partial` | Etkinleştirilirse, istenen görüntülerden herhangi biri eksikse veya bir hata döndürülürse yürütmeyi durdurur. Varsayılan: false. | BOOLEAN | Hayır | true / false |
| `seed` | Üretim için kullanılacak tohum. Varsayılan: 42. | INT | Hayır | 0 - 2147483647 |
| `watermark` | Görüntüye "AI generated" filigranı eklenip eklenmeyeceği. Varsayılan: false. | BOOLEAN | Hayır | true / false |
| `thinking` | Daha iyi uyum için modelin istem optimizasyonu akıl yürütmesini ('thinking') etkinleştirir. Üretim süresini önemli ölçüde artırabilir — özellikle Seedream 5.0 Pro'da. Yalnızca metinden görüntüye için devre dışı bırakılabilir (referans görüntüler sağlandığında değil). Varsayılan: true. | BOOLEAN | Hayır | true / false |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Büyütülebilir yuva: görüntüden görüntüye veya çok referanslı üretim için isteğe bağlı referans görüntü(ler). 1..N görüntü bağlayın (örn. `image_1`, `image_2`, ...); sayı sınırı modele göredir (aşağıdaki notlara bakın). Bağlanan bir görüntü bir görüntü yığını içeriyorsa, yığındaki her görüntü sınıra sayılır. | IMAGE | Hayır | 0 - 10 (Seedream 5.0 Pro, Seedream 4.5, Seedream 4.0)<br>0 - 14 (Seedream 5.0 Lite) |

**Notlar:**

- `prompt`, boşluklar kırpıldıktan sonra boş olmamalıdır.
- Maksimum referans görüntü sayısı: Seedream 5.0 Pro, Seedream 4.5 ve Seedream 4.0 için 10; Seedream 5.0 Lite için 14.
- Her referans görüntünün en-boy oranı 1:3 ile 3:1 arasında olmalıdır.
- `max_images` 1'den büyük olduğunda (Seedream 5.0 Pro'da mevcut değildir), referans görüntüler ile üretilen görüntülerin toplam sayısı 15'i aşamaz.
- `thinking` yalnızca metinden görüntüye üretimi için devre dışı bırakılabilir. Referans görüntüler sağlandığında `thinking` etkinleştirilmiş olmalıdır.
- `width` ve `height` yalnızca `size_preset` "Custom" olarak ayarlandığında kullanılır.
- `prompt_optimization` yalnızca Seedream 5.0 Pro'da kullanılabilir.
- `max_images` ve `fail_on_partial` yalnızca Seedream 5.0 Lite, Seedream 4.5 ve Seedream 4.0'da kullanılabilir; Seedream 5.0 Pro her zaman tek bir görüntü ister.
- Çözünürlük gereksinimleri (genişlik x yükseklik):
  - Seedream 5.0 Pro: 0.92MP (921,600 piksel) ile 4.19MP (4,194,304 piksel) arasında.
  - Seedream 5.0 Lite ve Seedream 4.5: en az 3.68MP (3,686,400 piksel).
  - Seedream 4.0: en az 0.92MP (921,600 piksel).
  - Pro olmayan tüm modeller: en fazla 16.78MP (16,777,216 piksel).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Üretilen görüntü tensörü. Birden fazla görüntü üretildiğinde, tek bir toplu IMAGE tensöründe birleştirilir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV3/tr.md)

---
**Source fingerprint (SHA-256):** `68dd23afdb5720491cef784b22ad66ff0baf80984ea652ea4c13e6c264c029ac`
