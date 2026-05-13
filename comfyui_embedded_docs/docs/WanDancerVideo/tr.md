> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/tr.md)

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

WanDancerVideo düğümü, WanDancer modeli ile video oluşturma için koşullandırma verilerini ve boş bir latent tensör hazırlar. Oluşturulan videoyu kontrol etmek için pozitif ve negatif koşullandırmayı, başlangıç görüntüsü, maske, CLIP vision gömmeleri ve ses özellikleri gibi isteğe bağlı girdilerle birleştirir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pozitif` | CONDITIONING | Evet | | Video oluşturmayı yönlendiren pozitif koşullandırma. |
| `negatif` | CONDITIONING | Evet | | Video oluşturmayı yönlendiren negatif koşullandırma. |
| `vae` | VAE | Evet | | Başlangıç görüntüsünü latent uzaya kodlamak için kullanılan VAE. |
| `genişlik` | INT | Evet | 16 ila MAX_RESOLUTION (adım: 16) | Oluşturulan videonun piksel cinsinden genişliği (varsayılan: 480). |
| `yükseklik` | INT | Evet | 16 ila MAX_RESOLUTION (adım: 16) | Oluşturulan videonun piksel cinsinden yüksekliği (varsayılan: 832). |
| `uzunluk` | INT | Evet | 1 ila MAX_RESOLUTION (adım: 4) | Oluşturulan videodaki kare sayısı. WanDancer için 149 olarak kalmalıdır (varsayılan: 149). |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Hayır | | İlk kare için CLIP vision gömmeleri. |
| `clip_vision_output_ref` | CLIP_VISION_OUTPUT | Hayır | | Referans görüntüsü için CLIP vision gömmeleri. |
| `başlangıç görseli` | IMAGE | Hayır | | Kodlanacak başlangıç görüntüsü(leri). Belirtilen `uzunluk` değerine kadar herhangi bir sayıda kare olabilir. |
| `mask` | MASK | Hayır | | Başlangıç görüntüsü(leri) için görüntü koşullandırma maskesi. Beyaz alanlar korunur, siyah alanlar oluşturulur. Yerel oluşturmalar için kullanılır. |
| `audio_encoder_output` | AUDIO_ENCODER_OUTPUT | Hayır | | Ses koşullu oluşturma için ses özellikleri, fps ve enjekte ölçeği sağlayan bir ses kodlayıcının çıktısı. |

**Parametre Kısıtlamalarına İlişkin Not:**
- `start_image` ve `mask` girdileri isteğe bağlıdır ancak birlikte kullanılabilir. `start_image` sağlandığında, kodlanır ve latent ile birleştirilir. Ayrıca `mask` sağlanırsa, başlangıç görüntüsünün hangi bölümlerinin korunacağını (beyaz) ve hangilerinin yeniden oluşturulacağını (siyah) kontrol eder. `mask` sağlanmazsa, başlangıç görüntüsü alanının tamamı bir koşullandırma kılavuzu olarak kullanılır.
- `clip_vision_output` ve `clip_vision_output_ref` girdileri isteğe bağlıdır ve ilk kare ve bir referans görüntüsü için görsel bağlam sağlamak üzere birlikte kullanılabilir.
- `audio_encoder_output` girdisi isteğe bağlıdır ve ses koşullu oluşturma için ses özellikleri sağlar.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | Ek veriler (birleştirilmiş latent, CLIP vision, ses) eklenmiş pozitif koşullandırma. |
| `latent` | CONDITIONING | Ek veriler (birleştirilmiş latent, CLIP vision, ses) eklenmiş negatif koşullandırma. |
| `latent` | LATENT | Boyutları belirtilen video uzunluğu, yüksekliği ve genişliğiyle eşleşen boş bir latent tensör. |

---
**Source fingerprint (SHA-256):** `7ab1b4662eb8d780295ea3a3e3139c64d81e03a979a293a481f82deaf1fc2f7e`
