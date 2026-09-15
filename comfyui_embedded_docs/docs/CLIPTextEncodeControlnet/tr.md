# CLIPMetinKodlamaControlnet

CLIP Text Encode (Controlnet) düğümü, bir metin istemini bir CLIP modeliyle kodlar ve ortaya çıkan metin kodlamasını mevcut koşullandırma verilerine ekler. Metin gömme vektörlerini her koşullandırma girdisinin içinde controlnet çapraz dikkat parametreleri olarak saklar, böylece döndürülen koşullandırma bu ek controlnet bilgisini taşır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Metin tokenizasyonu ve kodlaması için kullanılan CLIP modeli | CLIP | Evet | - |
| `koşullandırma` | CLIP metin kodlamasıyla birleştirilecek mevcut koşullandırma verisi | CONDITIONING | Evet | - |
| `metin` | CLIP modeli tarafından işlenecek metin istemi. Çok satırlı metni ve dinamik istemleri destekler | STRING | Evet | - |

**Not:** Bu düğümün çalışması için üç girdinin tümü (`clip`, `conditioning` ve `text`) gereklidir. `text` girdisi, esnek metin işleme için çok satırlı metni ve dinamik istemleri destekler. Bu düğüm, kaynak kodda deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | CLIP metin kodlamasından türetilen ve eklenen controlnet çapraz dikkat parametrelerini (`cross_attn_controlnet` ve `pooled_output_controlnet`) içeren zenginleştirilmiş koşullandırma verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/tr.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
