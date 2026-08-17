# SAM3 Video İzleme

SAM3'ün bellek tabanlı takipçisini kullanarak video kareleri arasında nesneleri takip edin. Bu düğüm, bir video kare dizisini işler ve başlangıç maskelerini veya metin istemlerini kullanarak neyin takip edileceğini tanımlar, nesne kimliklerini kareler arasında korur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `images` | Toplu görüntüler halinde video kareleri | IMAGE | Evet | Toplu video kareleri |
| `model` | Takip için kullanılacak SAM3 modeli | MODEL | Evet | SAM3 modeli |
| `initial_mask` | Takip edilecek ilk kare için maske(ler) (nesne başına bir adet). `conditioning` sağlanmadıysa gereklidir. | MASK | Hayır | Nesne başına bir maske |
| `conditioning` | Takip sırasında yeni nesneleri algılamak için metin koşullandırması. `initial_mask` sağlanmadıysa gereklidir. | CONDITIONING | Hayır | Metin koşullandırması |
| `detection_threshold` | Metin istemiyle algılama için skor eşiği (varsayılan: 0.5). | FLOAT | Evet | 0.0 to 1.0 |
| `max_objects` | Maksimum takip edilen nesne sayısı. Başlangıç maskeleri bu sınıra dahildir. 0, dahili üst sınır olan 64'ü kullanır (varsayılan: 4). | INT | Evet | 0 to 64 |
| `detect_interval` | Algılamayı her N karede bir çalıştırın (1=her kare). Daha yüksek değerler hesaplama gücünden tasarruf sağlar (varsayılan: 1). | INT | Evet | 1 veya daha yüksek |

**Not:** `initial_mask` veya `conditioning` değerlerinden en az biri sağlanmalıdır. İkisi de atlanırsa düğüm bir hata verir. İkisi de sağlandığında, başlangıç maskeleri ilk kareden itibaren takip edilecek nesneleri tanımlar ve metin istemleri takip sırasında ek nesneleri algılar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `track_data` | Orijinal kare boyutları dahil olmak üzere, tüm video kareleri boyunca nesne maskelerini ve meta verilerini içeren takip verileri. | SAM3_TRACK_DATA |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/tr.md)

---
**Source fingerprint (SHA-256):** `ef584628b334997a001a857a7deffb7eda34db8fa50e3d734a07b5e92566d48d`
