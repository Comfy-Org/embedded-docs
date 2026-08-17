# TextEncodeQwenImageEdit

TextEncodeQwenImageEdit düğümü, metin istemlerini ve isteğe bağlı görüntüleri işleyerek görüntü oluşturma veya düzenleme için koşullandırma verileri üretir. Girişi tokenize etmek için bir CLIP modeli kullanır ve referans görüntülerini isteğe bağlı olarak bir VAE kullanarak referans latentlerine kodlayabilir. Bir görüntü sağlandığında, tutarlı işleme boyutlarını korumak için görüntüyü otomatik olarak yeniden boyutlandırır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Metin ve görüntü tokenizasyonu için kullanılan CLIP modeli | CLIP | Evet | - |
| `prompt` | Koşullandırma üretimi için metin istemi; çok satırlı girişi ve dinamik istemleri destekler | STRING | Evet | - |
| `vae` | Referans görüntülerini latentlere kodlamak için isteğe bağlı VAE modeli | VAE | Hayır | - |
| `image` | Referans veya düzenleme amaçlı isteğe bağlı giriş görüntüsü | IMAGE | Hayır | - |

**Not:** Hem `image` hem de `vae` sağlandığında, düğüm görüntüyü referans latentlerine kodlar ve bunları koşullandırma çıktısına ekler. Görüntü, yaklaşık 1024x1024 piksel tutarlı bir işleme ölçeği sağlamak için otomatik olarak yeniden boyutlandırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Görüntü oluşturma için metin tokenlerini ve isteğe bağlı referans latentlerini içeren koşullandırma verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEdit/tr.md)

---
**Source fingerprint (SHA-256):** `ec6980a63eab0d6c95be3abea00b2bf3018d30a1267f0b39a21be29a3e9228fe`
