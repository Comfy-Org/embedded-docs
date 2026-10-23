# VPZamanlayıcı

VPScheduler düğümü, Varyans Koruyan (VP) zamanlama yöntemine dayalı olarak bir dizi gürültü seviyesi (sigma) oluşturmak için tasarlanmıştır. Bu dizi, difüzyon modellerinde gürültü giderme sürecini yönlendirmek için kritik öneme sahiptir ve görüntüler veya diğer veri türlerinin kontrollü bir şekilde üretilmesine olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `adımlar` | Difüzyon sürecindeki adım sayısını belirler, oluşturulan gürültü seviyelerinin ayrıntı düzeyini etkiler. | INT |
| `beta_d` | Genel gürültü seviyesi dağılımını belirler, oluşturulan gürültü seviyelerinin varyansını etkiler. | FLOAT |
| `beta_min` | Gürültü seviyesi için minimum sınırı ayarlar, gürültünün belirli bir eşiğin altına düşmemesini sağlar. | FLOAT |
| `eps_s` | Başlangıç epsilon değerini ayarlar, difüzyon sürecindeki ilk gürültü seviyesini ince ayarlar. | FLOAT |

## Çıkışlar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | VP zamanlama yöntemine dayalı olarak oluşturulan bir dizi gürültü seviyesi (sigma), difüzyon modellerinde gürültü giderme sürecini yönlendirmek için kullanılır. | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VPScheduler/tr.md)
