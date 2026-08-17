# QwenImageTextToImageApi

Qwen Image 3 Text to Image, Qwen-Image 3.0 modellerini kullanarak bir metin isteminden (prompt) bir veya daha fazla görsel üretir. Bir model seçip bir prompt sağlarsınız ve düğüm, üretilen görselleri bir batch olarak döndürür.
## Girişler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `model` | Kullanılacak model (varsayılan: "qwen-image-3.0-pro"). Bu birleşik seçici ayrıca prompt, görsel genişliği, görsel yüksekliği ve isteğe bağlı negatif prompt sağlar. | DYNAMIC_COMBO | Evet | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `n` | Üretilecek görsel sayısı, bir batch olarak döndürülür (varsayılan: 1). | INT | Hayır | 1 to 6 |
| `seed` | Üretim için kullanılacak seed (varsayılan: 42). Her üretimden sonra otomatik güncellenecek şekilde ayarlanabilir. | INT | Hayır | 0 to 2147483647 |
| `prompt_extend` | Promptun yapay zeka yardımıyla geliştirilip geliştirilmeyeceği (varsayılan: true). Gelişmiş seçenek. | BOOLEAN | Hayır | true<br>false |
| `watermark` | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği (varsayılan: false). Gelişmiş seçenek. | BOOLEAN | Hayır | true<br>false |

### qwen-image-3.0-pro ve qwen-image-3.0 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `prompt` | Görseli tanımlayan prompt. İngilizce ve Çince destekler. En az 1 karakter içermelidir. | STRING | Evet | Free text |
| `negative_prompt` | Kaçınılması gerekenleri tanımlayan negatif prompt (varsayılan: ""). | STRING | Hayır | Free text |
| `width` | Toplam piksel alanı 512x512 ile 2560x2560 arasında olmalıdır; en-boy oranı 1:8 ile 8:1 arasında olmalıdır. (varsayılan: 1024) | INT | Hayır | 256 to 2560 (step 16) |
| `height` | Toplam piksel alanı 512x512 ile 2560x2560 arasında olmalıdır; en-boy oranı 1:8 ile 8:1 arasında olmalıdır. (varsayılan: 1024) | INT | Hayır | 256 to 2560 (step 16) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|---|---|---|
| `image` | The generated image or images, returned as a batch. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageTextToImageApi/tr.md)

---
**Source fingerprint (SHA-256):** `c58454d26360a78b795b28dd776fa8650ec0ec7b1e4a902e81b6561f292e0fa2`
