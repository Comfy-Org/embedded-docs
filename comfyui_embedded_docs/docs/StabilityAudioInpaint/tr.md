> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioInpaint/tr.md)

Mevcut bir ses örneğinin bir bölümünü metin talimatları kullanarak dönüştürür. Bu düğüm, açıklayıcı istemler sağlayarak sesin belirli bölümlerini değiştirmenize, sesin geri kalanını korurken seçilen kısımları "iç boyama" veya yeniden oluşturma yoluyla etkili bir şekilde değiştirmenize olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | "stable-audio-2.5"<br> | Ses iç boyama için kullanılacak AI modeli. |
| `prompt` | STRING | Evet |  | Sesin nasıl dönüştürüleceğine rehberlik eden metin açıklaması (varsayılan: boş). |
| `audio` | AUDIO | Evet |  | Dönüştürülecek girdi ses dosyası. Ses 6 ile 190 saniye arasında olmalıdır. |
| `duration` | INT | Hayır | 1-190 | Oluşturulan sesin saniye cinsinden süresini kontrol eder (varsayılan: 190). |
| `seed` | INT | Hayır | 0-4294967294 | Oluşturma için kullanılan rastgele tohum değeri (varsayılan: 0). |
| `steps` | INT | Hayır | 4-8 | Örnekleme adımlarının sayısını kontrol eder (varsayılan: 8). |
| `mask_start` | INT | Hayır | 0-190 | Dönüştürülecek ses bölümünün saniye cinsinden başlangıç konumu (varsayılan: 30). |
| `mask_end` | INT | Hayır | 0-190 | Dönüştürülecek ses bölümünün saniye cinsinden bitiş konumu (varsayılan: 190). |

**Not:** `mask_end` değeri, `mask_start` değerinden büyük olmalıdır. Girdi sesinin süresi 6 ile 190 saniye arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `audio` | AUDIO | Belirtilen bölümü isteme göre değiştirilmiş olan dönüştürülmüş ses çıktısı. |