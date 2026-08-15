# ElevenLabs Metinden Diyaloğa

ElevenLabs Text to Dialogue düğümü, metinden çok konuşmacılı bir sesli diyalog oluşturur. Her katılımcı için farklı metin satırları ve ayrı sesler belirleyerek bir konuşma oluşturmanıza olanak tanır. Düğüm, diyalog isteğini ElevenLabs API'sine gönderir ve oluşturulan sesi döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `kararlılık` | Ses stabilitesi. Düşük değerler daha geniş bir duygusal yelpaze sağlar; yüksek değerler daha tutarlı ancak potansiyel olarak tekdüze konuşma üretir. (varsayılan: 0.5) | FLOAT | Evet | 0.0 - 1.0 |
| `metin normalizasyonunu uygula` | Metin normalizasyon modu. 'auto' sistemin karar vermesini sağlar, 'on' her zaman normalizasyonu uygular, 'off' normalizasyonu atlar. | COMBO | Evet | `"auto"`<br>`"on"`<br>`"off"` |
| `model` | Diyalog üretimi için kullanılacak model. | COMBO | Evet | `"eleven_v3"` |
| `girdiler` | Diyalog girdisi sayısı. Bir sayı seçmek, bu sayıda metin ve ses girdi alanı oluşturur. | DYNAMIC_COMBO | Evet | `"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `dil_kodu` | ISO-639-1 veya ISO-639-3 dil kodu (örn. 'en', 'es', 'fra'). Otomatik algılama için boş bırakın. (varsayılan: boş) | STRING | Evet | - |
| `tohum` | Tekrarlanabilirlik için seed değeri. (varsayılan: 1) | INT | Evet | 0 - 4294967295 |
| `çıktı_formatı` | Ses çıktı formatı. | COMBO | Evet | `"mp3_44100_192"`<br>`"opus_48000_192"` |

**Not:** `inputs` parametresi dinamiktir. Bir sayı seçtiğinizde (örn. "3"), düğüm üç karşılık gelen `text` ve `voice` girdi alanı görüntüler (örn. `text1`, `voice1`, `text2`, `voice2`, `text3`, `voice3`). Her `text` alanı en az bir karakter içermelidir. Her `voice` alanı, Voice Selector veya Instant Voice Clone düğümünden bağlanan bir sesi kabul eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Seçilen çıktı formatında oluşturulan çok konuşmacılı diyalog sesi. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/tr.md)

---
**Source fingerprint (SHA-256):** `95b16143391a2282c58ebc66561b85338a8ce1f87e0ec769405225599d2c76ae`
