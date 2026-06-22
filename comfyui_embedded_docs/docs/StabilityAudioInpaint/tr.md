# Stability AI Ses İç Boyama

Mevcut bir ses örneğinin belirli bölümlerini metin talimatları kullanarak dönüştürür. Bu düğüm, tanımlayıcı istemler sağlayarak sesin belirli bölümlerini değiştirmenize, seçilen kısımları etkili bir şekilde "onararak" veya yeniden oluşturarak sesin geri kalanını korumanıza olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Ses onarımı için kullanılacak yapay zeka modeli. | COMBO | Evet | "stable-audio-2.5" |
| `komut` | Sesin nasıl dönüştürülmesi gerektiğini yönlendiren metin açıklaması (varsayılan: boş). | STRING | Evet |  |
| `ses` | Dönüştürülecek giriş ses dosyası. Ses 6 ila 190 saniye arasında olmalıdır. | AUDIO | Evet |  |
| `süre` | Oluşturulan sesin saniye cinsinden süresini kontrol eder (varsayılan: 190). | INT | Hayır | 1-190 |
| `tohum` | Üretim için kullanılan rastgele tohum değeri (varsayılan: 0). | INT | Hayır | 0-4294967294 |
| `adımlar` | Örnekleme adımlarının sayısını kontrol eder (varsayılan: 8). | INT | Hayır | 4-8 |
| `maske_başlangıç` | Dönüştürülecek ses bölümü için saniye cinsinden başlangıç konumu (varsayılan: 30). | INT | Hayır | 0-190 |
| `maske_bitiş` | Dönüştürülecek ses bölümü için saniye cinsinden bitiş konumu (varsayılan: 190). | INT | Hayır | 0-190 |

**Not:** `mask_end` değeri `mask_start` değerinden büyük olmalıdır. Giriş sesinin süresi 6 ila 190 saniye arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `ses` | Belirtilen bölümün isteme göre değiştirildiği dönüştürülmüş ses çıktısı. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioInpaint/tr.md)

---
**Source fingerprint (SHA-256):** `6589fdbff8387e403055c711a61bb3000d87e5f8cd3753d6e665b723be6f43e2`
