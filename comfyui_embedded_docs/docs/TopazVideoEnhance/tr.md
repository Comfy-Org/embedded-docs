> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/tr.md)

Topaz Video Enhance düğümü, video kalitesini iyileştirmek için harici bir API kullanır. Video çözünürlüğünü yükseltebilir, interpolasyon yoluyla kare hızını artırabilir ve sıkıştırma uygulayabilir. Düğüm, bir giriş MP4 videosunu işler ve seçilen ayarlara dayalı olarak geliştirilmiş bir sürüm döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Evet | - | Geliştirilecek giriş video dosyası. |
| `upscaler_enabled` | BOOLEAN | Evet | - | Video yükseltme özelliğini etkinleştirir veya devre dışı bırakır (varsayılan: True). |
| `upscaler_model` | COMBO | Evet | `"Proteus v3"`<br>`"Artemis v13"`<br>`"Artemis v14"`<br>`"Artemis v15"`<br>`"Gaia v6"`<br>`"Theia v3"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight (Astra) Optimized"`<br>`"Starlight (Astra) Balanced"`<br>`"Starlight (Astra) Quality"`<br>`"Starlight (Astra) Speed"` | Videoyu yükseltmek için kullanılan AI modeli. |
| `upscaler_resolution` | COMBO | Evet | `"FullHD (1080p)"`<br>`"4K (2160p)"` | Yükseltilmiş video için hedef çözünürlük. |
| `upscaler_creativity` | COMBO | Hayır | `"low"`<br>`"middle"`<br>`"high"` | Yaratıcılık seviyesi (sadece Starlight (Astra) Creative için geçerlidir). (varsayılan: "low") |
| `interpolation_enabled` | BOOLEAN | Hayır | - | Kare interpolasyonu özelliğini etkinleştirir veya devre dışı bırakır (varsayılan: False). |
| `interpolation_model` | COMBO | Hayır | `"apo-8"` | Kare interpolasyonu için kullanılan model (varsayılan: "apo-8"). |
| `interpolation_slowmo` | INT | Hayır | 1 - 16 | Giriş videosuna uygulanan ağır çekim faktörü. Örneğin, 2 çıktıyı iki kat yavaşlatır ve süreyi ikiye katlar. (varsayılan: 1) |
| `interpolation_frame_rate` | INT | Hayır | 15 - 240 | Çıkış kare hızı. (varsayılan: 60) |
| `interpolation_duplicate` | BOOLEAN | Hayır | - | Girişi yinelenen kareler için analiz eder ve bunları kaldırır. (varsayılan: False) |
| `interpolation_duplicate_threshold` | FLOAT | Hayır | 0.001 - 0.1 | Yinelenen kareler için algılama hassasiyeti. (varsayılan: 0.01) |
| `dynamic_compression_level` | COMBO | Hayır | `"Low"`<br>`"Mid"`<br>`"High"` | CQP seviyesi. (varsayılan: "Low") |

**Not:** En az bir iyileştirme özelliği etkinleştirilmiş olmalıdır. Hem `upscaler_enabled` hem de `interpolation_enabled` `False` olarak ayarlandığında düğüm bir hata verecektir. Giriş videosu MP4 formatında olmalıdır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | Geliştirilmiş çıkış video dosyası. |
