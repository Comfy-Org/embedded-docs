# WanAnimateToVideo

WanAnimateToVideo; referans görüntü, poz, yüz, arka plan ve önceki parçadan isteğe bağlı hareket gibi girdileri kullanarak Wan ile animasyonlu videolar üretmek için koşullandırma verilerini ve bir başlangıç latentini hazırlar. Ayrıca `video_frame_offset` değerini okuyup güncelleyerek videoların parçalar hâlinde daha uzun üretilmesini destekler. Bu düğüm deneysel olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Üretimi istenen içeriğe yönlendirmek için pozitif koşullandırma. | CONDITIONING | Evet | - |
| `negatif` | Üretimi istenmeyen içerikten uzaklaştırmak için negatif koşullandırma. | CONDITIONING | Evet | - |
| `vae` | Görüntü ve video girdilerini latent uzaya kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `genişlik` | Üretilen videonun piksel cinsinden genişliği (varsayılan: 832, adım: 16). | INT | Evet | 16 ila MAX_RESOLUTION |
| `yükseklik` | Üretilen videonun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16). | INT | Evet | 16 ila MAX_RESOLUTION |
| `uzunluk` | Üretilecek kare sayısı (varsayılan: 77, adım: 4). | INT | Evet | 1 ila MAX_RESOLUTION |
| `toplu_iş_boyutu` | Tek partide üretilecek video sayısı (varsayılan: 1). | INT | Evet | 1 ila 4096 |
| `clip_vision_çıkışı` | Hem pozitif hem negatif koşullandırmaya eklenen isteğe bağlı CLIP vision çıktısı. | CLIP_VISION_OUTPUT | Hayır | - |
| `referans_görsel` | Üretilen video için görünüm başlangıç noktası olarak kullanılan referans görüntü. Sağlanmazsa siyah bir görüntü kullanılır. | IMAGE | Hayır | - |
| `yüz_videosu` | Yüz ifadesi yönlendirmesi sağlayan video girdisi. Dahili olarak 512x512 boyutuna yeniden boyutlandırılır ve -1.0 ila 1.0 aralığına ölçeklenir. | IMAGE | Hayır | - |
| `poz_videosu` | Poz ve hareket yönlendirmesi sağlayan video girdisi. | IMAGE | Hayır | - |
| `devam_eden_hareket_maksimum_kare_sayısı` | Önceki bir hareket dizisinden aktarılacak maksimum kare sayısı (varsayılan: 5, adım: 4). | INT | Evet | 1 ila MAX_RESOLUTION |
| `arka_plan_videosu` | Karelerin karakter dışı kısımlarını doldurmak için kullanılan arka plan videosu. | IMAGE | Hayır | - |
| `karakter_maskesi` | Karakter bölgelerini tanımlayan ve karakteri arka plandan ayırmak için kullanılan maske. | MASK | Hayır | - |
| `devam_eden_hareket` | Önceki hareket kareleri; önceden üretilmiş parçalarla zamansal tutarlılığı korumak için devam ettirilir. | IMAGE | Hayır | - |
| `video_kare_konumu` | Tüm girdi videolarında aranacak kare miktarı. Daha uzun videoları parça parça üretmek için kullanılır. Bir videoyu uzatmak için önceki düğümün video_frame_offset çıktısına bağlayın. (varsayılan: 0, adım: 1) | INT | Evet | 0 ila MAX_RESOLUTION |

**Parametre Kısıtlamaları:**

- `continue_motion` sağlandığında, yalnızca son `continue_motion_max_frames` karesi kullanılır.
- Girdi videoları (`face_video`, `pose_video`, `background_video`, `character_mask`) kullanımdan önce `video_frame_offset` kadar ötelenir. Öteleme değeri girdinin kare sayısına eşit veya daha büyükse, tek karelik `character_mask` dışında bu girdi yok sayılır.
- `character_mask` yalnızca bir kareye sahipse, bu kare çıktının her karesi için tekrarlanır.
- `pose_video`, `length` değerinden kısaysa, kalan kareleri doldurmak için son karesi tekrarlanır; çıktı uzunluğu değişmez.
- `clip_vision_output` sağlanırsa, hem pozitif hem negatif koşullandırmaya eklenir.
- `reference_image` sağlanmazsa, varsayılan referans olarak siyah bir görüntü (tüm değerler sıfır) kullanılır.
- `continue_motion` sağlanmazsa, ilk hareket kareleri sabit gri (0,5 yoğunluk) karelerle doldurulur.
- `continue_motion` kullanıldığında, sonraki parça ötelemesi hesaplanmadan önce `video_frame_offset`, aktarılan kare sayısı kadar azaltılır; böylece örtüşen kareler iki kez işlenmez.
- `background_video`, referans-hareket kısmından sonraki hareket karelerini doldurur; referans görüntünün veya aktarılan `continue_motion` karelerinin yerini almaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | CLIP vision çıktısı, poz video latenti, yüz video pikselleri, birleştirilmiş latent görüntü ve birleştirilmiş maske dâhil olmak üzere ek video bağlamıyla değiştirilmiş pozitif koşullandırma. | CONDITIONING |
| `negatif` | CLIP vision çıktısı, poz video latenti, boş yüz pikselleri, birleştirilmiş latent görüntü ve birleştirilmiş maske dâhil olmak üzere ek video bağlamıyla değiştirilmiş negatif koşullandırma. | CONDITIONING |
| `gizli_uzay` | `[batch_size, 16, latent_length + trim_latent, latent_height, latent_width]` şeklinde, üretilen video için başlangıç latent tensörü (tüm örnekler sıfır). | LATENT |
| `kırpılmış_gizli_uzay` | Referans görüntü karelerine karşılık gelen, latentin başlangıcından kırpılacak latent kare sayısı. | INT |
| `kırpılmış_görsel` | Referans hareket karelerine karşılık gelen, başlangıçtan kırpılacak görüntü karesi sayısı. | INT |
| `video_kare_konumu` | İşlenen kare sayısına ve girdi ötelemesine bağlı olarak sonraki parça için kullanılacak güncellenmiş kare ötelemesi. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `a95bae4c7ae4ddc8a95bc9dafa2ca920b1d2166802615189537dce16949bfc03`
