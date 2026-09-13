# SAM3 Video İzleme

SAM3'ün bellek tabanlı izleyicisini kullanarak nesneleri video kareleri boyunca takip edin. Düğüm, bir video kareleri dizisini işler ve kareler arasında nesne kimliklerini korur; neyin izleneceğini tanımlamak için başlangıç maskelerini veya metin istemlerini kullanır ve metin koşullandırmasıyla izleme sırasında yeni nesneleri algılayabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `images` | Toplu görüntüler olarak video kareleri | IMAGE | Evet | Toplu video kareleri |
| `model` | İzleme için kullanılacak SAM3 modeli | MODEL | Evet | SAM3 modeli |
| `initial_mask` | İzlenecek ilk kare için maskeler (nesne başına bir tane) | MASK | Hayır | Nesne başına bir maske |
| `conditioning` | İzleme sırasında yeni nesneleri algılamak için metin koşullandırması | CONDITIONING | Hayır | Metin koşullandırması |
| `detection_threshold` | Metin istemiyle algılama için puan eşiği (varsayılan: 0.5) | FLOAT | Hayır | 0.0 ile 1.0 arası (adım 0.01) |
| `max_objects` | Maksimum izlenen nesne sayısı. Başlangıç maskeleri bu sınıra dahildir. 0, dahili 64 üst sınırını kullanır. (varsayılan: 4) | INT | Hayır | 0 ile 64 arası |
| `detect_interval` | Algılamayı her N karede bir çalıştır (1=her kare). Daha yüksek değerler hesaplamadan tasarruf sağlar. (varsayılan: 1) | INT | Hayır | 1 veya daha yüksek |

**Not:** `initial_mask` veya `conditioning` alanlarından biri sağlanmalıdır. İkisi de belirtilmezse düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `track_data` | Tüm video kareleri boyunca nesne maskelerini ve meta verileri içeren izleme verileri | SAM3_TRACK_DATA |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/tr.md)

---
**Source fingerprint (SHA-256):** `ef584628b334997a001a857a7deffb7eda34db8fa50e3d734a07b5e92566d48d`
