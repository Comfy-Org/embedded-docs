> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/tr.md)

# Bağlam Pencereleri (Manuel) Düğümü

Bağlam Pencereleri (Manuel) düğümü, örnekleme sırasında modeller için bağlam pencerelerini manuel olarak yapılandırmanıza olanak tanır. Belirtilen uzunluk, örtüşme ve zamanlama desenlerine sahip örtüşen bağlam segmentleri oluşturarak, segmentler arasında sürekliliği korurken verileri yönetilebilir parçalar halinde işler. Bu düğüm, gürültü karıştırma, koşullandırma saklama ve nedensel pencere düzeltmeleri dahil olmak üzere bağlam pencerelerinin nasıl uygulanacağını kontrol etmek için gelişmiş seçenekler sunar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Örnekleme sırasında bağlam pencerelerinin uygulanacağı model. |
| `bağlam uzunluğu` | INT | Hayır | 1+ | Bağlam penceresinin uzunluğu (varsayılan: 16). |
| `bağlam örtüşmesi` | INT | Hayır | 0+ | Bağlam penceresinin örtüşme miktarı (varsayılan: 4). |
| `bağlam çizelgesi` | COMBO | Hayır | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` | Bağlam penceresinin adım aralığı. |
| `bağlam adımı` | INT | Hayır | 1+ | Bağlam penceresinin adım aralığı; yalnızca tekdüze zamanlamalar için geçerlidir (varsayılan: 1). |
| `kapalı döngü` | BOOLEAN | Hayır | - | Bağlam penceresi döngüsünün kapatılıp kapatılmayacağı; yalnızca döngülü zamanlamalar için geçerlidir (varsayılan: False). |
| `birleştirme yöntemi` | COMBO | Hayır | `PYRAMID`<br>`LIST_STATIC` | Bağlam pencerelerini birleştirmek için kullanılacak yöntem (varsayılan: PYRAMID). |
| `boyut` | INT | Hayır | 0-5 | Bağlam pencerelerinin uygulanacağı boyut (varsayılan: 0). |
| `serbest_gürültü` | BOOLEAN | Hayır | - | FreeNoise gürültü karıştırmanın uygulanıp uygulanmayacağı, pencere harmanlamasını iyileştirir (varsayılan: False). |
| `cond_retain_index_list` | STRING | Hayır | - | Her pencere için koşullandırma tensörlerinde saklanacak gizli indekslerin listesi; örneğin, bunu '0' olarak ayarlamak her pencere için başlangıç görüntüsünü kullanır (varsayılan: ""). |
| `split_conds_to_windows` | BOOLEAN | Hayır | - | ConditionCombine tarafından oluşturulan birden çok koşullandırmanın, bölge indeksine göre her pencereye bölünüp bölünmeyeceği (varsayılan: False). |
| `causal_window_fix` | BOOLEAN | Hayır | - | 0 indeksli olmayan bağlam pencerelerine nedensel düzeltme çerçevesi eklenip eklenmeyeceği (varsayılan: True). |

**Parametre Kısıtlamaları:**

- `context_stride` yalnızca tekdüze zamanlamalar seçildiğinde kullanılır
- `closed_loop` yalnızca döngülü zamanlamalar için geçerlidir
- `dim` 0 ile 5 arasında olmalıdır (dahil)
- `cond_retain_index_list` virgülle ayrılmış tamsayı indekslerinden oluşan bir dize bekler (örneğin, "0,1,2")

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Örnekleme sırasında bağlam pencereleri uygulanmış model. |

---
**Source fingerprint (SHA-256):** `b05ddda0ba38588305e6f733cd218c8b462268c39d16226ca961d09054187261`
