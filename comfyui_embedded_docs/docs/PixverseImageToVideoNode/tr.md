# PixVerse Görüntüden Videoya

PixVerse kullanarak sabit bir görüntüden ve metin isteminden video üretir. Düğüm, giriş görüntüsünü yükler, seçilen kalite, süre ve hareket ayarlarını uygular ve üretim tamamlandığında ortaya çıkan videoyu döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Videoya dönüştürülecek giriş görüntüsü | IMAGE | Evet | - |
| `prompt` | Video üretimi için istem (varsayılan: boş dize) | STRING | Evet | - |
| `quality` | Video kalite ayarı (varsayılan: res_540p) | COMBO | Evet | `res_540p`<br>`res_1080p` |
| `duration_seconds` | Üretilen videonun saniye cinsinden süresi | COMBO | Evet | `dur_2`<br>`dur_5`<br>`dur_10` |
| `motion_mode` | Video üretimine uygulanan hareket stili | COMBO | Evet | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` |
| `seed` | Video üretimi için tohum (varsayılan: 0) | INT | Evet | 0-2147483647 |
| `negative_prompt` | Görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: boş dize) | STRING | Hayır | - |
| `pixverse_template` | Üretim stilini etkilemek için isteğe bağlı şablon; PixVerse Template düğümü tarafından oluşturulur | CUSTOM | Hayır | - |

**Not:** 1080p kalitesi kullanıldığında hareket modu otomatik olarak normal olarak ayarlanır ve süre 5 saniye ile sınırlandırılır. 5 saniye dışındaki sürelerde hareket modu da otomatik olarak normal olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Giriş görüntüsüne ve parametrelere göre üretilen video | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `93ea662a27159f55bf12e49ea230f0005813614ad07f5189d1fd61e7b937fd4b`
