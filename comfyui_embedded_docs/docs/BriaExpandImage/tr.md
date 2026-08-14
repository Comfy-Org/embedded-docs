# BriaExpandImage

Bria Expand Image, yeni içerik üreterek bir görseli orijinal sınırlarının ötesine genişletir. Hedef en-boy oranı, özel bir oran seçmenize veya orijinal görseli manuel yerleştirme ile bir tuval tanımlamanıza olanak tanır. Genişletme bir metin istemiyle yönlendirilebilir; istem boş bırakılırsa Bria otomatik olarak bir tane üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Genişletilecek girdi görseli. | IMAGE | Evet | — |
| `expand_mode` | Genişletilmiş görselin hedef şekli: ön tanımlı bir en-boy oranı, özel bir oran veya orijinal görselin bir tuval üzerine manuel yerleştirilmesi. Manuel, 1:2'den daha uzun bir tuvale ulaşabilen tek moddur. `custom_ratio` seçildiğinde `ratio_width` ve `ratio_height` görünür olur. `manual` seçildiğinde tuval ve görsel yerleştirme parametreleri görünür olur. | COMBO | Evet | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"custom_ratio"`<br>`"manual"` |
| `ratio_width` | Hedef oranın genişlik tarafı: 21 ve 9, 21:9 verir. Varsayılan: 21. | INT | Koşullu | 1–100 |
| `ratio_height` | Hedef oranın yükseklik tarafı: 21 ve 9, 21:9 verir. Bria yalnızca 0.5 ile 3.0 arasındaki genişlik/yükseklik oranlarını kabul eder, bu nedenle 1:2'den daha uzun her şey manuel mod gerektirir. Varsayılan: 9. | INT | Koşullu | 1–100 |
| `canvas_width` | Çıktı tuvalinin piksel cinsinden genişliği. Varsayılan: 1000. | INT | Koşullu | 64–5000 |
| `canvas_height` | Çıktı tuvalinin piksel cinsinden yüksekliği. Varsayılan: 1000. | INT | Koşullu | 64–5000 |
| `image_width` | Tuval içindeki orijinal görselin genişliği. Varsayılan: 500. | INT | Koşullu | 1–5000 |
| `image_height` | Tuval içindeki orijinal görselin yüksekliği. Varsayılan: 500. | INT | Koşullu | 1–5000 |
| `image_x` | Görselin sol üst köşesinin tuval içindeki X konumu; tuvalin dışına taşabilir ve görseli kırpabilir. Varsayılan: 250. | INT | Koşullu | -5000–5000 |
| `image_y` | Görselin sol üst köşesinin tuval içindeki Y konumu; tuvalin dışına taşabilir ve görseli kırpabilir. Varsayılan: 250. | INT | Koşullu | -5000–5000 |
| `prompt` | Genişletilmiş sahnenin isteğe bağlı açıklaması; boş olduğunda Bria, görselden bir tane üretir. Varsayılan: boş dize. | STRING | Hayır | Any string |
| `negative_prompt` | Genişletme için isteğe bağlı bir negatif istem. Varsayılan: boş dize. | STRING | Hayır | Any string |
| `seed` | Rastgele üretim süreci için tohum. Varsayılan: 42. | INT | Hayır | 1–2147483647 |
| `moderation` | Moderasyon ayarları. `true` olarak ayarlandığında ek moderasyon seçenekleri gösterilir. | COMBO | Hayır | `"false"`<br>`"true"` |
| `prompt_content_moderation` | Etkinleştirilirse, istem içeriğini denetler. Varsayılan: false. Yalnızca `moderation` `true` olduğunda kullanılabilir. | BOOLEAN | Koşullu | true/false |
| `visual_input_moderation` | Etkinleştirilirse, görsel girdiyi denetler. Varsayılan: false. Yalnızca `moderation` `true` olduğunda kullanılabilir. | BOOLEAN | Koşullu | true/false |
| `visual_output_moderation` | Etkinleştirilirse, görsel çıktıyı denetler. Varsayılan: false. Yalnızca `moderation` `true` olduğunda kullanılabilir. | BOOLEAN | Koşullu | true/false |

`expand_mode` `custom_ratio` olduğunda, `ratio_width` ve `ratio_height` hedef en-boy oranını tanımlar. Bria yalnızca 0.5 ile 3.0 arasındaki genişlik-yükseklik oranlarını kabul eder. Oran bu aralığın dışındaysa bir hata oluşturulur ve bunun yerine `manual` mod kullanılmalıdır.

`expand_mode` `manual` olduğunda, orijinal görsel belirtilen boyut ve konumda bir tuvale yerleştirilir. Görsel tuvalin dışına taşabilir; bu durumda dışta kalan kısım kırpılır.

`moderation` `true` olduğunda, üç moderasyon boolean değeri Bria'ya gönderilir. `moderation` `false` olduğunda, bunlar yok sayılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Bria tarafından üretilen genişletilmiş görsel. | IMAGE |
| `prompt` | Genişletme için kullanılan istem; istem girdisi boş olduğunda Bria tarafından otomatik üretilir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaExpandImage/tr.md)

---
**Source fingerprint (SHA-256):** `d2c9431837f200ccbcb39037f7b26013494c4dea3d40d899db4e717ddbbea71c`
