# TextEncodeQwenImageEditPlus

TextEncodeQwenImageEditPlus düğümü, görüntü oluşturma veya düzenleme görevleri için koşullandırma verisi üretmek amacıyla bir metin istemini ve en fazla üç isteğe bağlı görüntüyü işler. Önce modelden girdi görüntülerinin temel özelliklerini tanımlamasını, ardından kullanıcının metin talimatının bunları nasıl değiştirmesi gerektiğini açıklamasını isteyen özel bir şablon kullanır; böylece kodlanan sonuç hem görüntüleri hem de istenen değişikliği anlar. Bir VAE sağlandığında düğüm, girdi görüntülerinden referans latentleri de oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Tokenizasyon ve kodlama için kullanılan CLIP modeli | CLIP | Evet | - |
| `prompt` | İstenen görüntü değişikliğini açıklayan metin talimatı (çok satırlı girdiyi ve dinamik istemleri destekler) | STRING | Evet | - |
| `vae` | Girdi görüntülerinden referans latentleri oluşturmak için isteğe bağlı VAE modeli | VAE | Hayır | - |
| `image1` | Analiz ve değişiklik için birinci isteğe bağlı girdi görüntüsü | IMAGE | Hayır | - |
| `image2` | Analiz ve değişiklik için ikinci isteğe bağlı girdi görüntüsü | IMAGE | Hayır | - |
| `image3` | Analiz ve değişiklik için üçüncü isteğe bağlı girdi görüntüsü | IMAGE | Hayır | - |

**Not:** Bir VAE sağlandığında düğüm, sağlanan tüm girdi görüntülerinden referans latentleri üretir. Aynı anda en fazla üç görüntü işlenebilir. Görüntüler, görsel-dil işleme için 384x384 piksel hedef alanına (en-boy oranı korunarak) ve VAE kodlama için 8'e bölünebilen boyutlara (1024x1024 piksel hedef alanıyla) ölçeklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Görüntü oluşturma için metin token'ları ve isteğe bağlı referans latentlerini içeren kodlanmış koşullandırma verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/tr.md)

---
**Source fingerprint (SHA-256):** `5eea53a84045924b44d445244e6149b341188d22573aaaced87bac8a139dac96`
