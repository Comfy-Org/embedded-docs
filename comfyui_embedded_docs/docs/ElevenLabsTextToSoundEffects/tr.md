# ElevenLabs Metinden Ses Efektine

ElevenLabs Text to Sound Effects düğümü, ElevenLabs API'sini kullanarak bir metin açıklamasından ses efekti sesi üretir. Yazılı isteminizi ElevenLabs ses üretim hizmetine gönderir ve ortaya çıkan sesi; süre, döngü davranışı ve sesin metni ne kadar yakından takip ettiği kontrolleriyle birlikte döndürür.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Ses efekti üretimi için kullanılacak model. Seçilen model, aşağıda listelenen mevcut üretim parametrelerini belirler. | DYNAMIC_COMBO | Evet | `"eleven_sfx_v2"` |
| `metin` | Üretilecek ses efektinin metin açıklaması. En az 1 karakter içermelidir. (varsayılan: boş) | STRING | Evet | N/A |
| `çıktı_formatı` | Ses çıktı biçimi. | COMBO | Evet | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Eleven SFX v2 Girdileri

`model` `"eleven_sfx_v2"` olarak ayarlandığında gösterilen alt parametreler.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `duration` | Üretilen sesin saniye cinsinden süresi. (varsayılan: 5.0) | FLOAT | Evet | 0.5 ile 30.0 (adım: 0.1) |
| `loop` | Sorunsuz döngü yapan bir ses efekti oluşturur. (varsayılan: False) | BOOLEAN | Hayır | True veya False |
| `prompt_influence` | Üretimin istemi ne kadar yakından takip ettiğini belirler. Daha yüksek değerler sesin metni daha yakından takip etmesini sağlar. (varsayılan: 0.3) | FLOAT | Evet | 0.0 ile 1.0 (adım: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Üretilen ses efekti ses dosyası. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/tr.md)

---
**Source fingerprint (SHA-256):** `218ff617256cea33f310c1bcfc6407c46aaadc59201a0324b0ec64583166ce58`
