# Sd4xupscaleConditioning

Bu düğüm, çıktıyı iyileştirmek için koşullandırma öğelerini dahil ederek görüntülerin çözünürlüğünü 4 kat büyütme işlemiyle artırma konusunda uzmanlaşmıştır. Görüntüleri büyütmek için difüzyon tekniklerinden yararlanırken, ölçek oranı ve gürültü artırımının ayarlanmasına olanak tanıyarak iyileştirme sürecini ince ayarlar.

## Girişler

| Parametre | Açıklama | Comfy Veri Türü |
| --- | --- | --- |
| `images` | Büyütülecek giriş görüntüleri. Bu parametre, çıktı görüntülerinin kalitesini ve çözünürlüğünü doğrudan etkilediği için çok önemlidir. | `IMAGE` |
| `positive` | Büyütme işlemini çıktı görüntülerinde istenen niteliklere veya özelliklere yönlendiren olumlu koşullandırma öğeleri. | `CONDITIONING` |
| `negative` | Büyütme işleminin kaçınması gereken, çıktıyı istenmeyen niteliklerden veya özelliklerden uzaklaştırmaya yardımcı olan olumsuz koşullandırma öğeleri. | `CONDITIONING` |
| `scale_ratio` | Görüntü çözünürlüğünün artırılma faktörünü belirler. Daha yüksek bir ölçek oranı, daha büyük bir çıktı görüntüsüyle sonuçlanarak daha fazla ayrıntı ve netlik sağlar. | `FLOAT` |
| `noise_augmentation` | Büyütme işlemi sırasında uygulanan gürültü artırımının seviyesini kontrol eder. Bu, değişkenlik eklemek ve çıktı görüntülerinin sağlamlığını iyileştirmek için kullanılabilir. | `FLOAT` |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Büyütme işlemi sonucunda elde edilen iyileştirilmiş olumlu koşullandırma öğeleri. | `CONDITIONING` |
| `negative` | Büyütme işlemi sonucunda elde edilen iyileştirilmiş olumsuz koşullandırma öğeleri. | `CONDITIONING` |
| `latent` | Büyütme işlemi sırasında oluşturulan ve daha sonraki işlemlerde veya model eğitiminde kullanılabilecek bir gizli temsil. | `LATENT` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Sd4xupscaleConditioning/tr.md)
