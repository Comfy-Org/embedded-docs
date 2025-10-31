> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageUpscaleWithModel/tr.md)

Bu düğüm, belirli bir yükseltme modeli kullanarak görüntüleri yükseltmek için tasarlanmıştır. Görüntüyü uygun cihaza ayarlayarak, bellek kullanımını optimize ederek ve olası bellek yetersizliği hatalarını önlemek için yükseltme modelini mozaik yöntemiyle uygulayarak yükseltme işlemini verimli bir şekilde yönetir.

## Girişler

| Parametre         | Comfy Veri Türü   | Açıklama                                                                 |
|-------------------|-------------------|----------------------------------------------------------------------------|
| `upscale_model`   | `UPSCALE_MODEL`   | Görüntüyü yükseltmek için kullanılacak yükseltme modeli. Yükseltme algoritmasını ve parametrelerini tanımlamak için çok önemlidir. |
| `image`           | `IMAGE`           | Yükseltilecek görüntü. Bu giriş, yükseltme işlemine tabi tutulacak kaynak içeriği belirlemek için gereklidir. |

## Çıkışlar

| Parametre | Veri Türü   | Açıklama                                        |
|-----------|-------------|----------------------------------------------------|
| `image`   | `IMAGE`     | Yükseltme modeli tarafından işlenen yükseltilmiş görüntü. Bu çıktı, yükseltme işleminin sonucu olup, geliştirilmiş çözünürlüğü veya kaliteyi sergiler. |