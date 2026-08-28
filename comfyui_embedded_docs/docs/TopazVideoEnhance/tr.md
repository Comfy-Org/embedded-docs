# Topaz Video Enhance

Topaz Video Enhance düğümü, video kalitesini artırmak için harici bir API kullanarak güçlü ölçekleme ve kurtarma teknolojisiyle videolara yeni bir soluk getirir. Video çözünürlüğünü yükseltebilir, enterpolasyon yoluyla kare hızını artırabilir ve sıkıştırma uygulayabilir. Düğüm, girdi olarak bir MP4 videosunu işler ve seçilen ayarlara göre geliştirilmiş bir sürüm döndürür. Bu düğüm, kullanımdan kaldırılmış (eski) olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Geliştirilecek girdi video dosyası. | VIDEO | Evet | - |
| `upscaler_enabled` | Video ölçekleme özelliğini etkinleştirir veya devre dışı bırakır (varsayılan: True). | BOOLEAN | Evet | - |
| `upscaler_model` | Videoyu ölçeklemek için kullanılan yapay zeka modeli. | COMBO | Evet | `"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"` |
| `upscaler_resolution` | Ölçeklenen video için hedef çözünürlük. | COMBO | Evet | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_creativity` | Yaratıcılık düzeyi (yalnızca Starlight (Astra) Creative için geçerlidir). (varsayılan: "low") | COMBO | Hayır | `"low"`<br>`"middle"`<br>`"high"` |
| `interpolation_enabled` | Kare enterpolasyonu özelliğini etkinleştirir veya devre dışı bırakır (varsayılan: False). | BOOLEAN | Hayır | - |
| `interpolation_model` | Kare enterpolasyonu için kullanılan model (varsayılan: "apo-8"). | COMBO | Hayır | `"apo-8"` |
| `interpolation_slowmo` | Girdi videoya uygulanan ağır çekim faktörü. Örneğin, 2 çıktıyı iki kat yavaşlatır ve süresini iki katına çıkarır. (varsayılan: 1) | INT | Hayır | 1 ila 16 |
| `interpolation_frame_rate` | Çıktı kare hızı. (varsayılan: 60) | INT | Hayır | 15 ila 240 |
| `interpolation_duplicate` | Girdiyi yinelenen kareler için analiz eder ve bunları kaldırır. (varsayılan: False) | BOOLEAN | Hayır | - |
| `interpolation_duplicate_threshold` | Yinelenen kareler için algılama hassasiyeti. (varsayılan: 0.01) | FLOAT | Hayır | 0.001 ila 0.1 |
| `dynamic_compression_level` | CQP düzeyi. (varsayılan: "Low") | COMBO | Hayır | `"Low"`<br>`"Mid"`<br>`"High"` |

**Not:** En az bir iyileştirme özelliği etkinleştirilmelidir. Hem `upscaler_enabled` hem de `interpolation_enabled` False olarak ayarlanırsa düğüm bir hata verir. Girdi video MP4 biçiminde olmalıdır. `upscaler_creativity` ayarı yalnızca `upscaler_model` "Starlight (Astra) Creative" olarak ayarlandığında geçerlidir. Çok parçalı yükleme gerektiren çok büyük video dosyaları desteklenmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Geliştirilmiş çıktı video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/tr.md)

---
**Source fingerprint (SHA-256):** `b3b14a301b529256ddf04b7e3a9b99814ad5bfa149366b2a5c51c396dbffb190`
