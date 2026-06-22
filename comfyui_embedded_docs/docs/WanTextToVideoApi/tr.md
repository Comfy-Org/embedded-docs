# Wan Metinden Videoya

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

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak model (varsayılan: "wan2.6-t2v") | COMBO | Evet | "wan2.5-t2v-preview"<br>"wan2.6-t2v" |
| `prompt` | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çinceyi destekler (varsayılan: "") | STRING | Evet | - |
| `negative_prompt` | Kaçınılması gerekenleri tanımlayan olumsuz istem (varsayılan: "") | STRING | Hayır | - |
| `size` | Video çözünürlüğü ve en-boy oranı (varsayılan: "720p: 1:1 (960x960)") | COMBO | Hayır | "480p: 1:1 (624x624)"<br>"480p: 16:9 (832x480)"<br>"480p: 9:16 (480x832)"<br>"720p: 1:1 (960x960)"<br>"720p: 16:9 (1280x720)"<br>"720p: 9:16 (720x1280)"<br>"720p: 4:3 (1088x832)"<br>"720p: 3:4 (832x1088)"<br>"1080p: 1:1 (1440x1440)"<br>"1080p: 16:9 (1920x1080)"<br>"1080p: 9:16 (1080x1920)"<br>"1080p: 4:3 (1632x1248)"<br>"1080p: 3:4 (1248x1632)" |
| `duration` | Videonun saniye cinsinden süresi. 15 saniyelik süre yalnızca Wan 2.6 modeli için kullanılabilir (varsayılan: 5) | INT | Hayır | 5-15 (5'er adımlarla) |
| `audio` | Ses, net ve yüksek bir konuşma içermeli, gereksiz gürültü veya arka plan müziği olmamalıdır | AUDIO | Hayır | - |
| `seed` | Üretim için kullanılacak tohum değeri (varsayılan: 0) | INT | Hayır | 0-2147483647 |
| `generate_audio` | Ses girişi sağlanmazsa, sesi otomatik olarak oluştur (varsayılan: False) | BOOLEAN | Hayır | - |
| `prompt_extend` | İstemin yapay zeka yardımıyla geliştirilip geliştirilmeyeceği (varsayılan: True) | BOOLEAN | Hayır | - |
| `watermark` | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği (varsayılan: False) | BOOLEAN | Hayır | - |
| `çekim_türü` | Oluşturulan video için çekim türünü belirtir; yani videonun tek bir sürekli çekim mi yoksa kesmeli birden çok çekim mi olduğunu belirler. Bu parametre yalnızca prompt_extend True olduğunda etkilidir (varsayılan: "single") | COMBO | Hayır | "single"<br>"multi" |

**Not:** Wan 2.6 modeli 480p çözünürlükleri desteklemez. 15 saniyelik süre yalnızca Wan 2.6 modeli tarafından desteklenir. Ses girişi sağlarken, süresi 3.0 ile 29.0 saniye arasında olmalı ve arka plan gürültüsü veya müzik olmadan net bir konuşma içermelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Giriş parametrelerine göre oluşturulan video | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToVideoApi/tr.md)

---
**Source fingerprint (SHA-256):** `e978f384365060a6d71899e4e2e22b2c6f4268fb0da988c8902e4876d8597a96`
