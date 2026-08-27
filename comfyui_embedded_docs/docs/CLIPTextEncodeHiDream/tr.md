# CLIPMetinKodlamaHiDream

CLIPTextEncodeHiDream düğümü, dört ayrı metin girdisini farklı dil modelleri (CLIP-L, CLIP-G, T5-XXL ve LLaMA) kullanarak işler ve bunları tek bir koşullandırma çıktısında birleştirir. Her metin girdisini karşılık gelen modeliyle tokenize eder ve bunları zamanlanmış kodlama yaklaşımı kullanarak birlikte kodlar; böylece birden fazla dil modelini aynı anda kullanarak daha gelişmiş metin koşullandırması sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Tokenizasyon ve kodlama için kullanılan CLIP modeli | CLIP | Evet | - |
| `clip_l` | CLIP-L modeli işleme için metin girdisi. Çok satırlı metin ve dinamik promptları destekler. | STRING | Evet | - |
| `clip_g` | CLIP-G modeli işleme için metin girdisi. Çok satırlı metin ve dinamik promptları destekler. | STRING | Evet | - |
| `t5xxl` | T5-XXL modeli işleme için metin girdisi. Çok satırlı metin ve dinamik promptları destekler. | STRING | Evet | - |
| `llama` | LLaMA modeli işleme için metin girdisi. Çok satırlı metin ve dinamik promptları destekler. | STRING | Evet | - |

**Not:** Dört metin girdisinin tamamı (`clip_l`, `clip_g`, `t5xxl` ve `llama`) düzgün çalışma için gereklidir; çünkü her biri zamanlanmış kodlama süreci aracılığıyla nihai koşullandırma çıktısına katkıda bulunur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | İşlenen tüm metin girdilerinden elde edilen, zamanlanmış kodlama yöntemiyle kodlanmış birleşik koşullandırma çıktısı | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHiDream/tr.md)

---
**Source fingerprint (SHA-256):** `c5e269c17bd2dd7d7171c02598a87983a988d953dd7df285978fc25a9c896e46`
