# WAN Bağlam Pencereleri (Manuel)

Wan Context Windows (Manual) düğümü, 2 boyutlu işleme sahip Wan benzeri modeller için bağlam pencerelerini manuel olarak yapılandırmanızı sağlar. Pencere uzunluğunu, örtüşmeyi, zamanlama yöntemini ve birleştirme tekniğini belirterek örnekleme sırasında bağlam penceresi ayarlarını uygular ve modelin farklı bağlam bölgelerini nasıl işleyeceği üzerinde kontrol sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Örnekleme sırasında bağlam pencerelerinin uygulanacağı model. | MODEL | Evet | - |
| `context_length` | Bağlam penceresinin gerçek kare cinsinden uzunluğu. 4*n + 1 olmalıdır. (varsayılan: 81) | INT | Evet | 1 to 16384 (step 4) |
| `context_overlap` | Bağlam penceresinin gerçek kare cinsinden örtüşme miktarı. (varsayılan: 30) | INT | Evet | 0 or greater |
| `context_schedule` | Bağlam pencereleri için adım bağımlı zamanlama algoritması. (varsayılan: "uniform_standard") | COMBO | Evet | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `context_stride` | Bağlam penceresinin adımı; yalnızca tekdüze zamanlamalara uygulanabilir. (varsayılan: 1) | INT | Evet | 1 or greater |
| `closed_loop` | Bağlam penceresi döngüsünün kapatılıp kapatılmayacağı; yalnızca döngülü zamanlamalara uygulanabilir. (varsayılan: False) | BOOLEAN | Evet | True or False |
| `fuse_method` | Bağlam pencerelerini birleştirmek için kullanılacak yöntem. (varsayılan: "pyramid") | COMBO | Evet | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` |
| `freenoise` | FreeNoise gürültü karıştırmanın uygulanıp uygulanmayacağı; pencere harmanlamasını iyileştirir. (varsayılan: True) | BOOLEAN | Evet | True or False |
| `retain_first_frame` | Her bağlam penceresinde ilk I2V karesini korur (başlangıç referansının korunmasına yardımcı olabilir). (varsayılan: False) | BOOLEAN | Evet | True or False |
| `split_conds_to_windows` | Birden fazla conditioning'in (ConditionCombine tarafından oluşturulan) bölge dizinine göre her pencereye bölünüp bölünmeyeceği. (varsayılan: False) | BOOLEAN | Evet | True or False |

**Not:** `context_stride` yalnızca tekdüze zamanlamaları etkiler; `closed_loop` ise yalnızca döngülü zamanlamalara uygulanır. `context_length`, 4n + 1 desenini izlemelidir. Düğüm, `context_length` ve `context_overlap` değerlerini uygulamadan önce gerçek karelerden model birimlerine dönüştürür ve `context_length` için minimum 1, `context_overlap` için minimum 0 zorunlu kılar. `context_stride`, `closed_loop`, `freenoise` ve `split_conds_to_windows` girdileri gelişmiş seçeneklerdir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Bağlam penceresi yapılandırması uygulanmış model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/tr.md)

---
**Source fingerprint (SHA-256):** `cf4927371e9d4b509f2e6e5319cd6109e3ef36da6b3faee278bcf8c906672857`
