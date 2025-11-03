> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHiDream/tr.md)

CLIPTextEncodeHiDream düğümü, birden fazla metin girişini farklı dil modelleri kullanarak işler ve bunları tek bir koşullandırma çıktısında birleştirir. Dört farklı kaynaktan (CLIP-L, CLIP-G, T5-XXL ve LLaMA) gelen metinleri tokenleştirir ve planlanmış bir kodlama yaklaşımı kullanarak bunları kodlar. Bu, birden fazla dil modelinden aynı anda yararlanarak daha karmaşık metin koşullandırmasına olanak tanır.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | Gerekli Girdi | - | - | Tokenleştirme ve kodlama için kullanılan CLIP modeli |
| `clip_l` | STRING | Çok Satırlı Metin | - | - | CLIP-L modeli işlemesi için metin girişi |
| `clip_g` | STRING | Çok Satırlı Metin | - | - | CLIP-G modeli işlemesi için metin girişi |
| `t5xxl` | STRING | Çok Satırlı Metin | - | - | T5-XXL modeli işlemesi için metin girişi |
| `llama` | STRING | Çok Satırlı Metin | - | - | LLaMA modeli işlemesi için metin girişi |

**Not:** Tüm metin girdileri dinamik prompt'ları ve çok satırlı metin girişini destekler. Düğüm, planlanmış kodlama süreci aracılığıyla her birinin nihai koşullandırma çıktısına katkıda bulunması nedeniyle, düzgün çalışması için dört metin parametresinin de sağlanmasını gerektirir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | İşlenen tüm metin girdilerinden birleştirilmiş koşullandırma çıktısı |