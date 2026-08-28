# TextEncodeQwenImageEdit

TextEncodeQwenImageEdit düğümü, metin istemlerini ve isteğe bağlı görüntüleri, görüntü üretimi veya düzenlemesi için koşullandırma verisine dönüştürür. Girdiyi tokenize etmek için bir CLIP modeli kullanır ve isteğe bağlı olarak referans görüntülerini bir VAE ile kodlayarak referans latentleri oluşturabilir. Bir görüntü sağlandığında, tutarlı bir işleme ölçeği elde etmek için otomatik olarak yeniden boyutlandırılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Metin ve görüntü tokenizasyonu için kullanılan CLIP modeli | CLIP | Evet | - |
| `prompt` | Koşullandırma üretimi için metin istemi; çok satırlı girdi ve dinamik istemleri destekler | STRING | Evet | - |
| `vae` | Referans görüntülerini latentlere kodlamak için isteğe bağlı VAE modeli | VAE | Hayır | - |
| `görüntü` | Referans veya düzenleme amaçlı isteğe bağlı girdi görüntüsü | IMAGE | Hayır | - |

**Not:** Bir görüntü sağlandığında, toplam piksel sayısı 1.048.576'ya (1024 × 1024) yakın kalacak şekilde yeniden boyutlandırılır ve yalnızca RGB kanalları kullanılır. Yeniden boyutlandırılan görüntü, istemle birlikte CLIP tokenizere iletilir. Hem `image` hem de `vae` sağlandığında, düğüm görüntüyü ayrıca referans latentlerine kodlar ve bunları koşullandırma çıktısına ekler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Görüntü üretimi için metin tokenlerini ve isteğe bağlı referans latentlerini içeren koşullandırma verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEdit/tr.md)

---
**Source fingerprint (SHA-256):** `ec6980a63eab0d6c95be3abea00b2bf3018d30a1267f0b39a21be29a3e9228fe`
