# MiniMaxMusic3TextEncode

MiniMax Music3 Text Encode, MiniMax Music3 CLIP modelini kullanarak metin açıklamalarını ve şarkı sözlerini, müzik oluşturmak için kullanılan akustik koşul dizilerine dönüştürür. Bu düğüm, dönüştürülmüş CONDITIONING verilerini ve girdi süresine göre hesaplanan gerçek ses saniyelerini döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | MiniMax Music3 CLIP modeli; metin kodlama ve koşul dizisi üretimi için kullanılır. | CLIP | Evet | - |
| `caption` | Oluşturulacak müziği tanımlayan metin içeriği. Çok satırlı metin ve dinamik promptları destekler. | STRING | Evet | - |
| `lyrics` | Müzik oluşturmak için kullanılacak şarkı sözü metni. Çok satırlı metin ve dinamik promptları destekler. | STRING | Evet | - |
| `seed` | Üretim süreci için tekrarlanabilir rastgele tohum değeri. Varsayılan değer: 0. | INT | Evet | 0 ile 18446744073709551615 (0xffffffffffffffff) arası |
| `max_duration` | Oluşturulacak müziğin maksimum süresi (saniye). Model, şarkıyı erken sonlandırabilir. Varsayılan değer: 120.0. | FLOAT | Evet | 0.04 ile modelin maksimum ses süresi (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND) arası, adım 0.04 |
| `cfg_scale` | Sınıflandırıcısız rehberlik ölçek katsayısı. Varsayılan değer: model sabiti CFG_SCALE. Gelişmiş parametre. | FLOAT | Evet | 0.0 ile 100.0 arası, adım 0.1 (2 ondalık basamak korunur) |
| `top_k` | Akustik token seçimi için top-k örnekleme değeri. Varsayılan değer: model sabiti CFG_TOP_K. Gelişmiş parametre. | INT | Evet | 1 ile model sözlük boyutu (C0_VOCAB_SIZE) arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `conditioning` | Sonraki müzik üretimini yönlendirmek için kullanılan, üretilmiş akustik koşul dizisi. | CONDITIONING |
| `seconds` | Koşul dizisine karşılık gelen gerçek süre, saniye cinsinden. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxMusic3TextEncode/tr.md)

---
**Source fingerprint (SHA-256):** `c3fbfd189d0358ebf081dd4f9c32be9231a9d0b97fd767401ea4b7955224c25c`
