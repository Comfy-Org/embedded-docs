# OpenAI GPT Görüntü 2

OpenAI'nin GPT Image uç noktası aracılığıyla eşzamanlı olarak görüntüler üretir. Bir metin isteminden yeni görüntüler oluşturabilir veya bir giriş görüntüsü ve isteğe bağlı maske sağlandığında mevcut görüntüleri düzenleyebilir. Düğüm `gpt-image-1`, `gpt-image-1.5` ve `gpt-image-2` modellerini destekler ve kullanımdan kaldırılmış olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `istem` | GPT Image için metin istemi (varsayılan: "") | STRING | Evet | - |
| `tohum` | Üretim için rastgele tohum; arka uçta henüz uygulanmadı (varsayılan: 0) | INT | Hayır | 0 - 2147483647 |
| `kalite` | Görüntü kalitesi; maliyeti ve üretim süresini etkiler (varsayılan: "low") | COMBO | Hayır | "low"<br>"medium"<br>"high" |
| `arka_plan` | Görüntüyü arka planlı veya arka plansız döndürür (varsayılan: "auto") | COMBO | Hayır | "auto"<br>"opaque"<br>"transparent" |
| `boyut` | Görüntü boyutu. Özel genişlik ve yüksekliği kullanmak için "Custom" seçin (yalnızca GPT Image 2) (varsayılan: "auto") | COMBO | Hayır | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024"<br>"2048x2048"<br>"2048x1152"<br>"1152x2048"<br>"3840x2160"<br>"2160x3840"<br>"Custom" |
| `n` | Kaç görüntü üretileceği (varsayılan: 1) | INT | Hayır | 1 - 8 |
| `görüntü` | Görüntü düzenleme için isteğe bağlı referans görüntüsü | IMAGE | Hayır | - |
| `maske` | Inpainting için isteğe bağlı maske (beyaz alanlar değiştirilecek) | MASK | Hayır | - |
| `model` | Kullanılacak GPT Image modeli (varsayılan: "gpt-image-2") | COMBO | Hayır | "gpt-image-1"<br>"gpt-image-1.5"<br>"gpt-image-2" |
| `özel_genişlik` | Yalnızca `size` "Custom" olduğunda kullanılır. 16'nın katı olmalıdır (yalnızca GPT Image 2) (varsayılan: 1024) | INT | Hayır | 1024 - 3840, adım 16 |
| `özel_yükseklik` | Yalnızca `size` "Custom" olduğunda kullanılır. 16'nın katı olmalıdır (yalnızca GPT Image 2) (varsayılan: 1024) | INT | Hayır | 1024 - 3840, adım 16 |

**Parametre Kısıtlamaları:**

- `image` sağlandığında, düğüm görüntü düzenleme uç noktasını kullanır.
- `mask` yalnızca `image` sağlandığında kullanılabilir.
- `mask` kullanılırken yalnızca tek görüntü desteklenir (toplu iş boyutu 1 olmalıdır).
- `mask` ve `image` aynı boyutta olmalıdır.
- Özel çözünürlük (`size` = "Custom") yalnızca `gpt-image-2` modeli tarafından desteklenir.
- Özel genişlik ve yükseklik 16'nın katı olmalıdır.
- Özel bir çözünürlüğün en uzun kenarı 3840 veya daha az olmalıdır.
- Özel çözünürlük en-boy oranı 3:1'i aşmamalıdır.
- Özel çözünürlüğün toplam piksel sayısı 655.360 ile 8.294.400 arasında olmalıdır.
- `gpt-image-1` ve `gpt-image-1.5` modelleri yalnızca `auto`, `1024x1024`, `1024x1536` ve `1536x1024` boyutlarını destekler. Diğer boyutlar yalnızca `gpt-image-2` modeli tarafından desteklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Üretilen veya düzenlenen görüntü(ler). Birden çok görüntü toplu iş olarak döndürülür; döndürülen görüntülerin boyutları farklıysa ilk görüntüyle eşleşecek şekilde yeniden boyutlandırılır. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/tr.md)

---
**Source fingerprint (SHA-256):** `f0f0db7fd2cdf8efd2155522b289aa8f3f939fa79a6e9060b0ffbb2dd20efa1e`
