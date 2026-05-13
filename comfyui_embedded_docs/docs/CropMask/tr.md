> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropMask/tr.md)

CropMask düğümü, belirli bir maskeden belirtilen alanı kırpmak için tasarlanmıştır. Kullanıcıların koordinatlar ve boyutlar belirterek ilgilenilen bölgeyi tanımlamasına olanak tanır ve böylece maskenin bir kısmını daha sonraki işlemler veya analizler için etkili bir şekilde çıkarır.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `maske`    | MASK        | Maske girişi, kırpılacak maske görüntüsünü temsil eder. Belirtilen koordinatlara ve boyutlara göre çıkarılacak alanı tanımlamak için gereklidir. |
| `x`       | INT         | x koordinatı, kırpma işleminin başlaması gereken yatay eksendeki başlangıç noktasını belirtir. |
| `y`       | INT         | y koordinatı, kırpma işlemi için dikey eksendeki başlangıç noktasını belirler. |
| `genişlik`   | INT         | Genişlik, başlangıç noktasından itibaren kırpma alanının yatay kapsamını tanımlar. |
| `yükseklik`  | INT         | Yükseklik, başlangıç noktasından itibaren kırpma alanının dikey kapsamını belirtir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `maske`    | MASK        | Çıktı, belirtilen koordinatlar ve boyutlar tarafından tanımlanan orijinal maskenin bir kısmı olan kırpılmış maskedir. |