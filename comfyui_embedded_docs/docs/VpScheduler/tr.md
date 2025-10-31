> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VPScheduler/tr.md)

VPScheduler düğümü, Varyans Koruma (VP) planlama yöntemine dayalı olarak bir gürültü seviyeleri dizisi (sigmas) oluşturmak için tasarlanmıştır. Bu dizi, difüzyon modellerinde gürültü giderme işlemini yönlendirmek için çok önemli olup, kontrollü bir şekilde görüntü veya diğer veri türlerinin oluşturulmasını sağlar.

## Girdiler

| Parametre   | Veri Türü | Açıklama                                                                                                                                      |
|-------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `adımlar`     | INT         | Difüzyon işlemindeki adım sayısını belirtir ve oluşturulan gürültü seviyelerinin detay düzeyini etkiler.                              |
| `beta_d`    | FLOAT       | Genel gürültü seviyesi dağılımını belirler ve oluşturulan gürültü seviyelerinin varyansını etkiler.                                 |
| `beta_min`  | FLOAT       | Gürültü seviyesi için minimum sınırı ayarlar ve gürültünün belirli bir eşiğin altına düşmemesini sağlar.                              |
| `eps_s`     | FLOAT       | Başlangıç epsilon değerini ayarlayarak difüzyon işlemindeki başlangıç gürültü seviyesini ince ayarlar.                                    |

## Çıktılar

| Parametre   | Veri Türü | Açıklama                                                                                   |
|-------------|-------------|-----------------------------------------------------------------------------------------------|
| `sigmas`    | SIGMAS      | VP planlama yöntemine dayalı olarak oluşturulan bir gürültü seviyeleri dizisi (sigmas), difüzyon modellerinde gürültü giderme işlemini yönlendirmek için kullanılır. |