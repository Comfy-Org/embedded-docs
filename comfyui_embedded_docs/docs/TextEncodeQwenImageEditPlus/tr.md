# TextEncodeQwenImageEditPlus

TextEncodeQwenImageEditPlus düğümü, görüntü oluşturma veya düzenleme görevleri için koşullandırma verileri üretmek amacıyla metin istemlerini ve isteğe bağlı görüntüleri işler. Giriş görüntülerini analiz etmek ve metin talimatlarının bunları nasıl değiştirmesi gerektiğini anlamak için özel bir şablon kullanır; ardından bu bilgiyi sonraki oluşturma adımlarında kullanılmak üzere kodlar. Düğüm, en fazla üç giriş görüntüsünü işleyebilir ve bir VAE sağlandığında isteğe bağlı olarak referans latentleri üretebilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Tokenizasyon ve kodlama için kullanılan CLIP modeli | CLIP | Evet | - |
| `prompt` | İstenen görüntü değişikliğini tanımlayan metin talimatı (çok satırlı girişi ve dinamik istemleri destekler) | STRING | Evet | - |
| `vae` | Giriş görüntülerinden referans latentleri üretmek için isteğe bağlı VAE modeli | VAE | Hayır | - |
| `image1` | Analiz ve değişiklik için ilk isteğe bağlı giriş görüntüsü | IMAGE | Hayır | - |
| `image2` | Analiz ve değişiklik için ikinci isteğe bağlı giriş görüntüsü | IMAGE | Hayır | - |
| `image3` | Analiz ve değişiklik için üçüncü isteğe bağlı giriş görüntüsü | IMAGE | Hayır | - |

**Not:** Bir VAE sağlandığında, düğüm tüm giriş görüntülerinden referans latentler üretir. Düğüm aynı anda en fazla üç görüntüyü işleyebilir. Görüntüler, görsel-dil işleme için yaklaşık 384×384 piksel hedef alanına otomatik olarak ölçeklenir (en-boy oranı korunur); VAE kodlaması için ise yaklaşık 1024×1024 piksel hedef alanıyla 8'e bölünebilen boyutlara ölçeklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Görüntü oluşturma için metin token'larını ve isteğe bağlı referans latentleri içeren kodlanmış koşullandırma verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/tr.md)

---
**Source fingerprint (SHA-256):** `5eea53a84045924b44d445244e6149b341188d22573aaaced87bac8a139dac96`
