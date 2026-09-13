# Luma Ray 3.2 Anahtar Karelerden Videoya

Bu düğüm, Luma Ray 3.2 kullanarak zaman çizelgesinde belirli bir konuma sabitlenmiş bir dizi kılavuz görüntü arasında geçiş yapan bir video oluşturur. Ana kare dizisini Luma Ray 3.2 Keyframe düğümlerini kullanarak oluşturun ve animasyonu tanımlamak için en az 2 ana kare bağlayın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi (varsayılan: boş dize). | STRING | Evet | 1 ila 6000 karakter |
| `resolution` | Oluşturulan videonun çıktı çözünürlüğü (varsayılan: "720p"). | STRING | Evet | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | Oluşturulan videonun süresi (varsayılan: "5s"). | STRING | Evet | `"5s"`<br>`"10s"` |
| `seed` | Yeniden üretilebilirliği kontrol etmek için rastgele sayı üretiminde kullanılan tohum. | INT | Evet | 0 ila 4294967295 |
| `keyframes` | Luma Ray 3.2 Keyframe düğümlerinden ana kare dizisi (en az 2). | LUMA_RAY32_KEYFRAME | Evet | 2 ila 64 ana kare |

**Not:** Ana kare dizisi en az 2 ve en fazla 64 ana kare içermelidir. Her ana karenin zaman çizelgesinde farklı bir konumu olmalıdır. Ana kare konumları, seçilen süreye göre çıktı kare indekslerine dönüştürülür (5 sn için 120 kare, 10 sn için 240 kare). Saniye modundaki ana kare konumları toplam video süresini aşmamalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video çıktısı. | VIDEO |
| `generation_id` | Oluşturma isteği için benzersiz tanımlayıcı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframesToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `28099e5990942860a20e23cfd5c71a36b23a6264b44097ca617f8bdd06e7857a`
