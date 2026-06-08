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

ElevenLabs Konuşmayı Metne Çevir düğümü, ses dosyalarını metne dönüştürür. ElevenLabs'ın API'sini kullanarak konuşulan kelimeleri yazılı bir metne çevirir; otomatik dil algılama, farklı konuşmacıları tanımlama ve müzik veya kahkaha gibi konuşma dışı sesleri etiketleme gibi özellikleri destekler.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ses` | Metne çevrilecek ses. | AUDIO | Evet | - |
| `model` | Metne çevirme için kullanılacak model. Bu modelin seçilmesi ek parametreleri ortaya çıkarır. | COMBO | Evet | `"scribe_v2"` |
| `tag_audio_events` | Metinde (kahkaha), (müzik) gibi sesleri açıklama. Bu parametre, `"scribe_v2"` modeli seçildiğinde görünür hale gelir. (varsayılan: False) | BOOLEAN | Hayır | - |
| `diarize` | Hangi konuşmacının konuştuğunu açıklama. Bu parametre, `"scribe_v2"` modeli seçildiğinde görünür hale gelir. (varsayılan: False) | BOOLEAN | Hayır | - |
| `diarization_threshold` | Konuşmacı ayırma hassasiyeti. Daha düşük değerler konuşmacı değişikliklerine karşı daha hassastır. Bu parametre, `"scribe_v2"` modeli seçildiğinde ve `diarize` etkinleştirildiğinde görünür hale gelir. (varsayılan: 0.22) | FLOAT | Hayır | 0.1 - 0.4 |
| `temperature` | Rastgelelik kontrolü. 0.0 model varsayılanını kullanır. Daha yüksek değerler rastgeleliği artırır. Bu parametre, `"scribe_v2"` modeli seçildiğinde görünür hale gelir. (varsayılan: 0.0) | FLOAT | Hayır | 0.0 - 2.0 |
| `timestamps_granularity` | Metin kelimeleri için zamanlama hassasiyeti. Bu parametre, `"scribe_v2"` modeli seçildiğinde görünür hale gelir. (varsayılan: "word") | COMBO | Hayır | `"word"`<br>`"character"`<br>`"none"` |
| `dil_kodu` | ISO-639-1 veya ISO-639-3 dil kodu (ör. 'en', 'es', 'fra'). Otomatik algılama için boş bırakın. (varsayılan: "") | STRING | Hayır | - |
| `konuşmacı_sayısı` | Tahmin edilecek maksimum konuşmacı sayısı. Otomatik algılama için 0 olarak ayarlayın. (varsayılan: 0) | INT | Hayır | 0 - 32 |
| `tohum` | Tekrarlanabilirlik için tohum değeri (determinizm garanti edilmez). (varsayılan: 1) | INT | Hayır | 0 - 2147483647 |

**Not:** `diarize` seçeneği etkinleştirildiğinde `num_speakers` parametresi 0'dan büyük bir değere ayarlanamaz. `diarize` seçeneğini devre dışı bırakmalı veya `num_speakers` değerini 0 olarak ayarlamalısınız.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `dil_kodu` | Sesten metne çevrilmiş metin. | STRING |
| `kelimeler_json` | Sesin algılanan dil kodu. | STRING |
| `words_json` | Zaman damgaları ve etkinleştirilmişse konuşmacı etiketleri dahil olmak üzere kelime düzeyinde ayrıntılı bilgiler içeren JSON biçimli bir dize. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/tr.md)

---
**Source fingerprint (SHA-256):** `aca2ac04d7280ef2b604f7c8d29ad7fea1e7abcfc38beabb64ba6b268a8cade1`
