# StartLoop

Start Loop düğümü, bir iş akışı içinde döngü yapısı başlatır. Bağlı döngü gövdesini her yineleme için bir kez çalıştırır ve yinelemeleri üç şekilde sayabilir: sabit sayıda tekrar (simple), sayısal bir dizin aralığı (For) veya bir listedeki her öğe için bir geçiş (List). Her geçiş, geçerli dizini, ilk/son bayraklarını ve bir yinelemeden sonrakine aktarılabilen isteğe bağlı taşınan bir değeri sunar.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mode` | Döngü yineleme modu (varsayılan: "simple"). Seçilen mod, hangi ek parametrelerin gösterileceğini belirler. | DYNAMIC_COMBO | Evet | `"simple"`<br>`"For"`<br>`"List"` |
| `cache_iterations` | Önceki yürütmelerden değişmemiş yineleme sonuçlarını yeniden kullanın. Her yinelemeyi yeniden yürütmek için devre dışı bırakın. Varsayılan: false. | BOOLEAN | Hayır | true<br>false |
| `parent_iteration` | Bu döngüyü iç içe yerleştirmek için bir dış Start Loop'tan iteration_index bağlayın. Bu girdi yalnızca zorunlu girdidir (bir bağlantı gereklidir). | INT | Hayır | Herhangi bir tam sayı |
| `initial_iteration_value` | İlk yinelemede current_iteration_value olarak sunulan değer. | ANY (type-matched) | Hayır | Herhangi bir değer |

### Simple Modu Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `num_iterations` | Döngü gövdesinin kaç kez yürütüleceği. Varsayılan: 4. | INT | Evet | En az 0 |

### For Modu Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `start_iteration_index` | For döngü modu kullanılırken ilk yinelemenin dizini. Varsayılan: 0. | INT | Evet | Herhangi bir tam sayı |
| `max_iteration` | For modunda iteration_index için hariç tutulan durdurma değeri. Varsayılan: 4. | INT | Evet | Maksimum 0xffffffffffffffff |
| `step` | For döngü modu kullanılırken her yineleme arasındaki dizin adım boyutu. Varsayılan: 1. | INT | Evet | En az 1 |

### List Modu Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `list` | Döngünün üzerinde yinelediği öğelerin listesi. Döngü gövdesi her öğe için bir kez yürütülür. | ANY (type-matched list item) | Evet | Herhangi bir liste |

Notlar:

- Yalnızca seçili `mode` değerine ait parametreler gösterilir ve kullanılır.
- Simple modunda, yineleme dizinleri 0'dan `num_iterations` eksi 1'e kadar ilerler. For modunda, dizinler `start_iteration_index` değerinden (`max_iteration` dahil olmamak üzere) `max_iteration` değerine kadar `step` kadar artarak ilerler. List modunda, `list` içindeki her öğe için bir yineleme çalışır.
- `step` 0 olmamalıdır; 0 değeri hata verir. 1'in altındaki değerlere izin verilmez.
- Hesaplanan yineleme sayısı sıfırsa, `is_last` çıktısı true olarak bildirilir ve döngü gövdesi çalışmaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `iteration_index` | Geçerli döngü yinelemesinin dizini. | INT |
| `is_first` | Döngünün ilk yinelemesi sırasında true. | BOOLEAN |
| `is_last` | Döngünün son yinelemesi sırasında true. | BOOLEAN |
| `list_item` | List modu kullanılırken listedeki geçerli öğe. Simple ve For modlarında None. | ANY (type-matched) |
| `current_iteration_value` | Geçerli yineleme için döngü tarafından taşınan değer: ilk yinelemede initial_iteration_value, sonraki her yinelemede End Loop'tan next_iteration_value. | ANY (type-matched) |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StartLoop/tr.md)

---
**Source fingerprint (SHA-256):** `2584af9fd623f4762f440a043679e47aeef25ad0d571cfac11506cb513dd1b98`
