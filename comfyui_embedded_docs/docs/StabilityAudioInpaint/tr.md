> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioInpaint/tr.md)

Mevcut bir ses örneğinin belirli bölümlerini metin talimatları kullanarak dönüştürür. Bu düğüm, tanımlayıcı istemler sağlayarak sesin belirli bölümlerini değiştirmenize, seçilen kısımları etkili bir şekilde "onararak" veya yeniden oluşturarak sesin geri kalanını korumanıza olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | COMBO | Evet | "stable-audio-2.5" | Ses onarımı için kullanılacak yapay zeka modeli. |
| `komut` | STRING | Evet |  | Sesin nasıl dönüştürülmesi gerektiğini yönlendiren metin açıklaması (varsayılan: boş). |
| `ses` | AUDIO | Evet |  | Dönüştürülecek giriş ses dosyası. Ses 6 ila 190 saniye arasında olmalıdır. |
| `süre` | INT | Hayır | 1-190 | Oluşturulan sesin saniye cinsinden süresini kontrol eder (varsayılan: 190). |
| `tohum` | INT | Hayır | 0-4294967294 | Üretim için kullanılan rastgele tohum değeri (varsayılan: 0). |
| `adımlar` | INT | Hayır | 4-8 | Örnekleme adımlarının sayısını kontrol eder (varsayılan: 8). |
| `maske_başlangıç` | INT | Hayır | 0-190 | Dönüştürülecek ses bölümü için saniye cinsinden başlangıç konumu (varsayılan: 30). |
| `maske_bitiş` | INT | Hayır | 0-190 | Dönüştürülecek ses bölümü için saniye cinsinden bitiş konumu (varsayılan: 190). |

**Not:** `mask_end` değeri `mask_start` değerinden büyük olmalıdır. Giriş sesinin süresi 6 ila 190 saniye arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `ses` | AUDIO | Belirtilen bölümün isteme göre değiştirildiği dönüştürülmüş ses çıktısı. |

---
**Source fingerprint (SHA-256):** `6589fdbff8387e403055c711a61bb3000d87e5f8cd3753d6e665b723be6f43e2`
