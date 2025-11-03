> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/tr.md)

CLIPTextEncodeControlnet düğümü, metin girişini bir CLIP modeli kullanarak işler ve mevcut koşullandırma verileriyle birleştirerek controlnet uygulamaları için geliştirilmiş koşullandırma çıktısı oluşturur. Girdi metnini tokenize eder, CLIP modeli aracılığıyla kodlar ve ortaya çıkan gömme vektörlerini sağlanan koşullandırma verilerine cross-attention controlnet parametreleri olarak ekler.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | Gerekli | - | - | Metin tokenizasyonu ve kodlama için kullanılan CLIP modeli |
| `koşullandırma` | CONDITIONING | Gerekli | - | - | Controlnet parametreleriyle geliştirilecek mevcut koşullandırma verisi |
| `metin` | STRING | Çok Satırlı, Dinamik İstemler | - | - | CLIP modeli tarafından işlenecek metin girdisi |

**Not:** Bu düğümün düzgün çalışması için hem `clip` hem de `conditioning` girdileri gereklidir. `text` girdisi, esnek metin işleme için dinamik istemleri ve çok satırlı metni destekler.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Eklenen controlnet cross-attention parametreleriyle geliştirilmiş koşullandırma verisi |