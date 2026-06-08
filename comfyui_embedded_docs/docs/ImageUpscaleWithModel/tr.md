Bu düğüm, belirtilen bir yükseltme modelini kullanarak görüntüleri yükseltmek için tasarlanmıştır. Görüntüyü uygun cihaza ayarlayarak, bellek kullanımını optimize ederek ve olası bellek taşması hatalarını önlemek için yükseltme modelini döşemeli bir şekilde uygulayarak yükseltme sürecini verimli bir şekilde yönetir.

## Girişler

| Parametre | Açıklama | Comfy dtype |
| --- | --- | --- |
| `büyütme_modeli` | Görüntüyü yükseltmek için kullanılacak yükseltme modeli. Yükseltme algoritmasını ve parametrelerini tanımlamak için çok önemlidir. | `UPSCALE_MODEL` |
| `görüntü` | Yükseltilecek görüntü. Bu girdi, yükseltme işlemine tabi tutulacak kaynak içeriğin belirlenmesi için gereklidir. | `IMAGE` |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Yükseltme modeli tarafından işlenmiş, yükseltilmiş görüntü. Bu çıktı, yükseltme işleminin sonucudur ve geliştirilmiş çözünürlük veya kaliteyi sergiler. | `IMAGE` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageUpscaleWithModel/tr.md)
