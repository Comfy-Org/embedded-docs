> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/tr.md)

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

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Evet | - | Geliştirilecek giriş video dosyası. |
| `upscaler_enabled` | BOOLEAN | Evet | - | Video yükseltme özelliğini etkinleştirir veya devre dışı bırakır (varsayılan: True). |
| `upscaler_model` | COMBO | Evet | `"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"` | Videoyu yükseltmek için kullanılan AI modeli. |
| `upscaler_resolution` | COMBO | Evet | `"FullHD (1080p)"`<br>`"4K (2160p)"` | Yükseltilmiş video için hedef çözünürlük. |
| `upscaler_creativity` | COMBO | Hayır | `"low"`<br>`"middle"`<br>`"high"` | Yaratıcılık seviyesi (yalnızca Starlight (Astra) Creative için geçerlidir). (varsayılan: "low") |
| `interpolation_enabled` | BOOLEAN | Hayır | - | Kare enterpolasyonu özelliğini etkinleştirir veya devre dışı bırakır (varsayılan: False). |
| `interpolation_model` | COMBO | Hayır | `"apo-8"` | Kare enterpolasyonu için kullanılan model (varsayılan: "apo-8"). |
| `interpolation_slowmo` | INT | Hayır | 1 ila 16 | Giriş videosuna uygulanan ağır çekim faktörü. Örneğin, 2 değeri çıktının iki kat daha yavaş olmasını ve süresinin iki katına çıkmasını sağlar. (varsayılan: 1) |
| `interpolation_frame_rate` | INT | Hayır | 15 ila 240 | Çıktı kare hızı. (varsayılan: 60) |
| `interpolation_duplicate` | BOOLEAN | Hayır | - | Girişteki yinelenen kareleri analiz eder ve kaldırır. (varsayılan: False) |
| `interpolation_duplicate_threshold` | FLOAT | Hayır | 0.001 ila 0.1 | Yinelenen kareler için algılama hassasiyeti. (varsayılan: 0.01) |
| `dynamic_compression_level` | COMBO | Hayır | `"Low"`<br>`"Mid"`<br>`"High"` | CQP seviyesi. (varsayılan: "Low") |

**Not:** En az bir geliştirme özelliği etkinleştirilmelidir. Hem `upscaler_enabled` hem de `interpolation_enabled` değerleri `False` olarak ayarlanırsa düğüm bir hata verecektir. Giriş videosu MP4 formatında olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | Geliştirilmiş çıktı video dosyası. |

---
**Source fingerprint (SHA-256):** `70e1a6e0d7bd250f58c43beefe070fd83af19d11ac08cb9a6ac9655a9bfa839f`
