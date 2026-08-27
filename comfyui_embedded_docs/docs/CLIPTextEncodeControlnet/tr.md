# CLIPMetinKodlamaControlnet

CLIPTextEncodeControlnet düğümü, bir CLIP modeli kullanarak bir metin istemini işler ve ortaya çıkan metin kodlamasını mevcut conditioning verileriyle birleştirir. Metinden türetilen embedding'leri, controlnet çapraz dikkat parametreleri olarak her conditioning girişine ekler ve controlnet uygulamaları için geliştirilmiş conditioning çıktısı üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Metin tokenizasyonu ve kodlama için kullanılan CLIP modeli | CLIP | Evet | - |
| `koşullandırma` | CLIP metin kodlamasıyla birleştirilecek mevcut conditioning verisi | CONDITIONING | Evet | - |
| `metin` | CLIP modeli tarafından işlenecek metin istemi. Çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet | - |

**Not:** Bu düğümün işlev görebilmesi için her üç girdi de (`clip`, `conditioning` ve `text`) gereklidir. `text` girdisi, esnek metin işleme için çok satırlı metin ve dinamik istemleri destekler. Bu düğüm, kaynak kodda deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | CLIP metin kodlamasından türetilmiş controlnet çapraz dikkat parametrelerinin (`cross_attn_controlnet` ve `pooled_output_controlnet`) eklendiği geliştirilmiş conditioning verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/tr.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
