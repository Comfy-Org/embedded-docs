# QwenImageEditApi

Bu düğüm, Qwen-Image 3.0 modellerini kullanarak, bir metin istemi rehberliğinde en fazla 3 referans görselini düzenler veya birleştirir. Metin istemini ve referans görsellerini siz sağlarsınız; düğüm, oluşturulan sonucu bir veya daha fazla görsel olarak döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. Bu seçim ayrıca metin istemini, en fazla 3 referans görseli girdisini ve isteğe bağlı bir negatif istemi içerir. | COMBO | Evet | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `size` | Çıktı çözünürlüğü. "match input" ilk referans görselin boyutunu yeniden kullanır, "auto" modelin aynı en-boy oranına sahip bir boyut seçmesini sağlar, "custom" açık bir genişlik ve yükseklik belirler. | COMBO | Evet | "match input"<br>"auto"<br>"custom" |
| `n` | Oluşturulacak görsel sayısı, bir toplu iş olarak döndürülür. (varsayılan: 1) | INT | Hayır | 1 ile 6 arası |
| `seed` | Üretim için kullanılacak tohum değeri. (varsayılan: 42) | INT | Hayır | 0 ile 2147483647 arası |
| `prompt_extend` | İstemin yapay zeka yardımıyla geliştirilip geliştirilmeyeceği. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |
| `watermark` | Sonuca yapay zeka tarafından oluşturulan bir filigran eklenip eklenmeyeceği. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |

### qwen-image-3.0-pro ve qwen-image-3.0 Girdileri

Her iki model de aynı alt parametreleri paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Düzenleme talimatları. İngilizce ve Çince ile girdi görsellerine @Image1 tarzı referansları destekler. (varsayılan: "") | STRING | Evet | - |
| `negative_prompt` | Kaçınılması gerekenleri tanımlayan negatif istem. (varsayılan: "") | STRING | Hayır | - |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Genişletilebilir yuva: 1 ila 3 referans görseli bağlayın (`image_1`, `image_2`, `image_3`). İstemde bunlara girdi sırasına göre numaralandırılmış şekilde @Image1, @Image2, @Image3 olarak başvurun; toplu bir girdi her görsel için bir kez sayılır. | IMAGE | Evet | 1 ile 3 arası |

### Özel Boyut Girdileri

`size` "custom" olarak ayarlandığında gösterilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `width` | Çıktı genişliği. Toplam piksel alanı 512x512 ile 2560x2560 arasında olmalıdır; bu alan içindeki herhangi bir en-boy oranı çalışır. (varsayılan: 1024) | INT | Evet (`size` "custom" olduğunda) | 256 ile 2560 arası, adım 16 |
| `height` | Çıktı yüksekliği. Toplam piksel alanı 512x512 ile 2560x2560 arasında olmalıdır; bu alan içindeki herhangi bir en-boy oranı çalışır. (varsayılan: 1024) | INT | Evet (`size` "custom" olduğunda) | 256 ile 2560 arası, adım 16 |

### Kısıtlamalar

- Metin istemi zorunludur ve en az bir karakter içermelidir.
- En fazla 3 referans görseli desteklenir; daha fazlası sağlanırsa bir hata oluşturulur (toplu bir girdi her görsel için bir kez sayılır).
- `size` "custom" olarak ayarlandığında, açık genişlik ve yükseklik değerleri sağlanmalı ve doğrulanmalıdır: toplam piksel alanı 262.144 (512x512) ile 6.553.600 (2560x2560) piksel arasında olmalı ve en-boy oranı 1:8 ile 8:1 arasında olmalıdır.
- `size` "match input" olarak ayarlandığında, ilk referans görselin boyutları kullanıldığı için en az bir referans görseli gereklidir; boyutlar desteklenen alana ve en-boy oranı aralığına sığacak şekilde ölçeklenir.
- `size` "auto" olarak ayarlandığında model, girdi en-boy oranını koruyarak çıktı boyutunu seçer.
- İstem referansları, girdi sırasına göre numaralandırılmış @Image1, @Image2, @Image3 kullanır; bağlı görsel sayısından daha yüksek bir dizine yapılan referans hata oluşturur. Etiketler yalnızca sözcük sınırlarında tanınır, bu nedenle user@image1.com gibi adresler değiştirilmeden bırakılır.
- Girdi referans görselleri, API'ye gönderilmeden önce en fazla 2048x2048 piksele küçültülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Oluşturulan görsel veya görseller toplu iş olarak döndürülür. En fazla `n` görsel döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `efa8d2b1a039a7b91789c0332b751a5f90ab8dad755ef0e25124d7d1c44d9abb`
