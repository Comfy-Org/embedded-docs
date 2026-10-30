# MiniMax H3 Context Windows

Örneklemeyi, bir MiniMax H3 videosunun modelin tek geçişli penceresinden daha uzun olabilmesi için örtüşen bağlam pencerelerine böler. Pencereler modelin 17 karelik parçalarına yerleştirilir; bu, oluşturulan video ve sesin pencere sınırları boyunca hizalı kalmasını sağlar. Döndürülen modeli orijinal modelin yerine örnekleyiciye bağlayın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Örnekleme sırasında bağlam pencerelerinin uygulanacağı model. | MODEL | Evet | - |
| `context_length` | Bağlam penceresinin gerçek kare cinsinden uzunluğu. 17*n + 5 olmalıdır (varsayılan: 124). | INT | Evet | 22 ila 16384 (MAX_RESOLUTION), adım 17 |
| `context_overlap` | Bağlam penceresinin gerçek kare cinsinden örtüşmesi. 17*n + 5 olmalıdır (varsayılan: 39). | INT | Evet | 5 veya daha yüksek, adım 17 |
| `fuse_method` | Bağlam pencerelerini birleştirmek için kullanılan yöntem (varsayılan: `"pyramid"`). | COMBO | Evet | `"pyramid"`<br>`"relative"`<br>`"flat"`<br>`"overlap-linear"` |
| `freenoise` | Pencere harmanlamasını iyileştiren FreeNoise gürültü karıştırmasının uygulanıp uygulanmayacağı (varsayılan: True, gelişmiş parametre). | BOOLEAN | Evet | true<br>false |
| `split_conds_to_windows` | Birden çok koşullandırmanın (ConditionCombine tarafından oluşturulan) bölge indeksine göre her pencereye bölünüp bölünmeyeceği (varsayılan: False, gelişmiş parametre). | BOOLEAN | Evet | true<br>false |

Her iki uzunluk da gerçek kare cinsinden verilir ve örneklemeden önce latentlere dönüştürülür: `context_length`, 5 kare veya daha az olduğunda 2 latent olur, aksi takdirde `((frames - 5) / 17) * 5 + 2` olur. `context_overlap` aynı şekilde dönüştürülür ve ardından `context_length` eksi 5 ile sınırlandırılır, böylece örtüşme her zaman ilerlemek için tam bir parça bırakır. Düğüm her zaman 1 adım boyutunda statik zamanlamayı kullanır, pencereleri latent zaman boyutuna uygular ve nedensel düzeltme karesini eklemez, çünkü her pencere bir parça sınırında başlar. `split_conds_to_windows`, ConditionCombine düğümü tarafından oluşturulan birden çok koşullandırma bekler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Bağlam penceresi yapılandırması uygulanmış model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ContextWindows/tr.md)

---
**Source fingerprint (SHA-256):** `e9e019d0bc870abfe226ef1aafb2607f55c0cc1b297884db35fe98c465cc0d91`
