# ByteDanceSeedreamNodeV3

ByteDance Seedream 4.5 & 5.0; ByteDance Seedream 4.0, 4.5 ve 5.0 modellerini 4K çözünürlüğe kadar kullanarak, bir metin isteminden (metinden görüntüye) görüntü üretir veya isteğe bağlı referans görüntülerinin rehberliğinde görüntü üretir/düzenler. Düğüm, istemi ve varsa referans görüntülerini ByteDance API'sine gönderir, üretim görevinin tamamlanmasını bekler ve sonuçta oluşan görüntü tensörünü veya tensörlerini döndürür.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Görüntü oluşturma veya düzenleme için metin istemi. Baştaki ve sondaki boşluklar silindikten sonra boş olmamalıdır. | STRING | Evet | Multiline text |
| `model` | Kullanılacak Seedream modelini seçer. Her model, aşağıda kendi alt parametrelerini ve sınırlarını sunar. | DYNAMIC_COMBO | Evet | "seedream 5.0 pro"<br>"seedream 5.0 lite"<br>"seedream-4-5-251128"<br>"seedream-4-0-250828" |

### Seedream 5.0 Pro Girdileri (seedream 5.0 pro)

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Önerilen bir boyut seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Custom seçeneğini belirleyin. Varsayılan: bu model için önerilen ilk hazır ayar. | COMBO | Hayır | Model-specific recommended size presets<br>"Custom" |
| `width` | Görüntü için özel genişlik. Değer yalnızca `size_preset` "Custom" olarak ayarlandığında çalışır. Varsayılan: 2048. | INT | Hayır | 1024 to 3136 (step 2) |
| `height` | Görüntü için özel yükseklik. Değer yalnızca `size_preset` "Custom" olarak ayarlandığında çalışır. Varsayılan: 2048. | INT | Hayır | 1024 to 2496 (step 2) |
| `prompt_optimization` | Referans görüntüler sağlandığında istem iyileştirme modu: 'standard' daha yüksek kalite, 'fast' daha kısa üretim süresi sağlar. Varsayılan: "standard". | COMBO | Hayır | "standard"<br>"fast" |
| `seed` | Üretim için kullanılacak seed değeri. Varsayılan: 42. | INT | Hayır | 0 to 2147483647 |
| `watermark` | Görüntüye "AI generated" filigranı eklenip eklenmeyeceği. Varsayılan: false. | BOOLEAN | Hayır | true / false |
| `thinking` | Daha iyi uyum için modelin istem iyileştirme muhakemesini ('thinking') etkinleştirir. Üretim süresini önemli ölçüde artırabilir — özellikle Seedream 5.0 Pro'da. Yalnızca metinden görüntüye üretimde devre dışı bırakılabilir (referans görüntüler sağlandığında değil). Varsayılan: true. | BOOLEAN | Hayır | true / false |

### Seedream 5.0 Lite Girdileri (seedream 5.0 lite)

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Önerilen bir boyut seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Custom seçeneğini belirleyin. Varsayılan: bu model için önerilen ilk hazır ayar. | COMBO | Hayır | Model-specific recommended size presets<br>"Custom" |
| `width` | Görüntü için özel genişlik. Değer yalnızca `size_preset` "Custom" olarak ayarlandığında çalışır. Varsayılan: 2048. | INT | Hayır | 1024 to 6240 (step 2) |
| `height` | Görüntü için özel yükseklik. Değer yalnızca `size_preset` "Custom" olarak ayarlandığında çalışır. Varsayılan: 2048. | INT | Hayır | 1024 to 4992 (step 2) |
| `max_images` | Üretilecek maksimum görüntü sayısı. 1 ile tam olarak bir görüntü üretilir. >1 ile model, 1 ile max_images arasında ilişkili görüntü üretir (örn. hikaye sahneleri, karakter varyasyonları). Toplam görüntü (girdi + üretilen) 15'i aşamaz. Varsayılan: 1. | INT | Hayır | 1 to 14 |
| `fail_on_partial` | Etkinleştirilirse, istenen görüntülerden herhangi biri eksikse veya bir hata dönerse yürütmeyi durdurur. Varsayılan: false. | BOOLEAN | Hayır | true / false |
| `seed` | Üretim için kullanılacak seed değeri. Varsayılan: 42. | INT | Hayır | 0 to 2147483647 |
| `watermark` | Görüntüye "AI generated" filigranı eklenip eklenmeyeceği. Varsayılan: false. | BOOLEAN | Hayır | true / false |
| `thinking` | Daha iyi uyum için modelin istem iyileştirme muhakemesini ('thinking') etkinleştirir. Üretim süresini önemli ölçüde artırabilir — özellikle Seedream 5.0 Pro'da. Yalnızca metinden görüntüye üretimde devre dışı bırakılabilir (referans görüntüler sağlandığında değil). Varsayılan: true. | BOOLEAN | Hayır | true / false |

