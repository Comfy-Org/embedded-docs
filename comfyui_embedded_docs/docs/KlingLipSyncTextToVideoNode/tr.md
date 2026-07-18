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

Kling Lip Sync Text to Video Node, bir video dosyasındaki ağız hareketlerini bir metin istemiyle eşleştirmek için senkronize eder. Bir girdi videosu alır ve karakterin dudak hareketlerinin sağlanan metinle uyumlu olduğu yeni bir video oluşturur. Düğüm, doğal görünümlü konuşma senkronizasyonu oluşturmak için ses sentezi kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Dudak senkronizasyonu için girdi video dosyası | VIDEO | Evet | - |
| `metin` | Dudak Senkronizasyonu Video Oluşturma için Metin İçeriği. Mod text2video olduğunda gereklidir. Maksimum uzunluk 120 karakterdir. | STRING | Evet | - |
| `ses` | Dudak senkronizasyonu sesi için ses seçimi (varsayılan: "Melody") | COMBO | Hayır | "Melody"<br>"Bella"<br>"Aria"<br>"Ethan"<br>"Ryan"<br>"Dorothy"<br>"Nathan"<br>"Lily"<br>"Aaron"<br>"Emma"<br>"Grace"<br>"Henry"<br>"Isabella"<br>"James"<br>"Katherine"<br>"Liam"<br>"Mia"<br>"Noah"<br>"Olivia"<br>"Sophia" |
| `ses_hızı` | Konuşma Hızı. Geçerli aralık: 0.8~2.0, bir ondalık basamağa kadar hassas. (varsayılan: 1) | FLOAT | Hayır | 0.8-2.0 |

**Video Gereksinimleri:**

- Video dosyası 100MB'tan büyük olmamalıdır
- Yükseklik/genişlik 720px ile 1920px arasında olmalıdır
- Süre 2s ile 10s arasında olmalıdır

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video_kimliği` | Dudak senkronizasyonlu ses ile oluşturulan video | VIDEO |
| `video_kimliği` | Oluşturulan video için benzersiz tanımlayıcı | STRING |
| `süre` | Oluşturulan video için süre bilgisi | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `f16200d52ba05acfedebc027dde91e2c91bdbb80086888d947c9f56a4e92856d`
