> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraSave/tr.md)

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

LoraSave düğümü, model farklılıklarından LoRA (Düşük Dereceli Uyarlama) dosyalarını çıkarır ve kaydeder. Difüzyon modeli farklılıklarını, metin kodlayıcı farklılıklarını veya her ikisini birden işleyerek, belirtilen derece ve tür ile LoRA formatına dönüştürebilir. Ortaya çıkan LoRA dosyası, daha sonra kullanılmak üzere çıktı dizinine kaydedilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `filename_prefix` | STRING | Evet | - | Çıktı dosya adı için ön ek (varsayılan: "loras/ComfyUI_extracted_lora") |
| `rank` | INT | Evet | 1-4096 | LoRA için derece değeri; boyutu ve karmaşıklığı kontrol eder (varsayılan: 8) |
| `lora_type` | COMBO | Evet | `"standard"`<br>`"locon"`<br>`"loha"`<br>`"lokr"`<br>`"dylora"` | Oluşturulacak LoRA türü (varsayılan: "standard") |
| `bias_diff` | BOOLEAN | Evet | - | LoRA hesaplamasına bias farklılıklarının dahil edilip edilmeyeceği (varsayılan: True) |
| `model_diff` | MODEL | Hayır | - | LoRA'ya dönüştürülecek ModelSubtract çıktısı |
| `text_encoder_diff` | CLIP | Hayır | - | LoRA'ya dönüştürülecek CLIPSubtract çıktısı |

**Not:** Düğümün çalışması için `model_diff` veya `text_encoder_diff` girdilerinden en az birinin sağlanması gerekir. Her ikisi de atlanırsa, düğüm herhangi bir çıktı üretmez.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| - | - | Bu düğüm, çıktı dizinine bir LoRA dosyası kaydeder ancak iş akışı üzerinden herhangi bir veri döndürmez. |

---
**Source fingerprint (SHA-256):** `fdf020915ee233cf68250dcdcf87e7862d13ccc4fa73d8da8245727fdac46015`
