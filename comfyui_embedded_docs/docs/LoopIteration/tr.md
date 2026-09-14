# LoopIteration

Bu düğüm, döngü tarzı iş akışları için yineleme meta verileri sağlar. Liste tabanlı girdiler alır ve her listenin ilk öğesini geçirir; böylece bir döngü geçerli dizini, ilk ya da son adım olup olmadığını, geçerli liste öğesini ve varsa devam eden yineleme değerini izleyebilir. Önbellek davranışı `reuse_cache` bayrağıyla denetlenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `iteration_index` | Geçerli yinelemenin dizini, liste olarak sağlanır. İlk öğe çıktıya geçirilir. | INT | Evet | - |
| `is_first` | Geçerli yinelemenin ilk olup olmadığını belirtir; liste olarak sağlanır. İlk öğe çıktıya geçirilir. | BOOLEAN | Evet | - |
| `is_last` | Geçerli yinelemenin son olup olmadığını belirtir; liste olarak sağlanır. İlk öğe çıktıya geçirilir. | BOOLEAN | Evet | - |
| `list_item` | Bu yineleme için listeden alınan öğe. İsteğe bağlıdır; sağlandığında ilk öğe çıktıya geçirilir, aksi halde None döndürülür. | ANY | Hayır | - |
| `current_iteration_value` | Geçerli yineleme tarafından taşınan değer. İsteğe bağlıdır; sağlandığında ilk öğe çıktıya geçirilir, aksi halde None döndürülür. | ANY | Hayır | - |
| `reuse_cache` | Sonucun önbellekten yeniden kullanılıp kullanılamayacağını denetler. Etkinleştirildiğinde düğüm kararlı bir parmak izi tutar, böylece önbelleğe alınmış sonuçlar yeniden kullanılabilir. Devre dışı bırakıldığında eşleşmeyen bir parmak izi üretilir, böylece düğüm her yinelemede yeniden çalışır. | BOOLEAN | Evet | - |

Not: Bu düğüm liste girdisi etkindir; yani her girdinin bir liste olarak gelmesi beklenir ve düğüm her listenin yalnızca ilk öğesini çıktılar. Ayrıca burada listelenenlerin ötesinde ek girdileri de kabul eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `iteration_index` | Geçerli yinelemenin dizini. | INT |
| `is_first` | Geçerli yinelemenin ilk olup olmadığı. | BOOLEAN |
| `is_last` | Geçerli yinelemenin son olup olmadığı. | BOOLEAN |
| `list_item` | Bu yineleme için listeden alınan öğe; öğe sağlanmadıysa None. | ANY |
| `current_iteration_value` | Geçerli yineleme tarafından taşınan değer; değer sağlanmadıysa None. | ANY |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopIteration/tr.md)

---
**Source fingerprint (SHA-256):** `1d167860b89de0f7b435a3715f6d543cad7602648abb58575b572c0406631cda`
