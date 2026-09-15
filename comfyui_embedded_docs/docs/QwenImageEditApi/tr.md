# Qwen Image 3 Düzenle

Bu düğüm, Qwen-Image 3.0 modellerini kullanarak bir metin istemi rehberliğinde en fazla 3 referans görselini düzenler veya birleştirir. Bir model seçer, istemi ve referans görsellerini sağlarsınız ve düğüm bir veya daha fazla oluşturulmuş görsel döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. Bu seçim ayrıca metin istemini, en fazla 3 referans görsel girdisini ve isteğe bağlı bir negatif istemi içerir. | DYNAMIC_COMBO | Evet | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `size` | Çıktı çözünürlüğü. "match input" ilk referans görselin boyutunu yeniden kullanır, "auto" modelin aynı en-boy oranına sahip bir boyut seçmesini sağlar, "custom" açık bir genişlik ve yükseklik belirler. | DYNAMIC_COMBO | Evet | "match input"<br>"auto"<br>"custom" |
| `n` | Oluşturulacak görsel sayısı, bir toplu işlem olarak döndürülür. (varsayılan: 1) | INT | Hayır | 1 ile 6 |
| `seed` | Oluşturma için kullanılacak tohum. (varsayılan: 42) | INT | Hayır | 0 ile 2147483647 |
| `prompt_extend` | İstemin yapay zeka desteğiyle geliştirilip geliştirilmeyeceği. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |
| `watermark` | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |

### qwen-image-3.0-pro ve qwen-image-3.0 Girdileri

Her iki model de aynı alt parametreleri paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Düzenleme talimatları. İngilizce ve Çinceyi ve giriş görsellerine @Image1 tarzı referansları destekler. (varsayılan: "") | STRING | Evet | - |
| `negative_prompt` | Kaçınılması gerekenleri açıklayan negatif istem. (varsayılan: "") | STRING | Hayır | - |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Genişletilebilir yuva: 1 ila 3 referans görseli bağlayın (`image_1`, `image_2`, `image_3`). İstemde bunlara @Image1, @Image2, @Image3 olarak atıfta bulunun; giriş sırasına göre numaralandırılır; toplu bir girdi, her görsel için bir kez sayılır. | IMAGE | Evet | 1 ile 3 |

### Özel Boyut Girdileri

`size` "custom" olarak ayarlandığında gösterilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `width` | Çıktı genişliği. Toplam piksel alanı 512x512 ile 2560x2560 arasında olmalıdır; bu alan içindeki herhangi bir en-boy oranı çalışır. (varsayılan: 1024) | INT | Evet (`size` "custom" olduğunda) | 256 ile 2560, step 16 |
| `height` | Çıktı yüksekliği. Toplam piksel alanı 512x512 ile 2560x2560 arasında olmalıdır; bu alan içindeki herhangi bir en-boy oranı çalışır. (varsayılan: 1024) | INT | Evet (`size` "custom" olduğunda) | 256 ile 2560, step 16 |

### Kısıtlamalar

- Metin istemi gereklidir ve en az bir karakter içermelidir.
- En fazla 3 referans görseli desteklenir; daha fazlası sağlanırsa hata verilir (toplu bir girdi, her görsel için bir kez sayılır).
- `size` "custom" olarak ayarlandığında, açık genişlik ve yükseklik değerleri sağlanmalıdır ve doğrulanır: toplam piksel alanı 262.144 (512x512) ile 6.553.600 (2560x2560) piksel arasında olmalıdır ve en-boy oranı 1:8 ile 8:1 arasında olmalıdır.
- `size` "match input" olarak ayarlandığında, ilk referans görselin boyutları kullanıldığı için en az bir referans görseli gereklidir; boyutlar desteklenen alan ve en-boy oranı aralığına sığacak şekilde ölçeklenir.
- `size` "auto" olarak ayarlandığında, model giriş en-boy oranını koruyarak çıktı boyutunu (1,9-4,2 megapiksel) seçer.
- İstem referansları, giriş sırasına göre numaralandırılan @Image1, @Image2, @Image3 kullanır; bağlı görsel sayısından daha yüksek bir indekse yapılan referans hata verir. Etiketler yalnızca sözcük sınırlarında tanınır, bu nedenle user@image1.com gibi adresler değiştirilmeden bırakılır.
- Giriş referans görselleri API'ye gönderilmeden önce en fazla 2048x2048 piksele küçültülür. PNG kodlaması API boyut sınırını aşarsa, bunun yerine JPEG kodlaması kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Oluşturulan görsel veya görseller bir toplu işlem olarak döndürülür. En fazla `n` görsel döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `efa8d2b1a039a7b91789c0332b751a5f90ab8dad755ef0e25124d7d1c44d9abb`
