> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/tr.md)

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

CLIPTextEncodeControlnet düğümü, bir CLIP modeli kullanarak metin girdisini işler ve mevcut koşullandırma verileriyle birleştirerek controlnet uygulamaları için gelişmiş koşullandırma çıktısı oluşturur. Girdi metnini tokenleştirir, CLIP modeli aracılığıyla kodlar ve elde edilen gömme vektörlerini, çapraz dikkat controlnet parametreleri olarak sağlanan koşullandırma verilerine ekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Evet | - | Metin tokenleştirme ve kodlama için kullanılan CLIP modeli |
| `koşullandırma` | CONDITIONING | Evet | - | Controlnet parametreleriyle geliştirilecek mevcut koşullandırma verileri |
| `metin` | STRING | Evet | - | CLIP modeli tarafından işlenecek metin girdisi. Çok satırlı metin ve dinamik istemleri destekler |

**Not:** Bu düğümün düzgün çalışması için üç girdinin de (`clip`, `conditioning` ve `text`) sağlanması gerekir. `text` girdisi, esnek metin işleme için dinamik istemleri ve çok satırlı metni destekler.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | CLIP metin kodlamasından türetilen ek controlnet çapraz dikkat parametreleri (`cross_attn_controlnet` ve `pooled_output_controlnet`) ile geliştirilmiş koşullandırma verileri |

---
**Source fingerprint (SHA-256):** `dd6f68d822cc38e27c826b634c938d62e07b075e18a0f46f80b462aecca0b70b`
