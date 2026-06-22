# PixVerse Görüntüden Videoya

Giriş görüntüsü ve metin istemine dayalı olarak videolar oluşturur. Bu düğüm, bir görüntü alır ve belirtilen hareket ve kalite ayarlarını uygulayarak statik görüntüyü hareketli bir diziye dönüştürerek animasyonlu bir video oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Videoya dönüştürülecek giriş görüntüsü | IMAGE | Evet | - |
| `istem` | Video oluşturma için istem | STRING | Evet | - |
| `kalite` | Video kalite ayarı (varsayılan: res_540p) | COMBO | Evet | `res_540p`<br>`res_1080p` |
| `süre_saniye` | Oluşturulan videonun saniye cinsinden süresi | COMBO | Evet | `dur_2`<br>`dur_5`<br>`dur_10` |
| `hareket_modu` | Video oluşturmaya uygulanan hareket stili | COMBO | Evet | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` |
| `tohum` | Video oluşturma için tohum değeri (varsayılan: 0) | INT | Evet | 0-2147483647 |
| `negatif_istem` | Bir görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması | STRING | Hayır | - |
| `pixverse_şablonu` | PixVerse Şablon düğümü tarafından oluşturulan, oluşturma stilini etkilemek için isteğe bağlı şablon | CUSTOM | Hayır | - |

**Not:** 1080p kalite kullanıldığında, hareket modu otomatik olarak normal olarak ayarlanır ve süre 5 saniye ile sınırlandırılır. 5 saniye dışındaki süreler için hareket modu da otomatik olarak normal olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Giriş görüntüsü ve parametrelere dayalı olarak oluşturulan video | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `7630c662a2506fb0c8be0cb9c6bfdfcf0fc06d2b6f16b8636664d587affededc`
