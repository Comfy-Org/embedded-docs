# CLIPTextEncodeKandinsky5

CLIPTextEncodeKandinsky5 düğümü, Kandinsky 5 modeliyle kullanılmak üzere metin istemlerini hazırlar. İki ayrı metin girişi alır, bunları sağlanan bir CLIP modeli kullanarak tokenleştirir ve bunları tek bir koşullandırma çıktısında birleştirir. Bu çıktı, görüntü oluşturma sürecini yönlendirmek için kullanılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Metin istemlerini tokenleştirmek ve kodlamak için kullanılan CLIP modeli. | CLIP | Evet |  |
| `clip_l` | Birincil metin istemi. Bu girdi çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet |  |
| `qwen25_7b` | İkincil bir metin istemi. Bu girdi çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet |  |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Her iki metin isteminden üretilen ve görüntü oluşturma için bir Kandinsky 5 modeline girdi olarak verilmeye hazır birleşik koşullandırma verisi. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/tr.md)

---
**Source fingerprint (SHA-256):** `d988c47ab9a5f01549a3ae01b365d39e9fa2464bb69ea018ec20151939dcfc56`
