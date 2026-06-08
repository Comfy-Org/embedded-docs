ComfyUI düğüm belgelerini İngilizceden Türkçeye çevirmede uzmanlaşmış teknik çeviri uzmanısınız.

## Çeviri Kuralları

1. **Çevrilmemesi gereken içerik:**
   - Ters tırnak içindeki parametre adları: `image`, `seed`, `model`
   - BÜYÜK harflerle veri türleri: IMAGE, STRING, INT, FLOAT, MODEL, CONDITIONING, vb.
   - Range sütunundaki değerler: sayılar, "auto", seçenek adları
   - Kod, dosya yolları

2. **Çevrilmesi gereken içerik:**
   - Bölüm başlıkları: ## Genel Bakış, ## Girdiler, ## Çıktılar
   - Tüm açıklayıcı metinler
   - Parametre açıklamaları

3. **Çeviri kalitesi:**
   - Standart Türkçe kullanın
   - Profesyonel ama anlaşılır bir üslup koruyun
   - Teknik doğruluğu sağlayın
   - Standart Türkçe teknik terminolojiyi kullanın

4. **Format:**
   - Tüm Markdown biçimlendirmesini koruyun
   - Tablo yapısını koruyun
   - Belgenin başına herhangi bir not veya bağlantı eklemeyin (otomatik olarak eklenecektir)

Lütfen aşağıdaki belgeyi Türkçeye çevirin (belgenin başlangıç notunu dahil etmeyin):

TextEncodeQwenImageEdit düğümü, görüntü oluşturma veya düzenleme için koşullama verileri üretmek amacıyla metin istemlerini ve isteğe bağlı görüntüleri işler. Girişi tokenleştirmek için bir CLIP modeli kullanır ve isteğe bağlı olarak referans görüntülerini bir VAE kullanarak referans gizil değişkenlerine (latent) kodlayabilir. Bir görüntü sağlandığında, tutarlı işleme boyutlarını korumak için görüntüyü otomatik olarak yeniden boyutlandırır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Metin ve görüntü tokenleştirme için kullanılan CLIP modeli | CLIP | Evet | - |
| `prompt` | Koşullama oluşturma için metin istemi, çok satırlı girişi ve dinamik istemleri destekler | STRING | Evet | - |
| `vae` | Referans görüntülerini gizil değişkenlere kodlamak için isteğe bağlı VAE modeli | VAE | Hayır | - |
| `görüntü` | Referans veya düzenleme amaçlı isteğe bağlı giriş görüntüsü | IMAGE | Hayır | - |

**Not:** Hem `image` hem de `vae` sağlandığında, düğüm görüntüyü referans gizil değişkenlerine kodlar ve bunları koşullama çıktısına ekler. Görüntü, yaklaşık 1024x1024 piksel tutarlı bir işleme ölçeğini korumak için otomatik olarak yeniden boyutlandırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Görüntü oluşturma için metin tokenlerini ve isteğe bağlı referans gizil değişkenlerini içeren koşullama verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEdit/tr.md)

---
**Source fingerprint (SHA-256):** `143af2c93aa56ace3594ecb257cac9dbaef2666665f3fb6dfd7a987cd2ea326f`
