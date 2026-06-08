# Bağlam Pencereleri (Manuel) Düğümü

Bağlam Pencereleri (Manuel) düğümü, örnekleme sırasında modeller için bağlam pencerelerini manuel olarak yapılandırmanıza olanak tanır. Belirtilen uzunluk, örtüşme ve zamanlama desenlerine sahip örtüşen bağlam segmentleri oluşturarak, segmentler arasında sürekliliği korurken verileri yönetilebilir parçalar halinde işler. Bu düğüm, gürültü karıştırma, koşullandırma saklama ve nedensel pencere düzeltmeleri dahil olmak üzere bağlam pencerelerinin nasıl uygulanacağını kontrol etmek için gelişmiş seçenekler sunar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Örnekleme sırasında bağlam pencerelerinin uygulanacağı model. | MODEL | Evet | - |
| `bağlam uzunluğu` | Bağlam penceresinin uzunluğu (varsayılan: 16). | INT | Hayır | 1+ |
| `bağlam örtüşmesi` | Bağlam penceresinin örtüşme miktarı (varsayılan: 4). | INT | Hayır | 0+ |
| `bağlam çizelgesi` | Bağlam penceresinin adım aralığı. | COMBO | Hayır | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` |
| `bağlam adımı` | Bağlam penceresinin adım aralığı; yalnızca tekdüze zamanlamalar için geçerlidir (varsayılan: 1). | INT | Hayır | 1+ |
| `kapalı döngü` | Bağlam penceresi döngüsünün kapatılıp kapatılmayacağı; yalnızca döngülü zamanlamalar için geçerlidir (varsayılan: False). | BOOLEAN | Hayır | - |
| `birleştirme yöntemi` | Bağlam pencerelerini birleştirmek için kullanılacak yöntem (varsayılan: PYRAMID). | COMBO | Hayır | `PYRAMID`<br>`LIST_STATIC` |
| `boyut` | Bağlam pencerelerinin uygulanacağı boyut (varsayılan: 0). | INT | Hayır | 0-5 |
| `serbest_gürültü` | FreeNoise gürültü karıştırmanın uygulanıp uygulanmayacağı, pencere harmanlamasını iyileştirir (varsayılan: False). | BOOLEAN | Hayır | - |
| `cond_retain_index_list` | Her pencere için koşullandırma tensörlerinde saklanacak gizli indekslerin listesi; örneğin, bunu '0' olarak ayarlamak her pencere için başlangıç görüntüsünü kullanır (varsayılan: ""). | STRING | Hayır | - |
| `split_conds_to_windows` | ConditionCombine tarafından oluşturulan birden çok koşullandırmanın, bölge indeksine göre her pencereye bölünüp bölünmeyeceği (varsayılan: False). | BOOLEAN | Hayır | - |
| `causal_window_fix` | 0 indeksli olmayan bağlam pencerelerine nedensel düzeltme çerçevesi eklenip eklenmeyeceği (varsayılan: True). | BOOLEAN | Hayır | - |

**Parametre Kısıtlamaları:**

- `context_stride` yalnızca tekdüze zamanlamalar seçildiğinde kullanılır
- `closed_loop` yalnızca döngülü zamanlamalar için geçerlidir
- `dim` 0 ile 5 arasında olmalıdır (dahil)
- `cond_retain_index_list` virgülle ayrılmış tamsayı indekslerinden oluşan bir dize bekler (örneğin, "0,1,2")

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Örnekleme sırasında bağlam pencereleri uygulanmış model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/tr.md)

---
**Source fingerprint (SHA-256):** `b05ddda0ba38588305e6f733cd218c8b462268c39d16226ca961d09054187261`
