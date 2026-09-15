# StabilityAudioInpaint

Mevcut bir ses örneğinin bir bölümünü metin talimatlarını kullanarak dönüştürür. Bu düğüm, açıklayıcı istemler sağlayarak sesin belirli bölümlerini değiştirmenize olanak tanır; sesin geri kalanını korurken seçili kısımları etkili bir şekilde "inpainting" yapar veya yeniden oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Ses iç boyama için kullanılacak yapay zeka modeli. | STRING | Evet | `"stable-audio-2.5"` |
| `prompt` | Sesin nasıl dönüştürüleceğini yönlendiren metin açıklaması (varsayılan: boş). Maksimum uzunluk 10.000 karakterdir. | STRING | Evet |  |
| `audio` | Dönüştürülecek giriş ses dosyası. Ses 6 ile 190 saniye arasında olmalıdır. | AUDIO | Evet |  |
| `duration` | Üretilen sesin saniye cinsinden süresini kontrol eder (varsayılan: 190). | INT | Hayır | 1 ile 190 |
| `seed` | Üretim için kullanılan rastgele tohum (varsayılan: 0). | INT | Hayır | 0 ile 4294967294 |
| `steps` | Örnekleme adım sayısını kontrol eder (varsayılan: 8). | INT | Hayır | 4 ile 8 |
| `mask_start` | Dönüştürülecek ses bölümü için başlangıç konumu (saniye cinsinden) (varsayılan: 30). | INT | Hayır | 0 ile 190 |
| `mask_end` | Dönüştürülecek ses bölümü için bitiş konumu (saniye cinsinden) (varsayılan: 190). | INT | Hayır | 0 ile 190 |

**Not:** `mask_end` değeri `mask_start` değerinden büyük olmalıdır. Giriş sesi 6 ile 190 saniye arasında bir süreye sahip olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Belirtilen bölümün isteme göre değiştirildiği dönüştürülmüş ses çıktısı. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioInpaint/tr.md)

---
**Source fingerprint (SHA-256):** `3c180043c538311b1808cddd84b0c0ab22a6fa1d943b7f9ddc9edab0fb3413ad`
