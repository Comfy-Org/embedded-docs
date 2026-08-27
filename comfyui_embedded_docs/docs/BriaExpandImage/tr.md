# BriaExpandImage

Bria Expand Image, Bria ile yeni içerik üreterek bir görüntüyü orijinal sınırlarının ötesine genişletir. Hedef en-boy oranı, özel bir oran seçmenize veya orijinal görüntüyü elle yerleştirerek bir tuval tanımlamanıza olanak tanır. Genişletme bir metin istemiyle yönlendirilebilir; istem boş bırakılırsa Bria otomatik olarak bir istem oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Genişletilecek girdi görüntüsü. | IMAGE | Evet | — |
| `expand_mode` | Genişletilmiş görüntünün hedef şekli: ön tanımlı bir en-boy oranı, özel bir oran veya orijinal görüntünün tuval üzerine elle yerleştirilmesi. Manuel mod, 1:2'den daha dik bir tuvale ulaşabilen tek moddur. `custom_ratio` seçildiğinde `ratio_width` ve `ratio_height` görüntülenir. `manual` seçildiğinde tuval ve görüntü yerleştirme parametreleri görüntülenir. | DYNAMIC_COMBO | Evet | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"custom_ratio"`<br>`"manual"` |
| `ratio_width` | Hedef oranın genişlik tarafı: 21 ve 9, 21:9 verir. Varsayılan: 21. | INT | Koşullu | 1–100 |
| `ratio_height` | Hedef oranın yükseklik tarafı: 21 ve 9, 21:9 verir. Bria yalnızca genişlik/yükseklik oranı 0,5 ile 3,0 arasında olan değerleri kabul eder; bu nedenle 1:2'den daha dik herhangi bir oran manuel mod gerektirir. Varsayılan: 9. | INT | Koşullu | 1–100 |
| `canvas_width` | Çıktı tuvalinin piksel cinsinden genişliği. Varsayılan: 1000. | INT | Koşullu | 64–5000 |
| `canvas_height` | Çıktı tuvalinin piksel cinsinden yüksekliği. Varsayılan: 1000. | INT | Koşullu | 64–5000 |
| `image_width` | Tuval içindeki orijinal görüntünün genişliği. Varsayılan: 500. | INT | Koşullu | 1–5000 |
| `image_height` | Tuval içindeki orijinal görüntünün yüksekliği. Varsayılan: 500. | INT | Koşullu | 1–5000 |
| `image_x` | Görüntünün sol üst köşesinin tuval içindeki X konumu; tuvalin dışına düşebilir ve görüntünün kırpılmasına neden olabilir. Varsayılan: 250. | INT | Koşullu | -5000–5000 |
| `image_y` | Görüntünün sol üst köşesinin tuval içindeki Y konumu; tuvalin dışına düşebilir ve görüntünün kırpılmasına neden olabilir. Varsayılan: 250. | INT | Koşullu | -5000–5000 |
| `prompt` | Genişletilen sahnenin isteğe bağlı açıklaması; boş olduğunda Bria, görüntüden otomatik olarak bir istem oluşturur. Varsayılan: boş dize. | STRING | Hayır | Herhangi bir dize |
| `negative_prompt` | Genişletme için isteğe bağlı bir negatif istem. Varsayılan: boş dize. | STRING | Hayır | Herhangi bir dize |
| `seed` | Rastgele üretim süreci için tohum değeri. Varsayılan: 42. | INT | Hayır | 1–2147483647 |
| `moderation` | Moderasyon ayarları. `true` olarak ayarlandığında ek moderasyon seçenekleri gösterilir. | DYNAMIC_COMBO | Hayır | `"false"`<br>`"true"` |
| `prompt_content_moderation` | Etkinleştirilirse, istem içeriğini denetler. Varsayılan: false. Yalnızca `moderation` `true` olduğunda kullanılabilir. | BOOLEAN | Koşullu | true/false |
| `visual_input_moderation` | Etkinleştirilirse, görsel girdiyi denetler. Varsayılan: false. Yalnızca `moderation` `true` olduğunda kullanılabilir. | BOOLEAN | Koşullu | true/false |
| `visual_output_moderation` | Etkinleştirilirse, görsel çıktıyı denetler. Varsayılan: false. Yalnızca `moderation` `true` olduğunda kullanılabilir. | BOOLEAN | Koşullu | true/false |

`expand_mode` `custom_ratio` olduğunda, `ratio_width` ve `ratio_height` hedef en-boy oranını tanımlar. Bria yalnızca genişlik-yükseklik oranı 0,5 ile 3,0 arasında olan değerleri kabul eder. Oran bu aralığın dışındaysa bir hata oluşur ve bunun yerine `manual` mod kullanılmalıdır.

`expand_mode` `manual` olduğunda, orijinal görüntü belirtilen boyut ve konumda tuvale yerleştirilir. Görüntü tuvalin dışına taşabilir; bu durumda dışta kalan kısım kırpılır.

`moderation` `true` olduğunda, üç moderasyon boolean değeri Bria'ya gönderilir. `moderation` `false` olduğunda bunlar yok sayılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Bria tarafından üretilen genişletilmiş görüntü. | IMAGE |
| `prompt` | Genişletme için kullanılan istem; `prompt` girdisi boş olduğunda Bria tarafından otomatik olarak oluşturulur. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaExpandImage/tr.md)

---
**Source fingerprint (SHA-256):** `d2c9431837f200ccbcb39037f7b26013494c4dea3d40d899db4e717ddbbea71c`
