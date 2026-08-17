# WanAnimateToVideo

Bu deneysel düğüm, bir referans görüntüyü isteğe bağlı poz, yüz ve arka plan videolarıyla birleştirerek Wan video üretimini hazırlar. Sonraki üretim için koşullandırma verisi ve boş bir latent video tensörü oluşturur ve mevcut videoları parçalar halinde genişletmeye yardımcı olan kare ofseti bilgisi döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Üretimi istenen içeriğe yönlendirmek için pozitif koşullandırma. | CONDITIONING | Evet | - |
| `negative` | Üretimi istenmeyen içerikten uzaklaştırmak için negatif koşullandırma. | CONDITIONING | Evet | - |
| `vae` | Görüntü verilerini kodlamak ve çözmek için kullanılan VAE modeli. | VAE | Evet | - |
| `width` | Piksel cinsinden çıktı video genişliği (varsayılan: 832, adım: 16). | INT | Evet | 16 to MAX_RESOLUTION |
| `height` | Piksel cinsinden çıktı video yüksekliği (varsayılan: 480, adım: 16). | INT | Evet | 16 to MAX_RESOLUTION |
| `length` | Üretilecek kare sayısı (varsayılan: 77, adım: 4). | INT | Evet | 1 to MAX_RESOLUTION |
| `batch_size` | Tek seferde üretilecek video sayısı (varsayılan: 1). | INT | Evet | 1 to 4096 |
| `clip_vision_output` | İsteğe bağlı CLIP görüş modeli çıktısı; hem pozitif hem de negatif koşullandırma için ek koşullandırma olarak kullanılır. | CLIP_VISION_OUTPUT | Hayır | - |
| `reference_image` | Üretim için başlangıç noktası olarak kullanılan referans görüntü. Sağlanmazsa, siyah bir görüntü (tümü sıfır) kullanılır. | IMAGE | Hayır | - |
| `face_video` | Yüz ifadesi yönlendirmesi sağlayan video. İşlendiğinde 512x512 boyutuna yeniden boyutlandırılır ve -1.0 ile 1.0 aralığına normalleştirilir. | IMAGE | Hayır | - |
| `pose_video` | Poz ve hareket yönlendirmesi sağlayan video. `length` değerinden kısaysa, son karesiyle tekrarlanarak doldurulur. | IMAGE | Hayır | - |
| `continue_motion_max_frames` | Önceki bir hareketten devam edilecek maksimum kare sayısı. `continue_motion` girişinin yalnızca bu sayıdaki son karesi kullanılır (varsayılan: 5, adım: 4). | INT | Evet | 1 to MAX_RESOLUTION |
| `background_video` | Üretilen içerikle birleştirilecek arka plan videosu. | IMAGE | Hayır | - |
| `character_mask` | Seçici işleme için karakter bölgelerini tanımlayan maske. Maske yalnızca bir kareye sahipse, tüm karelerde tekrarlanır. | MASK | Hayır | - |
| `continue_motion` | Bir videoyu genişletirken zamansal tutarlılığı sağlamak için kullanılan önceki hareket dizisi. Yalnızca son `continue_motion_max_frames` karesi kullanılır. | IMAGE | Hayır | - |
| `video_frame_offset` | Tüm giriş videolarında aranacak kare miktarı. Daha uzun videoları parça parça üretmek için kullanılır. Bir videoyu genişletmek için önceki düğümün video_frame_offset çıktısına bağlayın. (varsayılan: 0, adım: 1) | INT | Evet | 0 to MAX_RESOLUTION |

**Parametre Kısıtlamaları:**

- `pose_video` sağlandığında, daha kısa bir poz videosu `length` değerine ulaşmak için son karesiyle doldurulur. Kaynak, şu anda devre dışı olan ve bunun yerine çıktıyı poz videosu uzunluğuyla eşleşecek şekilde kısaltacak bir `trim_to_pose_video` bayrağı içerir.
- `face_video` 512x512 boyutuna yeniden boyutlandırılır ve -1.0 ile 1.0 aralığına normalleştirilir.
- `continue_motion` son `continue_motion_max_frames` karesiyle sınırlıdır. `continue_motion` kullanıldığında, `video_frame_offset` alınan kare sayısı kadar azaltılır, ancak asla 0'ın altına düşmez.
- Giriş videoları (`face_video`, `pose_video`, `background_video`, `character_mask`) `video_frame_offset` kadar kaydırılır. Ofset, uzunluklarından büyük veya eşitse, giriş yok sayılır; ancak her zaman tekrarlanan tek karelik `character_mask` bunun dışındadır.
- `clip_vision_output` sağlandığında, hem pozitif hem de negatif koşullandırmaya uygulanır.
- `reference_image` sağlanmazsa, referans olarak siyah bir görüntü (tümü sıfır) kullanılır.
- `continue_motion` sağlanmazsa, hareket bölümü için piksel değeri 0.5 olan gri kareler kullanılır.
- `width` ve `height` 16'lık bir adım kullanır; buna karşılık gelen latent boyutlar `width / 8` ve `height / 8`'dir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Birleştirilmiş latent görüntüyü ve birleştirilmiş maskeyi her zaman içeren değiştirilmiş pozitif koşullandırma. `clip_vision_output`, `pose_video` veya `face_video` sağlanırsa, değerleri de eklenir. | CONDITIONING |
| `negative` | Birleştirilmiş latent görüntüyü ve birleştirilmiş maskeyi her zaman içeren değiştirilmiş negatif koşullandırma. `clip_vision_output`, `pose_video` veya `face_video` sağlanırsa, değerleri de eklenir; yüz videosu pikselleri -1.0 olarak ayarlanır. | CONDITIONING |
| `latent` | Sıfırlarla başlatılmış boş latent tensör; şekli `[batch_size, 16, latent_length + trim_latent, latent_height, latent_width]`. | LATENT |
| `trim_latent` | Baştan kırpılacak latent kare sayısı; referans görüntü latent karelerine karşılık gelir. | INT |
| `trim_image` | Baştan kırpılacak görüntü kare sayısı; referans hareket karelerine karşılık gelir. | INT |
| `video_frame_offset` | Parçalı video üretimi için güncellenmiş kare ofseti; ayarlanmış giriş ofseti artı üretilen uzunluğa eşittir. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `a95bae4c7ae4ddc8a95bc9dafa2ca920b1d2166802615189537dce16949bfc03`
