> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/tr.md)

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

Vidu Metinden Videoya Oluşturma düğümü, metin açıklamalarından videolar oluşturur. Metin istemlerinizi, süre, en boy oranı ve görsel stil için özelleştirilebilir ayarlarla video içeriğine dönüştürmek için Vidu video oluşturma modelini kullanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `viduq1` | Model adı |
| `prompt` | STRING | Evet | - | Video oluşturma için metinsel açıklama |
| `duration` | INT | Hayır | 5-5 | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5) |
| `seed` | INT | Hayır | 0-2147483647 | Video oluşturma için tohum değeri (0 rastgele için) (varsayılan: 0) |
| `aspect_ratio` | COMBO | Hayır | `16:9`<br>`9:16`<br>`1:1` | Çıktı videosunun en boy oranı |
| `resolution` | COMBO | Hayır | `1080p` | Desteklenen değerler modele ve süreye göre değişiklik gösterebilir |
| `movement_amplitude` | COMBO | Hayır | `auto`<br>`small`<br>`medium`<br>`large` | Karedeki nesnelerin hareket genliği |

**Not:** `prompt` alanı zorunludur ve boş olamaz. `duration` parametresi şu anda 5 saniye olarak sabitlenmiştir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Metin istemine göre oluşturulan video |

---
**Source fingerprint (SHA-256):** `0d331d3eab8a4af9c90831f3f8fd8ae34aa0c393142cb6f89404edc94024d95f`
