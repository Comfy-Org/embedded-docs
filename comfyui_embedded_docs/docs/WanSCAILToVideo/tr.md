# WanSCAILToVideo

WanSCAILToVideo düğümü, SCAIL ve SCAIL-2 video modelleriyle video üretimi için koşullandırma ve boş bir latent uzayı hazırlar. Referans görüntüleri, poz videoları, CLIP vision çıktıları, renkli kimlik maskeleri ve önceki kare parçaları gibi isteğe bağlı girdileri işleyerek bunları pozitif ve negatif koşullandırmaya gömer. Düğüm, değiştirilmiş koşullandırmayı ve belirtilen video boyutlarında boş bir latent tensörü çıkarır; örneklemeye hazırdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-----------|-----------|----------|-------|
| `pozitif` | Pozitif koşullandırma girdisi. | CONDITIONING | Evet | - |
| `negatif` | Negatif koşullandırma girdisi. | CONDITIONING | Evet | - |
| `vae` | Görüntüleri ve video karelerini kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 512). Değerler 32'şer artar. | INT | Evet | 32 to MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 896). Değerler 32'şer artar. | INT | Evet | 32 to MAX_RESOLUTION |
| `uzunluk` | Videodaki kare sayısı (varsayılan: 81). Değerler 4'er artar. | INT | Evet | 1 to MAX_RESOLUTION |
| `toplu_boyutu` | Bir partide (batch) üretilecek video sayısı (varsayılan: 1). | INT | Evet | 1 ile 4096 |
| `poz_videosu` | Poz koşullandırması için kullanılan video. Ana videonun çözünürlüğünün yarısına küçültülür. | IMAGE | Hayır | - |
| `pose_video_mask` | Yalnızca SCAIL-2. pose_video ile aynı çözünürlükte, kimlik başına renkli SAM3 maske videosu. | IMAGE | Hayır | - |
| `replacement_mode` | Yalnızca SCAIL-2. False = Animasyon Modu (pose_video_mask siyah arka plana sahip olmalıdır). True = Değiştirme Modu (pose_video_mask beyaz arka plana sahip olmalıdır). (varsayılan: False) | BOOLEAN | Hayır | - |
| `poz_gücü` | Poz latentinin gücü. (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 10.0 |
| `poz_başlangıcı` | Poz koşullandırmasının başlangıç adımı. (varsayılan: 0.0) | FLOAT | Evet | 0.0 ile 1.0 |
| `poz_bitişi` | Poz koşullandırmasının bitiş adımı. (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 |
| `referans_görsel` | Referans görüntü. İlk görüntü birincil referanstır (tüm kimlikler bunun üzerine birleştirilir). SCAIL-2: partideki ek görüntüler ek görünümler olarak kullanılır (arka görünüm, yakın çekim, kapanmış arka plan); her biri o kimliğin renginde eşleşen bir reference_image_mask gerektirir. | IMAGE | Hayır | - |
| `reference_image_mask` | Yalnızca SCAIL-2. Renkli referans maskesi; partideki reference_image ile eşleşir (ilki = birincil referans maskesi, geri kalanlar = ek reference_image için kimlik maskeleri). | IMAGE | Hayır | - |
| `clip_vision_output` | Koşullandırma için CLIP vision özellikleri. Model, en boy oranına esneterek yeniden boyutlandırma (stretch resize) ile eğitilmiştir. | CLIP_VISION_OUTPUT | Hayır | - |
| `video_frame_offset` | Bu parçanın başladığı kümülatif çıktı karesi. Önceki parçanın video_frame_offset çıktısından bağlayın. (varsayılan: 0) | INT | Evet | 0 to MAX_RESOLUTION |
| `previous_frame_count` | previous_frames içinden çıpa olarak kullanılacak son kareler. SCAIL-2, 5 değeriyle eğitilmiştir (81 karelik parçalar, 76 karelik adım). (varsayılan: 5) | INT | Evet | 1 to MAX_RESOLUTION |
| `previous_frames` | Yalnızca SCAIL-2. Önceki parçanın tamamen çözülmüş çıktısı. Yalnızca son previous_frame_count kare, uzantı çıpası olarak kullanılır. | IMAGE | Hayır | - |

**Not:** `pose_video` ve `pose_video_mask` girdileri birlikte, ikisinden kısa olanın uzunluğuna kırpılır ve yalnızca ilk `length` kare için işlenir. Girdilerden herhangi biri `video_frame_offset` değerinden kısa veya ona eşitse tamamen yok sayılır. `pose_video`, kodlamadan önce ana videonun çözünürlüğünün yarısına küçültülür; kodlanmış poz latenti `pose_strength` ile çarpılır ve koşullandırmaya yalnızca `pose_start` ile `pose_end` zaman adımları arasında uygulanır. `pose_video_mask` sağlanırsa, renkli maske videosu yarı çözünürlüğe küçültülür ve hem pozitif hem de negatif koşullandırmaya eklenen 28 kanallı bir sürüş maskesine (driving mask) dönüştürülür.

**Not:** `reference_image` sağlandığında, partideki her görüntü ayrı ayrı bir latent'e kodlanır ve hem pozitif hem de negatif koşullandırmaya gömülür. İlk görüntü birincil referanstır; ek görüntüler ek görünümler olarak kullanılır ve her biri eşleşen bir `reference_image_mask` gerektirir. `reference_image_mask` yalnızca `reference_image` de sağlandığında kullanılır; ikisi de verildiğinde, referans karelerini kimliklere bağlayan 28 kanallı bir referans maskesi de maskelerden oluşturulur ve koşullandırmaya eklenir. Değiştirme Modu'nda (`replacement_mode=True`), referans görüntüsü, referans görüntü maskesi bir alfa matı olarak kullanılarak siyah bir arka plan üzerine birleştirilir. `clip_vision_output` sağlandığında, hem pozitif hem de negatif koşullandırmaya uygulanır.

**Not:** `previous_frames` sağlandığında, yalnızca son `previous_frame_count` kare, uzantı çıpası olarak kullanılır ve `video_frame_offset` buna göre ayarlanır (çıpa olarak kullanılan kare sayısı kadar azaltılır, 0 ile sınırlandırılır). Çıpa olarak kullanılan kareler kodlanır ve çıktı latent'inin başına yazılır; bu karelerin üretim sırasında değişmeden kalması için bir gürültü maskesi eklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|-----------|-----------|
| `pozitif` | Değiştirilmiş pozitif koşullandırma; gömülü referans görüntü latentleri, CLIP vision çıktısı, poz video latentleri, sürüş maskeleri, referans maskeleri veya önceki kare latentlerini içerebilir. | CONDITIONING |
| `negatif` | Değiştirilmiş negatif koşullandırma; gömülü referans görüntü latentleri, CLIP vision çıktısı, poz video latentleri, sürüş maskeleri, referans maskeleri veya önceki kare latentlerini içerebilir. | CONDITIONING |
| `latent` | `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]` şeklinde boş bir latent tensörü. `previous_frames` sağlandığında latent, kodlanmış önceki karelerle kısmen doldurulur ve bir gürültü maskesi eklenir. | LATENT |
| `video_frame_offset` | Ayarlanmış offset + length. Ardışık video üretimi için bir sonraki parçaya bağlayın. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `4a1a2201dfa94bd2f1330db02ec18a5e0a6aae9e9ac5ae97d456b7af1aa84b7b`
