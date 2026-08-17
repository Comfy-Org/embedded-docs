# Grok Görüntü Düzenleme

Metin istemine dayalı olarak mevcut bir görüntüyü değiştirin. Bu düğüm, görüntülerinizi ve bir metin açıklamasını Grok API'ye gönderir; API, görüntüleri talimatlarınıza göre düzenler ve sonucu döndürür.
## Girişler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `model` | Kullanılacak Grok görüntü modeli. Aşağıda gösterilen alt parametreler, seçilen modele göre değişir. | DYNAMIC_COMBO | Evet | "grok-imagine-image-2.0"<br>"grok-imagine-image-quality"<br>"grok-imagine-image-pro"<br>"grok-imagine-image" |
| `prompt` | Görüntüyü oluşturmak için kullanılan metin istemi. (varsayılan: "") | STRING | Evet | N/A |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen seed; gerçek sonuçlar seed'den bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0 to 2147483647 |

### grok-imagine-image-2.0 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `resolution` | Düzenlenen görüntülerin çıktı çözünürlüğü. | COMBO | Evet | "1K"<br>"2K" |
| `number_of_images` | Oluşturulacak düzenlenmiş görüntü sayısı. (varsayılan: 1) | INT | Evet | 1 to 10 |
| `quality` | Oluşturulan görüntülerin kalite seviyesi. | COMBO | Evet | "medium"<br>"low" |
| `aspect_ratio` | Düzenlenen görüntünün en-boy oranı. (varsayılan: "auto") | COMBO | Evet | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-quality ve grok-imagine-image Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `resolution` | Düzenlenen görüntülerin çıktı çözünürlüğü. | COMBO | Evet | "1K"<br>"2K" |
| `number_of_images` | Oluşturulacak düzenlenmiş görüntü sayısı. (varsayılan: 1) | INT | Evet | 1 to 10 |
| `aspect_ratio` | Yalnızca birden fazla görüntü bağlandığında izin verilir. (varsayılan: "auto") | COMBO | Evet | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-pro Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `resolution` | Düzenlenen görüntülerin çıktı çözünürlüğü. | COMBO | Evet | "1K"<br>"2K" |
| `number_of_images` | Oluşturulacak düzenlenmiş görüntü sayısı. (varsayılan: 1) | INT | Evet | 1 to 10 |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `images` | Genişletilebilir yuva: düzenlemek için 1 veya daha fazla referans görüntü bağlayın. `image_1`, `image_2`, `image_3` gibi numaralı yuvalar eklenebilir. Maksimum görüntü sayısı seçilen modele bağlıdır (yukarıdaki model bölümlerine bakın). | IMAGE | Evet | 1 image for `grok-imagine-image-pro`<br>1 to 3 images for `grok-imagine-image-2.0`, `grok-imagine-image-quality`, and `grok-imagine-image` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|---|---|---|
| `IMAGE` | The edited image(s) returned by the Grok API. If a single image is generated, it is returned directly. If multiple images are generated, they are concatenated into a single batch tensor. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `7d75b1cb8405c5024567b1119bcbd5e4b318152605f74b62bdd5173dda75949f`
