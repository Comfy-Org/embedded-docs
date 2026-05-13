> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageUpscaleWithModel/tr.md)

Bu düğüm, belirtilen bir yükseltme modelini kullanarak görüntüleri yükseltmek için tasarlanmıştır. Görüntüyü uygun cihaza ayarlayarak, bellek kullanımını optimize ederek ve olası bellek taşması hatalarını önlemek için yükseltme modelini döşemeli bir şekilde uygulayarak yükseltme sürecini verimli bir şekilde yönetir.

## Girişler

| Parametre         | Comfy dtype       | Açıklama                                                                 |
|-------------------|-------------------|----------------------------------------------------------------------------|
| `upscale_model`   | `UPSCALE_MODEL`   | Görüntüyü yükseltmek için kullanılacak yükseltme modeli. Yükseltme algoritmasını ve parametrelerini tanımlamak için çok önemlidir. |
| `image`           | `IMAGE`           | Yükseltilecek görüntü. Bu girdi, yükseltme işlemine tabi tutulacak kaynak içeriğin belirlenmesi için gereklidir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama                                        |
|-----------|-------------|----------------------------------------------------|
| `image`   | `IMAGE`     | Yükseltme modeli tarafından işlenmiş, yükseltilmiş görüntü. Bu çıktı, yükseltme işleminin sonucudur ve geliştirilmiş çözünürlük veya kaliteyi sergiler. |