> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/tr.md)

ElevenLabs Speech to Speech düğümü, bir giriş ses dosyasını bir sesten diğerine dönüştürür. Orijinal sesin içeriğini ve duygusal tonunu koruyarak konuşmayı dönüştürmek için ElevenLabs API'sini kullanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `voice` | CUSTOM | Evet | - | Dönüşüm için hedef ses. Voice Selector veya Instant Voice Clone'dan bağlayın. |
| `audio` | AUDIO | Evet | - | Dönüştürülecek kaynak ses. |
| `stability` | FLOAT | Hayır | 0.0 - 1.0 | Ses kararlılığı. Düşük değerler daha geniş bir duygusal aralık sağlar, yüksek değerler daha tutarlı ancak potansiyel olarak monoton bir konuşma üretir (varsayılan: 0.5). |
| `model` | DYNAMICCOMBO | Hayır | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` | Konuşmadan-konuşmaya dönüşüm için kullanılacak model. Her seçenek belirli bir ses ayarları kümesi sağlar (similarity_boost, style, use_speaker_boost, speed). |
| `output_format` | COMBO | Hayır | `"mp3_44100_192"`<br>`"opus_48000_192"` | Ses çıkış formatı (varsayılan: "mp3_44100_192"). |
| `seed` | INT | Hayır | 0 - 4294967295 | Tekrarlanabilirlik için tohum değeri (varsayılan: 0). |
| `remove_background_noise` | BOOLEAN | Hayır | - | Giriş sesinden ses izolasyonu kullanarak arka plan gürültüsünü kaldırır (varsayılan: False). |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `audio` | AUDIO | Belirtilen çıkış formatındaki dönüştürülmüş ses dosyası. |