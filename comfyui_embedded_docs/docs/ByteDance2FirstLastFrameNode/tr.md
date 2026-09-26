# ByteDance Seedance 2.0 İlk-Son-Kareden Videoya

Bu düğüm, ByteDance Seedance modellerini kullanarak zorunlu bir ilk kare görüntüsünden ve isteğe bağlı bir son kare görüntüsünden video oluşturur. Videoyu bir metin istemiyle tanımlarsınız; ilk kare videonun başlangıcını, son kare ise bitişini yönlendirir. Seedance 2.5 ve Seedance 2.0 ailesini (Seedance 2.0, Seedance 2.0 Fast ve Seedance 2.0 Mini) destekler. `Seedance 2.5 Draft` modelini seçmek bunun yerine hızlı bir 480p önizleme oluşturur; elde edilen `draft_task_id` çıktısını 1080p finali oluşturmak için ByteDance Seedance 2.5 Draft to Final Video düğümüne bağlayın.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | En yeni model için Seedance 2.5; 30 saniyeye kadar videolar ve mp4 çıktısı; `draft_task_id` çıktısı ByteDance Seedance 2.5 Draft to Final Video düğümünde 1080p finali oluşturan hızlı 480p önizleme için Seedance 2.5 Draft; maksimum kalite ve 4k için Seedance 2.0; hız optimizasyonu için Fast; en hızlı, en düşük maliyetli üretim için Mini. Bir model seçildiğinde aşağıda modele özgü girdiler görünür. | DYNAMIC_COMBO | Evet | `"Seedance 2.5"`<br>`"Seedance 2.5 Draft"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `first_frame` | Video için ilk kare görüntüsü. | IMAGE | Hayır | - |
| `last_frame` | Video için son kare görüntüsü. | IMAGE | Hayır | - |
| `first_frame_asset_id` | İlk kare olarak kullanılacak Seedance asset_id değeri. `first_frame` görüntü girdisiyle karşılıklı olarak dışlayıcıdır. Varsayılan boş bir dizedir. | STRING | Hayır | - |
| `last_frame_asset_id` | Son kare olarak kullanılacak Seedance asset_id değeri. `last_frame` görüntü girdisiyle karşılıklı olarak dışlayıcıdır. Varsayılan boş bir dizedir. | STRING | Hayır | - |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan 0'dır. | INT | Evet | 0 - 2147483647 |
| `watermark` | Videoya filigran eklenip eklenmeyeceği. Varsayılan False. | BOOLEAN | Evet | False<br>True |

### Seedance 2.5 Girdileri

Bu girdiler `Seedance 2.5` seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video üretimi için metin istemi. Oluşturulan diyaloğu yönlendirmek için konuşma repliklerini çift tırnak içine alın. | STRING | Evet | - |
| `resolution` | Çıktı videosunun çözünürlüğü. Varsayılan 720p'dir. | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (4-30). Varsayılan 5'tir. | INT | Evet | 4 - 30 |
| `generate_audio` | Çıktı videosu için ses üretimini etkinleştir. Varsayılan True. | BOOLEAN | Evet | False<br>True |
| `output_format` | Çıktı videosunun kapsayıcı biçimi. Varsayılan mp4'tür. | COMBO | Evet | `"mp4"` |

### Seedance 2.5 Draft Girdileri

Bu girdiler `Seedance 2.5 Draft` seçildiğinde görünür. Parametre kümesi yukarıdaki Seedance 2.5 ile aynıdır; ancak `resolution` yalnızca `"480p"` sunar (varsayılan `"480p"`).

### Seedance 2.0 Girdileri

Bu girdiler `Seedance 2.0` seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video üretimi için metin istemi. | STRING | Evet | - |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Çıktı videosunun en-boy oranı. Varsayılan `adaptive`'dir; bu, girdi karesinin en-boy oranına en yakın desteklenen oranı kullanır. | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (4-15). Varsayılan 7'dir. | INT | Evet | 4 - 15 |
| `generate_audio` | Çıktı videosu için ses üretimini etkinleştir. Varsayılan True. | BOOLEAN | Evet | False<br>True |

### Seedance 2.0 Fast ve Seedance 2.0 Mini Girdileri

`Seedance 2.0 Fast` ve `Seedance 2.0 Mini` tarafından paylaşılır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video üretimi için metin istemi. | STRING | Evet | - |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"` |
| `ratio` | Çıktı videosunun en-boy oranı. Varsayılan `adaptive`'dir; bu, girdi karesinin en-boy oranına en yakın desteklenen oranı kullanır. | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (4-15). Varsayılan 7'dir. | INT | Evet | 4 - 15 |
| `generate_audio` | Çıktı videosu için ses üretimini etkinleştir. Varsayılan True. | BOOLEAN | Evet | False<br>True |

**Parametre Kısıtlamaları**

- İlk kareyi ya `first_frame` görüntüsü ya da `first_frame_asset_id` değeri olarak sağlamalısınız. Her ikisini de sağlamak hataya yol açar; hiçbirini sağlamamak da hataya yol açar.
- `last_frame` ve `last_frame_asset_id` girdileri isteğe bağlıdır, ancak aynı kare için ikisini birden sağlayamazsınız.
- Asset ID'leri mevcut ve etkin Seedance Image varlıklarına başvurmalıdır.
- `prompt` girdisi zorunludur ve boş olamaz.
- Her çalıştırma, görev kimliğini `draft_task_id` olarak döndürür; ancak yalnızca bir `Seedance 2.5 Draft` çalıştırmasının kimliği ByteDance Seedance 2.5 Draft to Final Video düğümü tarafından oluşturulabilir. Başka herhangi bir modelde çıktı bağlantısız bırakılmalıdır; aksi halde çalıştırma başarısız olur.
- `Seedance 2.5` ile çıktı en-boy oranı her zaman `adaptive`'tir ve ilk karenin kendi en-boy oranını izler; bu nedenle `ratio` girdisi gösterilmez.
- Seedance 2.0 ailesi modelleri ve yerel kare görüntüleri kullanıldığında, görüntüler üretimden önce hedef çıktı çözünürlüğüne ve oranına göre ortadan kırpılır ve yeniden boyutlandırılır. `ratio` `adaptive` olduğunda, girdi görüntüsüne en yakın desteklenen oran kullanılır.
- Yerel kare görüntüleri desteklenen en-boy oranı ve boyutlar açısından doğrulanır; aşırı büyük görüntüler küçültülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video. | VIDEO |
| `draft_task_id` | Çalıştırma tarafından döndürülen görev kimliği. Yalnızca bir `Seedance 2.5 Draft` çalıştırması, ByteDance Seedance 2.5 Draft to Final Video düğümünün oluşturabileceği bir taslak üretir; başka herhangi bir modelde çıktı bağlantısız bırakılmalıdır; aksi halde çalıştırma başarısız olur. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `363f1baac1685c2dada0e64a0b339f6ab2671161dccb002eb81f6b4f0d0aa243`
