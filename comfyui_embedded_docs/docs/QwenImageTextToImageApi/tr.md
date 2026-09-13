# Qwen Image 3 Metinden Görsele

Qwen Image 3 Text to Image, Qwen-Image 3.0 modellerini kullanarak bir metin isteminden bir veya daha fazla görüntü oluşturur. Bir model seçer ve bir istem sağlarsınız; düğüm, oluşturulan görüntüleri toplu olarak döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model (varsayılan: "qwen-image-3.0-pro"). Bu bileşik seçici ayrıca istemi, negatif istemi, görüntü genişliğini ve görüntü yüksekliğini sağlar. | DYNAMIC_COMBO | Evet | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `n` | Oluşturulacak görüntü sayısı, toplu olarak döndürülür (varsayılan: 1). | INT | Hayır | 1 - 6 |
| `seed` | Oluşturma için kullanılacak tohum (varsayılan: 42). Her oluşturmadan sonra otomatik olarak güncellenecek şekilde ayarlanabilir. | INT | Hayır | 0 - 2147483647 |
| `prompt_extend` | İstemin yapay zeka yardımıyla geliştirilip geliştirilmeyeceği (varsayılan: true). Gelişmiş seçenek. | BOOLEAN | Hayır | true<br>false |
| `watermark` | Sonuca yapay zeka tarafından oluşturulan filigran eklenip eklenmeyeceği (varsayılan: false). Gelişmiş seçenek. | BOOLEAN | Hayır | true<br>false |

### qwen-image-3.0-pro ve qwen-image-3.0 Girdileri

qwen-image-3.0-pro ve qwen-image-3.0 tarafından ortak kullanılır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Görüntüyü tanımlayan istem. İngilizce ve Çinceyi destekler. En az 1 karakter içermelidir. | STRING | Evet | Serbest metin |
| `negative_prompt` | Kaçınılması gerekenleri tanımlayan negatif istem (varsayılan: ""). | STRING | Hayır | Serbest metin |
| `width` | Toplam piksel alanı 512x512 ile 2560x2560 arasında olmalıdır; bu alan içindeki herhangi bir en-boy oranı geçerlidir. (varsayılan: 1024) | INT | Hayır | 256 - 2560 (adım 16) |
| `height` | Toplam piksel alanı 512x512 ile 2560x2560 arasında olmalıdır; bu alan içindeki herhangi bir en-boy oranı geçerlidir. (varsayılan: 1024) | INT | Hayır | 256 - 2560 (adım 16) |

Not: `model` girdisi, alt alanları `model` (model kimliği), `prompt` (gerekli, en az 1 karakter içermelidir), `negative_prompt` (isteğe bağlı), `width` ve `height` olan bir bileşik seçicidir. `width` ve `height` değerlerinin birleşik piksel alanı 262.144 piksel (512x512) ile 6.553.600 piksel (2560x2560) arasında olmalı ve en-boy oranı 1:8 ile 8:1 arasında kalmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Oluşturulan görüntü veya görüntüler, toplu olarak döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageTextToImageApi/tr.md)

---
**Source fingerprint (SHA-256):** `c58454d26360a78b795b28dd776fa8650ec0ec7b1e4a902e81b6561f292e0fa2`
