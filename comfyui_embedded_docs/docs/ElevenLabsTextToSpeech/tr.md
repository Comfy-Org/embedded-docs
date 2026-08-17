# ElevenLabs Metinden Konuşmaya

ElevenLabs Text to Speech düğümü, ElevenLabs API'sini kullanarak yazılı metni konuşmaya dönüştürür. Belirli bir ses seçmenize ve stabilite, hız ve stil gibi çeşitli konuşma özelliklerini ince ayarlayarak özelleştirilmiş bir ses çıktısı oluşturmanıza olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `voice` | Konuşma sentezi için kullanılacak ses. Voice Selector veya Instant Voice Clone'dan bağlayın. | CUSTOM | Evet | N/A |
| `text` | Sese dönüştürülecek metin. | STRING | Evet | N/A |
| `stability` | Ses stabilitesi. Düşük değerler daha geniş duygusal aralık sağlar, yüksek değerler daha tutarlı ancak potansiyel olarak monoton konuşma üretir (varsayılan: 0.5). | FLOAT | Hayır | 0.0 - 1.0 |
| `apply_text_normalization` | Metin normalizasyon modu. 'auto' sistemin karar vermesini sağlar, 'on' her zaman normalizasyon uygular, 'off' atlar. | COMBO | Hayır | `"auto"`<br>`"on"`<br>`"off"` |
| `model` | Metinden konuşma sentezi için kullanılacak model. Bir model seçmek, o modele özgü parametreleri ortaya çıkarır. | DYNAMIC_COMBO | Hayır | `"eleven_multilingual_v2"`<br>`"eleven_v3"` |
| `language_code` | ISO-639-1 veya ISO-639-3 dil kodu (ör. 'en', 'es', 'fra'). Otomatik algılama için boş bırakın (varsayılan: ""). | STRING | Hayır | N/A |
| `seed` | Tekrarlanabilirlik için tohum değeri (determinizm garanti edilmez) (varsayılan: 1). | INT | Hayır | 0 - 2147483647 |
| `output_format` | Ses çıktı formatı. | COMBO | Hayır | `"mp3_44100_192"`<br>`"opus_48000_192"` |

**Modele Özgü Parametreler:**

`model` parametresi `"eleven_multilingual_v2"` olarak ayarlandığında aşağıdaki ek parametreler kullanılabilir hale gelir:

- `speed`: Konuşma hızı. 1.0 normaldir, <1.0 daha yavaş, >1.0 daha hızlı (varsayılan: 1.0, aralık: 0.7 - 1.3).
- `similarity_boost`: Benzerlik artırma. Daha yüksek değerler sesi orijinale daha benzer hale getirir (varsayılan: 0.75, aralık: 0.0 - 1.0).
- `use_speaker_boost`: Orijinal konuşmacı sesine benzerliği artırır (varsayılan: False).
- `style`: Stil abartması. Daha yüksek değerler stilistik ifadeyi artırır ancak stabiliteyi azaltabilir (varsayılan: 0.0, aralık: 0.0 - 0.2).

`model` parametresi `"eleven_v3"` olarak ayarlandığında aşağıdaki ek parametreler kullanılabilir hale gelir:

- `speed`: Konuşma hızı. 1.0 normaldir, <1.0 daha yavaş, >1.0 daha hızlı (varsayılan: 1.0, aralık: 0.7 - 1.3).
- `similarity_boost`: Benzerlik artırma. Daha yüksek değerler sesi orijinale daha benzer hale getirir (varsayılan: 0.75, aralık: 0.0 - 1.0).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Metinden konuşmaya dönüştürme işlemiyle üretilen ses. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/tr.md)

---
**Source fingerprint (SHA-256):** `78ed1c6af2d0b1cc0293d725492a8b104b6d0c6bc18d9971b75047db946cdd33`
