> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/tr.md)

Kling Görüntüden Videoya Düğümü, başlangıç görüntüsünden metin istemlerini kullanarak video içeriği oluşturur. Bir referans görüntü alır ve sağlanan olumlu ve olumsuz metin açıklamalarına dayalı olarak, model seçimi, süre ve en-boy oranı için çeşitli yapılandırma seçenekleriyle bir video dizisi oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `başlangıç_karesi` | IMAGE | Evet | - | Videoyu oluşturmak için kullanılan referans görüntü. |
| `istem` | STRING | Evet | - | Olumlu metin istemi. |
| `negatif_istem` | STRING | Evet | - | Olumsuz metin istemi. |
| `model_adı` | COMBO | Evet | Birden fazla seçenek mevcut | Video oluşturma için model seçimi (varsayılan: "kling-v2-master"). |
| `cfg_ölçeği` | FLOAT | Evet | 0.0-1.0 | Yapılandırma ölçeği parametresi (varsayılan: 0.8). |
| `mod` | COMBO | Evet | Birden fazla seçenek mevcut | Video oluşturma modu seçimi (varsayılan: std). |
| `en_boy_oranı` | COMBO | Evet | Birden fazla seçenek mevcut | Oluşturulan video için en-boy oranı (varsayılan: field_16_9). |
| `süre` | COMBO | Evet | Birden fazla seçenek mevcut | Oluşturulan videonun süresi (varsayılan: field_5). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video_kimliği` | VIDEO | Oluşturulan video çıktısı. |
| `süre` | STRING | Oluşturulan video için benzersiz tanımlayıcı. |
| `süre` | STRING | Oluşturulan video için süre bilgisi. |