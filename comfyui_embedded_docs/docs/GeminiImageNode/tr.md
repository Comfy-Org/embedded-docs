# Google Gemini Görsel

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

GeminiImage düğümü, Google'ın Gemini AI modellerinden metin ve görüntü yanıtları üretir. Metin istemleri, görüntüler ve dosyalar dahil olmak üzere çok modlu girdiler sağlayarak tutarlı metin ve görüntü çıktıları oluşturmanıza olanak tanır. Bu düğüm, en yeni Gemini modelleriyle tüm API iletişimini ve yanıt ayrıştırmayı yönetir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Girdi Türü | Varsayılan | Aralık |
| --- | --- | --- | --- | --- | --- |
| `istek` | Üretim için metin istemi | STRING | zorunlu | "" | - |
| `model` | Yanıtları üretmek için kullanılacak Gemini modeli | COMBO | zorunlu | gemini_2_5_flash_image_preview | Kullanılabilir Gemini modelleri<br>Seçenekler GeminiImageModel enum'undan alınır |
| `tohum` | Tohum belirli bir değere sabitlendiğinde model, tekrarlanan istekler için aynı yanıtı sağlamak üzere en iyi çabayı gösterir. Deterministik çıktı garanti edilmez. Ayrıca, modeli veya sıcaklık gibi parametre ayarlarını değiştirmek, aynı tohum değerini kullansanız bile yanıtta farklılıklara neden olabilir. Varsayılan olarak rastgele bir tohum değeri kullanılır | INT | zorunlu | 42 | 0 ile 18446744073709551615 arası |
| `görseller` | Model için bağlam olarak kullanılacak isteğe bağlı görüntü(ler). Birden fazla görüntü eklemek için Batch Images düğümünü kullanabilirsiniz | IMAGE | isteğe bağlı | Yok | - |
| `dosyalar` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Generate Content Input Files düğümünden girdileri kabul eder | GEMINI_INPUT_FILES | isteğe bağlı | Yok | - |

*Not: Düğüm, sistem tarafından otomatik olarak işlenen ve kullanıcı girdisi gerektirmeyen gizli parametreler (`auth_token`, `comfy_api_key`, `unique_id`) içerir.*

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Gemini modelinden üretilen görüntü yanıtı | IMAGE |
| `STRING` | Gemini modelinden üretilen metin yanıtı | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImageNode/tr.md)
