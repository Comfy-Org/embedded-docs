> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideoApi/tr.md)

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

Wan Görüntüden Videoya düğümü, tek bir giriş görüntüsü ve bir metin isteminden bir video oluşturur. Sağlanan görüntüyü ilk kare olarak kullanır ve açıklamaya dayalı olarak çözünürlük, süre, ses ve diğer gelişmiş ayarlar için seçeneklerle bir video dizisi oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | "wan2.5-i2v-preview"<br>"wan2.6-i2v" | Kullanılacak model (varsayılan: "wan2.6-i2v") |
| `image` | IMAGE | Evet | - | Video oluşturma için ilk kare görevi gören giriş görüntüsü. Tam olarak bir görüntü gereklidir. |
| `prompt` | STRING | Evet | - | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çinceyi destekler (varsayılan: boş). |
| `negative_prompt` | STRING | Hayır | - | Nelerden kaçınılacağını tanımlayan olumsuz istem (varsayılan: boş). |
| `resolution` | COMBO | Hayır | "480P"<br>"720P"<br>"1080P" | Video çözünürlük kalitesi (varsayılan: "720P"). Wan 2.6 modeli 480P'yi desteklemez. |
| `duration` | INT | Hayır | 5-15 (adım: 5) | Oluşturulan videonun saniye cinsinden süresi. 15 saniyelik süre yalnızca Wan 2.6 modeli tarafından desteklenir (varsayılan: 5). |
| `audio` | AUDIO | Hayır | - | Ses, net ve yüksek bir ses içermeli, gereksiz gürültü veya arka plan müziği olmamalıdır. Sağlandığında, ses süresi 3.0 ile 29.0 saniye arasında olmalıdır. |
| `seed` | INT | Hayır | 0-2147483647 | Oluşturma için kullanılacak tohum değeri (varsayılan: 0). |
| `generate_audio` | BOOLEAN | Hayır | - | Ses girişi sağlanmazsa, sesi otomatik olarak oluştur (varsayılan: False). |
| `prompt_extend` | BOOLEAN | Hayır | - | İstemin yapay zeka yardımıyla geliştirilip geliştirilmeyeceği (varsayılan: True). |
| `watermark` | BOOLEAN | Hayır | - | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği (varsayılan: False). |
| `shot_type` | COMBO | Hayır | "single"<br>"multi" | Oluşturulan video için çekim türünü belirtir, yani videonun tek bir sürekli çekim mi yoksa kesmeli birden çok çekim mi olduğunu belirtir. Bu parametre yalnızca prompt_extend True olduğunda etkilidir (varsayılan: "single"). |

**Kısıtlamalar:**

- Video oluşturma için tam olarak bir giriş görüntüsü gereklidir.
- Wan 2.6 modeli (`wan2.6-i2v`) 480P çözünürlüğü desteklemez.
- 15 saniyelik süre yalnızca Wan 2.6 modeli (`wan2.6-i2v`) tarafından desteklenir.
- Ses sağlandığında, süresi 3.0 ile 29.0 saniye arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Giriş görüntüsüne ve isteme dayalı olarak oluşturulan video. |

---
**Source fingerprint (SHA-256):** `ad4947dbb9c12ebb97ace99cd447431ba6db88a3b74239099fcbea501cff71f0`
