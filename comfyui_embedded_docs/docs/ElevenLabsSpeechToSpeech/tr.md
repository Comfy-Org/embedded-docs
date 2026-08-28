# ElevenLabs Sesten Sese

ElevenLabs Speech to Speech düğümü, bir giriş ses dosyasını bir sesten başka bir sese dönüştürür. Konuşmayı dönüştürmek için ElevenLabs API'sini kullanır ve sesin orijinal içeriğini ve duygusal tonunu korur.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Konuşmadan konuşmaya dönüşüm için kullanılacak model. Seçilen model, aşağıda listelenen mevcut ses ayarlarını belirler. | DYNAMIC_COMBO | Evet | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` |
| `ses` | Dönüşüm için hedef ses. Voice Selector veya Instant Voice Clone'dan bağlayın. | CUSTOM | Evet | - |
| `ses` | Dönüştürülecek kaynak ses. | AUDIO | Evet | - |
| `kararlılık` | Ses kararlılığı. Daha düşük değerler daha geniş duygusal aralık sağlar, daha yüksek değerler daha tutarlı ancak potansiyel olarak tekdüze konuşma üretir (varsayılan: 0.5). | FLOAT | Evet | 0.0 - 1.0 |
| `çıktı_formatı` | Ses çıktı formatı (varsayılan: "mp3_44100_192"). | COMBO | Evet | `"mp3_44100_192"`<br>`"opus_48000_192"` |
| `tohum` | Tekrarlanabilirlik için seed (varsayılan: 0). | INT | Evet | 0 - 4294967295 |
| `arka_plan_gürültüsünü_kaldır` | Giriş sesindeki arka plan gürültüsünü ses izolasyonu kullanarak kaldırır (varsayılan: False). | BOOLEAN | Evet | - |

### eleven_multilingual_sts_v2 ve eleven_english_sts_v2 Girdileri

Her iki model de aşağıdaki aynı ses ayarlarını sunar.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `speed` | Konuşma hızı. 1.0 normal, <1.0 daha yavaş, >1.0 daha hızlıdır (varsayılan: 1.0). | FLOAT | Evet | 0.7 - 1.3 |
| `similarity_boost` | Benzerlik artırma. Daha yüksek değerler sesi orijinale daha benzer hale getirir (varsayılan: 0.75). | FLOAT | Evet | 0.0 - 1.0 |
| `use_speaker_boost` | Orijinal konuşmacı sesine benzerliği artırır (varsayılan: False). | BOOLEAN | Evet | - |
| `style` | Stil abartması. Daha yüksek değerler stilistik ifadeyi artırır ancak kararlılığı azaltabilir (varsayılan: 0.0). | FLOAT | Evet | 0.0 - 0.2 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Belirtilen çıktı formatında dönüştürülmüş ses dosyası. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/tr.md)

---
**Source fingerprint (SHA-256):** `a3cd602181d134b9ab517bfac092ea30b62ef5a9942a905c0c3e6959b34370ca`
