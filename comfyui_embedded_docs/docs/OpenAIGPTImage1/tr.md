OpenAI'nin GPT Image uç noktası aracılığıyla eşzamanlı olarak görseller oluşturur. Bu düğüm, metin istemlerinden yeni görseller oluşturabilir veya bir giriş görseli ve isteğe bağlı maske sağlandığında mevcut görselleri düzenleyebilir. gpt-image-1, gpt-image-1.5 ve gpt-image-2 dahil olmak üzere birden çok GPT Image modelini destekler.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | GPT Image için metin istemi (varsayılan: "") | STRING | Evet | - |
| `tohum` | Üretim için rastgele tohum (varsayılan: 0) - arka uçta henüz uygulanmadı | INT | Hayır | 0 ile 2147483647 arası |
| `kalite` | Görsel kalitesi, maliyeti ve üretim süresini etkiler (varsayılan: "low") | COMBO | Hayır | "low"<br>"medium"<br>"high" |
| `arka_plan` | Görseli arka planlı veya arka plansız döndürür (varsayılan: "auto") | COMBO | Hayır | "auto"<br>"opaque"<br>"transparent" |
| `boyut` | Görsel boyutu. Özel genişlik ve yüksekliği kullanmak için "Custom" seçeneğini seçin (yalnızca GPT Image 2) (varsayılan: "auto") | COMBO | Hayır | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024"<br>"2048x2048"<br>"2048x1152"<br>"1152x2048"<br>"3840x2160"<br>"2160x3840"<br>"Custom" |
| `n` | Oluşturulacak görsel sayısı (varsayılan: 1) | INT | Hayır | 1 ile 8 arası |
| `görüntü` | Görsel düzenleme için isteğe bağlı referans görseli | IMAGE | Hayır | - |
| `maske` | İç boyama (inpainting) için isteğe bağlı maske (beyaz alanlar değiştirilecektir) | MASK | Hayır | - |
| `model` | Kullanılacak GPT Image modeli (varsayılan: "gpt-image-2") | COMBO | Hayır | "gpt-image-1"<br>"gpt-image-1.5"<br>"gpt-image-2" |
| `özel_genişlik` | Yalnızca `boyut` "Custom" olduğunda kullanılır. 16'nın katı olmalıdır (yalnızca GPT Image 2) (varsayılan: 1024) | INT | Hayır | 1024 ile 3840 arası |
| `özel_yükseklik` | Yalnızca `boyut` "Custom" olduğunda kullanılır. 16'nın katı olmalıdır (yalnızca GPT Image 2) (varsayılan: 1024) | INT | Hayır | 1024 ile 3840 arası |

**Parametre Kısıtlamaları:**

- `image` sağlandığında, düğüm görsel düzenleme moduna geçer
- `mask` yalnızca `image` sağlandığında kullanılabilir
- `mask` kullanılırken yalnızca tek görseller desteklenir (toplu iş boyutu 1 olmalıdır)
- `mask` ve `image` aynı boyutta olmalıdır
- Özel çözünürlük (`size` = "Custom") yalnızca gpt-image-2 modeli tarafından desteklenir
- Özel genişlik ve yükseklik 16'nın katları olmalıdır
- Özel çözünürlük en boy oranı 3:1'i geçmemelidir
- Özel çözünürlük toplam piksel sayısı 655.360 ile 8.294.400 arasında olmalıdır
- Saydam arka plan gpt-image-2 modeli için desteklenmez
- 1536x1024'ten büyük boyutlar (örn. 2048x2048, 3840x2160) yalnızca gpt-image-2 modeli tarafından desteklenir

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Oluşturulan veya düzenlenen görsel(ler) | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/tr.md)

---
**Source fingerprint (SHA-256):** `44b258d6afcb388db3836427abdd5a7cb5c09a0328efceef7e114dd61a38eae1`
