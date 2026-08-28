# ByteDance Seedance 2.0 İlk-Son-Kareden Videoya

Bu düğüm, ByteDance Seedance modellerini kullanarak zorunlu bir ilk kare görüntüsünden ve isteğe bağlı bir son kare görüntüsünden video üretir. Videoyu bir metin istemiyle tanımlarsınız; ilk kare videonun başlangıcını, son kare ise bitişini yönlendirir. Seedance 2.5 ve Seedance 2.0 ailesini (Seedance 2.0, Seedance 2.0 Fast ve Seedance 2.0 Mini) destekler.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | En yeni model ve 30 saniyeye kadar videolar ve mp4/mov çıktısı için Seedance 2.5; maksimum kalite ve 4k için Seedance 2.0; hız optimizasyonu için Fast; en hızlı ve en düşük maliyetli üretim için Mini. Bir model seçmek, aşağıda modele özgü girdileri ortaya çıkarır. | DYNAMIC_COMBO | Evet | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `first_frame` | Video için ilk kare görüntüsü. | IMAGE | Hayır | - |
| `last_frame` | Video için son kare görüntüsü. | IMAGE | Hayır | - |
| `first_frame_asset_id` | İlk kare olarak kullanılacak Seedance asset_id'si. `first_frame` görüntü girdisi ile birbirini dışlar. Varsayılan değer boş bir dizedir. | STRING | Hayır | - |
| `last_frame_asset_id` | Son kare olarak kullanılacak Seedance asset_id'si. `last_frame` görüntü girdisi ile birbirini dışlar. Varsayılan değer boş bir dizedir. | STRING | Hayır | - |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. Varsayılan değer 0'dır. | INT | Evet | 0 ile 2147483647 |
| `watermark` | Videoya filigran eklenip eklenmeyeceğini belirtir. Varsayılan değer False'tır. | BOOLEAN | Evet | False<br>True |

### Seedance 2.5 Girdileri

Bu girdiler `Seedance 2.5` seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video üretimi için metin istemi. Oluşturulan diyaloğu yönlendirmek için sözlü satırları çift tırnak içine alın. | STRING | Evet | - |
| `resolution` | Çıktı videosunun çözünürlüğü. Varsayılan değer 720p'dir. | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (4-30). Varsayılan değer 5'tir. | INT | Evet | 4 ile 30 |
| `generate_audio` | Çıktı videosu için ses üretimini etkinleştirir. Varsayılan değer True'dur. | BOOLEAN | Evet | False<br>True |
| `output_format` | Çıktı videosunun kapsayıcı formatı. Varsayılan değer mp4'tür. | COMBO | Evet | `"mp4"` |

### Seedance 2.0 Girdileri

Bu girdiler `Seedance 2.0` seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video üretimi için metin istemi. | STRING | Evet | - |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Çıktı videosunun en-boy oranı. Varsayılan değer, giriş karesinin en-boy oranına en yakın desteklenen oranı kullanan `adaptive` değeridir. | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (4-15). Varsayılan değer 7'dir. | INT | Evet | 4 ile 15 |
| `generate_audio` | Çıktı videosu için ses üretimini etkinleştirir. Varsayılan değer True'dur. | BOOLEAN | Evet | False<br>True |

### Seedance 2.0 Fast ve Seedance 2.0 Mini Girdileri

`Seedance 2.0 Fast` ve `Seedance 2.0 Mini` tarafından paylaşılır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video üretimi için metin istemi. | STRING | Evet | - |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"` |
| `ratio` | Çıktı videosunun en-boy oranı. Varsayılan değer, giriş karesinin en-boy oranına en yakın desteklenen oranı kullanan `adaptive` değeridir. | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (4-15). Varsayılan değer 7'dir. | INT | Evet | 4 ile 15 |
| `generate_audio` | Çıktı videosu için ses üretimini etkinleştirir. Varsayılan değer True'dur. | BOOLEAN | Evet | False<br>True |

**Parametre Kısıtlamaları**

- İlk kareyi ya bir `first_frame` görüntüsü ya da bir `first_frame_asset_id` olarak sağlamanız gerekir. Her ikisinin birden sağlanması hata oluşturur; hiçbirinin sağlanmaması da hata oluşturur.
- `last_frame` ve `last_frame_asset_id` girdileri isteğe bağlıdır, ancak aynı kare için ikisini birden sağlayamazsınız.
- Asset ID'leri mevcut, etkin Seedance Image asset'lerini referans göstermelidir.
- `prompt` girdisi zorunludur ve boş olamaz.
- `Seedance 2.5` ile çıktı en-boy oranı her zaman adaptive'dir ve ilk karenin kendi en-boy oranını izler; bu nedenle `ratio` girdisi gösterilmez.
- Seedance 2.0 ailesi modellerinde ve yerel kare görüntülerinde, görüntüler üretimden önce merkezden kırpılır ve hedef çıktı çözünürlüğüne ve oranına yeniden boyutlandırılır. `ratio` `adaptive` olduğunda, giriş görüntüsüne en yakın desteklenen oran kullanılır.
- Yerel kare görüntüleri, desteklenen en-boy oranı ve boyutlar açısından doğrulanır; aşırı büyük görüntüler küçültülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `bc2eb5f43c935986ad870703cfbc92dd99a53d6f0ac91cf0cad46bee33ff2cc0`
