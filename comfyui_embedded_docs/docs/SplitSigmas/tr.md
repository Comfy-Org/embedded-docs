# SigmalarıBöl

SplitSigmas düğümü, bir sigma değerleri dizisini belirtilen bir adıma göre iki parçaya bölmek için tasarlanmıştır. Bu işlevsellik, sigma dizisinin başlangıç ve sonraki bölümlerinin farklı şekilde işlenmesini veya ele alınmasını gerektiren işlemler için kritik öneme sahiptir ve bu değerler üzerinde daha esnek ve hedefli bir manipülasyon sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmalar` | 'sigmas' parametresi, bölünecek sigma değerleri dizisini temsil eder. Bölünme noktasının ve sonuçta ortaya çıkan iki sigma değerleri dizisinin belirlenmesi için gereklidir; düğümün yürütülmesini ve sonuçlarını etkiler. | `SIGMAS` |
| `adım` | 'step' parametresi, sigma dizisinin bölünmesi gereken dizin numarasını belirtir. Ortaya çıkan iki sigma dizisi arasındaki sınırı tanımlamada kritik bir rol oynar; düğümün işlevselliğini ve çıktının özelliklerini etkiler. | `INT` |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `yüksek_sigma` | Düğüm, her biri belirtilen adımda bölünmüş orijinal dizinin bir parçasını temsil eden iki sigma değerleri dizisi çıktısı verir. Bu çıktılar, sigma değerlerinin farklılaştırılmış şekilde ele alınmasını gerektiren sonraki işlemler için çok önemlidir. | `SIGMAS` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmas/tr.md)
