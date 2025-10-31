> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlT2VNode/tr.md)

Kling Text to Video Camera Control Node, metni gerçek dünya sinematografisini taklit eden profesyonel kamera hareketlerine sahip sinematik videolara dönüştürür. Bu düğüm, orijinal metninize odaklanmayı korurken sanal kamera eylemlerini kontrol etmeyi destekler; bunlar yakınlaştırma, döndürme, kaydırma, eğme ve birinci şahıs görünümünü içerir. Süre, mod ve model adı sabit kodlanmıştır çünkü kamera kontrolü yalnızca pro modunda, kling-v1-5 modeli ve 5 saniyelik süre ile desteklenmektedir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | Olumlu metin istemi |
| `negatif_istem` | STRING | Evet | - | Olumsuz metin istemi |
| `cfg_ölçeği` | FLOAT | Hayır | 0.0-1.0 | Çıktının istemi ne kadar yakından takip ettiğini kontrol eder (varsayılan: 0.75) |
| `en_boy_oranı` | COMBO | Hayır | "16:9"<br>"9:16"<br>"1:1"<br>"21:9"<br>"3:4"<br>"4:3" | Oluşturulan video için en-boy oranı (varsayılan: "16:9") |
| `kamera_kontrolü` | CAMERA_CONTROL | Hayır | - | Kling Kamera Kontrolleri düğümü kullanılarak oluşturulabilir. Video oluşturma sırasındaki kamera hareketini ve devinimi kontrol eder. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video_kimliği` | VIDEO | Kamera kontrol efektleriyle oluşturulan video |
| `süre` | STRING | Oluşturulan video için benzersiz tanımlayıcı |
| `duration` | STRING | Oluşturulan videonun süresi |