# WAN Bağlam Pencereleri (Manuel)

WAN Bağlam Pencereleri (Manuel) düğümü, Wan tarzı video modelleri için bağlam pencerelerini manuel olarak yapılandırmanızı sağlar. Bu ayarları örnekleme sırasında uygulayarak, model videoyu işlerken kullanılan pencere uzunluğu, örtüşme, zamanlama ve birleştirme yöntemi üzerinde size kontrol verir. Bağlam uzunluğu ve örtüşme, gerçek kare cinsinden belirtilir ve modelin 2D işlemesi için dahili olarak dönüştürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Örnekleme sırasında bağlam pencerelerinin uygulanacağı model. | MODEL | Evet | - |
| `bağlam_uzunluğu` | Bağlam penceresinin gerçek kare cinsinden uzunluğu. 4*n + 1 biçiminde olmalıdır (varsayılan: 81). | INT | Evet | 1 ile 16384 (MAX_RESOLUTION), step 4 |
| `bağlam_örtüşmesi` | Bağlam penceresinin gerçek kare cinsinden örtüşme miktarı (varsayılan: 30). | INT | Evet | 0 or higher |
| `bağlam_çizelgesi` | Bağlam pencereleri için adıma bağlı zamanlama algoritması (varsayılan: "uniform_standard"). | COMBO | Evet | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `bağlam_adımı` | Bağlam penceresinin adım aralığı (stride); yalnızca uniform zamanlamalar için geçerlidir (varsayılan: 1). | INT | Evet | 1 or higher |
| `kapalı_döngü` | Bağlam penceresi döngüsünün kapatılıp kapatılmayacağı; yalnızca döngülü zamanlamalar için geçerlidir (varsayılan: False). | BOOLEAN | Evet | - |
| `birleştirme_yöntemi` | Bağlam pencerelerini birleştirmek için kullanılacak yöntem (varsayılan: "pyramid"). | COMBO | Evet | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` |
| `freenoise` | FreeNoise gürültü karıştırma işleminin uygulanıp uygulanmayacağı; pencere harmanlamasını iyileştirir (varsayılan: True). | BOOLEAN | Evet | - |
| `retain_first_frame` | Her bağlam penceresinde ilk I2V karesinin korunup korunmayacağı (ilk referansın korunmasına yardımcı olabilir) (varsayılan: False). | BOOLEAN | Evet | - |
| `split_conds_to_windows` | Birden fazla conditioning'in (ConditionCombine tarafından oluşturulan) bölge dizinine göre her pencereye bölünüp bölünmeyeceği (varsayılan: False). | BOOLEAN | Evet | - |

**Not:** `context_stride` yalnızca uniform zamanlamaları etkiler ve `closed_loop` yalnızca döngülü zamanlamalar için geçerlidir. Bağlam uzunluğu ve örtüşme gerçek kare cinsinden belirtilir ve işleme sırasında otomatik olarak dönüştürülür ve minimum geçerli değerlere kırpılır (`context_length`, ((length - 1) / 4) + 1 değerine, `context_overlap` ise overlap / 4 değerine dönüştürülür). `context_length`, 4*n + 1 biçiminde olmalıdır. `retain_first_frame`, görüntüden videoya (image-to-video) kullanım için tasarlanmıştır. `split_conds_to_windows`, ConditionCombine düğümü tarafından oluşturulan birden fazla conditioning bekler. `fuse_method` parametresi, yalnızca "pyramid" dışında birden fazla seçenek içerir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Bağlam penceresi yapılandırması uygulanmış model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/tr.md)

---
**Source fingerprint (SHA-256):** `cf4927371e9d4b509f2e6e5319cd6109e3ef36da6b3faee278bcf8c906672857`
