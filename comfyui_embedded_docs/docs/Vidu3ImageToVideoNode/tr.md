> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3ImageToVideoNode/tr.md)

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

Vidu Q3 Görüntüden Videoya Dönüştürme düğümü, bir giriş görüntüsünden başlayarak bir video dizisi oluşturur. Görüntüyü canlandırmak için bir Vidu Q3 modeli kullanır, isteğe bağlı olarak bir metin istemiyle yönlendirilir ve bir video dosyası çıktısı verir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"viduq3-pro"`<br>`"viduq3-turbo"` | Video oluşturma için kullanılacak model. |
| `model.resolution` | COMBO | Evet | `"720p"`<br>`"1080p"`<br>`"2K"` (yalnızca viduq3-pro) | Çıktı videosunun çözünürlüğü. Kullanılabilir seçenekler seçilen modele bağlıdır. |
| `model.duration` | INT | Evet | 1 ila 16 | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). |
| `model.audio` | BOOLEAN | Evet | `True` / `False` | Etkinleştirildiğinde, videoyu sesle (diyalog ve ses efektleri dahil) çıktılar (varsayılan: False). |
| `image` | IMAGE | Evet | - | Oluşturulan videonun başlangıç karesi olarak kullanılacak bir görüntü. |
| `prompt` | STRING | Hayır | - | Video oluşturma için isteğe bağlı bir metin istemi (maksimum 2000 karakter) (varsayılan: boş). |
| `seed` | INT | Hayır | 0 ila 2147483647 | Oluşturmanın rastgeleliğini kontrol etmek için bir tohum değeri (varsayılan: 1). |

**Not:** `image` görüntüsünün en-boy oranı 1:4 ile 4:1 arasında olmalıdır (dikeyden yataya). `prompt` isteğe bağlıdır ancak 2000 karakteri geçemez. `model.resolution` seçenekleri seçilen `model`'e bağlıdır: `"viduq3-pro"` `"720p"`, `"1080p"` ve `"2K"` destekler; `"viduq3-turbo"` ise `"720p"` ve `"1080p"` destekler.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `1dd3929860ee4a04b761014fd2cf7e9e32f9171d8b18fe1e93f27d0905ca04ee`
