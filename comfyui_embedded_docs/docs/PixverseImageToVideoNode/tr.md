> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/tr.md)

Giriş görüntüsü ve metin istemine dayalı olarak videolar oluşturur. Bu düğüm, bir görüntü alır ve belirtilen hareket ve kalite ayarlarını uygulayarak statik görüntüyü hareketli bir diziye dönüştürerek animasyonlu bir video oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntü` | IMAGE | Evet | - | Videoya dönüştürülecek giriş görüntüsü |
| `istem` | STRING | Evet | - | Video oluşturma için istem |
| `kalite` | COMBO | Evet | `res_540p`<br>`res_1080p` | Video kalite ayarı (varsayılan: res_540p) |
| `süre_saniye` | COMBO | Evet | `dur_2`<br>`dur_5`<br>`dur_10` | Oluşturulan videonun saniye cinsinden süresi |
| `hareket_modu` | COMBO | Evet | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` | Video oluşturmaya uygulanan hareket stili |
| `tohum` | INT | Evet | 0-2147483647 | Video oluşturma için tohum değeri (varsayılan: 0) |
| `negatif_istem` | STRING | Hayır | - | Bir görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması |
| `pixverse_şablonu` | CUSTOM | Hayır | - | PixVerse Şablon düğümü tarafından oluşturulan, oluşturma stilini etkilemek için isteğe bağlı şablon |

**Not:** 1080p kalite kullanıldığında, hareket modu otomatik olarak normal olarak ayarlanır ve süre 5 saniye ile sınırlandırılır. 5 saniye dışındaki süreler için hareket modu da otomatik olarak normal olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `output` | VIDEO | Giriş görüntüsü ve parametrelere dayalı olarak oluşturulan video |

---
**Source fingerprint (SHA-256):** `7630c662a2506fb0c8be0cb9c6bfdfcf0fc06d2b6f16b8636664d587affededc`
