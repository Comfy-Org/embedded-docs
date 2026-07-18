# HeyGenVideoTranslateNode

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

5. **KRİTİK KURAL - Çıktı Adları:** Çıktılar tablosunun ilk sütunu, İngilizce kalması ZORUNLU olan çıktı adlarını içerir (örn. `positive`, `negative`, `latent`, `image`, `model`, `conditioning`). Çıktı adlarını çevirmek yinelenen girdilere ve belge yapısının bozulmasına neden olur.

Sesli bir videoyu, ses klonlama ve dudak senkronizasyonu ile başka bir dile çevirin. Bu düğüm, orijinal konuşmacının sesini klonlar ve çevrilen konuşmaya uyacak şekilde ağzı yeniden canlandırarak doğal görünümlü bir sonuç üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Çevrilecek konuşma içeren video. | VIDEO | Evet | - |
| `output_language` | Çevrilen video için hedef dil. | STRING | Evet | "Arabic"<br>"Bengali"<br>"Chinese"<br>"Danish"<br>"Dutch"<br>"English"<br>"French"<br>"German"<br>"Greek"<br>"Hindi"<br>"Indonesian"<br>"Italian"<br>"Japanese"<br>"Korean"<br>"Malay"<br>"Polish"<br>"Portuguese"<br>"Russian"<br>"Spanish"<br>"Swedish"<br>"Tamil"<br>"Telugu"<br>"Thai"<br>"Turkish"<br>"Ukrainian"<br>"Vietnamese" |
| `mode` | 'speed' daha hızlıdır; 'precision' iki kat fiyata daha yüksek kaliteli dudak senkronizasyonu üretir. | STRING | Evet | "speed"<br>"precision" |
| `translate_audio_only` | Yalnızca ses parçasını değiştirir, orijinal ağız hareketlerini korur (dudak senkronizasyonu yok). (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `speaker_count` | Videodaki konuşmacı sayısı. 0 = otomatik olarak algıla. (varsayılan: 0) | INT | Hayır | 0 ile 10 arası |
| `seed` | HeyGen'e gönderilmez; yeniden çalıştırmayı zorlamak için değiştirin. (varsayılan: 42) | INT | Hayır | 0 ile 2147483647 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Ses klonlama ve dudak senkronizasyonu uygulanmış çevrilmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVideoTranslateNode/tr.md)

---
**Source fingerprint (SHA-256):** `31056060b6309b8ec28b37b353322403e173fd2862b56021392dba24e7a15f69`
