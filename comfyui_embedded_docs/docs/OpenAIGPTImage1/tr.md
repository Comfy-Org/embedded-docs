> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/tr.md)

OpenAI'nin GPT Image 1 uç noktası aracılığıyla görüntüleri eşzamanlı olarak oluşturur. Bu düğüm, metin istemlerinden yeni görüntüler oluşturabilir veya bir girdi görüntüsü ve isteğe bağlı bir maske sağlandığında mevcut görüntüleri düzenleyebilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | GPT Image 1 için metin istemi (varsayılan: "") |
| `tohum` | INT | Hayır | 0 ile 2147483647 arası | Üretim için rastgele tohum (varsayılan: 0) - arka uçta henüz uygulanmadı |
| `kalite` | COMBO | Hayır | "low"<br>"medium"<br>"high" | Görüntü kalitesi, maliyeti ve üretim süresini etkiler (varsayılan: "low") |
| `arka_plan` | COMBO | Hayır | "opaque"<br>"transparent" | Arka planlı veya arka plansız görüntü döndürür (varsayılan: "opaque") |
| `boyut` | COMBO | Hayır | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024" | Görüntü boyutu (varsayılan: "auto") |
| `n` | INT | Hayır | 1 ile 8 arası | Kaç adet görüntü oluşturulacağı (varsayılan: 1) |
| `görüntü` | IMAGE | Hayır | - | Görüntü düzenleme için isteğe bağlı referans görüntüsü (varsayılan: None) |
| `maske` | MASK | Hayır | - | İç boyama için isteğe bağlı maske (beyaz alanlar değiştirilecektir) (varsayılan: None) |

**Parametre Kısıtlamaları:**

- `image` sağlandığında, düğüm görüntü düzenleme moduna geçer
- `mask` yalnızca `image` sağlandığında kullanılabilir
- `mask` kullanılırken yalnızca tek görüntüler desteklenir (toplu iş boyutu 1 olmalıdır)
- `mask` ve `image` aynı boyutta olmalıdır

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Oluşturulan veya düzenlenen görüntü(ler) |