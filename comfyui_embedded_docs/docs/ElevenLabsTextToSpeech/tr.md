# ElevenLabs Metinden Konuşmaya

ElevenLabs Text to Speech düğümü, yazılı metni ElevenLabs API'sini kullanarak sesli konuşmaya dönüştürür. Belirli bir ses seçmenize ve kararlılık, hız ve stil gibi çeşitli konuşma özelliklerini ince ayarlamanıza olanak tanır. Metin en az bir karakter içermelidir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Metinden konuşmaya dönüştürme için kullanılacak model. Bir model seçildiğinde, o modele özgü parametreler görünür. | DYNAMIC_COMBO | Hayır | `"eleven_multilingual_v2"`<br>`"eleven_v3"` |
| `ses` | Konuşma sentezi için kullanılacak ses. Voice Selector veya Instant Voice Clone'dan bağlayın. | CUSTOM | Evet | N/A |
| `metin` | Konuşmaya dönüştürülecek metin. En az bir karakter içermelidir. | STRING | Evet | N/A |
| `kararlılık` | Ses kararlılığı. Düşük değerler daha geniş duygusal aralık sağlar, yüksek değerler daha tutarlı ancak potansiyel olarak monoton konuşma üretir (varsayılan: 0.5). | FLOAT | Hayır | 0.0 - 1.0 |
| `metin normalizasyonunu uygula` | Metin normalleştirme modu. 'auto' sistemin karar vermesini sağlar, 'on' normalleştirmeyi her zaman uygular, 'off' ise atlar. | COMBO | Hayır | `"auto"`<br>`"on"`<br>`"off"` |
| `dil_kodu` | ISO-639-1 veya ISO-639-3 dil kodu (örn. 'en', 'es', 'fra'). Otomatik algılama için boş bırakın (varsayılan: ""). | STRING | Hayır | N/A |
| `tohum` | Yeniden üretilebilirlik için tohum (determinizm garanti edilmez) (varsayılan: 1). | INT | Hayır | 0 - 2147483647 |
| `çıktı_formatı` | Ses çıktısı biçimi. | COMBO | Hayır | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### eleven_multilingual_v2 Girdileri

Bu parametreler `model` `"eleven_multilingual_v2"` olarak ayarlandığında kullanılabilir hale gelir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `speed` | Konuşma hızı. 1.0 normaldir, <1.0 daha yavaş, >1.0 daha hızlıdır (varsayılan: 1.0). | FLOAT | Hayır | 0.7 - 1.3 |
| `similarity_boost` | Benzerlik artırımı. Yüksek değerler sesi orijinaline daha benzer hale getirir (varsayılan: 0.75). | FLOAT | Hayır | 0.0 - 1.0 |
| `use_speaker_boost` | Orijinal konuşmacı sesine benzerliği artırın (varsayılan: False). | BOOLEAN | Hayır | True / False |
| `style` | Stil abartısı. Yüksek değerler biçemsel ifadeyi artırır ancak kararlılığı azaltabilir (varsayılan: 0.0). | FLOAT | Hayır | 0.0 - 0.2 |

### eleven_v3 Girdileri

Bu parametreler `model` `"eleven_v3"` olarak ayarlandığında kullanılabilir hale gelir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `speed` | Konuşma hızı. 1.0 normaldir, <1.0 daha yavaş, >1.0 daha hızlıdır (varsayılan: 1.0). | FLOAT | Hayır | 0.7 - 1.3 |
| `similarity_boost` | Benzerlik artırımı. Yüksek değerler sesi orijinaline daha benzer hale getirir (varsayılan: 0.75). | FLOAT | Hayır | 0.0 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Metinden konuşmaya dönüştürme işleminden üretilen ses. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/tr.md)

---
**Source fingerprint (SHA-256):** `78ed1c6af2d0b1cc0293d725492a8b104b6d0c6bc18d9971b75047db946cdd33`
