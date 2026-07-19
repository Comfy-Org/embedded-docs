# MiniMax Görüntüden Videoya

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

MiniMax'ın API'sini kullanarak bir görsel ve metin istemine dayalı olarak, isteğe bağlı parametrelerle eşzamanlı olarak videolar oluşturur. Bu düğüm, bir video dizisi oluşturmak için bir girdi görseli ve metin açıklaması alır; çeşitli model seçenekleri ve yapılandırma ayarları mevcuttur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Video oluşturmanın ilk karesi olarak kullanılacak görsel | IMAGE | Evet | - |
| `istem_metni` | Video oluşturmayı yönlendirecek metin istemi (varsayılan: boş dize) | STRING | Evet | - |
| `model` | Video oluşturma için kullanılacak model (varsayılan: "I2V-01") | COMBO | Evet | "I2V-01-Direktör"<br>"I2V-01"<br>"I2V-01-canlı" |
| `tohum` | Gürültü oluşturmak için kullanılan rastgele tohum (varsayılan: 0) | INT | Hayır | 0 ile 18446744073709551615 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video çıktısı | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `9ad1659352e363361f09d6a7a0e24835056b20cc84532247251f516b0ac284e8`
