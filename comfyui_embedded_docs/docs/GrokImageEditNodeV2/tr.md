# Grok Görüntü Düzenleme

Metin istemine dayalı olarak mevcut bir görüntüyü değiştirin. Bu düğüm, görüntülerinizi ve bir metin açıklamasını Grok API'ye gönderir; API, görüntüleri talimatlarınıza göre düzenler ve sonucu döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak Grok görüntü modeli. Aşağıda gösterilen alt parametreler, seçilen modele göre değişir. | MODEL | Evet | "grok-imagine-image-2.0"<br>"grok-imagine-image-quality"<br>"grok-imagine-image-pro"<br>"grok-imagine-image" |
| `istem` | Görüntüyü oluşturmak için kullanılan metin istemi. (varsayılan: "") | STRING | Evet | N/A |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen seed; gerçek sonuçlar seed'den bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0 ila 2147483647 |

### grok-imagine-image-2.0 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Düzenlenecek referans görüntü(ler). En fazla 3 görüntü. | IMAGE | Evet | 1 ila 3 görüntü |
| `resolution` | Düzenlenen görüntülerin çıktı çözünürlüğü. | STRING | Evet | "1K"<br>"2K" |
| `number_of_images` | Oluşturulacak düzenlenmiş görüntü sayısı. (varsayılan: 1) | INT | Evet | 1 ila 10 |
| `quality` | Oluşturulan görüntülerin kalite seviyesi. | STRING | Evet | "medium"<br>"low" |
| `aspect_ratio` | Düzenlenen görüntünün en-boy oranı. (varsayılan: "auto") | STRING | Evet | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-quality ve grok-imagine-image Girdileri

grok-imagine-image-quality ve grok-imagine-image tarafından paylaşılır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Düzenlenecek referans görüntü(ler). En fazla 3 görüntü. | IMAGE | Evet | 1 ila 3 görüntü |
| `resolution` | Düzenlenen görüntülerin çıktı çözünürlüğü. | STRING | Evet | "1K"<br>"2K" |
| `number_of_images` | Oluşturulacak düzenlenmiş görüntü sayısı. (varsayılan: 1) | INT | Evet | 1 ila 10 |
| `aspect_ratio` | Yalnızca birden fazla görüntü bağlandığında izin verilir. (varsayılan: "auto") | STRING | Evet | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-pro Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Düzenlenecek referans görüntü. | IMAGE | Evet | 1 görüntü |
| `resolution` | Düzenlenen görüntülerin çıktı çözünürlüğü. | STRING | Evet | "1K"<br>"2K" |
| `number_of_images` | Oluşturulacak düzenlenmiş görüntü sayısı. (varsayılan: 1) | INT | Evet | 1 ila 10 |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Genişletilebilir yuva: düzenlemek için 1 veya daha fazla referans görüntü bağlayın. `image_1`, `image_2`, `image_3` gibi numaralı yuvalar eklenebilir. Maksimum görüntü sayısı seçilen modele bağlıdır (yukarıdaki model bölümlerine bakın). | IMAGE | Evet | Modele bağlı olarak 1 ila 3 görüntü |

**Kısıtlamalarla ilgili not:**
- `prompt` en az 1 boşluk olmayan karakter içermelidir.
- Düzenleme için en az bir referans görüntü gereklidir; hiçbir görüntü bağlanmazsa düğüm bir hata verir.
- Maksimum giriş görüntüsü sayısı `grok-imagine-image-pro` için 1, `grok-imagine-image-2.0`, `grok-imagine-image-quality` ve `grok-imagine-image` için 3'tür. Modelin desteklediğinden daha fazla görüntü bağlanması hata verir.
- `grok-imagine-image-quality` ve `grok-imagine-image` için özel bir `aspect_ratio` ("auto" dışında herhangi bir değer) yalnızca birden fazla görüntü bağlandığında izin verilir. Tek görüntüde `aspect_ratio` "auto" olmalıdır.
- `grok-imagine-image-2.0` için `aspect_ratio`, tek görüntüyle bile serbestçe ayarlanabilir.
- `quality` alt parametresi yalnızca `grok-imagine-image-2.0` ile kullanılabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Grok API tarafından döndürülen düzenlenmiş görüntü(ler). Tek bir görüntü oluşturulursa doğrudan döndürülür. Birden fazla görüntü oluşturulursa tek bir grup tensöründe birleştirilir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `7d75b1cb8405c5024567b1119bcbd5e4b318152605f74b62bdd5173dda75949f`
