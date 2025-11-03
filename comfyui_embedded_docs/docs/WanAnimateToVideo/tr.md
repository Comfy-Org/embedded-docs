> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/tr.md)

WanAnimateToVideo düğümü, poz referansları, yüz ifadeleri ve arka plan öğeleri dahil olmak üzere birden fazla koşullandırma girdisini birleştirerek video içeriği oluşturur. Çeşitli video girdilerini işleyerek tutarlı animasyon dizileri oluşturur ve kareler arasında zamansal tutarlılığı korur. Düğüm, latent uzay operasyonlarını yönetir ve mevcut hareket kalıplarını devam ettirerek mevcut videoları uzatabilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | İstenen içeriğe yönlendirmek için pozitif koşullandırma |
| `negative` | CONDITIONING | Evet | - | İstenmeyen içerikten uzaklaştırmak için negatif koşullandırma |
| `vae` | VAE | Evet | - | Görüntü verilerini kodlamak ve çözmek için kullanılan VAE modeli |
| `width` | INT | Hayır | 16'dan MAX_RESOLUTION'a | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, adım: 16) |
| `height` | INT | Hayır | 16'dan MAX_RESOLUTION'a | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) |
| `length` | INT | Hayır | 1'den MAX_RESOLUTION'a | Oluşturulacak kare sayısı (varsayılan: 77, adım: 4) |
| `batch_size` | INT | Hayır | 1'den 4096'ya | Aynı anda oluşturulacak video sayısı (varsayılan: 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Hayır | - | Ek koşullandırma için isteğe bağlı CLIP görüntü modeli çıktısı |
| `reference_image` | IMAGE | Hayır | - | Oluşturma için başlangıç noktası olarak kullanılan referans görüntü |
| `face_video` | IMAGE | Hayır | - | Yüz ifadesi rehberliği sağlayan video girdisi |
| `pose_video` | IMAGE | Hayır | - | Poz ve hareket rehberliği sağlayan video girdisi |
| `continue_motion_max_frames` | INT | Hayır | 1'den MAX_RESOLUTION'a | Önceki harekete devam edilecek maksimum kare sayısı (varsayılan: 5, adım: 4) |
| `background_video` | IMAGE | Hayır | - | Oluşturulan içerikle birleştirilecek arka plan videosu |
| `character_mask` | MASK | Hayır | - | Seçici işleme için karakter bölgelerini tanımlayan maske |
| `continue_motion` | IMAGE | Hayır | - | Zamansal tutarlılık için devam edilecek önceki hareket dizisi |
| `video_frame_offset` | INT | Hayır | 0'dan MAX_RESOLUTION'a | Tüm girdi videolarında atlanacak kare miktarı. Videoyu parçalar halinde uzatarak daha uzun videolar oluşturmak için kullanılır. Bir videoyu uzatmak için önceki düğümün video_frame_offset çıktısına bağlayın. (varsayılan: 0, adım: 1) |

**Parametre Kısıtlamaları:**

- `pose_video` sağlandığında ve `trim_to_pose_video` mantığı etkin olduğunda, çıktı uzunluğu poz videosunun süresine uyacak şekilde ayarlanır
- `face_video` işlendiğinde otomatik olarak 512x512 çözünürlüğe yeniden boyutlandırılır
- `continue_motion` kareleri `continue_motion_max_frames` parametresi ile sınırlıdır
- Girdi videoları (`face_video`, `pose_video`, `background_video`, `character_mask`) işlemeden önce `video_frame_offset` değeri kadar kaydırılır
- `character_mask` yalnızca bir kare içeriyorsa, tüm kareler boyunca tekrarlanır
- `clip_vision_output` sağlandığında, hem pozitif hem de negatif koşullandırmaya uygulanır

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Ek video bağlamı ile değiştirilmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Ek video bağlamı ile değiştirilmiş negatif koşullandırma |
| `latent` | LATENT | Latent uzay formatında oluşturulan video içeriği |
| `trim_latent` | INT | Sonraki işlemler için latent uzay kırpma bilgisi |
| `trim_image` | INT | Referans hareket kareleri için görüntü uzayı kırpma bilgisi |
| `video_frame_offset` | INT | Video oluşturmayı parçalar halinde devam ettirmek için güncellenmiş kare ofseti |