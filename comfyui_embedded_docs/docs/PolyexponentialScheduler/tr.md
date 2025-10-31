> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PolyexponentialScheduler/tr.md)

PolyexponentialScheduler düğümü, poliyüstel gürültü zamanlamasına dayalı bir gürültü seviyeleri (sigmalar) dizisi oluşturmak için tasarlanmıştır. Bu zamanlama, sigma'nın logaritmasında polinom fonksiyonudur ve difüzyon süreci boyunca gürültü seviyelerinin esnek ve özelleştirilebilir bir ilerleyişine olanak tanır.

## Girdiler

| Parametre | Veri Türü | Açıklama                                                                                                                                                                                                                                                                                                                                                      |
|-----------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `steps`   | INT       | Difüzyon sürecindeki adım sayısını belirler ve oluşturulan gürültü seviyelerinin detay seviyesini etkiler.                                                                                                                                                                                                                                                              |
| `sigma_max` | FLOAT     | Maksimum gürültü seviyesidir, gürültü zamanlamasının üst sınırını belirler.                                                                                                                                                                                                                                                                                             |
| `sigma_min` | FLOAT     | Minimum gürültü seviyesidir, gürültü zamanlamasının alt sınırını belirler.                                                                                                                                                                                                                                                                                             |
| `rho`     | FLOAT     | Poliyüstel gürültü zamanlamasının şeklini kontrol eden bir parametredir; gürültü seviyelerinin minimum ve maksimum değerler arasında nasıl ilerlediğini etkiler.                                                                                                                                                                                              |

## Çıktılar

| Parametre | Veri Türü | Açıklama                                                                 |
|-----------|-----------|-------------------------------------------------------------------------|
| `sigmas`  | SIGMAS    | Çıktı, belirtilen poliyüstel gürültü zamanlamasına uyarlanmış bir gürültü seviyeleri (sigmalar) dizisidir. |