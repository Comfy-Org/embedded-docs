# ByteDance Seedance 2.0 İlk-Son-Kareden Videoya

Bu düğüm, ByteDance Seedance 2.5 veya Seedance 2.0 modellerini kullanarak zorunlu bir ilk kare görüntüsünden ve isteğe bağlı bir son kare görüntüsünden bir video oluşturur. İlk kare klibin başlangıcını tanımlar, son kare (sağlandığında) bitişi tanımlar ve bir metin istemi hareketi açıklar. Seçilen model, kullanılabilir çözünürlükleri, süreleri ve çıktı formatı seçeneklerini kontrol eder.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturma için kullanılan model. Seedance 2.5, 30 saniyeye kadar videolar ve mp4/mov çıktısı sunan en yeni modeldir; Seedance 2.0 maksimum kalite ve 1080p/4k sunar; Fast hız için optimize edilmiştir; Mini en hızlı, en düşük maliyetli üretimdir. Bir model seçmek, aşağıda o modele özgü girdileri ortaya çıkarır. | DYNAMIC_COMBO | Evet | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `first_frame` | Video için ilk kare görüntüsü. `first_frame` veya `first_frame_asset_id` alanlarından biri gereklidir. | IMAGE | Hayır | - |
| `last_frame` | Video için son kare görüntüsü. | IMAGE | Hayır | - |
| `first_frame_asset_id` | İlk kare olarak kullanılacak Seedance asset_id. `first_frame` görüntü girdisiyle karşılıklı olarak dışlayıcıdır. Varsayılan olarak boş bir dizedir. | STRING | Hayır | - |
| `last_frame_asset_id` | Son kare olarak kullanılacak Seedance asset_id. `last_frame` görüntü girdisiyle karşılıklı olarak dışlayıcıdır. Varsayılan olarak boş bir dizedir. | STRING | Hayır | - |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak belirleyici değildir. Varsayılan 0'dır. | INT | Hayır | 0 to 2147483647 |
| `watermark` | Videoya filigran eklenip eklenmeyeceği. Varsayılan False'tır. | BOOLEAN | Hayır | - |

### Seedance 2.5 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. Oluşturulan diyaloğu yönlendirmek için konuşma satırlarını çift tırnak içine alın. Varsayılan olarak boş bir dizedir. | STRING | Evet | - |
| `resolution` | Çıktı videosunun çözünürlüğü. Varsayılan "720p"dir. | COMBO | Evet | `"480p"`<br>`"720p"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (4-30). Varsayılan 5'tir. | INT | Evet | 4 to 30 |
| `generate_audio` | Çıktı videosu için ses oluşturmayı etkinleştirir. Varsayılan True'dur. | BOOLEAN | Evet | - |
| `output_format` | Çıktı videosunun kapsayıcı formatı. Varsayılan "mp4"tür. | COMBO | Evet | `"mp4"` |

### Seedance 2.0 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. Varsayılan olarak boş bir dizedir. | STRING | Evet | - |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Çıktı videosunun en-boy oranı. Varsayılan "adaptive"dir. | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (4-15). Varsayılan 7'dir. | INT | Evet | 4 to 15 |
| `generate_audio` | Çıktı videosu için ses oluşturmayı etkinleştirir. Varsayılan True'dur. | BOOLEAN | Evet | - |

### Seedance 2.0 Fast ve Seedance 2.0 Mini Tarafından Paylaşılan Girdiler

Bu iki model, yalnızca 480p ve 720p çözünürlüklerin kullanılabilir olması dışında Seedance 2.0 ile aynı girdileri sunar.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. Varsayılan olarak boş bir dizedir. | STRING | Evet | - |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"` |
| `ratio` | Çıktı videosunun en-boy oranı. Varsayılan "adaptive"dir. | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (4-15). Varsayılan 7'dir. | INT | Evet | 4 to 15 |
| `generate_audio` | Çıktı videosu için ses oluşturmayı etkinleştirir. Varsayılan True'dur. | BOOLEAN | Evet | - |

**Kısıtlamalar ve sınırlamalar:**

*   `prompt` alanı gereklidir ve en az bir boşluk olmayan karakter içermelidir (baştaki ve sondaki boşluklar yok sayılır).
*   Tam olarak bir ilk kare kaynağı sağlamalısınız: ya `first_frame` görüntüsü ya da `first_frame_asset_id`. Her ikisinin de sağlanması bir hata oluşturur; hiçbirinin sağlanmaması da bir hata oluşturur.
*   `last_frame` görüntüsü ve `last_frame_asset_id` karşılıklı olarak dışlayıcıdır. Her ikisi de atlanabilir.
*   Varlık kimlikleri (asset ID), Active durumuna sahip mevcut Seedance varlıklarına başvurmalıdır. Bir varlık aktif değilse veya bir Görüntü varlığı değilse, bir hata oluşturulur.
*   Yerel görüntüler 0,4 ile 2,5 (2:5 ile 5:2) arasında bir en-boy oranına sahip olmalıdır.
*   Seedance 2.0 modelleri için yerel görüntüler en az 300x300 piksel olmalıdır. Seçilen çözünürlük ve oran için desteklenen çıktı boyutlarına otomatik olarak yeniden boyutlandırılır ve istek "adaptive" oranıyla gönderilir. `ratio` değeri "adaptive" olduğunda, çıktı en-boy oranı ilk karenin kendi en-boy oranından türetilir ve desteklenen en yakın orana yuvarlanır. Yerel görüntüler yerine varlık kimlikleri kullanıldığında, seçilen `ratio` değeri doğrudan uygulanır.
*   Seedance 2.5 için ve varlık kimlikleri kullanıldığında herhangi bir model için, görüntüler otomatik olarak en fazla 6000 piksel olacak şekilde küçültülür ve her boyutta 300 ile 6000 piksel arasında olmalıdır.
*   Seedance 2.5 her zaman ilk karenin kendi en-boy oranını korur, bu nedenle bu model için `ratio` girdisi gösterilmez.
*   Süre sınırları modele göre farklılık gösterir: Seedance 2.5, 4 ila 30 saniyeyi desteklerken, Seedance 2.0, 2.0 Fast ve 2.0 Mini, 4 ila 15 saniyeyi destekler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `d87265eb75d67f7d80f76474fc699f7ca87b6edbddda36733d5e440708b074a2`
