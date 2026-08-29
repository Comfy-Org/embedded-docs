# PixVerse Görüntüden Videoya

Giriş görüntüsüne ve metin istemine dayalı videolar üretir. Bu düğüm, bir görüntüyü alır; belirtilen hareket ve kalite ayarlarını uygulayarak statik görüntüyü hareketli bir sekansa dönüştürür ve böylece canlı bir video oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Videoya dönüştürülecek giriş görüntüsü | IMAGE | Evet | - |
| `istem` | Video üretimi için istem | STRING | Evet | - |
| `kalite` | Video kalitesi ayarı (varsayılan: res_540p) | COMBO | Evet | `res_540p`<br>`res_1080p` |
| `süre_saniye` | Üretilen videonun saniye cinsinden süresi | COMBO | Evet | `dur_2`<br>`dur_5`<br>`dur_10` |
| `hareket_modu` | Video üretimine uygulanan hareket stili | COMBO | Evet | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` |
| `tohum` | Video üretimi için tohum değeri (varsayılan: 0) | INT | Evet | 0-2147483647 |
| `negatif_istem` | Görüntüde istenmeyen öğeleri belirten isteğe bağlı metin açıklaması | STRING | Hayır | - |
| `pixverse_şablonu` | PixVerse Şablon düğümü tarafından oluşturulan, üretimin stilini etkilemek için kullanılan isteğe bağlı bir şablon | CUSTOM | Hayır | - |

**Not:** 1080p kalitesi kullanıldığında, hareket modu otomatik olarak normal olarak ayarlanır ve süre 5 saniye ile sınırlandırılır. 5 saniye dışındaki sürelerde de hareket modu otomatik olarak normal olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Giriş görüntüsüne ve parametrelere dayalı olarak üretilen video | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `93ea662a27159f55bf12e49ea230f0005813614ad07f5189d1fd61e7b937fd4b`
