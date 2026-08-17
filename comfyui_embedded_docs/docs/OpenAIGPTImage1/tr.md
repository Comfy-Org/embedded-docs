# OpenAI GPT Görüntü 2

OpenAI'ın GPT Image uç noktası üzerinden eşzamanlı olarak görüntü üretir. Bu düğüm, metin istemlerinden yeni görüntüler oluşturabilir veya bir giriş görüntüsü ve isteğe bağlı maske sağlandığında mevcut görüntüleri düzenleyebilir. gpt-image-1, gpt-image-1.5 ve gpt-image-2 dahil olmak üzere birden fazla GPT Image modelini destekler. Bu düğüm kullanımdan kaldırılmıştır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | GPT Image için metin istemi (varsayılan: "") | STRING | Evet | - |
| `seed` | Üretim için rastgele tohum (varsayılan: 0) - arka uçta henüz uygulanmadı | INT | Hayır | 0 ila 2147483647 |
| `quality` | Görüntü kalitesi, maliyeti ve üretim süresini etkiler (varsayılan: "low") | COMBO | Hayır | "low"<br>"medium"<br>"high" |
| `background` | Görüntüyü arka planlı veya arka plansız döndürür (varsayılan: "auto") | COMBO | Hayır | "auto"<br>"opaque"<br>"transparent" |
| `size` | Görüntü boyutu. Özel genişlik ve yüksekliği kullanmak için "Custom" seçeneğini seçin (yalnızca GPT Image 2) (varsayılan: "auto") | COMBO | Hayır | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024"<br>"2048x2048"<br>"2048x1152"<br>"1152x2048"<br>"3840x2160"<br>"2160x3840"<br>"Custom" |
| `n` | Kaç adet görüntü oluşturulacağı (varsayılan: 1) | INT | Hayır | 1 ila 8 |
| `image` | Görüntü düzenleme için isteğe bağlı referans görüntü | IMAGE | Hayır | - |
| `mask` | İç boyama (inpainting) için isteğe bağlı maske (beyaz alanlar değiştirilecek) | MASK | Hayır | - |
| `model` | Kullanılacak GPT Image modeli (varsayılan: "gpt-image-2") | COMBO | Hayır | "gpt-image-1"<br>"gpt-image-1.5"<br>"gpt-image-2" |
| `custom_width` | Yalnızca `size` değeri "Custom" olduğunda kullanılır. 16'nın katı olmalıdır (yalnızca GPT Image 2) (varsayılan: 1024) | INT | Hayır | 1024 ila 3840 |
| `custom_height` | Yalnızca `size` değeri "Custom" olduğunda kullanılır. 16'nın katı olmalıdır (yalnızca GPT Image 2) (varsayılan: 1024) | INT | Hayır | 1024 ila 3840 |

**Parametre Kısıtlamaları:**

- `image` sağlandığında, düğüm görüntü düzenleme moduna geçer
- `mask` yalnızca `image` sağlandığında kullanılabilir
- `mask` kullanılırken yalnızca tek görüntüler desteklenir (parti boyutu 1 olmalıdır)
- `mask` ve `image` aynı boyutta olmalıdır
- Özel çözünürlük (`size` = "Custom") yalnızca gpt-image-2 modeli tarafından desteklenir
- Özel genişlik ve yükseklik 16'nın katı olmalıdır
- Özel çözünürlüğün en-boy oranı 3:1'i aşmamalıdır
- Özel çözünürlüğün toplam piksel sayısı 655.360 ile 8.294.400 arasında olmalıdır
- Transparan arka plan, gpt-image-2 modeli tarafından desteklenmez
- 1536x1024'ten büyük boyutlar (örn. 2048x2048, 3840x2160) yalnızca gpt-image-2 modeli tarafından desteklenir

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Üretilen veya düzenlenen görüntü(ler) | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/tr.md)

---
**Source fingerprint (SHA-256):** `bf588bffced6e66536b4cb54655ef6ebb9cf988d9739e3c379a8ebda1486e20a`
