# MiniMax Music3 Metin Kodlama

MiniMax Music3 Text Encode, metin açıklamalarını ve şarkı sözlerini müzik üretimi için akustik koşullandırma dizisine dönüştürmek üzere bir MiniMax Music3 CLIP modeli kullanır. Düğüm, ortaya çıkan CONDITIONING verisini ve girdi maksimum süresinden hesaplanan saniye cinsinden gerçek ses süresini döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | Metin kodlama ve koşullandırma dizisi oluşturma için kullanılan MiniMax Music3 CLIP modeli. | CLIP | Evet | - |
| `caption` | Üretilecek müziği tanımlayan metin. Çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet | - |
| `şarkı sözleri` | Müziği üretmek için kullanılacak şarkı sözü metni. Çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet | - |
| `tohum` | Üretim süreci için yeniden üretilebilir rastgele tohum. Varsayılan: 0. Üretim sonrası kontrol widget'ı sağlanır. | INT | Evet | 0 ile 18446744073709551615 (0xffffffffffffffff) arası |
| `max_duration` | Saniye cinsinden maksimum süre; model şarkıyı daha erken bitirebilir. Varsayılan: 120.0. | FLOAT | Evet | 0.04 ile modelin maksimum ses süresi (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND) arası, adım 0.04 |
| `cfg_scale` | Sınıflandırıcısız yönlendirme ölçeği. Varsayılan: model sabiti CFG_SCALE. Gelişmiş parametre. | FLOAT | Evet | 0.0 ile 100.0 arası, adım 0.1 (2 ondalık basamağı korur) |
| `top_k` | Akustik token seçimi için kullanılan top-k örnekleme değeri. Varsayılan: model sabiti CFG_TOP_K. Gelişmiş parametre. | INT | Evet | 1 ile modelin sözlük boyutu (C0_VOCAB_SIZE) arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `conditioning` | Sonraki müzik üretimini yönlendirmek için kullanılan, oluşturulmuş akustik koşullandırma dizisi. | CONDITIONING |
| `seconds` | Koşullandırma dizisinin saniye cinsinden gerçek süresi. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxMusic3TextEncode/tr.md)

---
**Source fingerprint (SHA-256):** `c3fbfd189d0358ebf081dd4f9c32be9231a9d0b97fd767401ea4b7955224c25c`
