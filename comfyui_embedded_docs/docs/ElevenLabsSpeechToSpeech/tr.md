> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/tr.md)

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

ElevenLabs Konuşmadan Konuşmaya düğümü, bir giriş ses dosyasını bir sesten başka bir sese dönüştürür. Sesin orijinal içeriğini ve duygusal tonunu koruyarak konuşmayı dönüştürmek için ElevenLabs API'sini kullanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `ses` | CUSTOM | Evet | - | Dönüşüm için hedef ses. Ses Seçici veya Anlık Ses Klonlama'dan bağlantı kurun. |
| `ses` | AUDIO | Evet | - | Dönüştürülecek kaynak ses. |
| `kararlılık` | FLOAT | Hayır | 0.0 - 1.0 | Ses kararlılığı. Düşük değerler daha geniş bir duygusal yelpaze sağlar, yüksek değerler daha tutarlı ancak potansiyel olarak monoton konuşma üretir (varsayılan: 0.5). |
| `model` | DYNAMICCOMBO | Hayır | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` | Konuşmadan konuşmaya dönüşüm için kullanılacak model. Her seçenek belirli bir ses ayarları kümesi sağlar (similarity_boost, style, use_speaker_boost, speed). |
| `çıktı_formatı` | COMBO | Hayır | `"mp3_44100_192"`<br>`"opus_48000_192"` | Ses çıktı formatı (varsayılan: "mp3_44100_192"). |
| `tohum` | INT | Hayır | 0 - 4294967295 | Tekrarlanabilirlik için tohum değeri (varsayılan: 0). |
| `arka_plan_gürültüsünü_kaldır` | BOOLEAN | Hayır | - | Ses izolasyonu kullanarak giriş sesinden arka plan gürültüsünü kaldırır (varsayılan: False). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `ses` | AUDIO | Belirtilen çıktı formatında dönüştürülmüş ses dosyası. |

---
**Source fingerprint (SHA-256):** `118fe6e85b146d0649b104d814abb518d37f69ade2e53becac365a0ec90146fd`
