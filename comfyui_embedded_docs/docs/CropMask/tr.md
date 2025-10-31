> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropMask/tr.md)

CropMask düğümü, belirli bir maskenin belirtilen bir alanını kırpmak için tasarlanmıştır. Kullanıcıların koordinatları ve boyutları belirterek ilgi alanını tanımlamasına olanak tanır, böylece maskenin bir bölümü etkili bir şekilde daha fazla işleme veya analiz için çıkarılır.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `maske`    | MASK        | Maske girdisi, kırpılacak olan maske görüntüsünü temsil eder. Belirtilen koordinatlar ve boyutlar temel alınarak çıkarılacak alanı tanımlamak için gereklidir. |
| `x`       | INT         | X koordinatı, kırpma işleminin başlayacağı yatay eksendeki başlangıç noktasını belirtir. |
| `y`       | INT         | Y koordinatı, kırpma işlemi için dikey eksendeki başlangıç noktasını belirler. |
| `genişlik`   | INT         | Genişlik, başlangıç noktasından itibaren kırpma alanının yatay uzantısını tanımlar. |
| `yükseklik`  | INT         | Yükseklik, başlangıç noktasından itibaren kırpma alanının dikey uzantısını belirtir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `maske`    | MASK        | Çıktı, kırpılmış bir maskedir ve orijinal maskenin belirtilen koordinatlar ve boyutlar ile tanımlanmış bir bölümüdür. |