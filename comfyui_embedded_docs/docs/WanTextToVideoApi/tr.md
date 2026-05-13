> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToVideoApi/tr.md)

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

Wan Metinden Videoya düğümü, metin açıklamalarına dayalı video içeriği oluşturur. İstemlerden video oluşturmak için yapay zeka modelleri kullanır ve çeşitli video boyutlarını, sürelerini ve isteğe bağlı ses girişlerini destekler. Düğüm, gerektiğinde otomatik olarak ses oluşturabilir ve istem geliştirme ile filigran ekleme seçenekleri sunar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | "wan2.5-t2v-preview"<br>"wan2.6-t2v" | Kullanılacak model (varsayılan: "wan2.6-t2v") |
| `prompt` | STRING | Evet | - | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çinceyi destekler (varsayılan: "") |
| `negative_prompt` | STRING | Hayır | - | Kaçınılması gerekenleri tanımlayan olumsuz istem (varsayılan: "") |
| `size` | COMBO | Hayır | "480p: 1:1 (624x624)"<br>"480p: 16:9 (832x480)"<br>"480p: 9:16 (480x832)"<br>"720p: 1:1 (960x960)"<br>"720p: 16:9 (1280x720)"<br>"720p: 9:16 (720x1280)"<br>"720p: 4:3 (1088x832)"<br>"720p: 3:4 (832x1088)"<br>"1080p: 1:1 (1440x1440)"<br>"1080p: 16:9 (1920x1080)"<br>"1080p: 9:16 (1080x1920)"<br>"1080p: 4:3 (1632x1248)"<br>"1080p: 3:4 (1248x1632)" | Video çözünürlüğü ve en-boy oranı (varsayılan: "720p: 1:1 (960x960)") |
| `duration` | INT | Hayır | 5-15 (5'er adımlarla) | Videonun saniye cinsinden süresi. 15 saniyelik süre yalnızca Wan 2.6 modeli için kullanılabilir (varsayılan: 5) |
| `audio` | AUDIO | Hayır | - | Ses, net ve yüksek bir konuşma içermeli, gereksiz gürültü veya arka plan müziği olmamalıdır |
| `seed` | INT | Hayır | 0-2147483647 | Üretim için kullanılacak tohum değeri (varsayılan: 0) |
| `generate_audio` | BOOLEAN | Hayır | - | Ses girişi sağlanmazsa, sesi otomatik olarak oluştur (varsayılan: False) |
| `prompt_extend` | BOOLEAN | Hayır | - | İstemin yapay zeka yardımıyla geliştirilip geliştirilmeyeceği (varsayılan: True) |
| `watermark` | BOOLEAN | Hayır | - | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği (varsayılan: False) |
| `shot_type` | COMBO | Hayır | "single"<br>"multi" | Oluşturulan video için çekim türünü belirtir; yani videonun tek bir sürekli çekim mi yoksa kesmeli birden çok çekim mi olduğunu belirler. Bu parametre yalnızca prompt_extend True olduğunda etkilidir (varsayılan: "single") |

**Not:** Wan 2.6 modeli 480p çözünürlükleri desteklemez. 15 saniyelik süre yalnızca Wan 2.6 modeli tarafından desteklenir. Ses girişi sağlarken, süresi 3.0 ile 29.0 saniye arasında olmalı ve arka plan gürültüsü veya müzik olmadan net bir konuşma içermelidir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Giriş parametrelerine göre oluşturulan video |

---
**Source fingerprint (SHA-256):** `e978f384365060a6d71899e4e2e22b2c6f4268fb0da988c8902e4876d8597a96`