### Seedream 4.5 Girdileri (seedream-4-5-251128)

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Önerilen bir boyut seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Custom seçeneğini belirleyin. Varsayılan: bu model için önerilen ilk hazır ayar. | COMBO | Hayır | Model-specific recommended size presets<br>"Custom" |
| `width` | Görüntü için özel genişlik. Değer yalnızca `size_preset` "Custom" olarak ayarlandığında çalışır. Varsayılan: 2048. | INT | Hayır | 1024 to 6240 (step 2) |
| `height` | Görüntü için özel yükseklik. Değer yalnızca `size_preset` "Custom" olarak ayarlandığında çalışır. Varsayılan: 2048. | INT | Hayır | 1024 to 4992 (step 2) |
| `max_images` | Üretilecek maksimum görüntü sayısı. 1 ile tam olarak bir görüntü üretilir. >1 ile model, 1 ile max_images arasında ilişkili görüntü üretir (örn. hikaye sahneleri, karakter varyasyonları). Toplam görüntü (girdi + üretilen) 15'i aşamaz. Varsayılan: 1. | INT | Hayır | 1 to 10 |
| `fail_on_partial` | Etkinleştirilirse, istenen görüntülerden herhangi biri eksikse veya bir hata dönerse yürütmeyi durdurur. Varsayılan: false. | BOOLEAN | Hayır | true / false |
| `seed` | Üretim için kullanılacak seed değeri. Varsayılan: 42. | INT | Hayır | 0 to 2147483647 |
| `watermark` | Görüntüye "AI generated" filigranı eklenip eklenmeyeceği. Varsayılan: false. | BOOLEAN | Hayır | true / false |
| `thinking` | Daha iyi uyum için modelin istem iyileştirme muhakemesini ('thinking') etkinleştirir. Üretim süresini önemli ölçüde artırabilir — özellikle Seedream 5.0 Pro'da. Yalnızca metinden görüntüye üretimde devre dışı bırakılabilir (referans görüntüler sağlandığında değil). Varsayılan: true. | BOOLEAN | Hayır | true / false |

### Seedream 4.0 Girdileri (seedream-4-0-250828)

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Önerilen bir boyut seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Custom seçeneğini belirleyin. Varsayılan: bu model için önerilen ilk hazır ayar. | COMBO | Hayır | Model-specific recommended size presets<br>"Custom" |
| `width` | Görüntü için özel genişlik. Değer yalnızca `size_preset` "Custom" olarak ayarlandığında çalışır. Varsayılan: 2048. | INT | Hayır | 1024 to 6240 (step 2) |
| `height` | Görüntü için özel yükseklik. Değer yalnızca `size_preset` "Custom" olarak ayarlandığında çalışır. Varsayılan: 2048. | INT | Hayır | 1024 to 4992 (step 2) |
| `max_images` | Üretilecek maksimum görüntü sayısı. 1 ile tam olarak bir görüntü üretilir. >1 ile model, 1 ile max_images arasında ilişkili görüntü üretir (örn. hikaye sahneleri, karakter varyasyonları). Toplam görüntü (girdi + üretilen) 15'i aşamaz. Varsayılan: 1. | INT | Hayır | 1 to 10 |
| `fail_on_partial` | Etkinleştirilirse, istenen görüntülerden herhangi biri eksikse veya bir hata dönerse yürütmeyi durdurur. Varsayılan: false. | BOOLEAN | Hayır | true / false |
| `seed` | Üretim için kullanılacak seed değeri. Varsayılan: 42. | INT | Hayır | 0 to 2147483647 |
| `watermark` | Görüntüye "AI generated" filigranı eklenip eklenmeyeceği. Varsayılan: false. | BOOLEAN | Hayır | true / false |
| `thinking` | Daha iyi uyum için modelin istem iyileştirme muhakemesini ('thinking') etkinleştirir. Üretim süresini önemli ölçüde artırabilir — özellikle Seedream 5.0 Pro'da. Yalnızca metinden görüntüye üretimde devre dışı bırakılabilir (referans görüntüler sağlandığında değil). Varsayılan: true. | BOOLEAN | Hayır | true / false |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Büyüyebilir yuva: görüntüden görüntüye veya çoklu referans üretimi için isteğe bağlı referans görüntüsü/görüntüleri. 1..N görüntü bağlayın (örn. `image_1`, `image_2`, ...); sayı sınırı modele göredir (aşağıdaki notlara bakın). Bağlı bir görüntü bir görüntü kümesi içeriyorsa, kümedeki her görüntü sınıra dahil sayılır. | IMAGE | Hayır | 0 to 10 (Seedream 5.0 Pro, Seedream 4.5, Seedream 4.0)<br>0 to 14 (Seedream 5.0 Lite) |

**Notlar:**

- `prompt` boşluk karakterleri silindikten sonra boş olmamalıdır.
- Maksimum referans görüntü sayısı: Seedream 5.0 Pro, Seedream 4.5 ve Seedream 4.0 için 10; Seedream 5.0 Lite için 14.
- Her referans görüntüsünün en-boy oranı 1:3 ile 3:1 arasında olmalıdır.
- `max_images` değeri 1'den büyük olduğunda (Seedream 5.0 Pro'da kullanılamaz), referans görüntüleri ile üretilen görüntülerin toplam sayısı 15'i aşamaz.
- `thinking` yalnızca metinden görüntüye üretimde devre dışı bırakılabilir. Referans görüntüler sağlandığında `thinking` etkinleştirilmiş olmalıdır.
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
| `image` | Üretilen görüntü tensörü. Birden çok görüntü üretildiğinde, bunlar tek bir toplu (batched) IMAGE tensöründe birleştirilir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV3/tr.md)

---
**Source fingerprint (SHA-256):** `68dd23afdb5720491cef784b22ad66ff0baf80984ea652ea4c13e6c264c029ac`
