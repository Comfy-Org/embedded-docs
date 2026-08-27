# TextEncodeQwenImageEditPlus

TextEncodeQwenImageEditPlus düğümü, görüntü oluşturma veya düzenleme görevleri için koşullandırma verileri üretmek amacıyla metin istemlerini ve isteğe bağlı görüntüleri işler. Giriş görüntülerini analiz etmek ve metin talimatlarının bu görüntüleri nasıl değiştirmesi gerektiğini anlamak için özel bir şablon kullanır; ardından bu bilgiyi sonraki oluşturma adımlarında kullanılmak üzere kodlar. Düğüm, en fazla üç giriş görüntüsünü işleyebilir ve bir VAE sağlandığında isteğe bağlı olarak referans latentleri üretebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Tokenizasyon ve kodlama için kullanılan CLIP modeli | CLIP | Evet | - |
| `prompt` | İstenen görüntü değişikliğini açıklayan metin talimatı (çok satırlı girişi ve dinamik istemleri destekler) | STRING | Evet | - |
| `vae` | Giriş görüntülerinden referans latentleri üretmek için kullanılan isteğe bağlı VAE modeli | VAE | Hayır | - |
| `görüntü1` | Analiz ve değişiklik için ilk isteğe bağlı giriş görüntüsü | IMAGE | Hayır | - |
| `görüntü2` | Analiz ve değişiklik için ikinci isteğe bağlı giriş görüntüsü | IMAGE | Hayır | - |
| `görüntü3` | Analiz ve değişiklik için üçüncü isteğe bağlı giriş görüntüsü | IMAGE | Hayır | - |

**Not:** Bir VAE sağlandığında düğüm, sağlanan tüm giriş görüntülerinden referans latentleri üretir. Aynı anda en fazla üç görüntü işlenebilir. Görüntüler, görüntü-dil işleme için 384x384 piksellik bir hedef alana (en-boy oranı korunarak) ve VAE kodlaması için 8'e bölünebilen boyutlara (1024x1024 piksellik hedef alanla) ölçeklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Görüntü oluşturma için metin tokenlarını ve isteğe bağlı referans latentlerini içeren kodlanmış koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/tr.md)

---
**Source fingerprint (SHA-256):** `5eea53a84045924b44d445244e6149b341188d22573aaaced87bac8a139dac96`
