# ElevenLabs Metinden Ses Efektine

ElevenLabs Metinden Ses Efektleri düğümü, bir metin açıklamasından ses efektleri üretir. İsteminize dayalı ses efektleri oluşturmak için ElevenLabs API'sini kullanır; süreyi, döngü davranışını ve sesin metni ne kadar yakından takip edeceğini kontrol etmenize olanak tanır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Ses efekti üretimi için kullanılacak model. Şu anda yalnızca bir model mevcuttur: `eleven_sfx_v2`. | DYNAMIC_COMBO | Evet | `"eleven_sfx_v2"` |
| `metin` | Oluşturulacak ses efektinin metin açıklaması. (varsayılan: boş) | STRING | Evet | N/A |
| `çıktı_formatı` | Ses çıkış formatı. | COMBO | Evet | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### eleven_sfx_v2 Girdileri

Bu parametreler, `eleven_sfx_v2` modeli seçildiğinde gösterilir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `duration` | Oluşturulan sesin süresi (saniye). (varsayılan: 5.0) | FLOAT | Evet | 0.5 ila 30.0 |
| `loop` | Sorunsuz döngü yapan bir ses efekti oluşturur. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `prompt_influence` | Üretimin istemi ne kadar yakından takip ettiği. Daha yüksek değerler sesin metni daha yakından takip etmesini sağlar. (varsayılan: 0.3) | FLOAT | Evet | 0.0 ila 1.0 |

**Not:** `text` parametresi boş olmamalıdır; ses üretim isteği gönderilmeden önce doğrulanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Oluşturulan ses efekti ses dosyası. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/tr.md)

---
**Source fingerprint (SHA-256):** `218ff617256cea33f310c1bcfc6407c46aaadc59201a0324b0ec64583166ce58`
