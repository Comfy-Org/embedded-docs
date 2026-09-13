# ElevenLabs Metinden Diyaloğa

ElevenLabs Text to Dialogue düğümü, metinden çok konuşmacılı bir sesli diyalog oluşturur. Her katılımcı için farklı metin satırları ve ayrı sesler belirterek bir konuşma oluşturmanıza olanak tanır. Düğüm, diyalog isteğini ElevenLabs API'sine gönderir ve oluşturulan sesi döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `stability` | Ses kararlılığı. Düşük değerler daha geniş bir duygusal aralık sağlar; yüksek değerler daha tutarlı ancak potansiyel olarak monoton bir konuşma üretir. (varsayılan: 0.5) | FLOAT | Evet | 0.0 - 1.0 |
| `apply_text_normalization` | Metin normalleştirme modu. 'auto' sistemin karar vermesini sağlar, 'on' normalleştirmeyi her zaman uygular, 'off' bunu atlar. | COMBO | Evet | `"auto"`<br>`"on"`<br>`"off"` |
| `model` | Diyalog oluşturma için kullanılacak model. | COMBO | Evet | `"eleven_v3"` |
| `inputs` | Diyalog öğesi sayısı. Bir sayı seçmek, o sayıda metin ve ses girdi çifti oluşturur. | DYNAMIC_COMBO | Evet | `"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `language_code` | ISO-639-1 veya ISO-639-3 dil kodu (örn., 'en', 'es', 'fra'). Otomatik algılama için boş bırakın. (varsayılan: boş) | STRING | Evet | - |
| `seed` | Yeniden üretilebilirlik için tohum. (varsayılan: 1) | INT | Evet | 0 - 4294967295 |
| `output_format` | Ses çıktısı biçimi. | COMBO | Evet | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Diyalog Öğesi Girdileri

Tüm `inputs` seçenekleri tarafından paylaşılır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `text1` ... `text10` | İlgili diyalog öğesi için metin içeriği. Düğüm, seçilen her diyalog öğesi için bir `text` alanı oluşturur. Her metin değeri en az bir karakter içermelidir. | STRING | Evet | - |
| `voice1` ... `voice10` | İlgili diyalog öğesi için ses. Bir Voice Selector veya Instant Voice Clone düğümünden bağlayın. Düğüm, seçilen her diyalog öğesi için bir `voice` alanı oluşturur. | ELEVENLABS_VOICE | Evet | - |

**Not:** `inputs` seçicisi en fazla 10 diyalog öğesi oluşturabilir. Her öğe hem bir `text` alanı hem de bir `voice` alanı gerektirir. `text` değeri boş olamaz. `voice` girdisi, uyumlu bir ElevenLabs ses düğümü tarafından sağlanan bir ses kimliği bekler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Seçilen çıktı biçiminde oluşturulan çok konuşmacılı diyalog sesi. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/tr.md)

---
**Source fingerprint (SHA-256):** `95b16143391a2282c58ebc66561b85338a8ce1f87e0ec769405225599d2c76ae`
