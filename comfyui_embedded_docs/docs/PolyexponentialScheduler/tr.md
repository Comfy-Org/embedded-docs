> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PolyexponentialScheduler/tr.md)

PolyexponentialScheduler düğümü, bir poliexponansiyel gürültü planına dayalı olarak bir dizi gürültü seviyesi (sigma) oluşturmak için tasarlanmıştır. Bu plan, sigma'nın logaritmasında bir polinom fonksiyonudur ve difüzyon süreci boyunca gürültü seviyelerinin esnek ve özelleştirilebilir bir şekilde ilerlemesine olanak tanır.

## Girişler

| Parametre   | Veri Türü | Açıklama                                                                                                                                                                                                                                                                                                                                                      |
|-------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `adımlar`     | INT         | Difüzyon sürecindeki adım sayısını belirtir ve oluşturulan gürültü seviyelerinin ayrıntı düzeyini etkiler.                                                                                                                                                                                                                                                                        |
| `sigma_maks` | FLOAT       | Maksimum gürültü seviyesi olup, gürültü planının üst sınırını belirler.                                                                                                                                                                                                                                                                                                                                 |
| `sigma_min` | FLOAT       | Minimum gürültü seviyesi olup, gürültü planının alt sınırını belirler.                                                                                                                                                                                                                                                                                                                                 |
| `rho`       | FLOAT       | Poliexponansiyel gürültü planının şeklini kontrol eden bir parametredir ve gürültü seviyelerinin minimum ile maksimum değerler arasında nasıl ilerleyeceğini etkiler.                                                                                                                                                                                                               |

## Çıktılar

| Parametre | Veri Türü | Açıklama                                                                 |
|-----------|-------------|-----------------------------------------------------------------------------|
| `sigmas`  | SIGMAS      | Çıktı, belirtilen poliexponansiyel gürültü planına göre uyarlanmış bir dizi gürültü seviyesidir (sigma). |