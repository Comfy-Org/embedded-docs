> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmas/tr.md)

SplitSigmas düğümü, bir sigma değerleri dizisini belirtilen bir adıma göre iki parçaya bölmek için tasarlanmıştır. Bu işlevsellik, sigma dizisinin başlangıç ve sonraki kısımlarının farklı şekilde işlenmesini veya işleme tabi tutulmasını gerektiren operasyonlar için çok önemlidir ve bu değerlerin daha esnek ve hedeflenen bir şekilde manipüle edilmesine olanak tanır.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `sigmalar`  | `SIGMAS`    | 'sigmas' parametresi, bölünecek olan sigma değerleri dizisini temsil eder. Bölünme noktasını ve ortaya çıkan iki sigma değerleri dizisini belirlemek için esastır, düğümün yürütülmesini ve sonuçlarını etkiler. |
| `adım`    | `INT`       | 'step' parametresi, sigma dizisinin hangi indekste bölüneceğini belirtir. Ortaya çıkan iki sigma dizisi arasındaki sınırı tanımlamada kritik bir rol oynar, düğümün işlevselliğini ve çıktıların özelliklerini etkiler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `düşük_sigmalar`  | `SIGMAS`    | Düğüm, her biri orijinal dizinin belirtilen adımda bölünmüş bir kısmını temsil eden iki sigma değerleri dizisi çıktılar. Bu çıktılar, sigma değerlerinin farklılaştırılmış bir şekilde ele alınmasını gerektiren sonraki operasyonlar için çok önemlidir. |