# Grok Görüntü Düzenleme

Bir metin istemine dayanarak bir veya daha fazla mevcut görüntüyü değiştirin. Düğüm, seçilen modeli kullanarak bağlı referans görüntüyü/görüntüleri ve istemi Grok görüntü düzenleme API'sine gönderir, ardından düzenlenmiş görüntüyü/görüntüleri döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak Grok görüntü modeli. Aşağıda gösterilen alt parametreler seçilen modele göre değişir. | DYNAMIC_COMBO | Evet | "grok-imagine-image-2.0"<br>"grok-imagine-image-quality"<br>"grok-imagine-image-pro"<br>"grok-imagine-image" |
| `prompt` | Görüntüyü oluşturmak için kullanılan metin istemi. (varsayılan: "") | STRING | Evet | N/A |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını belirleyen tohum; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0 ile 2147483647 |

### grok-imagine-image-2.0 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Düzenlenen görüntülerin çıktı çözünürlüğü. | COMBO | Evet | "1K"<br>"2K" |
| `number_of_images` | Oluşturulacak düzenlenmiş görüntü sayısı. (varsayılan: 1) | INT | Evet | 1 ile 10 |
| `quality` | Oluşturulan görüntülerin kalite düzeyi. | COMBO | Evet | "medium"<br>"low" |
| `aspect_ratio` | Düzenlenen görüntünün en-boy oranı. (varsayılan: "auto") | COMBO | Evet | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-quality ve grok-imagine-image Girdileri

grok-imagine-image-quality ve grok-imagine-image tarafından paylaşılır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Düzenlenen görüntülerin çıktı çözünürlüğü. | COMBO | Evet | "1K"<br>"2K" |
| `number_of_images` | Oluşturulacak düzenlenmiş görüntü sayısı. (varsayılan: 1) | INT | Evet | 1 ile 10 |
| `aspect_ratio` | Yalnızca birden fazla görüntü bağlandığında izin verilir. (varsayılan: "auto") | COMBO | Evet | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-pro Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Düzenlenen görüntülerin çıktı çözünürlüğü. | COMBO | Evet | "1K"<br>"2K" |
| `number_of_images` | Oluşturulacak düzenlenmiş görüntü sayısı. (varsayılan: 1) | INT | Evet | 1 ile 10 |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Genişletilebilir yuva: düzenlemek için 1 ile N arasında referans görüntü bağlayın. Yuvalar `image_1`, `image_2`, `image_3` şablon adlarını kullanır; maksimum yuva sayısı seçilen modele bağlıdır. | IMAGE | Evet | `grok-imagine-image-pro` için 1 görüntü<br>`grok-imagine-image-2.0`, `grok-imagine-image-quality` ve `grok-imagine-image` için 1 - 3 görüntü |

**Kısıtlamalarla ilgili not:**
- `prompt` en az 1 boşluk dışı karakter içermelidir.
- Düzenleme için en az bir referans görüntü gereklidir; hiçbir görüntü bağlı değilse düğüm bir hata verir.
- Maksimum girdi görüntüsü sayısı `grok-imagine-image-pro` için 1, `grok-imagine-image-2.0`, `grok-imagine-image-quality` ve `grok-imagine-image` için 3'tür. Modelin desteklediğinden daha fazla görüntü bağlamak bir hata verir.
- Görüntü sınırı, bağlı girdilerdeki her görüntüyü sayar; bu nedenle birkaç görüntü içeren bir toplu işlem, sınır açısından birkaç görüntü olarak sayılır.
- `grok-imagine-image-quality` ve `grok-imagine-image` için özel bir `aspect_ratio` ("auto" dışında herhangi bir değer) yalnızca birden fazla görüntü bağlandığında izin verilir. Tek bir görüntüyle `aspect_ratio` "auto" olmalıdır.
- `grok-imagine-image-2.0` için `aspect_ratio`, tek bir görüntüyle bile serbestçe ayarlanabilir.
- `quality` alt parametresi yalnızca `grok-imagine-image-2.0` ile kullanılabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Grok API tarafından döndürülen düzenlenmiş görüntü(ler). Tek bir görüntü oluşturulursa doğrudan döndürülür. Birden fazla görüntü oluşturulursa tek bir toplu tensöre birleştirilir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `7d75b1cb8405c5024567b1119bcbd5e4b318152605f74b62bdd5173dda75949f`
