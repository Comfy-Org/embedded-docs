# ElevenLabs Sesten Sese

ElevenLabs Speech to Speech düğümü, girdi ses dosyasını bir sesten başka bir sese dönüştürür. Sesin orijinal içeriğini ve duygusal tonunu koruyarak konuşmayı dönüştürmek için ElevenLabs API'sini kullanır.

## Girişler

### Ortak Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Konuşmadan konuşmaya dönüşüm için kullanılacak model. Her model seçeneği, eşleşen bir ses ayarları kümesi sağlar (similarity_boost, style, use_speaker_boost, speed). | DYNAMIC_COMBO | Hayır | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` |
| `voice` | Dönüşüm için hedef ses. Voice Selector veya Instant Voice Clone'dan bağlayın. | CUSTOM | Evet | - |
| `audio` | Dönüştürülecek kaynak ses. | AUDIO | Evet | - |
| `stability` | Ses stabilitesi. Düşük değerler daha geniş duygusal yelpaze sağlar, yüksek değerler daha tutarlı ancak potansiyel olarak tekdüze konuşma üretir (varsayılan: 0.5). | FLOAT | Hayır | 0.0 - 1.0 |
| `output_format` | Ses çıktı biçimi (varsayılan: "mp3_44100_192"). | COMBO | Hayır | `"mp3_44100_192"`<br>`"opus_48000_192"` |
| `seed` | Tekrarlanabilirlik için seed değeri (varsayılan: 0). | INT | Hayır | 0 - 4294967295 |
| `remove_background_noise` | Ses izolasyonu kullanarak girdi sesinden arka plan gürültüsünü kaldırır (varsayılan: False). | BOOLEAN | Hayır | - |

### Ses Ayarları (`eleven_multilingual_sts_v2` ve `eleven_english_sts_v2` tarafından paylaşılır)

Bir model seçildiğinde, bu ses ayarları dönüşüm için kullanılabilir hale gelir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `speed` | Konuşma hızı. 1.0 normal, <1.0 daha yavaş, >1.0 daha hızlı (varsayılan: 1.0). | FLOAT | Hayır | 0.7 - 1.3 |
| `similarity_boost` | Benzerlik artırma. Yüksek değerler sesi orijinale daha benzer hale getirir (varsayılan: 0.75). | FLOAT | Hayır | 0.0 - 1.0 |
| `use_speaker_boost` | Orijinal konuşmacı sesine benzerliği artırır (varsayılan: False). | BOOLEAN | Hayır | - |
| `style` | Stil abartısı. Yüksek değerler stilistik ifadeyi artırır ancak stabiliteyi azaltabilir (varsayılan: 0.0). | FLOAT | Hayır | 0.0 - 0.2 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Belirtilen çıktı biçiminde dönüştürülmüş ses dosyası. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/tr.md)

---
**Source fingerprint (SHA-256):** `a3cd602181d134b9ab517bfac092ea30b62ef5a9942a905c0c3e6959b34370ca`
