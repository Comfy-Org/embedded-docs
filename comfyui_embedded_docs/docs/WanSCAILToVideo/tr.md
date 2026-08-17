# WanSCAILToVideo

WanSCAILToVideo düğümü, video üretimi için conditioning ve boş bir latent alan hazırlar. Referans görüntüler, poz videoları, CLIP vision çıktıları ve önceki kare parçaları gibi isteğe bağlı girdileri işleyerek bunları bir video modeli için pozitif ve negatif conditioning içine gömer. Düğüm, değiştirilmiş conditioning'i ve belirtilen video boyutlarında boş bir latent tensörü çıktı olarak verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `positive` | Pozitif conditioning girdisi. | CONDITIONING | Evet | - |
| `negative` | Negatif conditioning girdisi. | CONDITIONING | Evet | - |
| `vae` | Görüntüleri ve video karelerini kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `width` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 512). 32'lik adımlarla ayarlanabilir. | INT | Evet | 32 to MAX_RESOLUTION |
| `height` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 896). 32'lik adımlarla ayarlanabilir. | INT | Evet | 32 to MAX_RESOLUTION |
| `length` | Videodaki kare sayısı (varsayılan: 81). 1'den başlayarak 4'lük adımlarla ayarlanabilir. | INT | Evet | 1 to MAX_RESOLUTION |
| `batch_size` | Bir batch içinde üretilecek video sayısı (varsayılan: 1). | INT | Evet | 1 to 4096 |
| `pose_strength` | Poz latentinin gücü (varsayılan: 1.0). | FLOAT | Evet | 0.0 to 10.0 |
| `pose_start` | Poz conditioning'inin başlangıç adımı (varsayılan: 0.0). | FLOAT | Evet | 0.0 to 1.0 |
| `pose_end` | Poz conditioning'inin bitiş adımı (varsayılan: 1.0). | FLOAT | Evet | 0.0 to 1.0 |
| `video_frame_offset` | Bu parçanın başladığı kümülatif çıktı karesi. Önceki parçanın video_frame_offset çıktısından bağlayın (varsayılan: 0). | INT | Evet | 0 to MAX_RESOLUTION |
| `previous_frame_count` | Çıpa olarak kullanılacak previous_frames kuyruk kareleri. SCAIL-2, 5 ile eğitilmiştir (81 karelik parçalar, 76 karelik adım) (varsayılan: 5). | INT | Evet | 1 to MAX_RESOLUTION |
| `pose_video` | Poz conditioning için kullanılan video. Ana videonun çözünürlüğünün yarısına ölçeklenir. | IMAGE | Hayır | - |
| `pose_video_mask` | Yalnızca SCAIL-2. pose_video ile aynı çözünürlükte, kimlik başına renkli SAM3 maske videosu. | IMAGE | Hayır | - |
| `replacement_mode` | Yalnızca SCAIL-2. False = Animasyon Modu (pose_video_mask siyah arka plana sahip olmalıdır). True = Değiştirme Modu (pose_video_mask beyaz arka plana sahip olmalıdır). Varsayılan: False. | BOOLEAN | Hayır | - |
| `reference_image` | Referans görüntü. İlk görüntü birincil referanstır (tüm kimlikleri onun üzerinde birleştirin). SCAIL-2: ek batch görüntüleri ek görünümler olarak kullanılır (arka görünüm, yakın çekim, kapatılmış arka plan); her biri o kimliğin renginde eşleşen bir reference_image_mask gerektirir. | IMAGE | Hayır | - |
| `reference_image_mask` | Yalnızca SCAIL-2. Renkli referans maskesi; reference_image ile batch eşleşmesi (ilk = birincil referans maskesi, geri kalanı = ek reference_image için kimlik maskeleri). | IMAGE | Hayır | - |
| `clip_vision_output` | Conditioning için CLIP vision özellikleri. Model, en-boy oranına esnetilerek yeniden boyutlandırma ile eğitilmiştir. | CLIP_VISION_OUTPUT | Hayır | - |
| `previous_frames` | Yalnızca SCAIL-2. Önceki parçanın tamamen kod çözülmüş çıktısı. Uzatma çıpası olarak yalnızca son previous_frame_count kare kullanılır. | IMAGE | Hayır | - |

**Not:**

- `pose_video` ve `pose_video_mask` girdileri `video_frame_offset` konumundan başlayarak dilimlenir; video o ofsetin ötesinde kare içermiyorsa yok sayılır. Ardından birlikte ikisinden kısa olanına göre kısaltılır ve `length` kare ile sınırlandırılır. `pose_video`, kodlamadan önce ana videonun çözünürlüğünün yarısına ölçeklenir.
- `reference_image_mask` girdisi yalnızca `reference_image` de sağlandığında geçerlidir. `reference_image` batch'indeki her görüntü, tek karelik bir latent referans olarak ayrı ayrı kodlanır. Değiştirme Modunda (`replacement_mode=True`), referans görüntüler, referans görüntü maskesi alfa mat olarak kullanılarak siyah bir arka plan üzerinde birleştirilir.
- `clip_vision_output` sağlandığında, hem pozitif hem negatif conditioning'e uygulanır.
- `previous_frames` sağlandığında, uzatma çıpası olarak yalnızca son `previous_frame_count` kare kullanılır. Çıktı latent'i bu karelerin kodlamasıyla kısmen doldurulur, latent çıktıya bir gürültü maskesi dahil edilir ve `video_frame_offset`, korunan kare sayısı çıkarılarak ayarlanır (asla 0'ın altına inmez).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Değiştirilmiş pozitif conditioning; potansiyel olarak gömülü referans görüntü latentleri, CLIP vision çıktısı, poz video latentleri, sürüş maskeleri, referans maskeleri veya önceki kare latentleri içerir. | CONDITIONING |
| `negative` | Değiştirilmiş negatif conditioning; potansiyel olarak gömülü referans görüntü latentleri, CLIP vision çıktısı, poz video latentleri, sürüş maskeleri, referans maskeleri veya önceki kare latentleri içerir. | CONDITIONING |
| `latent` | Şekli `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]` olan boş bir latent tensör. previous_frames sağlandığında, latent kodlanmış önceki karelerle kısmen doldurulur ve bir gürültü maskesi dahil edilir. | LATENT |
| `video_frame_offset` | Ayarlanmış ofset + uzunluk. Sıralı video üretimi için bir sonraki parçaya bağlayın. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `4a1a2201dfa94bd2f1330db02ec18a5e0a6aae9e9ac5ae97d456b7af1aa84b7b`
