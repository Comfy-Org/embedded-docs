# ElevenLabs Metinden Diyaloğa

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

ElevenLabs Metinden Diyaloğa düğümü, metinden çok konuşmacılı bir ses diyaloğu oluşturur. Farklı metin satırları ve her katılımcı için farklı sesler belirleyerek bir konuşma oluşturmanıza olanak tanır. Düğüm, diyalog isteğini ElevenLabs API'sine gönderir ve oluşturulan sesi döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `kararlılık` | Ses kararlılığı. Düşük değerler daha geniş bir duygusal yelpaze sağlarken, yüksek değerler daha tutarlı ancak potansiyel olarak monoton konuşma üretir. (varsayılan: 0.5) | FLOAT | Hayır | 0.0 - 1.0 |
| `metin normalizasyonunu uygula` | Metin normalizasyon modu. 'auto' sistemin karar vermesini sağlar, 'on' her zaman normalizasyonu uygular, 'off' atlar. | COMBO | Hayır | `"auto"`<br>`"on"`<br>`"off"` |
| `model` | Diyalog oluşturma için kullanılacak model. | COMBO | Hayır | `"eleven_v3"` |
| `girdiler` | Diyalog girişi sayısı. Bir sayı seçmek, o kadar sayıda metin ve ses giriş alanı oluşturacaktır. | DYNAMICCOMBO | Evet | `"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `dil_kodu` | ISO-639-1 veya ISO-639-3 dil kodu (ör. 'en', 'es', 'fra'). Otomatik algılama için boş bırakın. (varsayılan: boş) | STRING | Hayır | - |
| `tohum` | Tekrarlanabilirlik için tohum değeri. (varsayılan: 1) | INT | Hayır | 0 - 4294967295 |
| `çıktı_formatı` | Ses çıktı formatı. | COMBO | Hayır | `"mp3_44100_192"`<br>`"opus_48000_192"` |

**Not:** `inputs` parametresi dinamiktir. Bir sayı seçtiğinizde (ör. "3"), düğüm üç adet karşılık gelen `text` ve `voice` giriş alanı görüntüleyecektir (ör. `text1`, `voice1`, `text2`, `voice2`, `text3`, `voice3`). Her `text` alanı en az bir karakter içermelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio` | Seçilen çıktı formatında oluşturulan çok konuşmacılı diyalog sesi. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/tr.md)

---
**Source fingerprint (SHA-256):** `2e1634e90314167320d715346f8d0c691dfabe82b090391afa2b0b18a8a126d8`
