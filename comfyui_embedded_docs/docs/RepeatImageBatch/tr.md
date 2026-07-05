# GörüntüGrubunuTekrarla

RepeatImageBatch düğümü, belirtilen bir görseli belirli sayıda çoğaltarak aynı görsellerden oluşan bir grup oluşturmak üzere tasarlanmıştır. Bu işlevsellik, toplu işleme veya veri artırma gibi aynı görselin birden fazla örneğini gerektiren işlemler için kullanışlıdır.

## Girişler

| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | 'image' parametresi, çoğaltılacak görseli temsil eder. Grup boyunca kopyalanacak içeriğin tanımlanması açısından kritik öneme sahiptir. | `IMAGE` |
| `miktar` | 'amount' parametresi, giriş görselinin kaç kez çoğaltılacağını belirtir. Çıktı grubunun boyutunu doğrudan etkileyerek esnek grup oluşturulmasını sağlar. | `INT` |

## Çıktılar

| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Çıktı, her biri giriş görseliyle aynı olan ve belirtilen 'amount' değerine göre çoğaltılmış bir görsel grubudur. | `IMAGE` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatImageBatch/tr.md)
