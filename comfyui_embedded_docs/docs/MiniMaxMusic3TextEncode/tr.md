# MiniMaxMusic3TextEncode

MiniMax Music3 Text Encode, metin açıklamalarını ve şarkı sözlerini müzik üretimi için akustik koşullandırma dizisine dönüştürmek üzere bir MiniMax Music3 CLIP modeli kullanır. Düğüm, sonuçta ortaya çıkan CONDITIONING verilerini ve girdi maksimum süresinden hesaplanan gerçek ses süresini (saniye cinsinden) döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | MiniMax Music3 CLIP modeli, metin kodlama ve koşullandırma dizisi oluşturma için kullanılır. | CLIP | Evet | - |
| `caption` | Müzik üretimini tanımlayan metin. Çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet | - |
| `şarkı sözleri` | Müzik üretiminde kullanılacak şarkı sözü metni. Çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet | - |
| `tohum` | Üretim süreci için tekrarlanabilir rastgele tohum. Varsayılan: 0. | INT | Evet | 0 ile 18446744073709551615 (0xffffffffffffffff) |
| `max_duration` | Saniye cinsinden maksimum süre; model şarkıyı daha erken bitirebilir. Varsayılan: 120.0. | FLOAT | Evet | 0.04 to the model's maximum audio duration (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), step 0.04 |
| `cfg_scale` | Sınıflandırıcısız rehberlik ölçeği. Varsayılan: model sabiti CFG_SCALE. Gelişmiş parametre. | FLOAT | Evet | 0.0 ile 100.0, step 0.1 (keeps 2 decimal places) |
| `top_k` | Akustik token seçimi için kullanılan top-k örnekleme değeri. Varsayılan: model sabiti CFG_TOP_K. Gelişmiş parametre. | INT | Evet | 1 to the model's vocabulary size (C0_VOCAB_SIZE) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `conditioning` | Üretilen akustik koşullandırma dizisi, sonraki müzik üretimini yönlendirmek için kullanılır. | CONDITIONING |
| `saniye` | Koşullandırma dizisinin gerçek süresi, saniye cinsinden. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxMusic3TextEncode/tr.md)

---
**Source fingerprint (SHA-256):** `c3fbfd189d0358ebf081dd4f9c32be9231a9d0b97fd767401ea4b7955224c25c`
