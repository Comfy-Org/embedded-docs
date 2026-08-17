# CLIPMetinKodlamaControlnet

CLIPTextEncodeControlnet düğümü, metin girdisini bir CLIP modeli kullanarak işler ve mevcut koşullandırma verileriyle birleştirerek controlnet uygulamaları için gelişmiş koşullandırma çıktısı oluşturur. Girdi metnini tokenleştirir, CLIP modeli aracılığıyla kodlar ve elde edilen yerleştirmeleri, sağlanan koşullandırma verilerine çapraz dikkat controlnet parametreleri olarak ekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Metin tokenleştirme ve kodlama için kullanılan CLIP modeli | CLIP | Evet | - |
| `conditioning` | Controlnet parametreleriyle geliştirilecek mevcut koşullandırma verileri | CONDITIONING | Evet | - |
| `text` | CLIP modeli tarafından işlenecek metin girdisi. Çok satırlı metin ve dinamik promptları destekler | STRING | Evet | - |

**Not:** Bu düğümün düzgün çalışması için üç girdinin de (`clip`, `conditioning` ve `text`) sağlanması gerekir. `text` girdisi, esnek metin işleme için dinamik promptları ve çok satırlı metni destekler. Bu düğüm deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | CLIP metin kodlamasından türetilen, eklenmiş controlnet çapraz dikkat parametrelerini (`cross_attn_controlnet` ve `pooled_output_controlnet`) içeren gelişmiş koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/tr.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
