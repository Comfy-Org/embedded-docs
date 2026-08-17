# CLIPMetinKodlamaHiDream

CLIPTextEncodeHiDream düğümü, farklı dil modellerini (CLIP-L, CLIP-G, T5-XXL ve LLaMA) kullanarak dört ayrı metin girişini işler ve bunları tek bir koşullandırma çıktısında birleştirir. Her metin girişini ilgili modeliyle tokenize eder ve zamanlanmış kodlama yaklaşımını kullanarak birlikte kodlar. Bu sayede birden fazla dil modelini aynı anda kullanarak daha gelişmiş metin koşullandırması sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Tokenizasyon ve kodlama için kullanılan CLIP modeli | CLIP | Evet | - |
| `clip_l` | CLIP-L model işleme için metin girişi. Çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet | - |
| `clip_g` | CLIP-G model işleme için metin girişi. Çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet | - |
| `t5xxl` | T5-XXL model işleme için metin girişi. Çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet | - |
| `llama` | LLaMA model işleme için metin girişi. Çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet | - |

**Not:** Dört metin girişinin tamamı (`clip_l`, `clip_g`, `t5xxl` ve `llama`) doğru çalışma için gereklidir; çünkü her biri zamanlanmış kodlama süreci aracılığıyla nihai koşullandırma çıktısına katkıda bulunur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Zamanlanmış kodlama yöntemiyle kodlanmış, işlenen tüm metin girişlerinden elde edilen birleşik koşullandırma çıktısı | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHiDream/tr.md)

---
**Source fingerprint (SHA-256):** `c5e269c17bd2dd7d7171c02598a87983a988d953dd7df285978fc25a9c896e46`
