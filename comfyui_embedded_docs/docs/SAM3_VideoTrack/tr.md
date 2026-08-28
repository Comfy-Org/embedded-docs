# SAM3 Video İzleme

SAM3'ün bellek tabanlı izleyicisini kullanarak video kareleri boyunca nesneleri takip edin. Bu düğüm, bir video karesi dizisini işler ve nesne kimliklerini kareler arasında korur; neyin izleneceğini tanımlamak için başlangıç maskelerini veya metin istemlerini kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntüler` | Toplu video kareleri olarak video kareleri | IMAGE | Evet | Toplu video kareleri |
| `model` | İzleme için kullanılacak SAM3 modeli | MODEL | Evet | SAM3 modeli |
| `ilk_maske` | İzlenecek ilk kareye ait maske(ler) (nesne başına bir adet) | MASK | Hayır | Nesne başına bir maske |
| `koşullandırma` | İzleme sırasında yeni nesneleri algılamak için metin koşullandırması | CONDITIONING | Hayır | Metin koşullandırması |
| `tespit_eşiği` | Metin istemli algılama için puan eşiği (varsayılan: 0.5) | FLOAT | Hayır | 0.0 ile 1.0 arası |
| `maks_nesne` | Maksimum izlenen nesne sayısı. Başlangıç maskeleri bu sınıra dahildir. 0, dahili 64 sınırını kullanır. (varsayılan: 4) | INT | Hayır | 0 ile 64 arası |
| `tespit_aralığı` | Algılamayı her N karede bir çalıştırın (1=her kare). Daha yüksek değerler hesaplama tasarrufu sağlar. (varsayılan: 1) | INT | Hayır | 1 veya daha yüksek |

**Not:** `initial_mask` veya `conditioning` girdilerinden en az biri sağlanmalıdır. İkisi de atlanırsa düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `iz_verisi` | Tüm video kareleri boyunca nesne maskelerini ve meta verilerini içeren izleme verisi | SAM3TrackData |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/tr.md)

---
**Source fingerprint (SHA-256):** `ef584628b334997a001a857a7deffb7eda34db8fa50e3d734a07b5e92566d48d`
