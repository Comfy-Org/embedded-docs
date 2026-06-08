PolyexponentialScheduler düğümü, bir poliexponansiyel gürültü planına dayalı olarak bir dizi gürültü seviyesi (sigma) oluşturmak için tasarlanmıştır. Bu plan, sigma'nın logaritmasında bir polinom fonksiyonudur ve difüzyon süreci boyunca gürültü seviyelerinin esnek ve özelleştirilebilir bir şekilde ilerlemesine olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `adımlar` | Difüzyon sürecindeki adım sayısını belirtir ve oluşturulan gürültü seviyelerinin ayrıntı düzeyini etkiler. | INT |
| `sigma_maks` | Maksimum gürültü seviyesi olup, gürültü planının üst sınırını belirler. | FLOAT |
| `sigma_min` | Minimum gürültü seviyesi olup, gürültü planının alt sınırını belirler. | FLOAT |
| `rho` | Poliexponansiyel gürültü planının şeklini kontrol eden bir parametredir ve gürültü seviyelerinin minimum ile maksimum değerler arasında nasıl ilerleyeceğini etkiler. | FLOAT |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Çıktı, belirtilen poliexponansiyel gürültü planına göre uyarlanmış bir dizi gürültü seviyesidir (sigma). | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PolyexponentialScheduler/tr.md)
