> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/tr.md)

Bir giriş görselini ve metin istemini temel alarak videolar oluşturur. Bu düğüm, statik bir görseli hareketli bir diziye dönüştürmek için belirtilen hareket ve kalite ayarlarını uygulayarak bir görsel alır ve animasyonlu bir video oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Videoya dönüştürülecek giriş görseli |
| `prompt` | STRING | Evet | - | Video oluşturma için istem |
| `quality` | COMBO | Evet | `res_540p`<br>`res_1080p` | Video kalite ayarı (varsayılan: res_540p) |
| `duration_seconds` | COMBO | Evet | `dur_2`<br>`dur_5`<br>`dur_10` | Oluşturulan videonun saniye cinsinden süresi |
| `motion_mode` | COMBO | Evet | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` | Video oluşturmaya uygulanan hareket stili |
| `seed` | INT | Evet | 0-2147483647 | Video oluşturma için tohum değeri (varsayılan: 0) |
| `negative_prompt` | STRING | Hayır | - | Görselde istenmeyen öğelerin isteğe bağlı metin açıklaması |
| `pixverse_template` | CUSTOM | Hayır | - | Oluşturma stilini etkilemek için PixVerse Şablon düğümü tarafından oluşturulan isteğe bağlı bir şablon |

**Not:** 1080p kalitesi kullanıldığında, hareket modu otomatik olarak normal olarak ayarlanır ve süre 5 saniye ile sınırlandırılır. 5 saniye dışındaki süreler için de hareket modu otomatik olarak normal olarak ayarlanır.

## Çıkışlar

| Çıkış Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Giriş görseli ve parametrelere dayalı olarak oluşturulan video |