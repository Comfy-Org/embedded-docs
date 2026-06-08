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

GeminiNanoBanana2 düğümü, Google'ın Vertex AI Gemini modelini kullanarak görseller oluşturur veya düzenler. Bir metin istemi ve isteğe bağlı referans görselleri veya dosyaları API'ye göndererek çalışır ve oluşturulan görsel ile varsa eşlik eden metni döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | Oluşturulacak görseli veya uygulanacak düzenlemeleri tanımlayan metin istemi. Modelin uyması gereken kısıtlamaları, stilleri veya detayları ekleyin. | STRING | Evet | Yok |
| `model` | Görsel oluşturma için kullanılacak belirli Gemini modeli. | COMBO | Evet | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | Tohum belirli bir değere sabitlendiğinde model, tekrarlanan istekler için aynı yanıtı sağlamak üzere elinden gelenin en iyisini yapar. Belirleyici (deterministik) çıktı garanti edilmez. Ayrıca, modeli veya sıcaklık gibi parametre ayarlarını değiştirmek, aynı tohum değerini kullansanız bile yanıtta farklılıklara neden olabilir. Varsayılan olarak rastgele bir tohum değeri kullanılır. (varsayılan: 42) | INT | Evet | 0 ile 18446744073709551615 arası |
| `aspect_ratio` | 'auto' olarak ayarlanırsa, giriş görselinizin en boy oranıyla eşleşir; hiçbir görsel sağlanmazsa, genellikle 16:9 kare oluşturulur. (varsayılan: "auto") | COMBO | Evet | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | Hedef çıktı çözünürlüğü. 2K/4K için yerel Gemini yükseltici (upscaler) kullanılır. | COMBO | Evet | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | Modelin döndüreceği içerik türünü belirler. (gelişmiş) | COMBO | Evet | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `thinking_level` | Modelin akıl yürütme sürecinin derinliğini kontrol eder. | COMBO | Evet | `"MINIMAL"`<br>`"HIGH"` |
| `images` | İsteğe bağlı referans görsel(ler)i. Birden fazla görsel eklemek için (en fazla 14), Toplu Görseller (Batch Images) düğümünü kullanın. | IMAGE | Hayır | Yok |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini İçerik Oluşturma Giriş Dosyaları (Gemini Generate Content Input Files) düğümünden girişleri kabul eder. | CUSTOM | Hayır | Yok |
| `system_prompt` | Bir yapay zekanın davranışını belirleyen temel talimatlar. (gelişmiş) | STRING | Hayır | Yok |

**Not:** `images` girişi en fazla 14 görseli destekler. Daha fazlası sağlanırsa, düğüm bir hata verecektir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Model tarafından oluşturulan veya düzenlenen birincil görsel. | IMAGE |
| `thought_image` | Model tarafından döndürülen herhangi bir metin içeriği. | STRING |
| `thought_image` | Modelin düşünme sürecindeki ilk görsel. Yalnızca thinking_level HIGH ve IMAGE+TEXT modalitesi ile kullanılabilir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/tr.md)

---
**Source fingerprint (SHA-256):** `bd53363da73ff0db66a872fc04f1af8ce4dfee1191ca01bd813701b5ad5e4f17`
