# LTXVContextWindows

Bu düğüm, örnekleme sırasında LTXV benzeri modeller için bağlam pencereleri ayarlar. Video oluşturma sürecini örtüşen pencerelere bölerek bellek kullanımını yönetir ve zamansal tutarlılığı iyileştirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Örnekleme sırasında bağlam pencerelerinin uygulanacağı model. | MODEL | Evet | - |
| `context_length` | Gerçek kare cinsinden bağlam penceresinin uzunluğu. 8*n + 1 olmalıdır. (varsayılan: 145) | INT | Evet | Minimum: 1<br>Maksimum: nodes.MAX_RESOLUTION<br>Adım: 8 |
| `context_overlap` | Gerçek kare cinsinden bağlam penceresinin örtüşme miktarı. (varsayılan: 40) | INT | Evet | Minimum: 0<br>Adım: 8 |
| `context_schedule` | Bağlam pencereleri için adıma bağlı zamanlama algoritması. (varsayılan: UNIFORM_STANDARD) | COMBO | Evet | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` |
| `context_stride` | Bağlam penceresinin adım uzunluğu; yalnızca tekdüze zamanlamalar için geçerlidir. (varsayılan: 1) | INT | Hayır | Minimum: 1 |
| `closed_loop` | Bağlam penceresi döngüsünün kapatılıp kapatılmayacağı; yalnızca döngülü zamanlamalar için geçerlidir. (varsayılan: Yanlış) | BOOLEAN | Hayır | Doğru<br>Yanlış |
| `fuse_method` | Bağlam pencerelerini birleştirmek için kullanılacak yöntem. (varsayılan: PYRAMID) | COMBO | Evet | comfy.context_windows.ContextFuseMethods.LIST_STATIC seçenekleri |
| `freenoise` | FreeNoise gürültü karıştırmanın uygulanıp uygulanmayacağı, pencere harmanlamasını iyileştirir. (varsayılan: Doğru) | BOOLEAN | Hayır | Doğru<br>Yanlış |
| `retain_first_frame` | Her bağlam penceresinde ilk gizli kareyi korur (başlangıç referansının korunmasına yardımcı olabilir). (varsayılan: Yanlış) | BOOLEAN | Hayır | Doğru<br>Yanlış |
| `split_conds_to_windows` | ConditionCombine tarafından oluşturulan birden fazla koşullandırmanın bölge indeksine göre her pencereye bölünüp bölünmeyeceği. (varsayılan: Yanlış) | BOOLEAN | Hayır | Doğru<br>Yanlış |

**Not:** `context_length` parametresi 8*n + 1 formülüne uymalıdır; burada n pozitif bir tam sayıdır. Düğüm, gerçek kareleri gizli karelere dönüştürerek değeri bu gereksinimi karşılayacak şekilde otomatik olarak ayarlar. `context_overlap` da gerçek karelerden gizli karelere dönüştürülür (8'e bölünür).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `MODEL` | Örnekleme için bağlam pencereleri uygulanmış model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVContextWindows/tr.md)

---
**Source fingerprint (SHA-256):** `ad0b8c54acaab1853f6fe98dbad675478f033caf867df954b40b7db5208f5ae4`
