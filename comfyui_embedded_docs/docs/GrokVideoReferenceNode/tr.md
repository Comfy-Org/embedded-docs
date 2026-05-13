> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/tr.md)

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

Grok Referanstan-Videoya düğümü, çıktının stilini ve içeriğini yönlendirmek için en fazla yedi referans görseli kullanarak bir metin istemine dayalı video oluşturur. Videoyu oluşturmak için harici bir API'ye bağlanır, ardından video indirilir ve döndürülür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | Yok | İstenen videonun metin açıklaması. |
| `model` | COMBO | Evet | `"grok-imagine-video"` | Video oluşturma için kullanılacak model. |
| `model.reference_images` | IMAGE | Evet | 1 ila 7 görsel | Video oluşturmayı yönlendirmek için en fazla 7 referans görseli. |
| `model.resolution` | COMBO | Evet | `"480p"`<br>`"720p"` | Çıktı videosunun çözünürlüğü. |
| `model.aspect_ratio` | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` | Çıktı videosunun en-boy oranı. |
| `model.duration` | INT | Evet | 2 ila 10 | Çıktı videosunun saniye cinsinden süresi (varsayılan: 6). |
| `seed` | INT | Hayır | 0 ila 2147483647 | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir (varsayılan: 0). |

**Not:** `model` parametresi, `reference_images`, `resolution`, `aspect_ratio` ve `duration` öğelerini içeren bir gruptur. En az bir referans görseli sağlamanız gerekir ve en fazla yedi görsel sağlayabilirsiniz.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | Oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `e368769b869b7a0d0be8e6fdcc2b82774c11805483b2e83a448b6985a6dd9f96`
