> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawVideoEnhance/tr.md)

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

HitPaw Video Enhance düğümü, videoların kalitesini artırmak için harici bir API kullanır. Düşük çözünürlüklü videoları daha yüksek bir çözünürlüğe yükseltir, görsel yapaylıkları giderir ve gürültüyü azaltır. İşlem maliyeti, giriş videosunun saniyesi başına hesaplanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | DYNAMIC COMBO | Evet | Birden çok seçenek mevcut | Video iyileştirme için kullanılacak AI modeli. Bir model seçmek, iç içe geçmiş bir `resolution` parametresini ortaya çıkarır. Mevcut modeller ve destekledikleri çözünürlükler farklılık gösterir. |
| `model.resolution` | COMBO | Evet | `"original"`<br>`"720p"`<br>`"1080p"`<br>`"2k/qhd"`<br>`"4k/uhd"`<br>`"8k"` | İyileştirilmiş video için hedef çözünürlük. Seçilen `model`'e bağlı olarak bazı seçenekler kullanılamayabilir. |
| `video` | VIDEO | Evet | Yok | İyileştirilecek giriş video dosyası. |

**Kısıtlamalar:**

* Giriş `video`'sunun süresi 0,5 saniye ile 60 dakika (3600 saniye) arasında olmalıdır.
* Seçilen `resolution`, giriş videosunun boyutlarından daha büyük olmalıdır. Video kare ise, seçilen çözünürlük genişliğinden/yüksekliğinden daha büyük olmalıdır. Kare olmayan videolar için, seçilen çözünürlük videonun daha kısa boyutundan daha büyük olmalıdır. Hedef çözünürlük daha küçükse bir hata oluşur. Giriş videosunun çözünürlüğünü korumak için `"original"` seçeneğini seçin.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | İyileştirilmiş video dosyası. |

---
**Source fingerprint (SHA-256):** `0f329cbf61784474ee5b97a92d28a3e2383dc40e208f8a8317f3c4f60b43e5b2`
