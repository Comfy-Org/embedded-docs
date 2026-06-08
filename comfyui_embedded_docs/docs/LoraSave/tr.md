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

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `dosyaadı_öneki` | Çıktı dosya adı için ön ek (varsayılan: "loras/ComfyUI_extracted_lora") | STRING | Evet | - |
| `rütbe` | LoRA için derece değeri; boyutu ve karmaşıklığı kontrol eder (varsayılan: 8) | INT | Evet | 1-4096 |
| `lora_türü` | Oluşturulacak LoRA türü (varsayılan: "standard") | COMBO | Evet | `"standard"`<br>`"locon"`<br>`"loha"`<br>`"lokr"`<br>`"dylora"` |
| `yanlılık_farkı` | LoRA hesaplamasına bias farklılıklarının dahil edilip edilmeyeceği (varsayılan: True) | BOOLEAN | Evet | - |
| `model_farkı` | LoRA'ya dönüştürülecek ModelSubtract çıktısı | MODEL | Hayır | - |
| `metin_kodlayıcı_farkı` | LoRA'ya dönüştürülecek CLIPSubtract çıktısı | CLIP | Hayır | - |

**Not:** Düğümün çalışması için `model_diff` veya `text_encoder_diff` girdilerinden en az birinin sağlanması gerekir. Her ikisi de atlanırsa, düğüm herhangi bir çıktı üretmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| - | Bu düğüm, çıktı dizinine bir LoRA dosyası kaydeder ancak iş akışı üzerinden herhangi bir veri döndürmez. | - |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraSave/tr.md)

---
**Source fingerprint (SHA-256):** `fdf020915ee233cf68250dcdcf87e7862d13ccc4fa73d8da8245727fdac46015`
