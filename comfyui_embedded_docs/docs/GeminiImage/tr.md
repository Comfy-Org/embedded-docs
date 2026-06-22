# GeminiImage

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

GeminiImage düğümü, Google'ın Gemini AI modellerinden metin ve görüntü yanıtları üretir. Metin istemleri, görüntüler ve dosyalar dahil olmak üzere çok modlu girdiler sağlayarak tutarlı metin ve görüntü çıktıları oluşturmanıza olanak tanır. Bu düğüm, en yeni Gemini modelleriyle tüm API iletişimini ve yanıt ayrıştırmasını yönetir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Girdi Türü | Varsayılan | Aralık |
| --- | --- | --- | --- | --- | --- |
| `prompt` | Üretim için metin istemi | STRING | zorunlu | "" | - |
| `model` | Yanıtları üretmek için kullanılacak Gemini modeli. | COMBO | zorunlu | gemini_2_5_flash_image_preview | `gemini_2_5_flash_image_preview`<br>`gemini_2_5_pro_exp_03_25`<br>`gemini_2_0_flash_exp_image_generation` |
| `seed` | Tohum belirli bir değere sabitlendiğinde model, tekrarlanan istekler için aynı yanıtı vermek üzere en iyi çabayı gösterir. Deterministik çıktı garanti edilmez. Ayrıca, modeli veya sıcaklık gibi parametre ayarlarını değiştirmek, aynı tohum değerini kullansanız bile yanıtta farklılıklara neden olabilir. Varsayılan olarak rastgele bir tohum değeri kullanılır. | INT | zorunlu | 42 | 0 ile 18446744073709551615 arası |
| `images` | Model için bağlam olarak kullanılacak isteğe bağlı görüntü(ler). Birden fazla görüntü eklemek için Toplu Görüntüler düğümünü kullanabilirsiniz. | IMAGE | isteğe bağlı | None | - |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini İçerik Girdi Dosyaları Oluştur düğümünden girdileri kabul eder. | GEMINI_INPUT_FILES | isteğe bağlı | None | - |

**Not:** Düğüm, sistem tarafından otomatik olarak işlenen ve kullanıcı girdisi gerektirmeyen gizli parametreler (`auth_token`, `comfy_api_key`, `unique_id`) içerir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Gemini modelinden üretilen görüntü yanıtı | IMAGE |
| `STRING` | Gemini modelinden üretilen metin yanıtı | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage/tr.md)

---
**Source fingerprint (SHA-256):** `bf55ec4f5a869a6bc5a15366f55f86ad25f9498c14056acc80951d3637bf08f2`
