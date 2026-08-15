# ElevenLabs Metinden Konuşmaya

ElevenLabs Text to Speech düğümü, ElevenLabs API'sini kullanarak yazılı metni sese dönüştürür. Bir ses seçmenize ve özelleştirilmiş ses çıktısı oluşturmak için stabilite, hız ve stil gibi konuşma özelliklerini ayarlamanıza olanak tanır.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Metinden sese sentez için kullanılacak model. Bir model seçmek, modele özgü parametreleri görüntüler. | DYNAMIC_COMBO | Evet | "eleven_multilingual_v2"<br>"eleven_v3" |
| `ses` | Konuşma sentezi için kullanılacak ses. Voice Selector veya Instant Voice Clone'dan bağlayın. | ELEVENLABS_VOICE | Evet | N/A |
| `metin` | Konuşmaya dönüştürülecek metin. En az bir karakter içermelidir. | STRING | Evet | N/A |
| `kararlılık` | Ses stabilitesi. Düşük değerler daha geniş duygusal aralık sağlar, yüksek değerler daha tutarlı ancak potansiyel olarak tekdüze konuşma üretir (varsayılan: 0.5). | FLOAT | Evet | 0.0 - 1.0 |
| `metin normalizasyonunu uygula` | Metin normalizasyon modu. 'auto' sistemin karar vermesini sağlar, 'on' normalizasyonu her zaman uygular, 'off' atlar. | COMBO | Evet | "auto"<br>"on"<br>"off" |
| `dil_kodu` | ISO-639-1 veya ISO-639-3 dil kodu (örn. 'en', 'es', 'fra'). Otomatik algılama için boş bırakın (varsayılan: ""). | STRING | Evet | N/A |
| `tohum` | Tekrarlanabilirlik için tohum (determinizm garanti edilmez) (varsayılan: 1). | INT | Evet | 0 - 2147483647 |
| `çıktı_formatı` | Ses çıktı biçimi. | COMBO | Evet | "mp3_44100_192"<br>"opus_48000_192" |

### eleven_multilingual_v2 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `speed` | Konuşma hızı. 1.0 normal, <1.0 yavaş, >1.0 hızlı (varsayılan: 1.0). | FLOAT | Evet | 0.7 - 1.3 |
| `similarity_boost` | Benzerlik artırma. Yüksek değerler sesi orijinaline daha benzer hale getirir (varsayılan: 0.75). | FLOAT | Evet | 0.0 - 1.0 |
| `use_speaker_boost` | Orijinal konuşmacı sesine benzerliği artır (varsayılan: False). | BOOLEAN | Evet | True<br>False |
| `style` | Stil abartısı. Yüksek değerler stilistik ifadeyi artırır ancak stabiliteyi azaltabilir (varsayılan: 0.0). | FLOAT | Evet | 0.0 - 0.2 |

### eleven_v3 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `speed` | Konuşma hızı. 1.0 normal, <1.0 yavaş, >1.0 hızlı (varsayılan: 1.0). | FLOAT | Evet | 0.7 - 1.3 |
| `similarity_boost` | Benzerlik artırma. Yüksek değerler sesi orijinaline daha benzer hale getirir (varsayılan: 0.75). | FLOAT | Evet | 0.0 - 1.0 |

**Not:** `metin` girdisi en az bir karakter içermelidir. `dil_kodu` boş bırakılırsa dil otomatik olarak algılanır. `use_speaker_boost` ve `style` parametreleri yalnızca `eleven_multilingual_v2` modeli için kullanılabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Metinden sese dönüştürme sonucu oluşturulan ses. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/tr.md)

---
**Source fingerprint (SHA-256):** `78ed1c6af2d0b1cc0293d725492a8b104b6d0c6bc18d9971b75047db946cdd33`
