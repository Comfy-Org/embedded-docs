# TextEncodeQwenImageEditPlus

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

TextEncodeQwenImageEditPlus düğümü, metin istemlerini ve isteğe bağlı görüntüleri işleyerek görüntü oluşturma veya düzenleme görevleri için koşullandırma verileri üretir. Giriş görüntülerini analiz etmek ve metin talimatlarının bu görüntüleri nasıl değiştirmesi gerektiğini anlamak için özel bir şablon kullanır, ardından bu bilgiyi sonraki oluşturma adımlarında kullanılmak üzere kodlar. Düğüm, en fazla üç giriş görüntüsünü işleyebilir ve bir VAE sağlandığında isteğe bağlı olarak referans latents (gizil değişkenler) üretebilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Belirteçleme (tokenization) ve kodlama için kullanılan CLIP modeli | CLIP | Evet | - |
| `prompt` | İstenen görüntü değişikliğini tanımlayan metin talimatı (çok satırlı giriş ve dinamik istemleri destekler) | STRING | Evet | - |
| `vae` | Giriş görüntülerinden referans latents (gizil değişkenler) oluşturmak için isteğe bağlı VAE modeli | VAE | Hayır | - |
| `görüntü1` | Analiz ve değişiklik için ilk isteğe bağlı giriş görüntüsü | IMAGE | Hayır | - |
| `görüntü2` | Analiz ve değişiklik için ikinci isteğe bağlı giriş görüntüsü | IMAGE | Hayır | - |
| `görüntü3` | Analiz ve değişiklik için üçüncü isteğe bağlı giriş görüntüsü | IMAGE | Hayır | - |

**Not:** Bir VAE sağlandığında, düğüm tüm giriş görüntülerinden referans latents (gizil değişkenler) üretir. Düğüm aynı anda en fazla üç görüntüyü işleyebilir. Görüntüler, görsel-dil işleme için otomatik olarak 384x384 piksel boyutuna ve VAE kodlaması için 8'e bölünebilen boyutlara (hedef alan 1024x1024 piksel olacak şekilde) yeniden boyutlandırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Görüntü oluşturma için metin belirteçleri ve isteğe bağlı referans latents (gizil değişkenler) içeren kodlanmış koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/tr.md)

---
**Source fingerprint (SHA-256):** `54889d9a3b70e41d623020f3fd5e3c798c72799492c67a9efd99f543c88bb968`
