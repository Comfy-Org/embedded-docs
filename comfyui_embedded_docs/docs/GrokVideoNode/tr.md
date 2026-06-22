# Grok Video

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

Grok Video düğümü, bir metin açıklamasından kısa bir video oluşturur. Bir istem kullanarak sıfırdan bir video oluşturabilir veya bir isteme dayalı olarak tek bir giriş görüntüsünü canlandırabilir. Düğüm, harici bir API'ye istek gönderir ve oluşturulan videoyu döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak model. | COMBO | Evet | `"grok-imagine-video"`<br>`"grok-imagine-video-beta"` |
| `istem` | İstenen videonun metin açıklaması. | STRING | Evet | - |
| `çözünürlük` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"` |
| `en boy oranı` | Çıktı videosunun en-boy oranı (varsayılan: "auto"). | COMBO | Evet | `"auto"`<br>`"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `süre` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 6). | INT | Evet | 1 ile 15 |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 ile 2147483647 |
| `görüntü` | Canlandırılacak isteğe bağlı bir giriş görüntüsü. | IMAGE | Hayır | - |

**Not:** Bir `image` sağlanırsa, yalnızca tek bir görüntü desteklenir. Birden fazla görüntü sağlanması hataya neden olur. `prompt` (istem), boşluklar temizlendikten sonra en az 1 karakter uzunluğunda olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `d48049fafbe4dbf50eb5a42495d445fa4c7fc590a1d70267e220ccedc2f5328a`
