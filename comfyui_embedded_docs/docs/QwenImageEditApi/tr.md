# QwenImageEditApi

Bu düğüm, Qwen-Image 3.0 modellerini kullanarak, bir metin istemi rehberliğinde en fazla 3 referans görselini düzenler veya birleştirir. Metin istemini ve referans görsellerini siz sağlarsınız; düğüm, oluşturulan sonucu bir veya daha fazla görsel olarak döndürür.
## Girişler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `model` | Kullanılacak model. Bu seçim ayrıca metin istemini, en fazla 3 referans görseli girdisini ve isteğe bağlı bir negatif istemi içerir. | DYNAMIC_COMBO | Evet | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `size` | Çıktı çözünürlüğü. "match input" ilk referans görselin boyutunu yeniden kullanır, "auto" modelin aynı en-boy oranına sahip bir boyut seçmesini sağlar, "custom" açık bir genişlik ve yükseklik belirler. | DYNAMIC_COMBO | Evet | "match input"<br>"auto"<br>"custom" |
| `n` | Oluşturulacak görsel sayısı, bir toplu iş olarak döndürülür. (varsayılan: 1) | INT | Hayır | 1 to 6 |
| `seed` | Üretim için kullanılacak tohum değeri. (varsayılan: 42) | INT | Hayır | 0 to 2147483647 |
| `prompt_extend` | İstemin yapay zeka yardımıyla geliştirilip geliştirilmeyeceği. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |
| `watermark` | Sonuca yapay zeka tarafından oluşturulan bir filigran eklenip eklenmeyeceği. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |

### qwen-image-3.0-pro ve qwen-image-3.0 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `prompt` | Düzenleme talimatları. İngilizce ve Çince ile girdi görsellerine @Image1 tarzı referansları destekler. (varsayılan: "") | STRING | Evet | - |
| `negative_prompt` | Kaçınılması gerekenleri tanımlayan negatif istem. (varsayılan: "") | STRING | Hayır | - |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `images` | Genişletilebilir yuva: 1 ila 3 referans görseli bağlayın (`image_1`, `image_2`, `image_3`). İstemde bunlara girdi sırasına göre numaralandırılmış şekilde @Image1, @Image2, @Image3 olarak başvurun; toplu bir girdi her görsel için bir kez sayılır. | IMAGE | Evet | 1 to 3 |

### Özel Boyut Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `width` | Çıktı genişliği. Toplam piksel alanı 512x512 ile 2560x2560 arasında olmalıdır; en-boy oranı 1:8 ile 8:1 arasında olmalıdır. (varsayılan: 1024) | INT | Hayır | 256 to 2560, step 16 |
| `height` | Çıktı yüksekliği. Toplam piksel alanı 512x512 ile 2560x2560 arasında olmalıdır; en-boy oranı 1:8 ile 8:1 arasında olmalıdır. (varsayılan: 1024) | INT | Hayır | 256 to 2560, step 16 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|---|---|---|
| `IMAGE` | The generated image or images returned as a batch. Up to `n` images are returned. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `efa8d2b1a039a7b91789c0332b751a5f90ab8dad755ef0e25124d7d1c44d9abb`
