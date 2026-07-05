# Maskeyi Kırp

CropMask düğümü, belirli bir maskeden belirtilen alanı kırpmak için tasarlanmıştır. Kullanıcıların koordinatlar ve boyutlar belirterek ilgilenilen bölgeyi tanımlamasına olanak tanır ve böylece maskenin bir kısmını daha sonraki işlemler veya analizler için etkili bir şekilde çıkarır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `maske` | Maske girişi, kırpılacak maske görüntüsünü temsil eder. Belirtilen koordinatlara ve boyutlara göre çıkarılacak alanı tanımlamak için gereklidir. | MASK |
| `x` | x koordinatı, kırpma işleminin başlaması gereken yatay eksendeki başlangıç noktasını belirtir. | INT |
| `y` | y koordinatı, kırpma işlemi için dikey eksendeki başlangıç noktasını belirler. | INT |
| `genişlik` | Genişlik, başlangıç noktasından itibaren kırpma alanının yatay kapsamını tanımlar. | INT |
| `yükseklik` | Yükseklik, başlangıç noktasından itibaren kırpma alanının dikey kapsamını belirtir. | INT |


| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `mask` | Çıktı, belirtilen koordinatlar ve boyutlar tarafından tanımlanan orijinal maskenin bir kısmı olan kırpılmış maskedir. | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropMask/tr.md)
