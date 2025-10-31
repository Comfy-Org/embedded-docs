> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/tr.md)

Kling Start-End Frame to Video düğümü, sağladığınız başlangıç ve bitiş görüntüleri arasında geçiş yapan bir video dizisi oluşturur. İlk kareden son kareye kadar düzgün bir dönüşüm üretmek için aradaki tüm kareleri oluşturur. Bu düğüm, görüntüden videoya API'sini çağırır, ancak yalnızca `image_tail` istek alanıyla çalışan giriş seçeneklerini destekler.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `başlangıç_karesi` | IMAGE | Evet | - | Referans Görüntü - URL veya Base64 kodlanmış dize, 10MB'ı aşamaz, çözünürlük 300*300px'den az olmamalı, en-boy oranı 1:2.5 ~ 2.5:1 arasında olmalı. Base64, data:image önekini içermemelidir. |
| `bitiş_karesi` | IMAGE | Evet | - | Referans Görüntü - Bitiş karesi kontrolü. URL veya Base64 kodlanmış dize, 10MB'ı aşamaz, çözünürlük 300*300px'den az olmamalı. Base64, data:image önekini içermemelidir. |
| `istem` | STRING | Evet | - | Olumlu metin istemi |
| `negatif_istem` | STRING | Evet | - | Olumsuz metin istemi |
| `cfg_ölçeği` | FLOAT | Hayır | 0.0-1.0 | İstemin rehberlik gücünü kontrol eder (varsayılan: 0.5) |
| `en_boy_oranı` | COMBO | Hayır | "16:9"<br>"9:16"<br>"1:1"<br>"21:9"<br>"9:21"<br>"3:4"<br>"4:3" | Oluşturulan video için en-boy oranı (varsayılan: "16:9") |
| `mod` | COMBO | Hayır | Birden fazla seçenek mevcut | Video oluşturma için kullanılacak yapılandırma, şu biçimi izler: mod / süre / model_adı. (varsayılan: mevcut modlardan üçüncü seçenek) |

**Görüntü Kısıtlamaları:**

- Hem `start_frame` hem de `end_frame` sağlanmalıdır ve 10MB dosya boyutunu aşmamalıdır
- Minimum çözünürlük: her iki görüntü için 300×300 piksel
- `start_frame` en-boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır
- Base64 kodlanmış görüntüler "data:image" önekini içermemelidir

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video_kimliği` | VIDEO | Oluşturulan video dizisi |
| `süre` | STRING | Oluşturulan video için benzersiz tanımlayıcı |
| `duration` | STRING | Oluşturulan videonun süresi |