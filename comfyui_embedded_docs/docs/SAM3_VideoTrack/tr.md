> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/tr.md)

Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/en.md)

## Genel Bakış

SAM3'ün bellek tabanlı izleyicisini kullanarak video kareleri arasındaki nesneleri takip edin. Bu düğüm, bir dizi video karesini işler ve nesne kimliklerini kareler arasında korur; neyin izleneceğini tanımlamak için başlangıç maskelerini veya metin istemlerini kullanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntüler` | IMAGE | Evet | Toplu video kareleri | Toplu görüntüler olarak video kareleri |
| `model` | MODEL | Evet | SAM3 modeli | İzleme için kullanılacak SAM3 modeli |
| `ilk_maske` | MASK | Hayır | Nesne başına bir maske | İzlenecek ilk kare için maske(lar) (nesne başına bir tane). `koşullandırma` sağlanmadıysa zorunludur. |
| `koşullandırma` | CONDITIONING | Hayır | Metin koşullandırması | İzleme sırasında yeni nesneleri algılamak için metin koşullandırması. `ilk_maske` sağlanmadıysa zorunludur. |
| `tespit_eşiği` | FLOAT | Hayır | 0.0 ila 1.0 (varsayılan: 0.5) | Metin istemiyle algılama için puan eşiği |
| `maks_nesne` | INT | Hayır | 0 ila 64 (varsayılan: 0) | Maksimum izlenen nesne sayısı. Başlangıç maskeleri bu sınıra dahildir. 0, dahili sınır olan 64'ü kullanır. |
| `tespit_aralığı` | INT | Hayır | 1 ila sınırsız (varsayılan: 1) | Her N karede bir algılama çalıştırın (1=her kare). Daha yüksek değerler hesaplama tasarrufu sağlar. |

**Not:** `initial_mask` veya `conditioning`'den biri sağlanmalıdır. Her ikisi de atlanırsa, düğüm bir hata verecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `track_data` | SAM3TrackData | Tüm video karelerindeki nesne maskelerini ve meta verilerini içeren izleme verileri |

---
**Source fingerprint (SHA-256):** `30768bdf5839c1d7b984675e68a127a27f21b17724a2dc885e27f00c272db3cb`
