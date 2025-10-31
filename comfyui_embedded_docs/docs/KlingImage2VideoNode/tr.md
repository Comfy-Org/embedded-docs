> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/tr.md)

Kling Görüntüden Videoya Düğümü, başlangıç görüntüsünden metin istemlerini kullanarak video içeriği oluşturur. Bir referans görüntü alır ve sağlanan olumlu ve olumsuz metin açıklamalarına dayalı olarak, model seçimi, süre ve en-boy oranı için çeşitli yapılandırma seçenekleriyle bir video dizisi oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | Evet | - | Videoyu oluşturmak için kullanılan referans görüntü. |
| `prompt` | STRING | Evet | - | Olumlu metin istemi. |
| `negative_prompt` | STRING | Evet | - | Olumsuz metin istemi. |
| `model_name` | COMBO | Evet | Birden fazla seçenek mevcut | Video oluşturma için model seçimi (varsayılan: "kling-v2-master"). |
| `cfg_scale` | FLOAT | Evet | 0.0-1.0 | Yapılandırma ölçeği parametresi (varsayılan: 0.8). |
| `mode` | COMBO | Evet | Birden fazla seçenek mevcut | Video oluşturma modu seçimi (varsayılan: std). |
| `aspect_ratio` | COMBO | Evet | Birden fazla seçenek mevcut | Oluşturulan video için en-boy oranı (varsayılan: field_16_9). |
| `duration` | COMBO | Evet | Birden fazla seçenek mevcut | Oluşturulan videonun süresi (varsayılan: field_5). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video çıktısı. |
| `video_id` | STRING | Oluşturulan video için benzersiz tanımlayıcı. |
| `duration` | STRING | Oluşturulan video için süre bilgisi. |