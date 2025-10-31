> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/tr.md)

TextEncodeQwenImageEditPlus düğümü, metin istemlerini ve isteğe bağlı görüntüleri işleyerek görüntü oluşturma veya düzenleme görevleri için koşullandırma verileri üretir. Girdi görüntülerini analiz etmek ve metin talimatlarının bu görüntüleri nasıl değiştirmesi gerektiğini anlamak için özel bir şablon kullanır, ardından bu bilgiyi sonraki oluşturma adımlarında kullanılmak üzere kodlar. Düğüm en fazla üç girdi görüntüsünü işleyebilir ve bir VAE sağlandığında isteğe bağlı olarak referans latents (gizli temsiller) üretebilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Evet | - | Tokenleştirme ve kodlama için kullanılan CLIP modeli |
| `prompt` | STRING | Evet | - | İstenen görüntü değişikliğini tanımlayan metin talimatı (çok satırlı girdi ve dinamik istemleri destekler) |
| `vae` | VAE | Hayır | - | Girdi görüntülerinden referans latents üretmek için isteğe bağlı VAE modeli |
| `image1` | IMAGE | Hayır | - | Analiz ve değişiklik için birinci isteğe bağlı girdi görüntüsü |
| `image2` | IMAGE | Hayır | - | Analiz ve değişiklik için ikinci isteğe bağlı girdi görüntüsü |
| `image3` | IMAGE | Hayır | - | Analiz ve değişiklik için üçüncü isteğe bağlı girdi görüntüsü |

**Not:** Bir VAE sağlandığında, düğüm tüm girdi görüntülerinden referans latents üretir. Düğüm aynı anda en fazla üç görüntüyü işleyebilir ve görüntüler işleme için uygun boyutlara otomatik olarak yeniden boyutlandırılır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Metin token'larını ve isteğe bağlı referans latents'leri içeren, görüntü oluşturma için kodlanmış koşullandırma verileri |