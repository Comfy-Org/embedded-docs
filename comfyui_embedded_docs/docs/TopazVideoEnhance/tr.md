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

Topaz Video Enhance düğümü, video kalitesini artırmak için harici bir API kullanır. Video çözünürlüğünü yükseltebilir, enterpolasyon yoluyla kare hızını artırabilir ve sıkıştırma uygulayabilir. Düğüm, bir giriş MP4 videosunu işler ve seçilen ayarlara göre geliştirilmiş bir sürüm döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Geliştirilecek giriş video dosyası. | VIDEO | Evet | - |
| `upscaler_enabled` | Video yükseltme özelliğini etkinleştirir veya devre dışı bırakır (varsayılan: True). | BOOLEAN | Evet | - |
| `upscaler_model` | Videoyu yükseltmek için kullanılan AI modeli. | COMBO | Evet | `"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"` |
| `upscaler_resolution` | Yükseltilmiş video için hedef çözünürlük. | COMBO | Evet | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_creativity` | Yaratıcılık seviyesi (yalnızca Starlight (Astra) Creative için geçerlidir). (varsayılan: "low") | COMBO | Hayır | `"low"`<br>`"middle"`<br>`"high"` |
| `interpolation_enabled` | Kare enterpolasyonu özelliğini etkinleştirir veya devre dışı bırakır (varsayılan: False). | BOOLEAN | Hayır | - |
| `interpolation_model` | Kare enterpolasyonu için kullanılan model (varsayılan: "apo-8"). | COMBO | Hayır | `"apo-8"` |
| `interpolation_slowmo` | Giriş videosuna uygulanan ağır çekim faktörü. Örneğin, 2 değeri çıktının iki kat daha yavaş olmasını ve süresinin iki katına çıkmasını sağlar. (varsayılan: 1) | INT | Hayır | 1 ila 16 |
| `interpolation_frame_rate` | Çıktı kare hızı. (varsayılan: 60) | INT | Hayır | 15 ila 240 |
| `interpolation_duplicate` | Girişteki yinelenen kareleri analiz eder ve kaldırır. (varsayılan: False) | BOOLEAN | Hayır | - |
| `interpolation_duplicate_threshold` | Yinelenen kareler için algılama hassasiyeti. (varsayılan: 0.01) | FLOAT | Hayır | 0.001 ila 0.1 |
| `dynamic_compression_level` | CQP seviyesi. (varsayılan: "Low") | COMBO | Hayır | `"Low"`<br>`"Mid"`<br>`"High"` |

**Not:** En az bir geliştirme özelliği etkinleştirilmelidir. Hem `upscaler_enabled` hem de `interpolation_enabled` değerleri `False` olarak ayarlanırsa düğüm bir hata verecektir. Giriş videosu MP4 formatında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Geliştirilmiş çıktı video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/tr.md)

---
**Source fingerprint (SHA-256):** `70e1a6e0d7bd250f58c43beefe070fd83af19d11ac08cb9a6ac9655a9bfa839f`
