> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlI2VNode/tr.md)

Kling Görüntüden Videoya Kamera Kontrol Düğümü, sabit görüntüleri profesyonel kamera hareketleriyle sinematik videolara dönüştürür. Bu özelleştirilmiş görüntüden videoya düğümü, orijinal görüntünüze odaklanmayı korurken sanal kamera eylemlerini (yakınlaştırma, döndürme, kaydırma, eğme ve birinci şahıs görünümü dahil) kontrol etmenize olanak tanır. Kamera kontrolü şu anda yalnızca pro modunda, kling-v1-5 modeli ve 5 saniyelik süre ile desteklenmektedir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | Evet | - | Referans Görüntü - URL veya Base64 kodlanmış dize, 10MB'ı aşamaz, çözünürlük 300*300px'den az olamaz, en-boy oranı 1:2.5 ~ 2.5:1 arasında olmalıdır. Base64, data:image önekini içermemelidir. |
| `prompt` | STRING | Evet | - | Olumlu metin istemi |
| `negative_prompt` | STRING | Evet | - | Olumsuz metin istemi |
| `cfg_scale` | FLOAT | Hayır | 0.0-1.0 | Metin kılavuzluğunun gücünü kontrol eder (varsayılan: 0.75) |
| `aspect_ratio` | COMBO | Hayır | Birden fazla seçenek mevcut | Video en-boy oranı seçimi (varsayılan: 16:9) |
| `camera_control` | CAMERA_CONTROL | Evet | - | Kling Kamera Kontrolleri düğümü kullanılarak oluşturulabilir. Video oluşturma sırasındaki kamera hareketini ve devinimi kontrol eder. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video çıktısı |
| `video_id` | STRING | Oluşturulan video için benzersiz tanımlayıcı |
| `duration` | STRING | Oluşturulan videonun süresi |