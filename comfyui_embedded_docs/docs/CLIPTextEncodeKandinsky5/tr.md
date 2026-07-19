# CLIPTextEncodeKandinsky5

CLIPTextEncodeKandinsky5 düğümü, metin istemlerini Kandinsky 5 modeliyle kullanılmak üzere hazırlar. Sağlanan bir CLIP modeli kullanarak iki ayrı metin girişini tokenleştirir ve bunları tek bir koşullama çıktısında birleştirir. Bu çıktı, görüntü oluşturma sürecini yönlendirmek için kullanılır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Metin istemlerini tokenleştirmek ve kodlamak için kullanılan CLIP modeli. | CLIP | Evet |  |
| `clip_l` | Birincil metin istemi. Bu giriş, çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet |  |
| `qwen25_7b` | İkincil bir metin istemi. Bu giriş, çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet |  |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Her iki metin isteminden oluşturulan birleşik koşullama verisi. Görüntü oluşturma için bir Kandinsky 5 modeline beslenmeye hazırdır. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/tr.md)

---
**Source fingerprint (SHA-256):** `80227cf87d46bfa42b07976ab29996ae9583a4c461b2f2408db4b7016d3e1a0c`
