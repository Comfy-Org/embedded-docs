# LoopIteration

Bu düğüm, döngü tarzı iş akışları için yineleme meta verileri sağlar. Liste tabanlı girdiler alır ve her listenin ilk öğesini geçirir; böylece bir döngü geçerli dizini, ilk veya son adım olup olmadığını, geçerli liste öğesini ve varsa çalışan yineleme değerini izleyebilir. Önbellek davranışı `reuse_cache` bayrağıyla denetlenir. Bu düğüm yalnızca geliştiriciye özel olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `iteration_index` | Geçerli yinelemenin dizini; liste olarak sağlanır. İlk öğe çıktıya geçirilir. | INT | Evet | - |
| `is_first` | Geçerli yinelemenin ilk olup olmadığını belirtir; liste olarak sağlanır. İlk öğe çıktıya geçirilir. | BOOLEAN | Evet | - |
| `is_last` | Geçerli yinelemenin son olup olmadığını belirtir; liste olarak sağlanır. İlk öğe çıktıya geçirilir. | BOOLEAN | Evet | - |
| `list_item` | Bu yineleme için listeden alınan öğe. İsteğe bağlıdır; sağlandığında ilk öğe çıktıya geçirilir, aksi takdirde None döndürülür. | ANY | Hayır | - |
| `current_iteration_value` | Geçerli yineleme tarafından taşınan değer. İsteğe bağlıdır; sağlandığında tam değer çıktıya geçirilir, aksi takdirde None döndürülür. | ANY | Hayır | - |
| `reuse_cache` | Sonucun önbellekten yeniden kullanılıp kullanılamayacağını denetler. Etkinleştirildiğinde, düğüm önbelleğe alınmış sonuçların yeniden kullanılabilmesi için kararlı bir parmak izi tutar. Devre dışı bırakıldığında, düğümün her yinelemede yeniden çalışması için eşleşmeyen bir parmak izi üretilir. | BOOLEAN | Evet | - |

Not: Bu düğüm liste girdisi etkindir; yani her girdinin bir liste olarak gelmesi beklenir ve düğüm her listenin yalnızca ilk öğesini çıktılar (`current_iteration_value` hariç; bu, liste olarak geçirilir). Ayrıca burada listelenenlerin ötesinde ek girdiler de kabul eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `iteration_index` | Geçerli yinelemenin dizini. | INT |
| `is_first` | Geçerli yinelemenin ilk olup olmadığı. | BOOLEAN |
| `is_last` | Geçerli yinelemenin son olup olmadığı. | BOOLEAN |
| `list_item` | Bu yineleme için listeden alınan öğe veya öğe sağlanmadığında None. | ANY |
| `current_iteration_value` | Geçerli yineleme tarafından taşınan değer veya değer sağlanmadığında None. Bu çıktı liste olarak döndürülür. | ANY |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopIteration/tr.md)

---
**Source fingerprint (SHA-256):** `c7072f22bd382f567792d2ea7a30312c64d33c213551f8983c25cd7b95adc4fb`
