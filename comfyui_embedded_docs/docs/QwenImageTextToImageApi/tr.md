# QwenImageTextToImageApi

Qwen Image 3 Text to Image, Qwen-Image 3.0 modellerini kullanarak bir metin isteminden bir veya daha fazla görüntü oluşturur. Bir model seçip bir istem sağlarsınız ve düğüm oluşturulan görüntüleri bir grup olarak döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model (varsayılan: "qwen-image-3.0-pro"). Bu birleşik seçici ayrıca istemi, görüntü genişliğini, görüntü yüksekliğini ve isteğe bağlı negatif istemi sağlar. | MODEL | Evet | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `n` | Oluşturulacak görüntü sayısı, grup olarak döndürülür (varsayılan: 1). | INT | Hayır | 1 ila 6 |
| `seed` | Üretim için kullanılacak tohum (varsayılan: 42). Her üretimden sonra otomatik güncellenecek şekilde ayarlanabilir. | INT | Hayır | 0 ila 2147483647 |
| `prompt_extend` | İstemin yapay zeka yardımıyla geliştirilip geliştirilmeyeceği (varsayılan: true). Gelişmiş seçenek. | BOOLEAN | Hayır | true<br>false |
| `watermark` | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği (varsayılan: false). Gelişmiş seçenek. | BOOLEAN | Hayır | true<br>false |

Not: `model` girdisi aşağıdaki alt alanlara sahip birleşik bir seçicidir: `model` (model kimliği), `prompt` (en az 1 karakter içermesi gereken metin istemi), `width` ve `height` (düğüm tarafından doğrulanan görüntü boyutları) ve `negative_prompt` (isteğe bağlı negatif istem).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Oluşturulan görüntü veya görüntüler, grup olarak döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageTextToImageApi/tr.md)

---
**Source fingerprint (SHA-256):** `c58454d26360a78b795b28dd776fa8650ec0ec7b1e4a902e81b6561f292e0fa2`
