# LTXV Bağlam Pencereleri

Bu düğüm, örnekleme sırasında LTXV benzeri modeller için bağlam pencerelerini ayarlar. Üretimi, bellek kullanımını yönetmeye yardımcı olmak ve zamansal tutarlılığı iyileştirmek için örtüşen pencerelere böler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Örnekleme sırasında bağlam pencerelerinin uygulanacağı model. | MODEL | Evet | - |
| `context_length` | Bağlam penceresinin gerçek kare cinsinden uzunluğu. 8*n + 1 olmalıdır. (varsayılan: 145) | INT | Evet | Minimum: 1<br>Maksimum: nodes.MAX_RESOLUTION<br>Adım: 8 |
| `context_overlap` | Bağlam penceresinin gerçek kare cinsinden örtüşmesi. (varsayılan: 40) | INT | Evet | Minimum: 0<br>Adım: 8 |
| `context_schedule` | Bağlam pencereleri için adıma bağlı zamanlama algoritması. (varsayılan: "UNIFORM_STANDARD") | COMBO | Evet | `"STATIC_STANDARD"`<br>`"UNIFORM_STANDARD"`<br>`"UNIFORM_LOOPED"`<br>`"BATCHED"` |
| `context_stride` | Bağlam penceresinin adım aralığı; yalnızca tekdüze zamanlamalar için geçerlidir. (varsayılan: 1) | INT | Evet | Minimum: 1 |
| `closed_loop` | Bağlam penceresi döngüsünün kapatılıp kapatılmayacağı; yalnızca döngülü zamanlamalar için geçerlidir. (varsayılan: False) | BOOLEAN | Evet | True<br>False |
| `fuse_method` | Bağlam pencerelerini birleştirmek için kullanılacak yöntem. Kullanılabilir seçenekler `ContextFuseMethods.LIST_STATIC` tarafından tanımlanır. (varsayılan: "PYRAMID") | COMBO | Evet | `ContextFuseMethods.LIST_STATIC` tarafından tanımlanır |
| `freenoise` | FreeNoise gürültü karıştırmasının uygulanıp uygulanmayacağı; pencere harmanlamayı iyileştirir. (varsayılan: True) | BOOLEAN | Evet | True<br>False |
| `retain_first_frame` | Her bağlam penceresinde ilk latent kareyi korur (başlangıç referansını korumaya yardımcı olabilir). (varsayılan: False) | BOOLEAN | Evet | True<br>False |
| `split_conds_to_windows` | Bölge indeksine göre her pencereye birden çok koşullandırmanın (ConditionCombine tarafından oluşturulan) bölünüp bölünmeyeceği. (varsayılan: False) | BOOLEAN | Evet | True<br>False |

**Not:** `context_length` değeri gerçek kare cinsinden verilir ve dahili olarak `((context_length - 1) // 8) + 1` formülü kullanılarak latent karelere dönüştürülür; minimum değeri 1'dir. `context_overlap` değeri de gerçek kare cinsinden verilir ve 8'e tam sayı bölmesi kullanılarak latent karelere dönüştürülür; minimum değeri 0'dır. `context_length` için araç ipucu, 8*n + 1 desenini izlemesi gerektiğini belirtir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `MODEL` | Örnekleme için bağlam pencereleri uygulanmış model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVContextWindows/tr.md)

---
**Source fingerprint (SHA-256):** `148649d0a938e08c932a163f5d7614332626fba37b8f79db7f92bbcf422e692f`
