# LumaRay32KeyframesToVideoNode

Bu düğüm, her biri zaman çizelgesinde belirli bir konuma sabitlenmiş bir dizi kılavuz görüntü arasında geçiş yapan bir video oluşturmak için Luma Ray 3.2'yi kullanır. Animasyonu tanımlamak için Luma Ray 3.2 Anahtar Kare düğümlerini kullanarak anahtar kare dizisini oluşturun ve en az 2 anahtar kareyi birbirine bağlayın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. | STRING | Evet | 1 ila 6000 karakter |
| `resolution` | Oluşturulan videonun çıktı çözünürlüğü (varsayılan: "720p"). | COMBO | Evet | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | Oluşturulan videonun süresi (varsayılan: "5s"). | COMBO | Evet | `"5s"`<br>`"10s"` |
| `seed` | Tekrarlanabilirliği kontrol etmek için rastgele sayı üretimindeki tohum değeri. | INT | Evet | 0 ila 4294967295 |
| `keyframes` | Luma Ray 3.2 Anahtar Kare düğümlerinden gelen anahtar kare dizisi (en az 2 tane). | LUMA_RAY32_KEYFRAME | Evet | 2 ila 64 anahtar kare |

**Not:** Anahtar kare dizisi en az 2, en fazla 64 anahtar kare içermelidir. Her anahtar karenin zaman çizelgesinde farklı bir konumu olmalıdır. Anahtar kare konumları, seçilen süreye göre (5s için 120 kare, 10s için 240 kare) çıktı kare indekslerine dönüştürülür. Saniye modundaki anahtar kare konumları, toplam video süresini aşmamalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video çıktısı. | VIDEO |
| `generation_id` | Oluşturma isteği için benzersiz tanımlayıcı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframesToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `28099e5990942860a20e23cfd5c71a36b23a6264b44097ca617f8bdd06e7857a`
