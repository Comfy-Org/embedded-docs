> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEdit/tr.md)

TextEncodeQwenImageEdit düğümü, metin istemlerini ve isteğe bağlı görselleri işleyerek görsel üretimi veya düzenlemesi için koşullandırma verileri oluşturur. Girdiyi tokenize etmek için bir CLIP modeli kullanır ve isteğe bağlı olarak referans görsellerini kodlamak için bir VAE kullanarak referans latents oluşturabilir. Bir görsel sağlandığında, tutarlı işleme boyutlarını korumak için görseli otomatik olarak yeniden boyutlandırır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Evet | - | Metin ve görsel tokenizasyonu için kullanılan CLIP modeli |
| `prompt` | STRING | Evet | - | Koşullandırma üretimi için metin istemi, çok satırlı girdi ve dinamik istemleri destekler |
| `vae` | VAE | Hayır | - | Referans görsellerini latents'e kodlamak için isteğe bağlı VAE modeli |
| `image` | IMAGE | Hayır | - | Referans veya düzenleme amaçlı isteğe bağlı girdi görseli |

**Not:** Hem `image` hem de `vae` sağlandığında, düğüm görseli referans latents'e kodlar ve bunları koşullandırma çıktısına ekler. Görsel, yaklaşık 1024x1024 piksel tutarlı bir işleme ölçeğini korumak için otomatik olarak yeniden boyutlandırılır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Metin token'larını ve isteğe bağlı referans latents'leri içeren, görsel üretimi için koşullandırma verisi |