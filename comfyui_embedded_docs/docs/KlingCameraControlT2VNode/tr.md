> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlT2VNode/tr.md)

Kling Metinden Videoya Kamera Kontrol Düğümü, profesyonel sinematografiyi simüle eden kamera hareketleriyle metinleri sinematik videolara dönüştürür. Bu düğüm; yakınlaştırma, döndürme, yatay kaydırma, dikey kaydırma ve birinci şahıs görüşü dahil olmak üzere sanal kamera eylemlerini kontrol ederken orijinal metninize odaklanmayı sürdürmeyi destekler. Süre, mod ve model adı sabit kodlanmıştır çünkü kamera kontrolü yalnızca kling-v1-5 modeliyle 5 saniyelik sürede pro modunda desteklenir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | Olumlu metin istemi |
| `negatif_istem` | STRING | Evet | - | Olumsuz metin istemi |
| `cfg_ölçeği` | FLOAT | Hayır | 0.0-1.0 | Çıktının istemi ne kadar yakından takip edeceğini kontrol eder (varsayılan: 0.75) |
| `en_boy_oranı` | COMBO | Hayır | "16:9"<br>"9:16"<br>"1:1"<br>"21:9"<br>"3:4"<br>"4:3" | Oluşturulan video için en boy oranı (varsayılan: "16:9") |
| `kamera_kontrolü` | CAMERA_CONTROL | Hayır | - | Kling Kamera Kontrolleri düğümü kullanılarak oluşturulabilir. Video oluşturma sırasında kamera hareketini ve akışını kontrol eder. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video_kimliği` | VIDEO | Kamera kontrol efektleriyle oluşturulan video |
| `süre` | STRING | Oluşturulan video için benzersiz tanımlayıcı |
| `duration` | STRING | Oluşturulan videonun süresi |

---
**Source fingerprint (SHA-256):** `4ebdd6af31f9e5c0816c4bcba886179b3f7d2b5030ff4fa3ddad6df25c528af7`
