# CLIPMetinKodlamaHiDream

CLIPTextEncodeHiDream düğümü, dört ayrı metin girdisini farklı dil modelleri (CLIP-L, CLIP-G, T5-XXL ve LLaMA) kullanarak işler ve bunları tek bir koşullama çıktısında birleştirir. Her metin girdisini karşılık gelen modeliyle tokenleştirir ve zamanlanmış kodlama yaklaşımı kullanarak birlikte kodlar. Bu sayede, birden fazla dil modelini aynı anda kullanarak daha karmaşık metin koşullaması sağlanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Tokenleştirme ve kodlama için kullanılan CLIP modeli | CLIP | Evet | - |
| `clip_l` | CLIP-L modeli işlemesi için metin girdisi. Çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet | - |
| `clip_g` | CLIP-G modeli işlemesi için metin girdisi. Çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet | - |
| `t5xxl` | T5-XXL modeli işlemesi için metin girdisi. Çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet | - |
| `llama` | LLaMA modeli işlemesi için metin girdisi. Çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet | - |

**Not:** Dört metin girdisinin tamamı (`clip_l`, `clip_g`, `t5xxl` ve `llama`) düzgün çalışma için gereklidir, çünkü her biri zamanlanmış kodlama süreci aracılığıyla nihai koşullama çıktısına katkıda bulunur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Zamanlanmış kodlama yöntemi kullanılarak kodlanmış, işlenen tüm metin girdilerinden elde edilen birleşik koşullama çıktısı | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHiDream/tr.md)

---
**Source fingerprint (SHA-256):** `51d117d82a9d833f095e874bf442d5cf8c46a12313fda6b98e628fa988797565`
