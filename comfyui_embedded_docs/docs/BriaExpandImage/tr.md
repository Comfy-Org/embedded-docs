# Bria Görüntü Genişletme

Bria Expand Image, Bria ile yeni içerik üreterek bir görüntüyü özgün sınırlarının ötesine genişletir. Hedef en-boy oranını, özel bir oranı seçmenize veya özgün görüntünün manuel yerleşimiyle bir tuval tanımlamanıza olanak tanır. Genişletme bir metin istemiyle yönlendirilebilir; istem boş bırakılırsa Bria otomatik olarak bir tane üretir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Genişletilecek girdi görüntüsü. | IMAGE | Evet | — |
| `expand_mode` | Genişletilmiş görüntünün hedef biçimi: ön ayarlı bir en-boy oranı, özel bir oran veya özgün görüntünün tuval üzerine manuel yerleştirilmesi. 1:2'den daha yüksek bir tuvale ulaşabilen tek mod Manuel'dir. `custom_ratio` seçildiğinde `ratio_width` ve `ratio_height` görünür. `manual` seçildiğinde tuval ve görüntü yerleştirme parametreleri görünür. | DYNAMIC_COMBO | Evet | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"custom_ratio"`<br>`"manual"` |
| `prompt` | Genişletilmiş sahnenin isteğe bağlı açıklaması; boş olduğunda Bria görüntüden bir tane üretir. Varsayılan: boş dize. | STRING | Evet | Herhangi bir dize |
| `negative_prompt` | Genişletme için isteğe bağlı negatif istem. Varsayılan: boş dize. | STRING | Evet | Herhangi bir dize |
| `seed` | Rastgele üretim süreci için tohum. Varsayılan: 42. | INT | Evet | 1–2147483647 |
| `moderation` | Moderasyon ayarları. `true` olarak ayarlandığında ek moderasyon seçenekleri gösterilir. | DYNAMIC_COMBO | Evet | `"false"`<br>`"true"` |

### Özel Oran Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ratio_width` | Hedef oranın genişlik tarafı: 21 ve 9, 21:9 verir. Varsayılan: 21. | INT | Evet | 1–100 |
| `ratio_height` | Hedef oranın yükseklik tarafı: 21 ve 9, 21:9 verir. Bria yalnızca 0.5 ile 3.0 arasındaki genişlik/yükseklik değerlerini kabul eder; bu nedenle 1:2'den daha yüksek olan her şey manuel modu gerektirir. Varsayılan: 9. | INT | Evet | 1–100 |

### Manuel Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `canvas_width` | Çıktı tuvalinin genişliği (piksel cinsinden). Varsayılan: 1000. | INT | Evet | 64–5000 |
| `canvas_height` | Çıktı tuvalinin yüksekliği (piksel cinsinden). Varsayılan: 1000. | INT | Evet | 64–5000 |
| `image_width` | Tuval içindeki özgün görüntünün genişliği. Varsayılan: 500. | INT | Evet | 1–5000 |
| `image_height` | Tuval içindeki özgün görüntünün yüksekliği. Varsayılan: 500. | INT | Evet | 1–5000 |
| `image_x` | Görüntünün sol üst köşesinin tuval içindeki X konumu; tuvalin dışına düşebilir ve görüntüyü kırpabilir. Varsayılan: 250. | INT | Evet | -5000–5000 |
| `image_y` | Görüntünün sol üst köşesinin tuval içindeki Y konumu; tuvalin dışına düşebilir ve görüntüyü kırpabilir. Varsayılan: 250. | INT | Evet | -5000–5000 |

### Moderasyon Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | Etkinleştirilirse istem içeriğini modere eder. Varsayılan: false. Yalnızca `moderation` `true` olduğunda kullanılabilir. | BOOLEAN | Evet | true/false |
| `visual_input_moderation` | Etkinleştirilirse görsel girdiyi modere eder. Varsayılan: false. Yalnızca `moderation` `true` olduğunda kullanılabilir. | BOOLEAN | Evet | true/false |
| `visual_output_moderation` | Etkinleştirilirse görsel çıktıyı modere eder. Varsayılan: false. Yalnızca `moderation` `true` olduğunda kullanılabilir. | BOOLEAN | Evet | true/false |

Ön ayarlı en-boy oranı seçeneklerinin (`1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`) ek girdisi yoktur.

`expand_mode` `custom_ratio` olduğunda, `ratio_width` ve `ratio_height` bir hedef en-boy oranı tanımlar. Bria yalnızca 0.5 ile 3.0 arasındaki genişlik-yükseklik oranlarını kabul eder. Oran bu aralığın dışındaysa bir hata oluşturulur ve bunun yerine `manual` modu kullanılmalıdır.

`expand_mode` `manual` olduğunda, özgün görüntü belirtilen boyut ve konumda bir tuvale yerleştirilir. Görüntü tuvalin dışına taşabilir; bu durumda dışta kalan kısım kırpılır.

`moderation` `true` olduğunda, üç moderasyon boolean değeri Bria'ya gönderilir. `moderation` `false` olduğunda yok sayılırlar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `image` | Bria tarafından üretilen genişletilmiş görüntü. | IMAGE |
| `prompt` | Genişletme için kullanılan istem; istem girdisi boş olduğunda Bria tarafından otomatik üretilir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaExpandImage/tr.md)

---
**Source fingerprint (SHA-256):** `d2c9431837f200ccbcb39037f7b26013494c4dea3d40d899db4e717ddbbea71c`
