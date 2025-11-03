> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Sd4xupscaleConditioning/tr.md)

Bu düğüm, görüntülerin çözünürlüğünü, çıktıyı iyileştirmek için koşullandırma öğelerini de içeren bir 4x büyütme işlemiyle artırmada uzmanlaşmıştır. Görüntüleri büyütürken yayılım tekniklerinden yararlanır ve aynı zamanda büyütme oranı ve gürültü artırımı ayarları yaparak iyileştirme sürecini hassas bir şekilde kontrol etme olanağı sağlar.

## Girişler

| Parametre            | Comfy Veri Türü   | Açıklama |
|----------------------|-------------------|-------------|
| `images`             | `IMAGE`           | Büyütülecek giriş görüntüleri. Bu parametre, çıktı görüntülerinin kalitesini ve çözünürlüğünü doğrudan etkilediği için çok önemlidir. |
| `positive`           | `CONDITIONING`    | Büyütme işlemini, çıktı görüntülerinde istenen niteliklere veya özelliklere yönlendiren olumlu koşullandırma öğeleri. |
| `negative`           | `CONDITIONING`    | Büyütme işleminin kaçınması gereken, çıktının istenmeyen niteliklerden veya özelliklerden uzaklaştırılmasına yardımcı olan olumsuz koşullandırma öğeleri. |
| `scale_ratio`        | `FLOAT`           | Görüntü çözünürlüğünün hangi faktörle artırılacağını belirler. Daha yüksek bir büyütme oranı, daha fazla detay ve netlik sağlayan daha büyük bir çıktı görüntüsüyle sonuçlanır. |
| `noise_augmentation` | `FLOAT`           | Büyütme işlemi sırasında uygulanan gürültü artırımı seviyesini kontrol eder. Bu, çeşitlilik katmak ve çıktı görüntülerinin sağlamlığını artırmak için kullanılabilir. |

## Çıktılar

| Parametre     | Veri Türü      | Açıklama |
|---------------|----------------|-------------|
| `positive`    | `CONDITIONING` | Büyütme işlemi sonucunda ortaya çıkan, iyileştirilmiş olumlu koşullandırma öğeleri. |
| `negative`    | `CONDITIONING` | Büyütme işlemi sonucunda ortaya çıkan, iyileştirilmiş olumsuz koşullandırma öğeleri. |
| `latent`      | `LATENT`       | Büyütme işlemi sırasında oluşturulan, ileri işleme veya model eğitiminde kullanılabilecek bir gizil (latent) temsil. |