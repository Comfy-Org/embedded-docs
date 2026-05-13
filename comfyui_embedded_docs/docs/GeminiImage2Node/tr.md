> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/tr.md)

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

GeminiImage2Node, Google'ın Vertex AI Gemini modelini kullanarak görseller oluşturur veya düzenler. API'ye bir metin istemi ve isteğe bağlı referans görselleri veya dosyaları gönderir ve oluşturulan görseli ve/veya bir metin açıklamasını döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | Yok | Oluşturulacak görseli veya uygulanacak düzenlemeleri tanımlayan metin istemi. Modelin takip etmesi gereken tüm kısıtlamaları, stilleri veya detayları ekleyin. |
| `model` | COMBO | Evet | `"gemini-3-pro-image-preview"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"` | Oluşturma için kullanılacak belirli Gemini modeli. "Nano Banana 2" seçeneği dahili olarak `gemini-3.1-flash-image-preview` modeline eşlenir. |
| `seed` | INT | Evet | 0 ile 18446744073709551615 arası | Belirli bir değere sabitlendiğinde, model tekrarlanan istekler için aynı yanıtı sağlamak üzere en iyi çabayı gösterir. Deterministik çıktı garanti edilmez. Modeli veya diğer ayarları değiştirmek, aynı tohum değeriyle bile farklılıklara neden olabilir. Varsayılan: 42. |
| `aspect_ratio` | COMBO | Evet | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` | Çıktı görseli için istenen en boy oranı. 'auto' olarak ayarlanırsa, giriş görselinizin en boy oranına uyar; görsel sağlanmazsa, genellikle 16:9 kare oluşturulur. Varsayılan: "auto". |
| `resolution` | COMBO | Evet | `"1K"`<br>`"2K"`<br>`"4K"` | Hedef çıktı çözünürlüğü. 2K/4K için yerel Gemini yükselticisi kullanılır. |
| `response_modalities` | COMBO | Evet | `"IMAGE+TEXT"`<br>`"IMAGE"` | Yalnızca görsel çıktısı için 'IMAGE' veya hem oluşturulan görseli hem de bir metin yanıtını döndürmek için 'IMAGE+TEXT' seçeneğini belirleyin. |
| `images` | IMAGE | Hayır | Yok | İsteğe bağlı referans görsel(ler)i. Birden fazla görsel eklemek için Toplu Görseller düğümünü kullanın (en fazla 14). |
| `files` | CUSTOM | Hayır | Yok | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini İçerik Oluşturma Giriş Dosyaları düğümünden girişleri kabul eder. |
| `system_prompt` | STRING | Hayır | Yok | Bir yapay zekanın davranışını belirleyen temel talimatlar. Varsayılan: Görsel oluşturma için önceden tanımlanmış bir sistem istemi. |

**Kısıtlamalar:**

* `images` girişi en fazla 14 görseli destekler. Daha fazlası sağlanırsa bir hata oluşur.
* `files` girişi, `GEMINI_INPUT_FILES` veri türünü çıkış olarak veren bir düğüme bağlanmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Gemini modeli tarafından oluşturulan veya düzenlenen görsel. |
| `string` | STRING | Modelden gelen metin yanıtı. `response_modalities` "IMAGE" olarak ayarlanmışsa bu çıktı boş olacaktır. |

---
**Source fingerprint (SHA-256):** `20a937a635f883a42e22582ae415f6d2a9a6ecc50f147c9090431877e5461144`
