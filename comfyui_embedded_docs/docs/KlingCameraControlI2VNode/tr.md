> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlI2VNode/tr.md)

Kling Görüntüden Videoya Kamera Kontrol Düğümü, sabit görüntüleri profesyonel kamera hareketleriyle sinematik videolara dönüştürür. Bu özelleştirilmiş görüntüden videoya düğümü, orijinal görüntünüze odaklanmayı korurken sanal kamera eylemlerini (yakınlaştırma, döndürme, kaydırma, eğme ve birinci şahıs görünümü dahil) kontrol etmenize olanak tanır. Kamera kontrolü şu anda yalnızca pro modunda, kling-v1-5 modeli ve 5 saniyelik süre ile desteklenmektedir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `başlangıç_karesi` | IMAGE | Evet | - | Referans Görüntü - URL veya Base64 kodlanmış dize, 10MB'ı aşamaz, çözünürlük 300*300px'den az olamaz, en-boy oranı 1:2.5 ~ 2.5:1 arasında olmalıdır. Base64, data:image önekini içermemelidir. |
| `istem` | STRING | Evet | - | Olumlu metin istemi |
| `negatif_istem` | STRING | Evet | - | Olumsuz metin istemi |
| `cfg_ölçeği` | FLOAT | Hayır | 0.0-1.0 | Metin kılavuzluğunun gücünü kontrol eder (varsayılan: 0.75) |
| `en_boy_oranı` | COMBO | Hayır | Birden fazla seçenek mevcut | Video en-boy oranı seçimi (varsayılan: 16:9) |
| `kamera_kontrolü` | CAMERA_CONTROL | Evet | - | Kling Kamera Kontrolleri düğümü kullanılarak oluşturulabilir. Video oluşturma sırasındaki kamera hareketini ve devinimi kontrol eder. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video_kimliği` | VIDEO | Oluşturulan video çıktısı |
| `süre` | STRING | Oluşturulan video için benzersiz tanımlayıcı |
| `duration` | STRING | Oluşturulan videonun süresi |